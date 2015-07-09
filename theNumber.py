from bs4 import BeautifulSoup
import urllib2
import re
import os
import time
import random
import csv
import sys
import pickle
from datetime import datetime



url = 'http://www.the-numbers.com/movie/budgets/all'

request = urllib2.Request(url)
page = urllib2.urlopen(request)
content = page.read()
soup = BeautifulSoup(content)

#results = soup.find_all('td', {'class' : 'data'})
results = soup.find_all('tr')
d = {}
i = 1
for result in results:
    result = result.find_all('td')
    if len(result) > 0:
        d[i] = {'movie':result[2].get_text(), 'release date':re.search(r'\d{4}$', result[1].get_text()).group(), 'budget':result[3].get_text(), 'domestic':result[4].get_text(), 'worldwide':result[5].get_text()}
        i += 1
f = open('moviemoney', 'w')
pickle.dump(d, f)
f.close()
