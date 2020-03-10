import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=India'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
# print(results.prettify()) # For printing out the entire structure of the HTML page in a readable format
job_elems = results.find_all('section', class_='card-content')

# Loop for getting all the job listing given on a page
print()
print("ALL THE JOB POSTINGS WE GET AFTER PERFORMING THE SEARCH QUERY: ")

job_serial_number = 0

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # We can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')

    if (title_elem != None) and (company_elem != None) and (location_elem != None):

        job_serial_number += 1
        print()
        print(job_serial_number, '.')
        print("---------------------------------------------------")
        print(title_elem.text.strip())
        print(company_elem.text.strip())
        print(location_elem.text.strip())
        print("---------------------------------------------------")
        print()

# Code for extracting the application link to the job posting with a particular word 'python'

print("APPLICATION LINK TO ALL THE JOB POSTINGS CONTAINING A PARTICULAR WORD")
print("IN THEIR JOB TITLE FROM THE ABOVE SEARCH QUERY: ")

print()

python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
pjob_serial_no = 0

for p_job in python_jobs:
    link = p_job.find('a')['href']
    pjob_serial_no += 1
    print(pjob_serial_no, '.')
    print("---------------------------------------------------")
    print(p_job.text.strip())
    print(f"Apply here: {link}")
    print("---------------------------------------------------")
