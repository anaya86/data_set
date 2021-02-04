from bs4 import BeautifulSoup
import re
import requests
import json

def function(soup):
    table=soup.find("table",class_="infobox vevent")
    name=table.tr.get_text(strip=True)
    data_set={"Title":name}
    
    for tr_tag in table.findAll("tr")[3:]:
        for td_tag in tr_tag.findAll("td"):
            items=[]
            children=[tag.name for tag in td_tag.contents]
            if "div" in children:
                
                for li_tag in td_tag.find("div").findAll("li"):
                    __str__=li_tag.get_text(" ",strip=True).replace("\xa0"," ")
                    
                    items.append(__str__)
            else:
                items.append(td_tag.get_text(" ",strip=True).replace("\xa0"," "))
            
            
        
        data_set[tr_tag.th.get_text(" ",strip=True)]=items
        
    

    return data_set
    
def requests_for_link(__soup__,path):
    __req__=requests.get(f"{url_all}{path}",headers=usr_agent)
    __soup__=BeautifulSoup(__req__.text,"lxml",multi_valued_attributes=None)
    data__set=function(__soup__)
    return data__set
    
for table_tagg in soup_main.findAll("table",class_="wikitable sortable")[0:10]:
    for tr_tag in table_tagg.tbody.findAll("tr")[1:]:
        a_tag=tr_tag.findAll("td")[1].a
        if a_tag:
            print(a_tag["href"])
            try:
                item=requests_for_link(__soup__,a_tag["href"])
                dictionary_of_movies.append(item)
            except Exception as e:
                print(e)
with open("movie_data_set.json", 'w') as file:
    json.dump(dictionary_of_movies,file)
            
