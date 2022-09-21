import json
import logging
import os
import re
import time
import argparse

import requests
import telegram
from bs4 import BeautifulSoup

# Log setting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
fh = logging.FileHandler('log.txt', 'w', 'utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)


def GetFirstInfo(brand):
    res = requests.get("http://market.dcview.com/brand/" + brand, timeout=10)
    soup = BeautifulSoup(res.text, features="html.parser")
    body = soup.select("tbody")

    lineStr = ""
    i = body[0].find("a", href=re.compile("http://market.dcview.com/post.*"))
    if (i.parent.name == "p"):
        for j in (i.find_all(class_="btn-xs")):
            lineStr += j.get_text().strip() + " "
        lineStr += i.find(class_="h5").get_text().strip()
    return lineStr, i["href"]


def main():
    # Check config
    parser = argparse.ArgumentParser()
    parser.add_argument("--use_config", action="store_true",help="使用設定檔")
    parser.add_argument("--config_path", default="./config/botConfig.json",help="設定檔位置，不指定則為 ./config/botConfig.json")
    args = parser.parse_args()

    if (args.use_config):
        with open(args.config_path, "r") as f:
            conf = json.load(f)
            logging.info(conf)

        botToken = conf["TG_TOKEN"]
        myChatID = conf["TG_CHAT_ID"]
        trackInt = conf["YB_TRACK_INT"]
        brands = conf["YB_BRANDS"]
    else:
        botToken = os.getenv("TG_TOKEN")
        myChatID = os.getenv("TG_CHAT_ID")
        trackInt = int(os.getenv("YB_TRACK_INT"))
        brands = os.getenv("YB_BRANDS").split(',')

    # Open bot.
    bot = telegram.Bot(botToken)
    logging.info("Open BOT: " + bot.getMe().first_name)

    # Data Store temp.
    brandLens = len(brands)
    keep = [""] * brandLens

    # Main loop.
    while True:
        try:
            for i in range(brandLens):
                l, link = GetFirstInfo(brands[i])
                logging.info(l)

                if (l != keep[i]):
                    sendStr = "<a href=\"" + link + "\">" + l + "</a>"
                    bot.send_message(myChatID, text=sendStr, parse_mode="html")
                    logging.info("Sent.")
                    keep[i] = l
        except:
            logging.info("Parse Error!!!!!")
        time.sleep(trackInt)


if __name__ == "__main__":
    main()
