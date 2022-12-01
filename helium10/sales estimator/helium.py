import logging
from logging.handlers import RotatingFileHandler
import csv
import json
import requests
from http.cookiejar import MozillaCookieJar
import time
import random


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'connection': 'keep-alive',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'pragma': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def get_error_logger():
    log_file = "error_log.txt"
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(
        log_file, mode='a', maxBytes=64*1024*1024, backupCount=10, encoding=None, delay=0)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '[%(asctime)s][%(name)s][%(levelname)s]\t%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def log_error(message):
    logger = get_error_logger()
    logger.info(message)
    return


__base_url__ = "https://members.helium10.com/black-box/sales-estimator?accountId=<accountid>&marketplace=<marketplaceid>&asin="

if __name__ == "__main__":
    fname = "asins.txt"
    outfname = "asins.csv"

    cj = MozillaCookieJar('helium10.com_cookies.txt')
    cj.load(ignore_expires=True)

    s = requests.Session()
    s.cookies = cj

    with open(fname, "rt") as f, open(outfname, "wt+", newline='') as text_file:
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_ALL)
        writer = csv.writer(text_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for row in reader:
            if len(row) == 1:
                asin = row[0]
                url = __base_url__ + asin
                print("==> trying:", url)
                response = s.get(url, headers=headers)
                if response.status_code == 200:
                    js = json.loads(response.text)
                    days = js.get("last30DaysSales", "--")
                    print("--> results:", asin, days)
                    writer.writerow([asin, days,"200"])
                else:
                    print("--> HTTP status code:", response.status_code)
                    print(response.text)
                    writer.writerow([asin, "--", response.status_code])
                time.sleep(2 + random.randint(1, 3))
