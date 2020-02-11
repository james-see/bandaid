"""Gets latest band data for a particular band and adds to user watchlist."""
from bs4 import BeautifulSoup
import requests 
import redis
import argparse


def connectRedis():
    r = redis.Redis(host='localhost', port=6379,
                    charset="utf-8", decode_responses=True)
    try:
        r.ping()
    except redis.exceptions.ConnectionError:
        exit('Redis is not started.')
    return r


def getBand(rs, bandname):
    """
    Get band page and related data
    """
    baseurl = "https://www.bandsintown.com/{}"
    r = requests.get(baseurl.format(bandname))
    if r.status_code == 200:
        if "upcomingEventsSection" in r.text:
            print(f"{bandname} is on tour!")
        else:
            print(f"No upcoming events for {bandname}.")
        exit()
    else:
        exit(1)


def prepper():
    """
    Process all runtime arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--band', dest='bandname',
                        help="band to lookup", type=str, nargs='+')
    parser.add_argument('-w', '--watchlist', dest='watchlist',
                        action='store_true', help="add to watchlist")
    args = parser.parse_args()
    return args


def main():
    args = prepper()
    rs = connectRedis()
    getBand(rs, " ".join(args.bandname))


if __name__ == "__main__":
    main()
