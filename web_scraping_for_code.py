import requests
from bs4 import BeautifulSoup
data=[]
import pandas as pd
import re
import os
da=[]
k="https://www.sanfoundry.com/c-programming-examples/"
page0=requests.get(k)

soup0 =BeautifulSoup(page0.content,'html.parser')

# print(soup.find_all('div',{'class':'hts-messages hts-messages--info    '}))
f=0



divdata=soup0.find("div",{"class":"entry-content"})
num=1
data=divdata.find_all("a")

file_object = open('c2.txt', 'a')
for r in divdata.find_all("a"):
    print(r)
    
    
    num+=1
    print(num)
    #r=r.strip()
    page=requests.get(r["href"])
    
    soup =BeautifulSoup(page.content,'html.parser')
    for i in soup.find_all('td'):
            data=i.find_all('a')
            
            for j in data:
                    program=''
                    name=j.get_text()
                    program+=name+"\n"
                    print(j.get_text())
                    program+="================================ EOPN"+"\n"
                    
                    #k=j.find('a')
                    
                    page1=requests.get(j["href"])
                    
                    soup1 =BeautifulSoup(page1.content,'html.parser')
                    data1=soup1.find("div",{"class":"c"})
                    f=str(data1.get_text()).split("*/")[0]
                    program+=f+"\n"
                    program+="================================ EOKW"+"\n"
                    program+="--------------------------------"+"\n"
                    program+="output:"+"\n"
                    if soup1.find("div",{"class":"text"}):
                     f=str(soup1.find("div",{"class":"text"}).get_text())
                     program+=str(soup1.find("div",{"class":"text"}).get_text())+"\n"
                    elif soup1.find("div",{"class":"txt"}) :
                     program+=str(soup1.find("div",{"class":"txt"}).get_text())+"\n"
                    else:
                     program+=str(soup1.find("div",{"class":"bash"}).get_text())+"\n"
                    program+="--------------------------------"+"\n"
                    check=0;key=0;
                    if data1.find_all("li"):
                        data_p=""
                        for q in data1.find_all("li"):
                         if check == 1:
                            data_p=q.get_text().strip()
                            program+=data_p+"\n"
                         if "*/" in q.get_text().strip():
                             check=1
                         
                         
                    else:
                        data_p=data1.get_text().split("*/")[1]
                        program += data_p+"\n"
                    #program=program.replace("."," ")
                    file_object.write(program+" ETP \n********************************\n")


    

# Close the file



