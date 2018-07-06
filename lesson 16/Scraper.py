import requests
from bs4 import BeautifulSoup
import re

def number_of_prisons(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    divs = soup.findAll("div", {"class": "field field-name-field-number-of-establishments field-type-field-collection field-label-hidden"})
    for div in divs:
        text = div.get_text()
    return int(re.findall('(\d+)', text)[0])


r = requests.get('http://www.prisonstudies.org/map/europe')
soup = BeautifulSoup(r.text, 'html.parser')

href = []
tags = soup.find_all('a')
for t in tags:
    try:
        href.append(t.attrs['href'])
    except KeyError:
        pass
        
dictionary = {}
europe_index = href.index('/map/europe')
middle_east_index = href.index('/map/middle-east')

for i in range(europe_index+1, middle_east_index):
    link = "http://www.prisonstudies.org" + href[i]
    name = href[i][9:]
    number = number_of_prisons(link)
    dictionary[name] = number
    print(name, number)

print(dictionary)


