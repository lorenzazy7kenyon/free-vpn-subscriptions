#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборщик бесплатных VPN-подписок: публичные источники -> проверка -> подписки + сайт."""
import base64
import concurrent.futures
import datetime
import hashlib
import json
import os
import random
import re
import socket
import statistics
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWNER = "lorenzazy7kenyon"
REPO = "free-vpn-subscriptions"
SITE_BASE = f"https://{OWNER}.github.io/{REPO}"
RAW_BASE = f"https://github.com/{OWNER}/{REPO}/raw/main/output"
UA = {"User-Agent": "Mozilla/5.0 (compatible; free-vpn-subscriptions-sync/1.0)"}

SOURCES = [
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vless.txt",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vmess.txt",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/trojan.txt",
    "https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/ss.txt",
    "https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.txt",
    "https://raw.githubusercontent.com/chengaopan/AutoMergePublicNodes/master/list.txt",
    "https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/v2ray.txt",
    "https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.txt",
    "https://raw.githubusercontent.com/ts-sf/fly/main/v2",
]

SCHEME_RE = re.compile(r"^(vmess|vless|trojan|ss|hysteria2|hy2|tuic)://", re.I)
UDP_ONLY = {"hysteria2", "tuic"}
MAX_SELECTED = 2000
MAX_SHARD = 500
TCP_THREADS = 256
TCP_TIMEOUT = 3.0

RU_NAMES = {
    "JP": "Япония", "US": "США", "SG": "Сингапур", "NL": "Нидерланды", "DE": "Германия",
    "KR": "Корея", "HK": "Гонконг", "TW": "Тайвань", "GB": "Великобритания", "FR": "Франция",
    "RU": "Россия", "IN": "Индия", "PL": "Польша", "CA": "Канада", "TH": "Таиланд",
    "FI": "Финляндия", "SE": "Швеция", "AE": "ОАЭ", "ID": "Индонезия", "AU": "Австралия",
    "RO": "Румыния", "IT": "Италия", "MD": "Молдова", "TR": "Турция", "PH": "Филиппины",
    "HU": "Венгрия", "LV": "Латвия", "EE": "Эстония", "LT": "Литва", "AT": "Австрия",
    "ES": "Испания", "CH": "Швейцария", "CZ": "Чехия", "BG": "Болгария", "BR": "Бразилия",
    "MX": "Мексика", "AR": "Аргентина", "UA": "Украина", "BY": "Беларусь", "KZ": "Казахстан",
    "VN": "Вьетнам", "SA": "Саудовская Аравия", "ZA": "ЮАР", "PT": "Португалия", "GR": "Греция",
    "DK": "Дания", "NO": "Норвегия", "BE": "Бельгия", "MY": "Малайзия", "IR": "Иран",
    "AM": "Армения", "GE": "Грузия", "AL": "Албания", "RS": "Сербия", "CY": "Кипр",
}
PROTO_TITLES = {"vless": "VLESS", "vmess": "VMess", "trojan": "Trojan",
                "shadowsocks": "Shadowsocks", "hysteria2": "Hysteria2", "tuic": "TUIC"}


def now_utc():
    ts = datetime.datetime.now(datetime.timezone.utc)
    return ts.replace(minute=0, second=0, microsecond=0)


def hour_id(ts):
    return f"{ts.strftime('%Y%m%d%H')}"


def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def b64d(s):
    s = s.strip().replace("\n", "").replace(" ", "")
    s += "=" * (-len(s) % 4)
    try:
        return base64.urlsafe_b64decode(s)
    except Exception:
        try:
            return base64.b64decode(s)
        except Exception:
            return None


def tag_for(kind, host, port, secret, extra=""):
    key = f"{kind}|{host}|{port}|{secret}|{extra}"
    n = int(hashlib.md5(key.encode()).hexdigest()[:10], 16)
    return f"{kind}-{n}"


def parse_ss(rest):
    body, _, frag = rest.partition("#")
    frag = urllib.parse.unquote(frag)
    if "@" in body:
        userinfo, _, hostport = body.rpartition("@")
        hostport = hostport.split("/")[0].split("?")[0]
        dec = b64d(userinfo)
        if dec is not None:
            userinfo = dec.decode(errors="ignore")
        method, _, password = userinfo.partition(":")
        host, _, port = hostport.rpartition(":")
        return {"kind": "ss", "cipher": method, "password": password,
                "host": host, "port": int(port), "tag": frag}
    dec = b64d(body)
    if dec is None:
        return None
    userinfo, _, hostport = dec.decode(errors="ignore").rpartition("@")
    method, _, password = userinfo.partition(":")
    host, _, port = hostport.rpartition(":")
    return {"kind": "ss", "cipher": method, "password": password,
            "host": host, "port": int(port), "tag": frag}


def parse_query(qs):
    return dict(urllib.parse.parse_qsl(qs, keep_blank_values=True))


def parse_uri(uri):
    try:
        scheme, _, rest = uri.partition("://")
        scheme = scheme.lower()
        if scheme == "hy2":
            scheme = "hysteria2"
        rest = rest.strip()
        if scheme == "ss":
            node = parse_ss(rest)
            if node:
                node["tag"] = node["tag"] or "ss"
            return node
        if scheme == "vmess":
            raw = b64d(rest)
            if raw is None:
                return None
            j = json.loads(raw.decode(errors="ignore"))
            proto = str(j.get("scy") or "auto").lower()
            return {"kind": "vmess", "uuid": str(j.get("id") or ""), "host": str(j.get("add") or ""),
                    "port": int(j.get("port") or 0), "cipher": proto or "auto",
                    "aid": int(j.get("aid") or 0), "net": str(j.get("net") or "tcp"),
                    "path": str(j.get("path") or ""), "ws_host": str(j.get("host") or ""),
                    "tls": str(j.get("tls") or "").lower() == "tls",
                    "sni": str(j.get("sni") or ""), "fp": str(j.get("fp") or ""),
                    "tag": str(j.get("ps") or "vmess")}
        if scheme in ("vless", "trojan", "hysteria2", "tuic"):
            frag = ""
            if "#" in rest:
                rest, _, frag = rest.partition("#")
            frag = urllib.parse.unquote(frag)
            userinfo, _, hostport = rest.rpartition("@")
            hostport, _, qs = hostport.partition("?")
            host, _, port = hostport.partition("/")[-1].rpartition(":")
            if not host:
                host, _, port = hostport.rpartition(":")
            port = int(port or 0)
            q = parse_query(qs)
            node = {"kind": scheme, "host": host, "port": port, "tag": frag or scheme}
            if scheme == "vless":
                node["uuid"] = userinfo
                node["flow"] = q.get("flow", "")
                security = q.get("security", "")
                net = q.get("type", "tcp")
            elif scheme == "trojan":
                node["password"] = urllib.parse.unquote(userinfo)
                security = "tls"
                net = q.get("type", "tcp")
            elif scheme == "hysteria2":
                node["password"] = urllib.parse.unquote(userinfo)
                node["obfs"] = q.get("obfs", "")
                node["obfs_pass"] = q.get("obfs-password", "")
                security = "tls"
                net = "udp"
            else:
                node["uuid"] = userinfo.split(":")[0]
                node["password"] = userinfo.split(":", 1)[1] if ":" in userinfo else ""
                node["alpn"] = q.get("alpn", "")
                security = "tls"
                net = "udp"
            net = q.get("type", net)
            node["network"] = net
            node["path"] = q.get("path", "")
            node["ws_host"] = q.get("host", "")
            node["grpc_servicename"] = q.get("serviceName", "")
            node["security"] = security
            node["sni"] = q.get("sni", "")
            node["fp"] = q.get("fp", "")
            node["pbk"] = q.get("pbk", "")
            node["sid"] = q.get("sid", "")
            node["insecure"] = q.get("insecure", "0") in ("1", "true")
            node["allowinsecure"] = q.get("allowInsecure", "0") in ("1", "true")
            return node
    except Exception:
        return None
    return None


