import json 
import requests
import test

spotify_key = "BQD_n8ccu6xdR2p0OT-71-9EGlrWa6zl5AMH_fN89Hie8SMTIHYmVs63ehMGkbuRSbqbWCn-K0iYGCUi1ldp45JR89gvccld-5SFj_sZmPCYc-7DELCW7bczin2fSdA2zU6OOBLe2Qs"
nyt_key='1a4c5c66686604317fa4bfc11a77ff64:1:74958104'

artists_dic = {'T-Pain': "3aQeKQSyrW4qWr35idm0cy",
 'Chris Brown': '7bXgB6jMjp9ATFy66eO08Z', 
 'Rihanna':'5pKCCKE2ajJHZ9KAiaK11H',
  'Nelly':'2gBjLmx6zQnFGQJCAQpRgw', 
  'Ludacris':'3ipn9JLAPI5GUEo4y4jcoi',
  'T.I.':'4OBJLual30L7gRl5UkeRcT', 
  'Lil Wayne':'55Aa2cqylxrFIXC767Z865',
  'Rick Ross' : '1sBkRIssrMs1AbVkOJbc7a'}

print "The list of artists to choose from were" + str([x for x in artists_dic])

print """
-------------------------------------------------------------------------------------------------------------------
"""
user_artist = ""
while user_artist not in artists_dic.keys():
  user_artist = raw_input("Type an artist's name from the list above!! (Be very specific with spelling & capitalization!)^^")
user_artist_id = artists_dic[user_artist]
print "-------------------------------------------------------------------------------------------------------------------"
print "You Picked!!" + user_artist + '\n'

"""
cache_fname = ''
while cache_fname not in 
cache_fname = raw_input("Name a file and make sure to put .txt at the end of the name")"""

def get_artists_albums(artist=user_artist_id):
	baseurl = "https://api.spotify.com/v1/artists/" + artist + "/albums" 
	authorization = spotify_key
	data = requests.get(baseurl, headers = {"Authorization": "Bearer " + authorization})
	data = data.json()
	return data

def get_albums_from_data(response):
  album_names = []
  for x in response['items']:
    album_names.append(x['name'])

  return album_names


#def make_file(cache_fname=''):
def NYT_search(baseurl = 'https://api.nytimes.com/svc/search/v2/articlesearch.json', 
   response_format='json',
   api_key = nyt_key,
   cache_fname= "artistinfo.txt",
   extra_params={'q':user_artist,'fq':'The New York Times'}):
   d = {}
   d['api-key'] = api_key
   d['response_format'] = format
   for k in extra_params:
       d[k] = extra_params[k]
   resp = requests.get(baseurl, params = d)
   
  
   f = open(cache_fname, 'w')
   f.write(resp.text)
   f.close()
   # return the contents as text in this case
   return resp.text
NYT_search(cache_fname = "NYT_r2.txt", extra_params= {'q':user_artist,'fq':'The New York Times' })
f = open("NYT_r2.txt", 'r')
y = f.read()
z = json.loads(y)

new={}
for dictionary in z['response']['docs']:
    new[(dictionary)['web_url']]=(dictionary['snippet'])

new_dic=sorted(new,key=lambda x:new[x], reverse=True)    # list of printed out 
print "Here is a list of News paper weburls that we will itterated through in alphabetical order"
print 
print new_dic


print """
-------------------------------------------------------------------------------------------------------------------"""
print "Here are up to 10 weburls and snippets of articles that " + user_artist + " was featured in."

print"""
-------------------------------------------------------------------------------------------------------------------
"""
for key in new:
    try:
        print 'Article web url:{} \nSnippet:{}'.format(key,new[key]) + '\n'
    except:
        print
def pretty(obj):
  return json.dumps(obj, sort_keys=True, indent=2)


class Artist():
  def __init__(self, name = "", albums=[], article_count = 0):
    self.name = name
    self.albums = albums
    self.articles = article_count
    
  def __str__(self):
    albums = ""
    for x in self.albums:
      if x not in albums:
        albums += x 
      
   
    return "Artist " + self.name + " has his " + str(len(self.albums)) + " most played songs in the albums, which are called: " + "\n" + str(self.albums) + '\n' 

  def article_count(self):
    self.article_count = len(new_dic)
    print "There are" + self.article_count + "from the artist" + self.name




Artist()
album_data = get_artists_albums()
albums = get_albums_from_data(album_data)
artist_info= Artist(name = user_artist, albums = albums, article_count = len(new_dic))
print artist_info
print
print "There are " + str(len(new_dic)) + "results for your artist"

print 

#test.testEqual(get_from_csv("test.csv"), ["Kanye West\n", "Mary Poppins\n", "Lion King\n"])
test_artist = Artist(user_artist)
test.testEqual(test_artist.name, user_artist, "Artist")
test.testEqual(user_artist_id, artists_dic[user_artist], "Artist ID")
test.testEqual(type(test_artist.name), type(""), "String Test for Name")
test.testEqual(type(albums), type(unicode), "Unicode Test For Albums")


