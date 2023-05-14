import configparser

conf = configparser.ConfigParser()
app_id = conf.get("chatinfo", "app_id")
app_secret = conf.get("chatinfo", "app_secret")

from werobot.config import Config
from werobot import WeRoBot

config = Config(
    TOKEN="ai4e",
    HOST="0.0.0.0",
    PORT="80",
    APP_ID=app_id,
    APP_SECRET=app_secret,
)

robot = WeRoBot(config=config)


@robot.handler
def hello(message):
    return 'Hello World!'

if __name__ == '__main__':
    robot.run()
