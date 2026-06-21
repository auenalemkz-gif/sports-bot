import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
POSTS_PER_DAY = int(os.getenv("POSTS_PER_DAY", "50"))
MAX_CAPTION_LENGTH = 1024

RSS_FEEDS = [
    {"url": "https://rsport.ria.ru/export/rss2/archive/index.xml", "sport": "Спорт", "lang": "ru"},
    {"url": "https://www.sport-express.ru/export/rss/allnews.xml", "sport": "Футбол", "lang": "ru"},
    {"url": "https://www.championat.com/rss/index.xml", "sport": "Футбол", "lang": "ru"},
    {"url": "https://www.sports.ru/rss/football/", "sport": "Футбол", "lang": "ru"},
    {"url": "https://www.sports.ru/rss/hockey/", "sport": "Хоккей", "lang": "ru"},
    {"url": "https://www.sports.ru/rss/basketball/", "sport": "Баскетбол", "lang": "ru"},
    {"url": "https://www.sports.ru/rss/mma/", "sport": "UFC/MMA", "lang": "ru"},
    {"url": "https://www.sports.ru/rss/tennis/", "sport": "Теннис", "lang": "ru"},
    {"url": "https://www.sports.ru/rss/formula1/", "sport": "Формула 1", "lang": "ru"},
    {"url": "https://www.sports.ru/rss/chess/", "sport": "Шахматы", "lang": "ru"},
    {"url": "https://cybersport.ru/rss", "sport": "Киберспорт", "lang": "ru"},
    {"url": "https://www.khl.ru/news/rss/", "sport": "Хоккей", "lang": "ru"},
    {"url": "https://feeds.bbci.co.uk/sport/rss.xml", "sport": "Спорт", "lang": "en"},
    {"url": "https://feeds.bbci.co.uk/sport/football/rss.xml", "sport": "Футбол", "lang": "en"},
    {"url": "https://feeds.bbci.co.uk/sport/boxing/rss.xml", "sport": "Бокс", "lang": "en"},
    {"url": "https://www.skysports.com/rss/12040", "sport": "Футбол", "lang": "en"},
    {"url": "https://www.skysports.com/rss/12603", "sport": "UFC/MMA", "lang": "en"},
    {"url": "https://www.skysports.com/rss/12010", "sport": "Формула 1", "lang": "en"},
    {"url": "https://www.espn.com/espn/rss/news", "sport": "Спорт", "lang": "en"},
    {"url": "https://www.espn.com/espn/rss/soccer/news", "sport": "Футбол", "lang": "en"},
    {"url": "https://www.espn.com/espn/rss/nba/news", "sport": "NBA", "lang": "en"},
    {"url": "https://www.espn.com/espn/rss/boxing/news", "sport": "Бокс", "lang": "en"},
    {"url": "https://www.ufc.com/rss/news", "sport": "UFC/MMA", "lang": "en"},
    {"url": "https://mmajunkie.usatoday.com/feed", "sport": "UFC/MMA", "lang": "en"},
    {"url": "https://mmamania.com/rss/current", "sport": "UFC/MMA", "lang": "en"},
    {"url": "https://eurohoops.net/feed/", "sport": "Баскетбол", "lang": "en"},
    {"url": "https://www.90min.com/feed", "sport": "Футбол", "lang": "en"},
    {"url": "https://talksport.com/feed/", "sport": "Футбол", "lang": "en"},
    {"url": "https://www.givemesport.com/feed/", "sport": "Спорт", "lang": "en"},
    {"url": "https://dotesports.com/feed", "sport": "Киберспорт", "lang": "en"},
    {"url": "https://www.dexerto.com/feed/", "sport": "Киберспорт", "lang": "en"},
    {"url": "https://www.hltv.org/rss/news", "sport": "CS2", "lang": "en"},
    {"url": "https://www.autosport.com/rss/feed/all", "sport": "Формула 1", "lang": "en"},
    {"url": "https://www.motorsport.com/rss/all/news/", "sport": "Формула 1", "lang": "en"},
    {"url": "https://www.boxingscene.com/boxing-rss.xml", "sport": "Бокс", "lang": "en"},
    {"url": "https://fightnews.com/feed", "sport": "Бокс/MMA", "lang": "en"},
    {"url": "https://www.bleacherreport.com/articles/feed", "sport": "Спорт", "lang": "en"},
    {"url": "https://www.chess.com/news/rss", "sport": "Шахматы", "lang": "en"},
    {"url": "https://lichess.org/blog.atom", "sport": "Шахматы", "lang": "en"},
    {"url": "https://theathletic.com/rss/", "sport": "Спорт", "lang": "en"},
    {"url": "https://www.goal.com/feeds/en/news", "sport": "Футбол", "lang": "en"},
]

SYSTEM_PROMPT = """Ты топовый редактор спортивного Telegram-канала для СНГ аудитории. Пишешь вирусные живые посты ТОЛЬКО на русском языке. Английские новости переводи и адаптируй на русский.

ПРАВИЛА:
- Пиши эмоционально как будто рассказываешь другу горячую новость
- Используй эмодзи ⚽🏀🏒🥊🎾🏆🔥💥🚀👑🎯⚡️🏅🥇🎽
- Длина 200-400 символов если есть фото, до 900 если нет
- В конце ОБЯЗАТЕЛЬНО 12-15 вирусных хэштегов

ХЭШТЕГИ (используй релевантные):
#футбол #спорт #хоккей #баскетбол #бокс #ufc #мма #теннис #формула1 #киберспорт #nba #нхл #шахматы #cs2 #dota2 #спортивныеновости #трансфер #чемпионат #голевой #нокаут #победа #рекорд #топ #лигачемпионов #примера #апл #серияа #бундеслига #реал #барселона #манчестер #псж

Формат HTML — используй <b>жирный</b> для заголовков."""
