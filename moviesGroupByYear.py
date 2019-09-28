from pprint import pprint

#importing Top_Indian_Movie_List file 
from Top_Indian_Movie_List import*

#function definition
def getMovieYears(total_movies):
    i=0
    years=[]
    while i<len(total_movies):
        movie_year=total_movies[i]["year"]
        if movie_year not in years:
            years.append(movie_year)
        i=i+1
    return years

#function calling
totalYears=getMovieYears(all_movies)

#function definition
def group_by_year(movies,totalYears):
    j=0                          
    moviesByYear={}
    while j<len(totalYears):

        moviesByParticularYear=[]
        year=totalYears[j]

        for movie in  movies:
            if year == movie["year"]:
                moviesByParticularYear.append(movie)
                
        moviesByYear[year]=moviesByParticularYear
        j=j+1
    return moviesByYear

#function calling
moviesByYear=group_by_year(all_movies,totalYears)
pprint(moviesByYear)































# def data_list(sorted_list,group_of_year):
#     dict={}
#     dict["sort_list"]=sorted_list
#     dict["years_group"]=group_of_year
#     return dict
# years_data=data_list(totalYears,moviesByYear)
# # pprint(years_data)