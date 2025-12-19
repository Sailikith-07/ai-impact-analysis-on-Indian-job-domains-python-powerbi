import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

#paste your linkedin link here to scrap the details
url = "https://www.linkedin.com/jobs/search?keywords=Prompt%20Engineer&location=India&geoId=102713980&f_E=4&f_TPR=&f_PP=105214831%2C106888327%2C105556991%2C113968072%2C103671728&position=1&pageNum=0"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
job_id = soup.find_all('a',
                       class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2] outline-offset-[4px]')
print(len(job_id))
links_1 = []
for i in job_id:
    link = i.get('href')
    links_1.append(link)

links = links_1

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

job_title_2 = []
Company_Name_2 = []
location_2 = []
time_posted_2 = []
experience_level_2 = []
job_description_2 = []
Industry_2 = []
no_of_applications_2 = []
domain_2 = []
number = 1
for first in links:
    try:
        response = requests.get(first, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {first}: {e}")
        continue  # skip to next link
    print(f'{response.status_code},{number}', end=" ")  # response status
    number = number + 1
    link1 = BeautifulSoup(response.text, 'html.parser')
    # first_response=requests.get(first)
    # link1=BeautifulSoup(first_response.content,'html.parser')
    try:
        title = link1.find('h1',
                           class_='top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title')
        job_title1 = title.text
        job_title_2.append(job_title1)
    except:
        job_title_2.append('None')
    try:
        company = link1.find('a', class_='topcard__org-name-link topcard__flavor--black-link')
        comp = company.text.strip()
        Company_Name_2.append(comp)
    except:
        Company_Name_2.append('None')
    try:
        location1 = link1.find('span', class_='topcard__flavor topcard__flavor--bullet')
        loc = location1.text.strip()
        location_2.append(loc)
    except:
        location_2.append('None')
    try:
        time_post = link1.find('span',
                               class_='posted-time-ago__text topcard__flavor--metadata')
        time_posted1 = time_post.text.strip()
        time_posted_2.append(time_posted1)
    except:
        time_posted_2.append('None')
    try:
        seniority = link1.find('span', class_='description__job-criteria-text description__job-criteria-text--criteria')
        seniority_level = seniority.text.strip()
        experience_level_2.append(seniority_level)
    except:
        experience_level_2.append('None')
    try:
        desc = link1.find('div', class_='description__text description__text--rich')
        job_desc = desc.text.strip()
        job_description_2.append(job_desc)
    except:
        job_description_2.append('None')
    try:
        inds = link1.find_all('span', class_='description__job-criteria-text description__job-criteria-text--criteria')
        Industry1 = inds[3].text.strip()
        Industry_2.append(Industry1)
    except:
        Industry_2.append('None')
    try:
        applied = link1.find(class_='num-applicants__caption')
        apply = applied.text.strip()
        numbers = [word for word in apply.split() if word.isdigit()]
        no_of_applications1 = numbers[0]
        no_of_applications_2.append(no_of_applications1)
    except:
        no_of_applications_2.append('None')

    domain_2.append('Prompt Engineer')

    time.sleep(2)  