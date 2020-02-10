from bs4 import BeautifulSoup
import requests 
import redis

# example url 
# `curl https://www.bandsintown.com/a/1 | grep "upcomingEventsSection" | html2text -style pretty`
# `curl https://www.bandsintown.com/a/1 | grep "artistInfo" | html2text -style pretty`


def enumerator(url="https://www.bandsintown.com/a/1"):
    """
    What:
    ----
    Performs head request to confirm page exists and stores in queue

    Returns:
    Dictionary of True or false that page exists
    """
    r = requests.head(url)
    if r.status_code == 200:
        return url, 1
    else:
        return url, 0


def connectRedis():
    r = redis.Redis(host='localhost', port=6379, 
                        charset="utf-8", decode_responses=True)
    try:
        r.ping()
    except redis.exceptions.ConnectionError as e:
        exit('Redis is not started.')
    return r

def main():
    rs = connectRedis()
    url, status = enumerator()
    rs.hmset(url, {"name":url, "status_code":status})
    print(rs.hget(url, 'status_code'))


if __name__ == "__main__":
    main()
