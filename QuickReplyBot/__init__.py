import os
import logging
from dotenv import load_dotenv

# 配置日志记录器
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s- %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("log.txt")],
)
logging.getLogger("httpx").setLevel(logging.ERROR)
logger = logging.getLogger("QuickReplyBot")


load_dotenv(override=True)
bot_token = os.getenv("BOT_TOKEN") or exit("BOT_TOKEN not found in .env file")
try:
    admin_ids = [
        int(x.strip()) for x in os.getenv("ADMIN_IDS").replace("，", ",").split(",")
    ] or exit("ADMIN_IDS 未填写")
    log_group_id = int(os.getenv("LOG_GROUP_ID")) if os.getenv("LOG_GROUP_ID") else None
except Exception as e:
    exit(f"ADMIN_IDS 或者 LOG_GROUP_ID 格式错误。需要是整数。{e}")
proxy_uri = os.getenv("PROXY_URI")
inline_cmd = os.getenv("INLINE_COMMAND", "show")
