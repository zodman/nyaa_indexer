from feedfinder2 import find_feeds
import feedparser
import logging
from pprint import pprint
REMOVEWORDS=["comment",]


def find_url_feed(url):
    results = find_feeds(url, user_agent="zodman")
    for i in results:
        for w in REMOVEWORDS:
            if w in i:
                results.remove(i)
    return results

def dict_feed_data(urls, page_length=1):
    list_data = []
    for url in urls:
        for page in range(0,page_length):
            d = feedparser.parse(url + "?paged=%s" % page)
            for item in d.entries:
                list_data.append(item)
    return list_data

if __name__ == "__main__":
    import sys
    res = find_url_feed(sys.argv[1])
    list_data = dict_feed_data(res, 3)
    pprint(list_data)
