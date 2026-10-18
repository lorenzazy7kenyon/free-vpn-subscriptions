# Бесплатные VPN-подписки (Free VPN Subscriptions)

> **Самый простой способ получить рабочий бесплатный VPN — скопируйте ссылку подписки, вставьте в клиент, подключитесь.**
> Без регистрации. Без оплаты. Обновляется каждый час из публичных источников — TCP-проверка каждого узла перед публикацией.

[![обновлено](https://img.shields.io/badge/обновлено-2026--10--18_09--00--UTC-informational)](https://lorenzazy7kenyon.github.io/free-vpn-subscriptions/index.html) [![узлов](https://img.shields.io/badge/узлов-2000-brightgreen)](https://lorenzazy7kenyon.github.io/free-vpn-subscriptions/index.html) [![License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/blob/main/LICENSE)

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
| 🇽🇽 XX (`XX`) | 564 | [clash-XX.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-XX.yaml) | [singbox-XX.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-XX.json) | [v2ray-base64-XX.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-XX.txt) |
| 🇨🇦 Канада (`CA`) | 561 | [clash-CA.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-CA.yaml) | [singbox-CA.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-CA.json) | [v2ray-base64-CA.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-CA.txt) |
| 🇺🇸 США (`US`) | 381 | [clash-US.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-US.yaml) | [singbox-US.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-US.json) | [v2ray-base64-US.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-US.txt) |
| 🇳🇱 Нидерланды (`NL`) | 149 | [clash-NL.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-NL.yaml) | [singbox-NL.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-NL.json) | [v2ray-base64-NL.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-NL.txt) |
| 🇩🇪 Германия (`DE`) | 95 | [clash-DE.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-DE.yaml) | [singbox-DE.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-DE.json) | [v2ray-base64-DE.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-DE.txt) |
| 🇫🇷 Франция (`FR`) | 47 | [clash-FR.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-FR.yaml) | [singbox-FR.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-FR.json) | [v2ray-base64-FR.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-FR.txt) |
| 🇬🇧 Великобритания (`GB`) | 33 | [clash-GB.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-GB.yaml) | [singbox-GB.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-GB.json) | [v2ray-base64-GB.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-GB.txt) |
| 🇯🇵 Япония (`JP`) | 27 | [clash-JP.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-JP.yaml) | [singbox-JP.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-JP.json) | [v2ray-base64-JP.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-JP.txt) |
| 🇭🇰 Гонконг (`HK`) | 25 | [clash-HK.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-HK.yaml) | [singbox-HK.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-HK.json) | [v2ray-base64-HK.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-HK.txt) |
| 🇸🇨 SC (`SC`) | 13 | [clash-SC.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-SC.yaml) | [singbox-SC.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-SC.json) | [v2ray-base64-SC.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SC.txt) |
| 🇸🇪 Швеция (`SE`) | 9 | [clash-SE.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-SE.yaml) | [singbox-SE.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-SE.json) | [v2ray-base64-SE.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SE.txt) |
| 🇵🇱 Польша (`PL`) | 9 | [clash-PL.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-PL.yaml) | [singbox-PL.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-PL.json) | [v2ray-base64-PL.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-PL.txt) |
| 🇪🇸 Испания (`ES`) | 8 | [clash-ES.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-ES.yaml) | [singbox-ES.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-ES.json) | [v2ray-base64-ES.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-ES.txt) |
| 🇮🇷 Иран (`IR`) | 8 | [clash-IR.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-IR.yaml) | [singbox-IR.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-IR.json) | [v2ray-base64-IR.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-IR.txt) |
| 🇮🇹 Италия (`IT`) | 8 | [clash-IT.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-IT.yaml) | [singbox-IT.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-IT.json) | [v2ray-base64-IT.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-IT.txt) |
| 🇰🇷 Корея (`KR`) | 6 | [clash-KR.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-KR.yaml) | [singbox-KR.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-KR.json) | [v2ray-base64-KR.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-KR.txt) |
| 🇸🇰 SK (`SK`) | 6 | [clash-SK.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-SK.yaml) | [singbox-SK.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-SK.json) | [v2ray-base64-SK.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SK.txt) |
| 🇲🇪 ME (`ME`) | 6 | [clash-ME.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-ME.yaml) | [singbox-ME.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-ME.json) | [v2ray-base64-ME.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-ME.txt) |
| 🇷🇺 Россия (`RU`) | 4 | [clash-RU.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-RU.yaml) | [singbox-RU.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-RU.json) | [v2ray-base64-RU.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-RU.txt) |
| 🇧🇪 Бельгия (`BE`) | 4 | [clash-BE.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-BE.yaml) | [singbox-BE.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-BE.json) | [v2ray-base64-BE.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-BE.txt) |
| 🇫🇮 Финляндия (`FI`) | 4 | [clash-FI.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-FI.yaml) | [singbox-FI.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-FI.json) | [v2ray-base64-FI.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-FI.txt) |
| 🇦🇪 ОАЭ (`AE`) | 3 | [clash-AE.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-AE.yaml) | [singbox-AE.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-AE.json) | [v2ray-base64-AE.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-AE.txt) |
| 🇦🇹 Австрия (`AT`) | 3 | [clash-AT.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-AT.yaml) | [singbox-AT.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-AT.json) | [v2ray-base64-AT.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-AT.txt) |
| 🇮🇪 IE (`IE`) | 3 | [clash-IE.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-IE.yaml) | [singbox-IE.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-IE.json) | [v2ray-base64-IE.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-IE.txt) |
| 🇨🇭 Швейцария (`CH`) | 3 | [clash-CH.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-CH.yaml) | [singbox-CH.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-CH.json) | [v2ray-base64-CH.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-CH.txt) |
| 🇪🇪 Эстония (`EE`) | 3 | [clash-EE.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-EE.yaml) | [singbox-EE.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-EE.json) | [v2ray-base64-EE.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-EE.txt) |
| 🇨🇷 CR (`CR`) | 2 | [clash-CR.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-CR.yaml) | [singbox-CR.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-CR.json) | [v2ray-base64-CR.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-CR.txt) |
| 🇹🇼 Тайвань (`TW`) | 2 | [clash-TW.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-TW.yaml) | [singbox-TW.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-TW.json) | [v2ray-base64-TW.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-TW.txt) |
| 🇦🇿 AZ (`AZ`) | 2 | [clash-AZ.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-AZ.yaml) | [singbox-AZ.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-AZ.json) | [v2ray-base64-AZ.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-AZ.txt) |
| 🇳🇿 NZ (`NZ`) | 1 | [clash-NZ.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-NZ.yaml) | [singbox-NZ.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-NZ.json) | [v2ray-base64-NZ.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-NZ.txt) |
| 🇱🇹 Литва (`LT`) | 1 | [clash-LT.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-LT.yaml) | [singbox-LT.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-LT.json) | [v2ray-base64-LT.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-LT.txt) |
| 🇦🇺 Австралия (`AU`) | 1 | [clash-AU.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-AU.yaml) | [singbox-AU.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-AU.json) | [v2ray-base64-AU.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-AU.txt) |
| 🇧🇿 BZ (`BZ`) | 1 | [clash-BZ.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-BZ.yaml) | [singbox-BZ.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-BZ.json) | [v2ray-base64-BZ.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-BZ.txt) |
| 🇰🇿 Казахстан (`KZ`) | 1 | [clash-KZ.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-KZ.yaml) | [singbox-KZ.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-KZ.json) | [v2ray-base64-KZ.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-KZ.txt) |
| 🇲🇽 Мексика (`MX`) | 1 | [clash-MX.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-MX.yaml) | [singbox-MX.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-MX.json) | [v2ray-base64-MX.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-MX.txt) |
| 🇨🇿 Чехия (`CZ`) | 1 | [clash-CZ.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-CZ.yaml) | [singbox-CZ.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-CZ.json) | [v2ray-base64-CZ.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-CZ.txt) |
| 🇮🇱 IL (`IL`) | 1 | [clash-IL.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-IL.yaml) | [singbox-IL.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-IL.json) | [v2ray-base64-IL.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-IL.txt) |
| 🇳🇴 Норвегия (`NO`) | 1 | [clash-NO.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-NO.yaml) | [singbox-NO.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-NO.json) | [v2ray-base64-NO.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-NO.txt) |
| 🇰🇭 KH (`KH`) | 1 | [clash-KH.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-KH.yaml) | [singbox-KH.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-KH.json) | [v2ray-base64-KH.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-KH.txt) |
| 🇹🇷 Турция (`TR`) | 1 | [clash-TR.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-TR.yaml) | [singbox-TR.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-TR.json) | [v2ray-base64-TR.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-TR.txt) |
| 🇸🇬 Сингапур (`SG`) | 1 | [clash-SG.yaml](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/clash-SG.yaml) | [singbox-SG.json](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/singbox-SG.json) | [v2ray-base64-SG.txt](https://github.com/lorenzazy7kenyon/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SG.txt) |

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

- **Выбрано узлов**: 2000
- **Живых по TCP**: 2728
- **Записей из источников**: 4375
- **Медиана RTT**: 110 ms
- **Последнее обновление (UTC)**: 2026-10-18 09:00 UTC

**Распределение протоколов:** VLESS × 2104 · VMess × 220 · ss × 208 · Trojan × 155 · Hysteria2 × 41

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
