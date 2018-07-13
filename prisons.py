import requests
from bs4 import BeautifulSoup

r=requests.get('http://www.prisonstudies.org/map')
soup = BeautifulSoup(r.text, 'html.parser')
all_a = soup.find_all('a')
all_divs = soup.find_all('div')
country_list = list(filter(None, list(map(lambda i: i.get('href') if i.get('href') is not None and 'country' in i.get('href') else None, all_a))))

def request_country(country):
    g=requests.get('http://www.prisonstudies.org/{}'.format(country))
    soupp = BeautifulSoup(g.text, 'html.parser')
    all = soupp.find_all('div')
    return all    
    
def request_elem(all):
    search_class = 'field-name-field-number-of-establishments'    
    for div in all:
        div_class=div.get('class')
        if div_class and search_class in div_class:
            return div.div.div.div.div.div.div.div.div.string
            
new_dic =  {i[9:]:request_elem(request_country(i)) for i in country_list}
print(new_dic)

