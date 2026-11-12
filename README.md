# Бесплатные VPN-подписки (Free VPN Subscriptions)

> **Самый простой способ получить рабочий бесплатный VPN — скопируйте ссылку подписки, вставьте в клиент, подключитесь.**
> Без регистрации. Без оплаты. Обновляется каждый час из публичных источников — TCP-проверка каждого узла перед публикацией.

[![обновлено](https://img.shields.io/badge/обновлено-2026--11--12_20--00--UTC-informational)](https://lorenzazy7kenyon.github.io/free-vpn-subscriptions/index.html) [![узлов](https://img.shields.io/badge/узлов-681-brightgreen)](https://lorenzazy7kenyon.github.io/free-vpn-subscriptions/index.html) [![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/blob/main/LICENSE)

> бесплатный VPN · бесплатная подписка VPN · бесплатный прокси · Clash подписка · v2ray подписка · sing-box подписка · VLESS · Reality · VMess · Trojan · Shadowsocks · Hysteria2 · обновление каждый час · по стране

## 🚀 Подписка в один клик

Скопируйте URL, соответствующий вашему клиенту, и вставьте его в поле импорта подписки:

| Клиент | Формат | URL подписки |
|---|---|---|
| Clash / Clash Verge / ClashX | `clash.yaml` | `https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/clash.yaml` |
| sing-box | `singbox.json` | `https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/singbox.json` |
| v2rayN / v2rayNG / Shadowrocket / NekoBox | `v2ray-base64` | `https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/v2ray-base64.txt` |

Разрезанные по частям подписки (protocol / country / network): [output/](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/tree/main/output)

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
| 🇽🇽 XX (`XX`) | 138 | [clash-XX.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-XX.yaml) | [singbox-XX.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-XX.json) | [v2ray-base64-XX.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-XX.txt) |
| 🇺🇸 США (`US`) | 98 | [clash-US.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-US.yaml) | [singbox-US.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-US.json) | [v2ray-base64-US.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-US.txt) |
| 🇳🇱 Нидерланды (`NL`) | 64 | [clash-NL.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-NL.yaml) | [singbox-NL.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-NL.json) | [v2ray-base64-NL.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-NL.txt) |
| 🇨🇦 Канада (`CA`) | 51 | [clash-CA.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-CA.yaml) | [singbox-CA.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-CA.json) | [v2ray-base64-CA.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-CA.txt) |
| 🇩🇪 Германия (`DE`) | 37 | [clash-DE.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-DE.yaml) | [singbox-DE.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-DE.json) | [v2ray-base64-DE.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-DE.txt) |
| 🇪🇸 Испания (`ES`) | 26 | [clash-ES.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-ES.yaml) | [singbox-ES.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-ES.json) | [v2ray-base64-ES.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-ES.txt) |
| 🇯🇵 Япония (`JP`) | 24 | [clash-JP.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-JP.yaml) | [singbox-JP.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-JP.json) | [v2ray-base64-JP.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-JP.txt) |
| 🇫🇷 Франция (`FR`) | 24 | [clash-FR.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-FR.yaml) | [singbox-FR.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-FR.json) | [v2ray-base64-FR.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-FR.txt) |
| 🇬🇧 Великобритания (`GB`) | 23 | [clash-GB.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-GB.yaml) | [singbox-GB.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-GB.json) | [v2ray-base64-GB.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-GB.txt) |
| 🇸🇬 Сингапур (`SG`) | 23 | [clash-SG.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-SG.yaml) | [singbox-SG.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-SG.json) | [v2ray-base64-SG.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SG.txt) |
| 🇭🇰 Гонконг (`HK`) | 22 | [clash-HK.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-HK.yaml) | [singbox-HK.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-HK.json) | [v2ray-base64-HK.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-HK.txt) |
| 🇷🇺 Россия (`RU`) | 22 | [clash-RU.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-RU.yaml) | [singbox-RU.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-RU.json) | [v2ray-base64-RU.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-RU.txt) |
| 🇵🇱 Польша (`PL`) | 16 | [clash-PL.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-PL.yaml) | [singbox-PL.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-PL.json) | [v2ray-base64-PL.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-PL.txt) |
| 🇮🇹 Италия (`IT`) | 15 | [clash-IT.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-IT.yaml) | [singbox-IT.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-IT.json) | [v2ray-base64-IT.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-IT.txt) |
| 🇸🇪 Швеция (`SE`) | 11 | [clash-SE.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-SE.yaml) | [singbox-SE.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-SE.json) | [v2ray-base64-SE.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SE.txt) |
| 🇰🇷 Корея (`KR`) | 8 | [clash-KR.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-KR.yaml) | [singbox-KR.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-KR.json) | [v2ray-base64-KR.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-KR.txt) |
| 🇨🇭 Швейцария (`CH`) | 8 | [clash-CH.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-CH.yaml) | [singbox-CH.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-CH.json) | [v2ray-base64-CH.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-CH.txt) |
| 🇫🇮 Финляндия (`FI`) | 7 | [clash-FI.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-FI.yaml) | [singbox-FI.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-FI.json) | [v2ray-base64-FI.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-FI.txt) |
| 🇹🇷 Турция (`TR`) | 5 | [clash-TR.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-TR.yaml) | [singbox-TR.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-TR.json) | [v2ray-base64-TR.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-TR.txt) |
| 🇱🇻 Латвия (`LV`) | 4 | [clash-LV.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-LV.yaml) | [singbox-LV.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-LV.json) | [v2ray-base64-LV.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-LV.txt) |
| 🇧🇾 Беларусь (`BY`) | 4 | [clash-BY.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-BY.yaml) | [singbox-BY.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-BY.json) | [v2ray-base64-BY.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-BY.txt) |
| 🇬🇷 Греция (`GR`) | 4 | [clash-GR.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-GR.yaml) | [singbox-GR.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-GR.json) | [v2ray-base64-GR.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-GR.txt) |
| 🇺🇦 Украина (`UA`) | 4 | [clash-UA.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-UA.yaml) | [singbox-UA.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-UA.json) | [v2ray-base64-UA.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-UA.txt) |
| 🇮🇳 Индия (`IN`) | 4 | [clash-IN.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-IN.yaml) | [singbox-IN.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-IN.json) | [v2ray-base64-IN.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-IN.txt) |
| 🇹🇼 Тайвань (`TW`) | 3 | [clash-TW.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-TW.yaml) | [singbox-TW.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-TW.json) | [v2ray-base64-TW.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-TW.txt) |
| 🇷🇴 Румыния (`RO`) | 3 | [clash-RO.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-RO.yaml) | [singbox-RO.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-RO.json) | [v2ray-base64-RO.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-RO.txt) |
| 🇲🇽 Мексика (`MX`) | 2 | [clash-MX.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-MX.yaml) | [singbox-MX.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-MX.json) | [v2ray-base64-MX.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-MX.txt) |
| 🇮🇪 IE (`IE`) | 2 | [clash-IE.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-IE.yaml) | [singbox-IE.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-IE.json) | [v2ray-base64-IE.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-IE.txt) |
| 🇨🇿 Чехия (`CZ`) | 2 | [clash-CZ.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-CZ.yaml) | [singbox-CZ.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-CZ.json) | [v2ray-base64-CZ.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-CZ.txt) |
| 🇦🇹 Австрия (`AT`) | 2 | [clash-AT.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-AT.yaml) | [singbox-AT.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-AT.json) | [v2ray-base64-AT.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-AT.txt) |
| 🇦🇺 Австралия (`AU`) | 2 | [clash-AU.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-AU.yaml) | [singbox-AU.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-AU.json) | [v2ray-base64-AU.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-AU.txt) |
| 🇲🇾 Малайзия (`MY`) | 2 | [clash-MY.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-MY.yaml) | [singbox-MY.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-MY.json) | [v2ray-base64-MY.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-MY.txt) |
| 🇦🇱 Албания (`AL`) | 2 | [clash-AL.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-AL.yaml) | [singbox-AL.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-AL.json) | [v2ray-base64-AL.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-AL.txt) |
| 🇻🇳 Вьетнам (`VN`) | 2 | [clash-VN.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-VN.yaml) | [singbox-VN.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-VN.json) | [v2ray-base64-VN.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-VN.txt) |
| 🇦🇪 ОАЭ (`AE`) | 2 | [clash-AE.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-AE.yaml) | [singbox-AE.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-AE.json) | [v2ray-base64-AE.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-AE.txt) |
| 🇿🇦 ЮАР (`ZA`) | 2 | [clash-ZA.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-ZA.yaml) | [singbox-ZA.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-ZA.json) | [v2ray-base64-ZA.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-ZA.txt) |
| 🇧🇪 Бельгия (`BE`) | 1 | [clash-BE.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-BE.yaml) | [singbox-BE.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-BE.json) | [v2ray-base64-BE.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-BE.txt) |
| 🇳🇴 Норвегия (`NO`) | 1 | [clash-NO.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-NO.yaml) | [singbox-NO.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-NO.json) | [v2ray-base64-NO.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-NO.txt) |
| 🇨🇱 CL (`CL`) | 1 | [clash-CL.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-CL.yaml) | [singbox-CL.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-CL.json) | [v2ray-base64-CL.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-CL.txt) |
| 🇪🇪 Эстония (`EE`) | 1 | [clash-EE.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-EE.yaml) | [singbox-EE.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-EE.json) | [v2ray-base64-EE.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-EE.txt) |
| 🇱🇹 Литва (`LT`) | 1 | [clash-LT.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-LT.yaml) | [singbox-LT.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-LT.json) | [v2ray-base64-LT.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-LT.txt) |
| 🇧🇷 Бразилия (`BR`) | 1 | [clash-BR.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-BR.yaml) | [singbox-BR.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-BR.json) | [v2ray-base64-BR.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-BR.txt) |
| 🇸🇮 SI (`SI`) | 1 | [clash-SI.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-SI.yaml) | [singbox-SI.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-SI.json) | [v2ray-base64-SI.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SI.txt) |
| 🇧🇬 Болгария (`BG`) | 1 | [clash-BG.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-BG.yaml) | [singbox-BG.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-BG.json) | [v2ray-base64-BG.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-BG.txt) |
| 🇮🇱 IL (`IL`) | 1 | [clash-IL.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-IL.yaml) | [singbox-IL.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-IL.json) | [v2ray-base64-IL.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-IL.txt) |
| 🇳🇪 NE (`NE`) | 1 | [clash-NE.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-NE.yaml) | [singbox-NE.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-NE.json) | [v2ray-base64-NE.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-NE.txt) |
| 🇸🇦 Саудовская Аравия (`SA`) | 1 | [clash-SA.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-SA.yaml) | [singbox-SA.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-SA.json) | [v2ray-base64-SA.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SA.txt) |
| 🇰🇿 Казахстан (`KZ`) | 1 | [clash-KZ.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-KZ.yaml) | [singbox-KZ.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-KZ.json) | [v2ray-base64-KZ.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-KZ.txt) |
| 🇮🇷 Иран (`IR`) | 1 | [clash-IR.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-IR.yaml) | [singbox-IR.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-IR.json) | [v2ray-base64-IR.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-IR.txt) |

Полный список страниц по странам: [сайт](https://lorenzazy7kenyon.github.io/free-vpn-subscriptions/index.html)

## 📖 Пошаговые инструкции

- [**Clash Verge**](https://lorenzazy7kenyon.github.io/free-vpn-subscriptions/guides/clash-verge.html) · Windows / macOS / Linux
- [**v2rayNG**](https://lorenzazy7kenyon.github.io/free-vpn-subscriptions/guides/v2rayng.html) · Android
- [**Shadowrocket**](https://lorenzazy7kenyon.github.io/free-vpn-subscriptions/guides/shadowrocket.html) · iOS / iPadOS
- [**sing-box**](https://lorenzazy7kenyon.github.io/free-vpn-subscriptions/guides/sing-box.html) · все платформы

## 🧩 Поддерживаемые клиенты

- **Windows**: v2rayN, Clash Verge, Hiddify, NekoRay
- **macOS**: ClashX Pro, Clash Verge, sing-box, Hiddify
- **iOS**: Shadowrocket, Stash, Loon, sing-box, Hiddify
- **Android**: v2rayNG, NekoBox, Clash Meta for Android, Hiddify, sing-box
- **Linux**: mihomo (Clash.Meta), sing-box, v2ray-core

## 📊 Статистика

- **Выбрано узлов**: 681
- **Живых по TCP**: 681
- **Записей из источников**: 868
- **Медиана RTT**: 146 ms
- **Последнее обновление (UTC)**: 2026-11-12 20:00 UTC

**Распределение протоколов:** VLESS × 308 · ss × 189 · VMess × 105 · Trojan × 43 · Hysteria2 × 36

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
