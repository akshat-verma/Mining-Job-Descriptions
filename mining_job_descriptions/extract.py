'''
Created on Jul 21, 2015

@author: Akshat Verma
Computing Id: av2zf
'''

import urllib.request
from bs4 import BeautifulSoup
import re

location_list = []
company_list = []
description_url_list = []
job_description_list = []

'''
    1.  loop though all pages that have data scientist job listings:
        base_html_page = open(monster.com/data-scientist/pg-i)
    2.  loop through all the listings on the base html page:
        location_list.add(location) // add job locations to location list
        company_list.add(company) // add company names to company list
        job_description_url_list.add(url) // add description urls to url list
    
'''
for i in range(1,40):
    monster = urllib.request.urlopen("http://jobsearch.monster.com/search/data-scientist_5?pg="+str(i))
    soup = BeautifulSoup(monster.read(),'html.parser')
    even_list = soup.findAll("tr","even")
    odd_list = soup.findAll("tr","odd")
    location_list.extend([jobs.find("div","jobLocationSingleLine").a.contents[0] for jobs in even_list])
    location_list.extend([jobs.find("div","jobLocationSingleLine").a.contents[0] for jobs in odd_list])
    company_list.extend([jobs.find("div","companyContainer").a.a.contents[0] for jobs in even_list])
    company_list.extend([jobs.find("div","companyContainer").a.a.contents[0] for jobs in odd_list])
    description_url_list.extend([jobs.find("div","jobTitleContainer").a['href'] for jobs in even_list])
    description_url_list.extend([jobs.find("div","jobTitleContainer").a['href']for jobs in odd_list])

'''
    loop through all the urls in the url_list:
        job_description_list.add(description) // Add all the job descriptions to             the list

'''
    
HTML_TAG = re.compile(r'<[^>]+>')
BASE_URL = "job-openings.monster.com"
for url in description_url_list:
    try:
        if  BASE_URL in url:
            description = urllib.request.urlopen(url)
            soup = BeautifulSoup(description.read(),'html.parser')
            formatted_text = HTML_TAG.sub('',' '.join([str(t) for t in (soup.find("div","jobview-section").contents)]))
            job_description_list.append(formatted_text)
    except Exception:
        pass

'''
    From location list , extract city and state and populate the two lists: city list     and state list

'''
city_list = [location.split(",")[0].strip() for location in location_list]
state_list = [location.split(",")[1].strip() for location in location_list]

company_list = [company.strip() for company in company_list]

# Function to write a list to a file
def write_list_to_file(filename,list_to_write):
    f = open(filename,"w")
    f.writelines(["%s\n" % item  for item in list_to_write])

'''
    Write all the 4 lists - city list, state list, company list, job_description list to         different text files

'''

write_list_to_file("city_list.txt", city_list)
write_list_to_file("state_list.txt", state_list)
write_list_to_file("company_list.txt", company_list)
write_list_to_file("job_description_list.txt", job_description_list)
