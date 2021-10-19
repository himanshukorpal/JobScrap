from bs4 import BeautifulSoup
import requests
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation="
html_data = requests.get(url).text

soup = BeautifulSoup(html_data,'lxml')
jobs= soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
companies = []
skills = []
for job in jobs:
    published_date = job.find('span',class_="sim-posted").span.text
    if 'few' in published_date:
        company_name = job.find('h3',class_="joblist-comp-name").text.replace(' ','').replace('\r\n\r\n','\r\n').replace('\r\n','').replace('\n','')
        skills_req = job.find('span', class_="srp-skills").text.replace(' ', '').replace('\r\n\r\n','').replace('\n', '')
        exp = job.find('ul', class_="top-jd-dtl clearfix")
        f_exp= exp.find('li').text.replace('card_travel','')
        loc = job.find('ul',class_="top-jd-dtl clearfix").span.text.replace(' ','')
    
    #print(f_exp)
        print("Company Name: ", company_name)
        print("Required Skills:", skills_req)
        print("Experience Required:", f_exp)
        print("Location Of Job: ", loc)
        print(end='\n')
        
    else:
        continue
    #companies.append(company_name)
#print("Done")
#print(skills)