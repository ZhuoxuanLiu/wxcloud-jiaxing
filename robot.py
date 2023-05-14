import configparser

conf = configparser.ConfigParser()
conf.read('chatinfo.conf', encoding="utf-8")
app_id = conf.get("chatinfo", "app_id")
app_secret = conf.get("chatinfo", "app_secret")

from werobot.config import Config
from werobot import WeRoBot

config = Config(
   SERVER="auto",
   TOKEN="ai4e",
   HOST="0.0.0.0",
   PORT="80",
   APP_ID=app_id,
   APP_SECRET=app_secret,
)

myrobot = WeRoBot(config=config)


@myrobot.handler
def hello(message):
    return 'Hello World!'