def valid_node(n):
    try:
        if not n or not n.get("host") or not n.get("port"):
            return False
        p = int(n["port"])
        if p < 1 or p > 65535:
            return False
        if n["kind"] == "vmess":
            return bool(re.match(r"^[A-Za-z0-9]{16,64}$", n.get("uuid", ""))) or \
                   bool(re.match(r"^[0-9a-fA-F-]{36}$", n.get("uuid", "")))
        if n["kind"] == "vless":
            return bool(re.match(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$", n.get("uuid", "")))
        if n["kind"] == "trojan":
            return 4 <= len(n.get("password", "")) <= 256
        if n["kind"] == "ss":
            return bool(n.get("cipher")) and bool(n.get("password"))
        if n["kind"] == "hysteria2":
            return bool(n.get("password"))
        if n["kind"] == "tuic":
            return bool(n.get("uuid"))
    except Exception:
        return False
    return False


def node_key(n):
    secret = n.get("uuid") or n.get("password") or ""
    extra = ""
    if n["kind"] in ("vless", "vmess"):
        extra = f"{n.get('network')}|{n.get('path','')}|{n.get('security')}"
    return f"{n['kind']}|{n['host'].lower()}|{n['port']}|{secret}|{extra}"


def collect_nodes():
    raw = []
    seen = set()
    for url in SOURCES:
        try:
            blob = fetch(url).decode(errors="ignore")
        except Exception as e:
            print(f"[warn] источник недоступен: {url} ({e})")
            continue
        lines = [l.strip() for l in blob.splitlines() if l.strip()]
        dec = b64d(blob)
        if dec is not None:
            dec_lines = [l.strip() for l in dec.decode(errors="ignore").splitlines() if l.strip()]
            if len(dec_lines) >= len(lines):
                lines = lines + dec_lines
        got = 0
        for l in lines:
            if not SCHEME_RE.match(l):
                continue
            n = parse_uri(l)
            if not valid_node(n) or n["kind"] == "wireguard":
                continue
            k = node_key(n)
            if k in seen:
                continue
            seen.add(k)
            n["key"] = k
            n["origin"] = l
            n["tag"] = n.get("tag") or n["kind"]
            raw.append(n)
            got += 1
        print(f"[src] {url.rsplit('/',1)[-1]}: {got} узлов")
    return raw


def check_tcp(n):
    host, port, kind = n["host"], n["port"], n["kind"]
    if kind in UDP_ONLY:
        try:
            socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
            return n["key"], True, -1
        except Exception:
            return n["key"], False, None
    try:
        infos = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
        t0 = time.perf_counter()
        with socket.socket() as s:
            s.settimeout(TCP_TIMEOUT)
            s.connect((infos[0][4][0], port))
        rtt = int((time.perf_counter() - t0) * 1000)
        return n["key"], True, rtt
    except Exception:
        return n["key"], False, None


def geo_lookup(ip_list):
    res = {}
    ips = list(dict.fromkeys(ip_list))
    batch_names = ("status", "query", "countryCode", "country", "isp", "org", "as", "hosting")
    for i in range(0, len(ips), 100):
        chunk = ips[i:i + 100]
        for attempt in range(3):
            try:
                req = urllib.request.Request(
                    "http://ip-api.com/batch?fields=status,query,countryCode,country,isp,org,as,hosting",
                    data=json.dumps(chunk).encode(), headers={**UA, "Content-Type": "application/json"},
                    method="POST")
                with urllib.request.urlopen(req, timeout=30) as r:
                    data = json.loads(r.read().decode())
                for item in data:
                    if item.get("status") == "success":
                        ip = item.get("query")
                        res[ip] = {"cc": item.get("countryCode", ""), "country": item.get("country", ""),
                                   "isp": item.get("isp", ""), "org": item.get("org", ""),
                                   "as": item.get("as", ""), "hosting": bool(item.get("hosting"))}
                break
            except Exception:
                time.sleep(20)
        time.sleep(4)
    return res


def flag(cc):
    if not cc or len(cc) != 2 or not cc.isalpha():
        return "🏳️"
    return "".join(chr(ord("🇦") + ord(c) - ord("A")) for c in cc.upper())


def country_name(cc):
    return RU_NAMES.get(cc, cc or "Прочие")


def net_group(info):
    if info.get("hosting"):
        return "hosting"
    asm = (info.get("as", "") + " " + info.get("org", "")).lower()
    cloud_kw = ("amazon", "google", "azure", "microsoft", "ovh", "hetzner", "digitalocean",
                "linode", "vultr", "alibaba", "tencent", "oracle", "contabo", "scaleway",
                "upcloud", "hetzner", "choopa", "cogent", "colocationamerica")
    if any(k in asm for k in cloud_kw):
        return "cloud"
    isp = info.get("isp", "").lower()
    if not isp or "unknown" in isp or len(isp) < 4:
        return "unknown"
    return "isp"


def clash_proxy(n):
    name = n["tag"][:100]
    common = {"name": name, "server": n["host"], "port": n["port"], "udp": True}
    k = n["kind"]
    if k == "vless":
        p = {"type": "vless", "uuid": n["uuid"], **common}
        if n.get("flow"):
            p["flow"] = n["flow"]
        p["network"] = n.get("network", "tcp")
        sec = n.get("security", "")
        if sec in ("tls", "reality"):
            p["tls"] = True if k != "vless" or n.get("security") else True
            p["servername"] = n.get("sni") or n["host"]
            if n.get("fp"):
                p["client-fingerprint"] = n["fp"]
            if sec == "reality":
                p["reality-opts"] = {"public-key": n.get("pbk", "")}
                if n.get("sid"):
                    p["reality-opts"]["short-id"] = n["sid"]
        if n["network"] == "ws":
            p["ws-opts"] = {"path": n.get("path") or "/"}
            if n.get("ws_host"):
                p["ws-opts"]["headers"] = {"Host": n["ws_host"]}
        return p
    if k == "vmess":
        p = {"type": "vmess", "uuid": n["uuid"], "alterId": n.get("aid", 0),
             "cipher": n.get("cipher", "auto"), "network": n.get("net", "tcp"), **common}
        if n.get("tls"):
            p["tls"] = True
            p["servername"] = n.get("sni") or n["ws_host"] or n["host"]
        if n.get("net") == "ws":
            p["ws-opts"] = {"path": n.get("path") or "/"}
            if n.get("ws_host"):
                p["ws-opts"]["headers"] = {"Host": n["ws_host"]}
        return p
    if k == "trojan":
        p = {"type": "trojan", "password": n["password"], **common}
        p["sni"] = n.get("sni") or n["ws_host"] or n["host"]
        if n.get("insecure") or n.get("allowinsecure"):
            p["skip-cert-verify"] = True
        if n.get("network") == "ws":
            p["network"] = "ws"
            p["ws-opts"] = {"path": n.get("path") or "/"}
            if n.get("ws_host"):
                p["ws-opts"]["headers"] = {"Host": n["ws_host"]}
        return p
    if k == "ss":
        return {"type": "ss", "cipher": n["cipher"], "password": n["password"], **common}
    if k == "hysteria2":
        p = {"type": "hysteria2", "password": n["password"], **common}
        p["sni"] = n.get("sni") or n.get("ws_host") or ""
        if n.get("insecure") or n.get("allowinsecure"):
            p["skip-cert-verify"] = True
        if n.get("obfs"):
            p["obfs"] = n["obfs"]
            if n.get("obfs_pass"):
                p["obfs-password"] = n["obfs_pass"]
        return p
    if k == "tuic":
        p = {"type": "tuic", "uuid": n["uuid"], "password": n.get("password", ""),
             "sni": n.get("sni") or "", **common}
        if n.get("insecure") or n.get("allowinsecure"):
            p["skip-cert-verify"] = True
        return p
    return None


def singbox_out(n):
    k = n["kind"]
    o = {"tag": n["tag"], "server": n["host"], "server_port": n["port"], "type": k}
    if k == "vless":
        o["uuid"] = n["uuid"]
        if n.get("flow"):
            o["flow"] = n["flow"]
    elif k == "vmess":
        o["uuid"] = n["uuid"]
        o["alter_id"] = n.get("aid", 0)
        o["security"] = n.get("cipher", "auto")
    elif k in ("trojan", "hysteria2"):
        o["password"] = n["password"]
        if k == "hysteria2" and n.get("obfs"):
            o["obfs"] = {"type": n["obfs"], "password": n.get("obfs_pass", "")}
    elif k == "ss":
        o["method"] = n["cipher"]
        o["password"] = n["password"]
    elif k == "tuic":
        o["uuid"] = n["uuid"]
        o["password"] = n.get("password", "")
    sec = n.get("security", "")
    if k == "vmess" and n.get("tls"):
        sec = "tls"
    if k in ("hysteria2", "tuic"):
        sec = "tls"
    if n["kind"] == "trojan":
        sec = "tls"
    if sec in ("tls", "reality") or k in ("trojan", "hysteria2", "tuic"):
        tls = {"enabled": True, "insecure": bool(n.get("insecure") or n.get("allowinsecure"))}
        sni = n.get("sni") or n.get("ws_host")
        if sni:
            tls["server_name"] = sni
        if sec == "reality":
            r = {"enabled": True, "public_key": n.get("pbk", "")}
            if n.get("sid"):
                r["short_id"] = n["sid"]
            tls["reality"] = r
        if n.get("fp"):
            tls["utls"] = {"enabled": True, "fingerprint": n["fp"]}
        o["tls"] = tls
    net = n.get("network") or n.get("net") or "tcp"
    if net == "ws":
        t = {"type": "ws", "path": n.get("path") or "/"}
        if n.get("ws_host"):
            t["headers"] = {"Host": n["ws_host"]}
        o["transport"] = t
    elif net == "grpc" and n.get("grpc_servicename"):
        o["transport"] = {"type": "grpc", "service_name": n["grpc_servicename"]}
    return o


def v2ray_uri(n):
    k = n["kind"]
    q = []
    if k == "vless":
        q.append(f"security={n.get('security') or 'tls'}")
        if n.get("flow"):
            q.append(f"flow={n['flow']}")
        if n.get("fp"):
            q.append(f"fp={n['fp']}")
        if n.get("pbk"):
            q.append(f"pbk={n['pbk']}")
        if n.get("sid"):
            q.append(f"sid={n['sid']}")
        if n.get("sni"):
            q.append(f"sni={n['sni']}")
        net = n.get("network") or "tcp"
        q.append(f"type={net}")
        if net == "ws":
            if n.get("path"):
                q.append(f"path={urllib.parse.quote(n['path'], safe='')}")
            if n.get("ws_host"):
                q.append(f"host={n['ws_host']}")
        if n.get("insecure") or n.get("allowinsecure"):
            q.append("insecure=1")
        netloc = f"{n['uuid']}@{n['host']}:{n['port']}"
        return f"vless://{netloc}?{'&'.join(q)}#{urllib.parse.quote(n['tag'], safe='')}"
    if k == "trojan":
        if n.get("network") and n["network"] != "tcp":
            q.append(f"type={n['network']}")
            if n.get("path"):
                q.append(f"path={urllib.parse.quote(n['path'], safe='')}")
            if n.get("ws_host"):
                q.append(f"host={n['ws_host']}")
        if n.get("insecure") or n.get("allowinsecure"):
            q.append("allowInsecure=1")
        userinfo = urllib.parse.quote(n["password"], safe="")
        tail = f"?{'&'.join(q)}" if q else ""
        return f"trojan://{userinfo}@{n['host']}:{n['port']}{tail}#{urllib.parse.quote(n['tag'], safe='')}"
    if k == "ss":
        userinfo = base64.b64encode(f"{n['cipher']}:{n['password']}".encode()).decode().rstrip("=")
        return f"ss://{userinfo}@{n['host']}:{n['port']}#{urllib.parse.quote(n['tag'], safe='')}"
    if k == "hysteria2":
        if n.get("sni"):
            q.append(f"sni={n['sni']}")
        if n.get("insecure") or n.get("allowinsecure"):
            q.append("insecure=1")
        tail = f"?{'&'.join(q)}" if q else ""
        return f"hy2://{urllib.parse.quote(n['password'], safe='')}@{n['host']}:{n['port']}{tail}#{urllib.parse.quote(n['tag'], safe='')}"
    if k == "tuic":
        q.append(f"sni={n.get('sni') or ''}")
        tail = f"?{'&'.join(q)}"
        return f"tuic://{n['uuid']}:{n.get('password','')}@{n['host']}:{n['port']}{tail}#{urllib.parse.quote(n['tag'], safe='')}"
    if k == "vmess":
        j = {"v": "2", "ps": n["tag"], "add": n["host"], "port": str(n["port"]), "id": n["uuid"],
             "aid": str(n.get("aid", 0)), "scy": n.get("cipher", "auto"), "net": n.get("net", "tcp"),
             "type": "none", "host": n.get("ws_host", ""), "path": n.get("path", ""),
             "tls": "tls" if n.get("tls") else "", "sni": n.get("sni", "")}
        return "vmess://" + base64.b64encode(json.dumps(j, ensure_ascii=False).encode()).decode()
    return None


try:
    import yaml
except Exception:
    yaml = None


def write_clash(nodes, path):
    proxies = []
    for n in nodes:
        p = clash_proxy(n)
        if p:
            proxies.append(p)
    names = [p["name"] for p in proxies]
    data = {
        "mode": "rule",
        "log-level": "info",
        "allow-lan": False,
        "unified-delay": True,
        "tcp-concurrent": True,
        "dns": {"enable": True, "enhanced-mode": "fake-ip",
                "nameserver": ["1.1.1.1", "8.8.8.8"]},
        "proxies": proxies,
        "proxy-groups": [
            {"name": "AUTO", "type": "url-test", "url": "http://www.gstatic.com/generate_204",
             "interval": 300, "proxies": names},
            {"name": "SELECT", "type": "select", "proxies": ["AUTO"] + names},
        ],
        "rules": ["MATCH,SELECT"],
    }
    if yaml is not None:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    else:
        def line(v, ind):
            pad = "  " * (ind + 1)
            if isinstance(v, dict):
                out = []
                for k2, v2 in v.items():
                    out.append(("  " * ind) + f"{k2}: {line(v2, ind)}")
                return "\n" + "\n".join(out) if ind and out else "\n".join(out)
            if isinstance(v, list):
                if not v:
                    return "[]"
                out = []
                for item in v:
                    if isinstance(item, dict):
                        sub = "\n".join(f"{pad}  {k2}: {line(v2, ind + 1)}" for k2, v2 in item.items())
                        out.append(pad + "- " + sub.lstrip())
                    else:
                        out.append(pad + "- " + json.dumps(item, ensure_ascii=False))
                return "\n" + "\n".join(out)
            return json.dumps(v, ensure_ascii=False)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(f"{k}: {line(v, 0)}" for k, v in data.items()) + "\n")


def write_singbox(nodes, path):
    outs = [singbox_out(n) for n in nodes]
    tags = [o["tag"] for o in outs]
    auto = {"type": "urltest", "tag": "auto", "outbounds": tags,
            "url": "https://www.gstatic.com/generate_204", "interval": "5m"}
    sel = {"type": "selector", "tag": "select", "outbounds": ["auto"] + tags}
    data = {"outbounds": outs + [auto, sel, {"type": "direct", "tag": "direct"}],
            "route": {"final": "select"}}
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=2)
        f.write("\n")


