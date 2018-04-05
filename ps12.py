import test106 as test
import requests
import json
"""give_author = z["response"]["docs"][0]["byline"]['original'] #gives us author
give_title = z["response"]["docs"][0]["headline"] #Article headline/title
give_weburl = z ["response"]["docs"][0]["web_url"] #weburl
give_hits = z ['response']['meta']['hits'] #hits the article got
x = z ['response']['docs'][0]['keywords']
give_categories = [all_vals['value'] for all_vals in x]"""

key ='3d9823524f434a82349c6c233756a979:6:74971061'
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2) 

class article():
  def __init__(self, article_dic={}):
    if 'keywords' in article_dic:
      self.keywords = article_dic['response']['docs'][0]['keywords']
    else:
      self.keywords = ""

  def give_keywords(self):
    key_words_list = []
    for word in self.keywords:
      if word in ny_article_search_response:
        key_words_list.append(word)
    return key_words_list



    self.name = name
    self.hits= give_hits
    self.author = give_author
    self.title = give_title
    self.categories = give_categories

        #random range of pics from 1-10 = random.randrange(1000)
def get_request(baseurl = 'https://api.nytimes.com/svc/search/v2/articlesearch.json', 
  response_format='json',
  api_key = key,
  cache_fname="cached_data.txt",
  
  extra_params={}):
  dic = {}
  dic['api-key'] = api_key
  dic['response_format'] = format

  for x in extra_params:
    dic[x] = extra_params[x]
    resp = requests.get(baseurl, params = dic)
    print "caching data"
    f_name = open(cache_fname, 'w')
    f_name.write(resp.text)
    f_name.close()

    return resp.text
  

def get_from_txt(filename):
  f_name=open(filename, 'r')
  y=f_name.read()
  z=json.loads(y)
 
def responses(self):
  give_author =  z["response"]["docs"][0]["byline"]['original'] #gives us author
  give_title = z["response"]["docs"][0]["headline"] #Article headline/title
  give_weburl = z ["response"]["docs"][0]["web_url"] #weburl
  give_hits = z ['response']['meta']['hits'] #hits the article got
  x = z ['response']['docs'][0]['keywords']
  give_categories = [all_vals['value'] for all_vals in x]
  print give_categories
 
get_request(cache_fname='ny_article_search_response.txt', extra_params={'q':'basketball','fq':'The New York Times'}) 
