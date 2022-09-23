import requests
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest
import pandas as pd


jop_title = []
company_name = []
location = []
info_and_skills = []
type = []
links = []
salary = []

page_number = 0
while(page_number < 42):
    page = requests.get(f'https://wuzzuf.net/search/jobs/?a=hpb&q=data%20science&start={page_number}')   #fetch this url

    content = page.content  #page content
    soup = BeautifulSoup(content,'lxml')    #create soup object to parse content


    jop_title_html = soup.find_all('h2',{'class':'css-m604qf'})
    company_name_html = soup.find_all('a', {'class':'css-17s97q8'})
    location_html = soup.find_all('span',{'class':'css-5wys0k'})
    info_and_skills_html = soup.find_all('div',{'class':'css-y4udm8'})
    type_html = soup.find_all('div',{'class':'css-1lh32fc'})


    for i in range(len(jop_title_html)):
        jop_title.append(jop_title_html[i].text)
        company_name.append(company_name_html[i].text)
        location.append(location_html[i].text)
        info_and_skills.append(info_and_skills_html[i].text)
        type.append(type_html[i].text)
        links.append('https://wuzzuf.net'+str(jop_title_html[i].find('a').attrs['href']))


    for i in range(len(links)):
        links[i] = links[i].replace(' ','%20')

    '''
    for link in links:
        inner_page = requests.get(link)
        inner_content = inner_page.content
        inner_soup = BeautifulSoup(inner_content,'lxml')
        s = inner_soup.find('span',{'class':'css-4xky9y'})
        salary.append(s)
    '''
    page_number += 1




dict = {'jop_title': jop_title, 'company_name': company_name, 'location': location, 'type': type, 'links':links}  
df = pd.DataFrame(dict)
df.to_csv('Data_science_jobs.csv')
print(df)
    


