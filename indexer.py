import requests
from webscraping import xpath 

FANSUBS=(
  "158741",      
)


def scrape_nyaa_id(nyaa_id):
    url_base = "http://www.nyaa.se/?user=%s&page=separate" % nyaa_id
    res = requests.get(url_base).text
    titles = xpath.search(res, "//td[@class='name']/span/text()")
    tbody_complete = xpath.search(res, "//tbody[@class='hide']")
    list_dict = []
    for index,title in enumerate(titles):
        tbody = tbody_complete[index]
        rows= xpath.search(tbody,"//tr")
        rows = rows[1:]
        d = {'title': title, 'data':[]}
        for row in rows:
            part = xpath.get(row, "//td[1]/a/text()")
            link = xpath.get(row, "//td[1]/a/@href")
            type_ = xpath.get(row, "//td[2]/text()")
            size = xpath.get(row, "//td[5]/text()")
            crc = xpath.get(row, "//td[6]/text()")
            row_dict = dict(part=part,link= link, type=type_, size=size, crc=crc)
            d["data"].append(row_dict)
        list_dict.append(d)
    return list_dict


if __name__ == "__main__":
    import json
    for i in FANSUBS:
        l = scrape_nyaa_id(i)
        print json.dumps(l)
