import json
import urllib2
import time
import random
import pickle


f = open('moviemoney','r')
data = pickle.load(f)
f.close()

no_genre = []
no_production = []
no_imdbID = []
no_country = []
exception_list = []

for key in data:

    if int(key) % 30 == 0 :
        print key

    try:
        url = 'http://www.omdbapi.com/?t=%s&tomatoes=true' % data[key]['movie']
        url = url.replace(' ', '%20')
        r = urllib2.urlopen(url)
        newdata = json.loads(r.read())

        if 'Genre' in newdata:
            data[key]['genre'] = newdata['Genre']
        else:
            no_genre.append(data[key]['movie'])

        if 'Production' in newdata:
            data[key]['company'] = newdata['Production']
        else:
            no_production.append(data[key]['movie'])

        if 'Awards' in newdata:
            data[key]['awards'] = newdata['Awards']

        if 'imdbID' in newdata:
            data[key]['imdbID'] = newdata['imdbID']
        else:
            no_imdbID.append(data[key]['movie'])

        if 'Country' in newdata:
            data[key]['country'] = newdata['Country']
        else:
            no_country.append(data[key]['movie'])

        if 'Director' in newdata:
            data[key]['director'] = newdata['Director']

        if 'Actors' in newdata:
            data[key]['actors'] = newdata['Actors']

    except Exception, ex:
        exception_list.append(data[key]['movie'])
        continue

    time.sleep(random.uniform(0.1, 0.3))

f = open('moviedata', 'w')
pickle.dump(data, f)
f.close()

f = open('no_genre','w')
pickle.dump(no_genre, f)
f.close()

f = open('no_production', 'w')
pickle.dump(no_production, f)
f.close()

f = open('no_imdbID', 'w')
pickle.dump(no_imdbID, f)
f.close()

f = open('no_country', 'w')
pickle.dump(no_country, f)
f.close()

f = open('exception_list', 'w')
pickle.dump(exception_list, f)
f.close()

