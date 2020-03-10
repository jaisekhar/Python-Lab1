import requests
from bs4 import BeautifulSoup

#Initializing BeautifulSoup html parse
source = requests.get("https://catalog.umkc.edu/course-offerings/graduate/comp-sci/").text
soup=BeautifulSoup(source,"html.parser")

#Parsing all courses
results = soup.find_all('div', {'class': 'courseblock'})

#Iterating through Every course for Course code and secription
for result in results:
    code = result.find('span', {'class': 'code'}).text
    desc = result.find('p', {'class': 'courseblockdesc'}).text
    print("Course Code: {}\nCourse Description: {}\n".format(code,desc))