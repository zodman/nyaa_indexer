import requests
import urllib2
from urllib import urlencode
from collections import namedtuple
from webscraping import xpath
from tqdm import tqdm
import HTMLParser
from memorised.decorators import memorise

MalResult = namedtuple('MalResult',[
    'title','title_en','synonyms', 'episodes','img','resumen','status',"type",
    'id','synopsys'
    ])


@memorise()
def translate(to_translate, to_langage="auto", langage="auto"):
    agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
    before_trans = 'class="t0">'
#    link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+").replace("\n",""))
    link = "http://translate.google.com/m?"
    h = HTMLParser.HTMLParser()
    to_t = to_translate.decode("unicode-escape")
    to_trans = h.unescape(to_t)
    params = dict(hl=to_langage,sl=langage,q=to_trans)
    data = urlencode(dict([k, v.encode('utf-8')] for k, v in params.items()))
    request = urllib2.Request(link+data, headers=agents)
    page = urllib2.urlopen(request).read()
    result = page[page.find(before_trans)+len(before_trans):]
    result = result.split("<")[0]
    return result

@memorise()
def mal(mal_title, mal_id=False):
    cookies = {"incap_ses_224_81958":"P6tYbUr7VH9V6shgudAbA1g5FVYAAAAAyt7eDF9npLc6I7roc0UIEQ=="}
    response = requests.get(
        "http://myanimelist.net/api/anime/search.xml",
        params={'q':mal_title},
        cookies=cookies,
        auth=("zodman1","zxczxc"),
        headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'})
    content = response.content
    if not mal_id is False:
         for e in xpath.search(content,"//entry"):
             if mal_id in e:
                 content = e
                 break

    tqdm.write("%s %s"%((mal_title,), mal_id))
    id = xpath.get(content, "//id")
    title = xpath.get(content, "//title")
    title_en = xpath.get(content, "//english")
    type_ = xpath.get(content, "//type")
    synonyms = xpath.get(content, "//synonyms")
    status = xpath.get(content, "//status")
    synopsys = translate(xpath.get(content, "//synopsis"),"es")
    img  = xpath.get(content, "//image")
    episodes = xpath.get(content,"//episodes")
    resumen = synopsys.replace("&lt;br /&gt;", " ").replace("\n\r","")
    resumen = translate(resumen,'es')
    status = translate(status,'es')
    assert id is not "", mal_title

    data=dict(title=title, title_en=title_en, type=type_, status=status,
    resumen=resumen, img=img,episodes=episodes, synonyms=synonyms,id=id, synopsys=synopsys)
    return MalResult(**data)


