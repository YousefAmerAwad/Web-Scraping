from pyexpat import model
import requests
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest
import pandas as pd

links = []
price = []
year = []
showroom = []
model = []
mileage = []
specs = []

page = requests.get('https://oasiscars.com/Cars/List')
content = page.content
soup = BeautifulSoup(content,'lxml')

links_html = soup.find_all('a',{'class':'car-link'})
price_html = soup.find_all('div',{'class':'subtitle price-tags pull-right'})
year_html = soup.find_all('span',{'class':'srchYear'})
showroom_html = soup.find_all('span',{'class':'srchShowroom'})
model_html = soup.find_all('div',{'class':'content-inner'})





for i in range(len(price_html)):
    price.append(price_html[i].text.strip())
    year.append(year_html[i].text.strip())
    showroom.append(showroom_html[i].text.strip())
    model.append(model_html[i].find('h2').text.strip())
    links.append('https://oasiscars.com/'+str(links_html[i].attrs['href']))
    #mileage.append(mileage_html[i].find('#text'))



for link in links:
    page = requests.get(link)
    content = page.content
    soup = BeautifulSoup(content,'lxml')

    specs_html = soup.find_all('div',{'class':'icon-meta'})
    spec = ''
    for spec_html in specs_html[2:]:
        spec = spec + '   ' + spec_html.text.strip()
    specs.append(spec)
    
    mileage.append(specs_html[1].text.strip())

    
    

dict = {'Model': model, 'Year': year, 'Show_Room': showroom, 'Mileage': mileage, 'Specs':specs, 'Price':price}  
df = pd.DataFrame(dict)
df.to_csv('Cars_Qatar.csv')
print(df)
    