def write_v2ray(nodes, path):
    uris = [u for u in (v2ray_uri(n) for n in nodes) if u]
    blob = base64.b64encode("\n".join(uris).encode()).decode()
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(blob + "\n")


def ensure_dir(p):
    os.makedirs(p, exist_ok=True)


def html_head(title, desc, keywords, path, lang="ru"):
    canonical = f"{SITE_BASE}/{path}"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="robots" content="index,follow">
<meta name="theme-color" content="#0f172a">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Бесплатные VPN-подписки">
<meta property="og:locale" content="ru">
<style>
  :root {{ color-scheme: dark; }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; font-family: -apple-system,Segoe UI,Roboto,sans-serif;
    background: linear-gradient(180deg,#0f172a,#1e293b 400px); color: #e2e8f0; line-height: 1.55; }}
  .hero {{ text-align: center; padding: 32px 20px; max-width: 900px; margin: 0 auto; }}
  h1 {{ font-size: clamp(28px, 5vw, 44px); margin: 0 0 12px; }}
  .sub {{ font-size: 18px; color: #cbd5e1; max-width: 680px; margin: 0 auto 16px; }}
  .meta {{ display: flex; justify-content: center; flex-wrap: wrap; gap: 8px; margin: 16px 0; }}
  .badge {{ display: inline-block; padding: 4px 12px; border-radius: 999px; font-size: 13px; font-weight: 600; }}
  .badge-green {{ background: #065f46; color: #d1fae5; }}
  .badge-blue {{ background: #1e40af; color: #dbeafe; }}
  .badge-gray {{ background: #374151; color: #d1d5db; }}
  .btn-outline {{ border: 1px solid #3b82f6; color: #93c5fd; padding: 10px 20px;
    border-radius: 8px; text-decoration: none; font-weight: 600; }}
  .breadcrumb {{ padding: 16px 32px; max-width: 900px; margin: 0 auto; }}
  .breadcrumb a {{ color: #93c5fd; text-decoration: none; font-size: 14px; }}
  .card {{ background: #1e293b; border: 1px solid #334155; border-radius: 12px;
    padding: 28px 32px; margin: 20px auto; max-width: 900px; }}
  .card h2 {{ margin-top: 0; font-size: 22px; color: #f1f5f9; }}
  .urls {{ display: flex; flex-direction: column; gap: 12px; margin-top: 16px; }}
  .url-row strong {{ color: #f1f5f9; font-size: 14px; }}
  .url-row code {{ display: block; background: #0f172a; padding: 10px 14px; border-radius: 6px;
    font-size: 13px; overflow-x: auto; border: 1px solid #334155; }}
  .url-row code a {{ color: #60a5fa; text-decoration: none; word-break: break-all; }}
  .country-grid {{ display: grid; gap: 12px; margin-top: 16px;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); }}
  .country-card {{ display: flex; flex-direction: column; align-items: center; gap: 4px;
    padding: 20px 12px; background: #0f172a; border: 1px solid #334155; border-radius: 10px;
    text-decoration: none; color: inherit; transition: border-color .2s, transform .1s; }}
  .country-card:hover {{ border-color: #3b82f6; transform: translateY(-2px); }}
  .country-flag {{ font-size: 32px; }}
  .country-name {{ font-weight: 600; color: #f1f5f9; font-size: 14px; }}
  .country-count {{ color: #94a3b8; font-size: 13px; }}
  .stat-grid {{ display: grid; grid-template-columns: repeat(4,minmax(0,1fr)); gap: 12px; margin: 20px 0; }}
  .stat-card {{ display: flex; flex-direction: column; gap: 2px; padding: 16px;
    background: #0f172a; border: 1px solid #334155; border-radius: 10px; }}
  .stat-card strong {{ color: #f8fafc; font-size: 24px; }}
  .stat-card span {{ color: #94a3b8; font-size: 13px; }}
  .metric-list {{ display: flex; flex-direction: column; gap: 8px; }}
  .metric-row {{ display: grid; grid-template-columns: minmax(0,1fr) auto 64px; gap: 12px;
    align-items: center; padding: 8px 10px; background: #0f172a; border-radius: 7px; color: #cbd5e1; }}
  .metric-row strong {{ color: #f8fafc; }}
  .metric-row span:last-child {{ text-align: right; color: #93c5fd; }}
  details {{ margin: 10px 0; padding: 12px 16px; background: #0f172a; border-radius: 8px; border: 1px solid #334155; }}
  details summary {{ cursor: pointer; font-weight: 600; color: #f1f5f9; }}
  details p {{ margin: 12px 0 0; color: #cbd5e1; }}
  .steps {{ padding-left: 24px; }}
  .steps li {{ margin-bottom: 18px; }}
  .steps h3 {{ margin: 0 0 6px; color: #f1f5f9; font-size: 16px; }}
  .steps p {{ margin: 0; color: #cbd5e1; }}
  footer {{ text-align: center; padding: 40px 20px; color: #94a3b8; font-size: 14px; }}
  footer a {{ color: #93c5fd; }}
  @media (max-width: 700px) {{
    .card {{ padding: 22px 18px; margin: 14px 12px; }}
    .stat-grid {{ grid-template-columns: repeat(2,minmax(0,1fr)); }}
  }}
</style>
</head>
<body>
"""


def url_row(label, url):
    return f'<div class="url-row"><strong>{label}</strong><code><a href="{url}" target="_blank" rel="noopener">{url}</a></code></div>'


def plural_ru(n, one, few, many):
    n %= 100
    if 11 <= n <= 14:
        return many
    d = n % 10
    if d == 1:
        return one
    if 2 <= d <= 4:
        return few
    return many


def gen_index(out, status, countries, protocols):
    total = status["selected"]
    ts = status["updated"]
    proto_txt = " · ".join(f"{PROTO_TITLES.get(p, p)} × {c}" for p, c in protocols)
    cards = "".join(
        f'<a class="country-card" href="{cc.lower()}.html">'
        f'<div class="country-flag">{flag(cc)}</div>'
        f'<div class="country-name">{country_name(cc)}</div>'
        f'<div class="country-count">{cnt} {plural_ru(cnt, "узел", "узла", "узлов")}</div></a>'
        for cc, cnt in countries)
    html = html_head(
        "Бесплатные VPN-подписки — Clash, sing-box, v2rayN",
        f"{total} бесплатных VPN-узлов, проверены TCP, обновление каждый час. Готовые подписки для Clash, sing-box и v2ray.",
        "бесплатный vpn, бесплатная подписка vpn, clash подписка, v2ray подписка, sing-box подписка, vless, hysteria2",
        "index.html")
    html += f"""
<header class="hero">
  <h1>Бесплатные VPN-подписки ⚡</h1>
  <p class="sub">Скопируйте ссылку подписки, вставьте в клиент и подключитесь. Без регистрации, без оплаты. Обновление каждый час из публичных источников.</p>
  <p class="meta">
    <span class="badge badge-green">{total} {plural_ru(total, "узел", "узла", "узлов")}</span>
    <span class="badge badge-blue">обновлено · {ts} UTC</span>
  </p>
  <p><a class="btn-outline" href="https://github.com/{OWNER}/{REPO}" target="_blank" rel="noopener">GitHub-репозиторий →</a></p>
</header>

<section class="card">
  <h2>🚀 Подписка в один клик</h2>
  <div class="urls">
    {url_row("Clash / Clash Verge / ClashX", f"{RAW_BASE}/clash.yaml")}
    {url_row("sing-box", f"{RAW_BASE}/singbox.json")}
    {url_row("v2rayN / v2rayNG / Shadowrocket / NekoBox", f"{RAW_BASE}/v2ray-base64.txt")}
  </div>
</section>

<section class="card">
  <h2>📊 Статистика</h2>
  <div class="stat-grid">
    <div class="stat-card"><strong>{total}</strong><span>отобранных узлов</span></div>
    <div class="stat-card"><strong>{status['alive']}</strong><span>живых по TCP</span></div>
    <div class="stat-card"><strong>{status['raw']}</strong><span>записей из источников</span></div>
    <div class="stat-card"><strong>{status['median']} ms</strong><span>медиана RTT</span></div>
  </div>
  <p><strong>Протоколы:</strong> {proto_txt}</p>
</section>

<section class="card">
  <h2>🌍 По странам</h2>
  <div class="country-grid">
{cards}
  </div>
</section>

<section class="card">
  <h2>📖 Как подключить</h2>
  <div class="urls">
    <div class="url-row"><strong>Clash Verge — Windows / macOS / Linux</strong><code><a href="guides/clash-verge.html">guides/clash-verge.html</a></code></div>
    <div class="url-row"><strong>v2rayNG — Android</strong><code><a href="guides/v2rayng.html">guides/v2rayng.html</a></code></div>
    <div class="url-row"><strong>Shadowrocket — iOS</strong><code><a href="guides/shadowrocket.html">guides/shadowrocket.html</a></code></div>
    <div class="url-row"><strong>sing-box — все платформы</strong><code><a href="guides/sing-box.html">guides/sing-box.html</a></code></div>
  </div>
</section>

<section class="card">
  <h2>❓ Частые вопросы</h2>
  <details><summary>Это правда бесплатно?</summary>
    <p>Да. Узлы публикуются волонтёрами в открытых источниках. Мы только собираем, проверяем и переупаковываем их.</p></details>
  <details><summary>Как часто обновляется?</summary>
    <p>Каждый час (GitHub Actions): загрузка источников → проверка TCP → GeoIP → публикация файлов. См. метку «обновлено» выше.</p></details>
  <details><summary>Почему узлы иногда не работают?</summary>
    <p>Бесплатные узлы живут минуты. В clash.yaml есть группа url-test — клиент сам выбирает самый быстрый рабочий узел и переключается при падении.</p></details>
  <details><summary>Безопасно ли это?</summary>
    <p>Узел видит весь ваш трафик. Никогда не используйте бесплатные узлы для банкинга и логинов — только для смены гео-локации на публичном контенте.</p></details>
</section>

<footer>
  <p>Навигация: <a href="https://github.com/{OWNER}/{REPO}">GitHub</a> · <a href="{SITE_BASE}/index.html">Все страны</a></p>
</footer>
</body>
</html>
"""
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


def gen_country_page(out, cc, count, protocols, others, status):
    ts = status["updated"]
    name = country_name(cc)
    proto_rows = "".join(
        f'<div class="metric-row"><span>{PROTO_TITLES.get(p, p)}</span><strong>{c}</strong>'
        f'<span>{c * 100 // max(count, 1)}%</span></div>'
        for p, c in protocols[:8])
    other_cards = "".join(
        f'<a class="country-card" href="{c2.lower()}.html">'
        f'<div class="country-flag">{flag(c2)}</div>'
        f'<div class="country-name">{country_name(c2)}</div>'
        f'<div class="country-count">{c3} {plural_ru(c3, "узел", "узла", "узлов")}</div></a>'
        for c2, c3 in others[:32])
    path = f"{cc.lower()}.html"
    html = html_head(
        f"Бесплатная VPN-подписка {name}",
        f"{count} бесплатных VPN-узлов в {name}, проверены TCP, обновление каждый час. Готовые подписки для Clash, sing-box и v2ray.",
        f"бесплатный vpn {name.lower()}, подписка vpn {name.lower()}, clash, v2ray, прокси",
        path)
    html += f"""
<nav class="breadcrumb"><a href="{SITE_BASE}/index.html">← Все страны</a></nav>

<header class="hero">
  <h1>Бесплатная VPN-подписка {flag(cc)} {name}</h1>
  <p class="sub">{count} бесплатных VPN-узлов в {name}, проверены TCP, обновление каждый час.</p>
  <p class="meta">
    <span class="badge badge-green">{count} {plural_ru(count, "узел", "узла", "узлов")}</span>
    <span class="badge badge-gray">обновлено · {ts} UTC</span>
  </p>
</header>

<section class="card">
  <h2>🚀 Подписаться только на узлы {name}</h2>
  <div class="urls">
    {url_row("Clash / Clash Verge / ClashX", f"{RAW_BASE}/by-country/clash-{cc}.yaml")}
    {url_row("sing-box", f"{RAW_BASE}/by-country/singbox-{cc}.json")}
    {url_row("v2rayN / v2rayNG / Shadowrocket / NekoBox", f"{RAW_BASE}/by-country/v2ray-base64-{cc}.txt")}
  </div>
</section>

<section class="card">
  <h2>Протоколы ({name})</h2>
  <div class="metric-list">{proto_rows}</div>
</section>

<section class="card">
  <h2>🌍 Другие страны</h2>
  <div class="country-grid">{other_cards}</div>
</section>

<footer>
  <p><a href="https://github.com/{OWNER}/{REPO}">GitHub</a> · <a href="{SITE_BASE}/index.html">Главная</a></p>
</footer>
</body>
</html>
"""
    with open(os.path.join(out, path), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


GUIDES = {
    "clash-verge": ("Clash Verge", """<ol class="steps">
<li><h3>1. Скачайте Clash Verge Rev</h3><p>Возьмите свежий установщик на странице релизов проекта clash-verge-rev (GitHub) или с официального сайта.</p></li>
<li><h3>2. Установите и откройте</h3><p>Запустите приложение. Убедитесь, что включён режим ядра mihomo (Clash Meta).</p></li>
<li><h3>3. Импортируйте подписку</h3><p>Откройте «Профили» → «Импорт из URL» и вставьте ссылку <b>clash.yaml</b> отсюда. Нажмите Enter.</p></li>
<li><h3>4. Обновите профиль</h3><p>Кликните по карточке профиля — список узлов загрузится автоматически.</p></li>
<li><h3>5. Включите прокси</h3><p>На вкладке «Прокси» выберите группу <b>SELECT</b> или <b>AUTO</b>. AUTO сама выбирает самый быстрый живой узел.</p></li>
<li><h3>6. Проверьте</h3><p>Откройте любой сайт с проверкой геолокации. Готово.</p></li>
</ol>"""),
    "v2rayng": ("v2rayNG", """<ol class="steps">
<li><h3>1. Установите v2rayNG</h3><p>Скачайте APK с релизов GitHub-репозитория 2dust/v2rayNG или из Google Play.</p></li>
<li><h3>2. Добавьте подписку</h3><p>Меню (⋮) → «Подписки» → «+» → вставьте ссылку <b>v2ray-base64.txt</b> и сохраните.</p></li>
<li><h3>3. Обновите</h3><p>Потяните список вниз (обновить подписку) — появятся узлы.</p></li>
<li><h3>4. Выберите узел</h3><p>Нажмите «Проверить подключение» у нескольких узлов и выберите с низкой задержкой.</p></li>
<li><h3>5. Запустите</h3><p>Нажмите кнопку V в нижней части экрана и разрешите VPN-подключение.</p></li>
</ol>"""),
    "shadowrocket": ("Shadowrocket", """<ol class="steps">
<li><h3>1. Установите Shadowrocket</h3><p>Приложение доступно в App Store (платное, одно покупка — навсегда).</p></li>
<li><h3>2. Добавьте подписку</h3><p>Вкладка «Подписки» → «+» → вставьте ссылку <b>v2ray-base64.txt</b> → «Сохранить».</p></li>
<li><h3>3. Обновите</h3><p>Потяните список вниз, чтобы загрузить узлы.</p></li>
<li><h3>4. Подключитесь</h3><p>Выберите узел и нажмите кнопку «Подключить». Разрешите VPN-конфигурацию iOS.</p></li>
<li><h3>5. Проверьте</h3><p>Откройте сайт с проверкой IP — страна должна измениться.</p></li>
</ol>"""),
    "sing-box": ("sing-box", """<ol class="steps">
<li><h3>1. Скачайте sing-box</h3><p>Windows/macOS/Linux/iOS/Android — берите релиз с GitHub SagerNet/sing-box (или sing-boxSFI/شی روی iOS).</p></li>
<li><h3>2. Создайте профиль</h3><p>В приложении: «Профили» → «Создать» → тип «Удалённый».</p></li>
<li><h3>3. Вставьте ссылку</h3><p>Укажите адрес <b>singbox.json</b> отсюда и нажмите «Создать».</p></li>
<li><h3>4. Обновите профиль</h3><p>Перезагрузите профиль — появятся группа <b>select</b> со всеми узлами.</p></li>
<li><h3>5. Запустите</h3><p>Выберите группу «select» (или «auto» для авто-выбора) и включите туннель.</p></li>
</ol>"""),
}


def gen_guides(out):
    gdir = os.path.join(out, "guides")
    ensure_dir(gdir)
    for slug, (name, body) in GUIDES.items():
        path = f"guides/{slug}.html"
        html = html_head(
            f"Как подключить бесплатный VPN в {name}",
            f"Пошаговая инструкция: бесплатная VPN-подписка для {name}. Импорт ссылки, выбор узла, подключение.",
            f"{name} бесплатно, vpn {name}, бесплатная подписка, инструкция",
            path)
        raw = RAW_BASE + "/clash.yaml" if "clash" in slug else (RAW_BASE + "/singbox.json" if "sing-box" in slug else RAW_BASE + "/v2ray-base64.txt")
        html += f"""
<nav class="breadcrumb"><a href="{SITE_BASE}/index.html">← На главную</a></nav>
<header class="hero">
  <h1>{name} — подключение за 5 минут</h1>
  <p class="sub">Используйте эту бесплатную подписку: <code style="word-break:break-all">{raw}</code></p>
</header>
<section class="card"><h2>Пошагово</h2>{body}</section>
<footer><p><a href="{SITE_BASE}/index.html">Бесплатные VPN-подписки</a></p></footer>
</body>
</html>
"""
        with open(os.path.join(out, path), "w", encoding="utf-8", newline="\n") as f:
            f.write(html)


def gen_readme(status, countries):
    ts = status["updated"]
    proto_txt = " · ".join(f"{PROTO_TITLES.get(p, p)} × {c}" for p, c in status["protocol_distrib"])
    rows = "\n".join(
        f"| {flag(cc)} {country_name(cc)} (`{cc}`) | {cnt} | [clash-{cc}.yaml]({RAW_BASE}/by-country/clash-{cc}.yaml) | "
        f"[singbox-{cc}.json]({RAW_BASE}/by-country/singbox-{cc}.json) | [v2ray-base64-{cc}.txt]({RAW_BASE}/by-country/v2ray-base64-{cc}.txt) |"
        for cc, cnt in countries)
    return f"""# Бесплатные VPN-подписки (Free VPN Subscriptions)

> **Самый простой способ получить рабочий бесплатный VPN — скопируйте ссылку подписки, вставьте в клиент, подключитесь.**
> Без регистрации. Без оплаты. Обновляется каждый час из публичных источников — TCP-проверка каждого узла перед публикацией.

[![обновлено](https://img.shields.io/badge/обновлено-{ts.replace(' ', '_').replace(':', '-').replace('-', '--')}--UTC-informational)]({SITE_BASE}/index.html) [![узлов](https://img.shields.io/badge/узлов-{status['selected']}-brightgreen)]({SITE_BASE}/index.html) [![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/{OWNER}/{REPO}/blob/main/LICENSE)

> бесплатный VPN · бесплатная подписка VPN · бесплатный прокси · Clash подписка · v2ray подписка · sing-box подписка · VLESS · Reality · VMess · Trojan · Shadowsocks · Hysteria2 · обновление каждый час · по стране

## 🚀 Подписка в один клик

Скопируйте URL, соответствующий вашему клиенту, и вставьте его в поле импорта подписки:

| Клиент | Формат | URL подписки |
|---|---|---|
| Clash / Clash Verge / ClashX | `clash.yaml` | `{RAW_BASE}/clash.yaml` |
| sing-box | `singbox.json` | `{RAW_BASE}/singbox.json` |
| v2rayN / v2rayNG / Shadowrocket / NekoBox | `v2ray-base64` | `{RAW_BASE}/v2ray-base64.txt` |

Разрезанные по частям подписки (protocol / country / network): [output/](https://github.com/{OWNER}/{REPO}/tree/main/output)

## 🔬 Как мы проверяем узлы

1. **Загрузка источников** — собранные публичные списки подписок (Telegram-агрегаторы, открытые репозитории).
2. **Дедупликация и валидация** — битые, дублирующиеся и нестандартные записи отбрасываются.
3. **TCP-доступность** — к каждому `server:port` открывается реальное TCP-соединение; мёртвые хосты и неверный DNS отбрасываются. Для чисто UDP-протоколов (Hysteria2, TUIC) проверяется разрешение имени.
4. **GeoIP-классификация** — по выходному IP определяется страна и тип сети (ISP / hosting / cloud).
5. **Ранжирование по реальной RTT** — узлы сортируются по фактической задержке TCP-соединения; публикуются лучшие.

Клиентская страховка: публикуемый `clash.yaml` содержит группу `url-test`, которая каждые 5 минут перепроверяет узлы прямо на вашем устройстве и автоматически переключается на живой.

## 🌍 По странам

| Страна | Узлов | Clash | sing-box | v2ray |
|---|---|---|---|---|
{rows}

Полный список страниц по странам: [сайт]({SITE_BASE}/index.html)

## 📖 Пошаговые инструкции

- [**Clash Verge**]({SITE_BASE}/guides/clash-verge.html) · Windows / macOS / Linux
- [**v2rayNG**]({SITE_BASE}/guides/v2rayng.html) · Android
- [**Shadowrocket**]({SITE_BASE}/guides/shadowrocket.html) · iOS / iPadOS
- [**sing-box**]({SITE_BASE}/guides/sing-box.html) · все платформы

## 🧩 Поддерживаемые клиенты

- **Windows**: v2rayN, Clash Verge, Hiddify, NekoRay
- **macOS**: ClashX Pro, Clash Verge, sing-box, Hiddify
- **iOS**: Shadowrocket, Stash, Loon, sing-box, Hiddify
- **Android**: v2rayNG, NekoBox, Clash Meta for Android, Hiddify, sing-box
- **Linux**: mihomo (Clash.Meta), sing-box, v2ray-core

## 📊 Статистика

- **Выбрано узлов**: {status['selected']}
- **Живых по TCP**: {status['alive']}
- **Записей из источников**: {status['raw']}
- **Медиана RTT**: {status['median']} ms
- **Последнее обновление (UTC)**: {ts} UTC

**Распределение протоколов:** {proto_txt}

## ❓ Часто задаваемые вопросы

<details><summary>Это правда бесплатно?</summary>

Да. Узлы публикуются волонтёрами в открытых источниках. Этот репозиторий только агрегирует, проверяет и переупаковывает публичные данные.

</details>

<details><summary>Можно ли доверять этим узлам?</summary>

Бесплатные узлы видят весь ваш трафик. **Никогда не используйте их для банкинга, логинов или чувствительных данных.** Для реальной приватности используйте свой VPS.

</details>

<details><summary>Почему некоторые узлы не работают?</summary>

Бесплатные узлы умирают за минуты. Группа `url-test` в опубликованном `clash.yaml` автоматически переключает вас на следующий живой узел.

</details>

## ⚠️ Отказ от ответственности

Этот репозиторий агрегирует **публично доступные** конфигурации прокси от третьих лиц. Мы не управляем серверами, не гарантируем доступность и безопасность. Предназначено для образовательных и личных целей. Соблюдайте законы вашей юрисдикции.

---

Если проект вам помог — поставьте ⭐.
"""


def write_status(data_dir, status, history):
    ensure_dir(data_dir)
    with open(os.path.join(data_dir, "status.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(status, f, ensure_ascii=False, sort_keys=True, indent=2)
        f.write("\n")
    with open(os.path.join(data_dir, "network-history.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(history, f, ensure_ascii=False, sort_keys=True, indent=2)
        f.write("\n")


def write_sitemap(out, countries):
    urls = [f"{SITE_BASE}/index.html"] + [f"{SITE_BASE}/{cc.lower()}.html" for cc, _ in countries] + \
           [f"{SITE_BASE}/guides/{s}.html" for s in GUIDES]
    body = "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" + \
           "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls) + "\n</urlset>\n"
    with open(os.path.join(out, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write(body)
    with open(os.path.join(out, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_BASE}/sitemap.xml\n")


def shard(nodes, key_dir, group_dirs):
    for fmt in ("clash", "singbox", "v2ray-base64"):
        groups = {}
        for n in nodes:
            g = group_dirs(n)
            groups.setdefault(g, []).append(n)
        for g, ns in groups.items():
            d = os.path.join(key_dir, fmt, g)
            ensure_dir(d)
            for i in range(0, len(ns), MAX_SHARD):
                chunk = ns[i:i + MAX_SHARD]
                num = f"{i // MAX_SHARD + 1:04d}"
                fn = f"{fmt}-{num}." + ("yaml" if fmt == "clash" else ("json" if fmt == "singbox" else "txt"))
                fp = os.path.join(d, fn)
                if fmt == "clash":
                    write_clash(chunk, fp)
                elif fmt == "singbox":
                    write_singbox(chunk, fp)
                else:
                    write_v2ray(chunk, fp)


def main():
    ts = now_utc()
    ts_str = ts.strftime("%Y-%m-%d %H:%M")
    out_dir = os.path.join(ROOT, "output")
    docs_dir = os.path.join(ROOT, "docs")
    ensure_dir(out_dir)
    ensure_dir(docs_dir)

    raw_nodes = collect_nodes()
    if not raw_nodes:
        print("[error] нет ни одного узла из источников")
        sys.exit(1)

    print(f"[check] TCP-проверка {len(raw_nodes)} узлов...")
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=TCP_THREADS) as ex:
        for key, ok, rtt in ex.map(check_tcp, raw_nodes):
            results[key] = (ok, rtt)
    alive_nodes = [n for n in raw_nodes if results[n["key"]][0]]
    for n in alive_nodes:
        n["rtt"] = results[n["key"]][1]
    print(f"[check] живых узлов: {len(alive_nodes)} из {len(raw_nodes)}")

    ips = [n["host"] for n in alive_nodes if re.match(r"^\d+\.\d+\.\d+\.\d+$", n["host"])]
    geo = geo_lookup(ips) if ips else {}
    for n in alive_nodes:
        info = geo.get(n["host"], {"cc": "", "country": "", "isp": "", "hosting": False})
        n["geo"] = info

    alive_nodes.sort(key=lambda n: n["rtt"] if n["rtt"] >= 0 else 10000 + random.randrange(500))
    selected = alive_nodes[:MAX_SELECTED]
    for n in alive_nodes:
        n["_cc"] = n["geo"].get("cc") or "XX"
    country_counts = {}
    country_counts = {}
    for n in selected:
        cc = n["geo"].get("cc") or "XX"
        n["_cc"] = cc
        country_counts[cc] = country_counts.get(cc, 0) + 1
    countries = sorted(country_counts.items(), key=lambda x: -x[1])

    proto_distrib = {}
    for n in alive_nodes:
        proto_distrib[n["kind"]] = proto_distrib.get(n["kind"], 0) + 1
    proto_distrib = sorted(proto_distrib.items(), key=lambda x: -x[1])

    rtts = sorted(n["rtt"] for n in alive_nodes if n["rtt"] >= 0)
    median = int(statistics.median(rtts)) if rtts else 0

    # --- stable: узлы, живые в двух последних запусках ---
    state_path = os.path.join(docs_dir, "data", "state.json")
    prev_keys = set()
    try:
        with open(state_path, encoding="utf-8") as f:
            prev_keys = set(json.load(f).get("alive", []))
    except Exception:
        pass
    cur_keys = {n["key"] for n in alive_nodes}
    stable = [n for n in alive_nodes if n["key"] in prev_keys][:600]

    ensure_dir(os.path.dirname(state_path))
    with open(state_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"alive": sorted(cur_keys)[:5000], "ts": ts_str}, f)

    write_clash(selected, os.path.join(out_dir, "clash.yaml"))
    write_singbox(selected, os.path.join(out_dir, "singbox.json"))
    write_v2ray(selected, os.path.join(out_dir, "v2ray-base64.txt"))

    for fmt in ("clash", "singbox", "v2ray-base64"):
        d = os.path.join(out_dir, "by-country")
        ensure_dir(d)
        for cc, _ in countries:
            ns = [n for n in alive_nodes if n["geo"].get("cc") == cc]
            if not ns:
                continue
            fp = os.path.join(d, f"{fmt}-{cc}." + ("yaml" if fmt == "clash" else ("json" if fmt == "singbox" else "txt")))
            if fmt == "clash":
                write_clash(ns, fp)
            elif fmt == "singbox":
                write_singbox(ns, fp)
            else:
                write_v2ray(ns, fp)

    shard(alive_nodes, os.path.join(out_dir, "country"), lambda n: n["_cc"])
    shard(alive_nodes, os.path.join(out_dir, "protocol"), lambda n: n["kind"])
    shard(alive_nodes, os.path.join(out_dir, "network"), lambda n: net_group(n["geo"]))
    if stable:
        for fmt in ("clash", "singbox", "v2ray-base64"):
            d = os.path.join(out_dir, "stable")
            ensure_dir(d)
            idx = 0
            for i in range(0, len(stable), MAX_SHARD):
                chunk = stable[i:i + MAX_SHARD]
                num = f"{i // MAX_SHARD + 1:04d}"
                fn = f"{fmt}-{num}." + ("yaml" if fmt == "clash" else ("json" if fmt == "singbox" else "txt"))
                fp = os.path.join(d, fn)
                if fmt == "clash":
                    write_clash(chunk, fp)
                elif fmt == "singbox":
                    write_singbox(chunk, fp)
                else:
                    write_v2ray(chunk, fp)

    # --- сайт ---
    status = {"updated": ts_str, "raw": len(raw_nodes), "alive": len(alive_nodes),
              "selected": len(selected), "median": median, "protocol_distrib": proto_distrib,
              "countries": countries}
    gen_index(docs_dir, status, countries, proto_distrib)
    for i, (cc, cnt) in enumerate(countries):
        proto_cc = {}
        for n in alive_nodes:
            if n["geo"].get("cc") == cc:
                proto_cc[n["kind"]] = proto_cc.get(n["kind"], 0) + 1
        proto_cc = sorted(proto_cc.items(), key=lambda x: -x[1])
        others = [c for c in countries if c[0] != cc]
        gen_country_page(docs_dir, cc, cnt, proto_cc, others, status)
    gen_guides(docs_dir)
    write_sitemap(docs_dir, countries)

    net_hist = {"ts": ts_str}
    for grp in ("cloud", "hosting", "isp", "unknown"):
        net_hist[grp] = sum(1 for n in alive_nodes if net_group(n["geo"]) == grp)
    write_status(os.path.join(docs_dir, "data"), status, net_hist)

    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(gen_readme(status, countries))

    print(f"[done] обновлено {ts_str} UTC · выбрано {len(selected)} · живых {len(alive_nodes)} · стран {len(countries)}")


if __name__ == "__main__":
    main()
