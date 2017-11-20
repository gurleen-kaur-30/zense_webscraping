import datetime
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup
import requests
import webbrowser
import urllib3
urllib3.disable_warnings()
open("info.txt","w").close()
file = open("info.txt","a")
time = str(datetime.datetime.now())
file.write(time + "\n")


with requests.Session() as c:
	url = 'https://lms.iiitb.ac.in/moodle/login/index.php'
	USERNAME = #enter your username
	PASSWORD = #enter your password
	c.get(url, verify=False)
	login_data = dict(username=USERNAME, password=PASSWORD, next='/')
	c.post(url, data=login_data)
	page = c.get('https://lms.iiitb.ac.in/moodle/my/')
	

soup = BeautifulSoup(page.content, "html.parser")


courses = soup.find_all('div', attrs = { 'class' : 'box coursebox'})
for course in courses:
	titles = course.find_all('h2')
	for title in titles:

			file.write(">") 
			file.write(title.text + "\n")
	prompts = course.find_all('div',attrs = {'class' : 'collapsibleregioncaption'})
	
	for prompt in prompts :
		
		 	file.write(prompt.text + "\n")
	file.write("\n")

		 	


#cronjob line for hourly running of script 0 * * * * python /path/to/file/lms.py




