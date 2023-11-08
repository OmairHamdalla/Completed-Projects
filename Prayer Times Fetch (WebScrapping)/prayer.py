import os
import requests 
import bs4 
from datetime import date
today = date.today().strftime("%d,%m,%Y")

directory = os.path.dirname(__file__)
folder = "Prayer_Logs"
fileName = f"prayersTable_{today}.txt"
address = os.path.join(directory, folder)
filePath = os.path.join(address, fileName)

if not os.path.exists(address):
    os.makedirs(address)


query = "Prayer Times Istanbul"
url = "https://google.com/search?q=" + query 


request_result = requests.get( url ) 
soup = bs4.BeautifulSoup( request_result.text , "html.parser" ) 


#temp = soup.find( "div" , class_='CgE3Ac' ).prettify()

times = soup.findAll("span",class_='r0bn4c rQMQod')

fajr =  times[0].text
duhur = times[2].text
asr = times[3].text
maghrib= times[4].text
ishaa = times[5].text
    
Text = f'Fajr: {fajr}\nDuhur: {duhur}\nAsr: {asr}\nMaghrib: {maghrib}\nIshaa: {ishaa}'
print(Text)

with open(filePath, 'w', encoding='utf-8') as file:
    file.write(str(Text))
