""" My this program scrapes text,(corona update figures) from notable websites (worldometers.info and mohfw.gov.in)......
   Corona updates from any specific country can be known by running this program.....
   Much more detailed information is showed up for India by tabulating all the updates of every state as per the mohfw website
   
   Note: 1.This program is meant only for brushing up python concepts and not to legalize or promote any websites.
         2.This program is not responsible for any false figures as it is just scraped from aforementioned sites.So
           donot solely trust these figures.
 """
         

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate 
import os 
import numpy as np 

print("\n                                                            Welcome to Corona Updates  \n")

def reqmysite(url):
    
        r=requests.get(url)
        s=BeautifulSoup(r.text,"html.parser")
        data=s.find_all("div",class_="maincounter-number")

        return data

print("World wide Updates are as follows:\n")

url= "http://www.worldometers.info/coronavirus/"
data=reqmysite(url)
print("      Total Cases in the world:",data[0].text.strip())
print("      Total Deaths:",data[1].text.strip())
print("      Total Recovered:",data[2].text.strip())
print("")
nat=["INDIA","India","india"]
while True:
                print("Enter the country name you want to know about its corona updates:")
                country=input()
                if country=="USA"or country=="usa"or country=="america"or country=="AMERICA"or country=="America" or country=="US":
                        country="us"       
                try:
                                url= "http://www.worldometers.info/coronavirus/country/"+country
                                data=reqmysite(url)
                                print("\n      Total Cases in",country.upper(),":",data[0].text.strip())
                                print("      Total Deaths:",data[1].text.strip())
                                print("      Total Recovered:",data[2].text.strip())


                                if country in nat:
                                        content = lambda row: [x.text.replace('\n', '') for x in row] 
                                        URL = 'https://www.mohfw.gov.in/'

                                        heading = ['SNo', 'State','Indian-Confirmed', 'Foreign-Confirmed','Cured','Death'] 

                                        response = requests.get(URL).content 
                                        soup = BeautifulSoup(response, 'html.parser') 
                                        header = content(soup.tr.find_all('th')) 

                                        states = [] 
                                        all_rows = soup.find_all('tr') 

                                        for row in all_rows: 
                                            stat = content(row.find_all('td')) 
                                            if stat: 
                                                if len(stat) == 5: 
                                                    
                                                    stat = ['', *stat] 
                                                    states.append(stat) 
                                                elif len(stat) == 6: 
                                                    states.append(stat) 

                                        states[-1][1] = "Total Cases"

                                        states.remove(states[-1])

                                        objects = [] 
                                        for row in states : 
                                            objects.append(row[1]) 

                                        y_pos = np.arange(len(objects)) 

                                        performance = [] 
                                        for row in states : 
                                            performance.append((row[2]) + (row[3])) 

                                        table = tabulate(states, headers=heading) 
                                        print(table)
                                        break
                                else:
                                        break
                except IndexError:
                        print("country not available")
                        continue
