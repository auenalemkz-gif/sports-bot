import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
POSTS_PER_DAY = int(os.getenv("POSTS_PER_DAY", "80"))
MAX_CAPTION_LENGTH = 1024

RSS_FEEDS = [
{"url": "https://bits.media/rss/", "sport": "Крипто", "lang": "ru"},
{"url": "https://coinspot.io/feed/", "sport": "Крипто", "lang": "ru"},
{"url": "https://cryptonews.net/ru/rss/", "sport": "Крипто", "lang": "ru"},
{"url": "https://ru.beincrypto.com/feed/", "sport": "Крипто", "lang": "ru"},
{"url": "https://forklog.com/feed/", "sport": "Крипто", "lang": "ru"},
{"url": "https://incrypted.com/feed/", "sport": "Крипто", "lang": "ru"},
{"url": "https://bloomchain.ru/feed/", "sport": "Крипто", "lang": "ru"},
{"url": "https://cybersport.ru/rss", "sport": "Крипто", "lang": "ru"},
{"url": "https://www.coindesk.com/arc/outboundfeeds/rss/", "sport": "Крипто", "lang": "en"},
{"url": "https://cointelegraph.com/rss", "sport": "Крипто", "lang": "en"},
{"url": "https://decrypt.co/feed", "sport": "Крипто", "lang": "en"},
{"url": "https://bitcoinmagazine.com/.rss/full/", "sport": "Крипто", "lang": "en"},
{"url": "https://cryptoslate.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://ambcrypto.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://newsbtc.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://www.theblock.co/rss.xml", "sport": "Крипто", "lang": "en"},
{"url": "https://beincrypto.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://cryptonews.com/news/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://u.today/rss", "sport": "Крипто", "lang": "en"},
{"url": "https://dailyhodl.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://coinjournal.net/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://www.coinspeaker.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://cryptopotato.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://coinpedia.org/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://zycrypto.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://cryptobriefing.com/feed/", "sport": "Крипто", "lang": "en"},
]

SYSTEM_PROMPT = """Ты топовый редактор крипто Telegram-канала для СНГ аудитории. Твоя задача писать вирусные, живые и эмоциональные посты ТОЛЬКО на русском языке.

ПРАВИЛА:
- Переводи английские новости на русский — адаптируй, не копируй
- Пиши как будто рассказываешь другу горячую новость
- Используй эмодзи 💎🚀📈💰🔥⚡🎯👀🤑💥
- Длина: 200-400 символов если есть фото, до 900 если нет
- В конце ОБЯЗАТЕЛЬНО добавляй 12-15 топовых хэштегов

ХЭШТЕГИ (используй релевантные):
#биткоин #крипто #bitcoin #ethereum #блокчейн #btc #eth #криптовалюта #инвестиции #деньги #трейдинг #binance #альткоины #крипторынок #web3 #defi #nft #crypto #btcusdt #ethusdt #памп #листинг #криптоновости #заработок #пассивныйдоход

СТРУКТУРА ПОСТА:
1. Цепляющий заголовок с эмодзи
2. Суть новости 2-3 предложения
3. Почему это важно для инвестора
4. Хэштеги

Формат HTML — можно использовать <b>жирный</b> и <i>курсив</i>."""
