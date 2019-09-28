import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

# function definition

def scrape_top_list(url):
   
    # requesting to server for extracting the data of url
    Data=requests.get(url)

    # using Beautiful Soup for parsing HTML data
    soup=BeautifulSoup(Data.text,"html.parser")

    #using find function for extracting the content of tbody
    tbody=soup.find("tbody",class_="lister-list")

    # using findAll for the accessing the content of tbody in a list
    trs=tbody.findAll("tr")

    year_list=[]
    ratting_list=[]
    url_list=[]
    name_list=[]
  
    for tr in trs:
        name = tr.find("td",class_="titleColumn").a.get_text()
        name_list.append(name)

        movie_url=tr.find("td",class_="titleColumn").a["href"]
        movies_link="https://www.imdb.com"+movie_url
        url_list.append(movies_link)

        movie_year=tr.find("td",class_= "titleColumn").span.get_text()


    for tr in trs:
        name = tr.find("td",class_="titleColumn").a.get_text()
        name_list.append(name)

        movie_url=tr.find("td",class_="titleColumn").a["href"]
        movies_link="https://www.imdb.com"+movie_url
        url_list.append(movies_link)

        movie_year=tr.find("td",class_= "titleColumn").span.get_text()
        year_list.append(movie_year)

        movie_ratting=tr.find("td",class_="ratingColumn imdbRating").strong.get_text()
        ratting_list.append(movie_ratting)
        
    # declaring the list
    movies_list=[]
    
    for i in range(0,250):
        dict={}
        dict["rating"]=float(ratting_list[i])
        dict["position"]=i+1
        dict["name"]=name_list[i]
        dict["url"]=url_list[i]
        dict["year"]=int(year_list[i][1:5])
        movies_list.append(dict)
    return movies_list

# function calling
all_movies=scrape_top_list(url="https://www.imdb.com/india/top-rated-indian-movies/")
pprint(all_movies)

            
           
