
# coding: utf-8

# In[1]:


import httplib2
import json
import urllib.request
from konlpy.tag import Okt
from collections import Counter

h = httplib2.Http()
okt = Okt()


# In[2]:


# if result prints one result, show information of movie

def information(result):
    #  recive poster
    poster = resulta['poster_path']
    poster_name = str(poster).replace('/','')
    base_url = 'https://image.tmdb.org/t/p/'
    file_size = 'w500/'
    poster = base_url + file_size + str(poster)
    try:
        # make file of poster's images
        urllib.request.urlretrieve(str(poster),'./img/'+ poster_name)
    except urllib.error.HTTPError as err:
        # if images url cannot find the image
        print(err.code)
    
    name = resulta['original_title']
    overview = resulta['overview']
    
    print('Movie :',name)
    if 'genres' in resulta.keys():
        genre = resulta['genres'][0]['name']
        print('Genre :',genre)
    print('Overview :',overview)
    print()


# In[3]:


# api_ex recives discover of movie's information.

def make_result(api_ex):
    url = 'https://api.themoviedb.org/3/discover/movie'
    mykey = '?api_key=ff3bedd3d47493bf66e799c508aba82a'
    city = '&language=en-US'
    myrequest = url + mykey + city + api_ex
    response, content = h.request(myrequest, 'GET')
    resulta = json.loads(content.decode('utf-8'))
    
    return resulta


# In[4]:


# api_id recieves ip id of moive

def make_result_id(api_id):
    url = 'https://api.themoviedb.org/3/discover/movie'
    mykey = '?api_key=ff3bedd3d47493bf66e799c508aba82a'
    city = '&language=en-US'
    myrequest = url + str(api_id) + mykey + city
    response, content = h.request(myrequest, 'GET')
    resulta = json.loads(content.decode('utf-8'))
    
    return resulta


# In[5]:


# show results of lists what have many results of movie.

def info_list(result):
    if result['total_results'] > 20:
        times = 19
    else:
        times = result['total_results']-1
    for num in range(0, times):
        poster = result['results'][num]['poster_path'] # https://codevkr.tistory.com/36?category=705611
        poster_name = str(poster).replace('/','')
        base_url = 'https://image.tmdb.org/t/p/'
        file_size = 'w500/'
        poster = base_url + file_size + str(poster)
        try:
            urllib.request.urlretrieve(str(poster),'./img/'+ poster_name)
        except urllib.error.HTTPError as err:
            print()
        title = result['results'][num]['title']
        api_id = result['results'][num]['id']
        overview = result['results'][num]['overview']
        
        print('Poster :', poster)
        print('Title :', title)
        if 'genres' in result['results'][num].keys():
            genre = result['results'][num]['genres'][0]['name']
            print('Genre :',genre)
        print('Overview :',overview)
        print()


# In[6]:


def searchInfo(title, pages):
    url = 'https://api.themoviedb.org/3/search/company'
    myapi = '?api_key=ff3bedd3d47493bf66e799c508aba82a'
    query = '&query='
    page = '&page='
    sort = '&sort_by=popularity.desc'
    myrequest = url + myapi+ sort + page+str(pages)+query + title
    response, content = h.request(myrequest, 'GET')
    result = json.loads(content.decode('utf-8'))
    if result['total_results'] < 19:
        total_result = result['total_results']
    else:
        total_result = 19
    
    for num in range(0, total_result):
        print(result['results'][num]['name'])
    
    if result['total_results'] > 19:
        print("Do you want more about "+title+"?(y/n)")
        y = str(input())
        if y == "y" or y == "yes" or y == "Y":
            searchInfo(title, pages+1)


# In[7]:


def recentMovie():
    from datetime import datetime

    year = datetime.today().year

    month = datetime.today().month

    day = datetime.today().day
    
    if month == 1:
        monthL = 12
    else:
        monthL = month - 1
    
    
    info_list(make_result('&primary_release_date.gte='+str(year)+'-'+str(monthL)+'-01&primary_release_date.lte='+str(year)+'-'+str(month)+'-'+str(day)+''))


# In[8]:


def popularMovie():
    info_list(make_result('?certification_country=US&certification=R&sort_by=vote_average.desc'))


# In[9]:


def genreMovie():
    print("What kind of Genre do you want?")
    
    print("1. Action | 2. Adventure | 3. Animation | 4. Comedy | 5. Crime | 6. Documentary")
    print("7. Drama | 8. Family |9. Fantasy | 10. History | 11. Horror | 12. Music")
    print("13. Mystery | 14. Romance | 15. Science Fiction | 16. TV Movie | 17. Thriller | 18. War | 19. Western")
    
    x = int(input())
    print()
    
    if x == 1:
        info_list(make_result('?with_genres=28&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 2:
        info_list(make_result('?with_genres=12&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 3:
        info_list(make_result('?with_genres=16&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 4:
        info_list(make_result('?with_genres=35&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 5:
        info_list(make_result('?with_genres=80&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 6:
        info_list(make_result('?with_genres=99&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 7:
        info_list(make_result('?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 8:
        info_list(make_result('?with_genres=10751&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 9:
        info_list(make_result('?with_genres=14&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 10:
        info_list(make_result('?with_genres=36&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 11:
        info_list(make_result('?with_genres=27&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 12:
        info_list(make_result('?with_genres=10402&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 13:
        info_list(make_result('?with_genres=9648&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 14:
        info_list(make_result('?with_genres=10749&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 15:
        info_list(make_result('?with_genres=878&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 16:
        info_list(make_result('?with_genres=10770&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 17:
        info_list(make_result('?with_genres=53&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 18:
        info_list(make_result('?with_genres=10752&sort_by=vote_average.desc&vote_count.gte=10'))
    elif x == 19:
        info_list(make_result('?with_genres=37&sort_by=vote_average.desc&vote_count.gte=10'))
    else:
        print("wrong input")


# In[10]:


def yearMovie():
    from datetime import datetime
    
    print("When do you want to see a movie that opened in years?")
    print()
    
    x = int(input())
    print()
    
    year = datetime.today().year
    
    if(x > year):
        print("wrong input")
    else:
        info_list(make_result('&primary_release_year='+str(x)+'&sort_by=vote_average.desc'))


# In[11]:


def searchMovie():
    print("Find the movie with Title :")
    x = str(input())
    
    searchInfo(x, 1)


# In[12]:


def dialog(sentence):
    sentences_tag = []
    noun_list = []
    morph = okt.pos(sentence)
    sentences_tag.append(morph)
    
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun']:
                noun_list.append(word)
    
    success = 0
    
    for word in noun_list:
        if word == '최근':
            recentMovie()
            success = 1
            break
        elif word == '인기' or word == '추천':
            for word2 in noun_list:
                genre = 0
                if word2 == "중":
                    genre = 1
                    break
            if genre == 1:
                genreMovie()
                success = 1
            else:
                popularMovie()
                success = 1
        elif word == '개봉':
            yearMovie()
            success = 1
            break
        elif word == '검색':
            searchMovie()
            success = 1
            break
    if success == 0:
        print("Wrong input")
        print("Do you want manual?")
        y = input()
        
        if y == "y" or y == "yes" or y == "Y":
            ask()


# In[13]:


def ask():
        print("What are you looking for?")
        print()
        print("1. Recent Movie  |  2. Popular Movie  |  3. Movie Recommendation(genre)  |  4. Movie Recommendation(year)  |  5. Search(Movie title)")
        x = int(input())
        print()
    
        if x == 1:
            recentMovie()
        elif x == 2:
            popularMovie()
        elif x == 3:
            genreMovie()
        elif x == 4:
            yearMovie()
        elif x == 5:
            searchMovie()
        else:
            print("Wrong input")
        
        print()
        print()


# In[14]:


def movieApp():
    print("Welcome.")
    print("If you input the sentence with specific keyword, I can find the movie.")
    print()
    
    while True:    
        print("What are you looking for?")
        print("Do you wonder what I can do? Then press A")
        x = input()
        print()
        print()
        
        if x == "a" or x == "A":
            ask()
        else:
            dialog(x)
        
        print("Do you want more?(y/n)")
        y = input()
        
        if y == "y" or y == "yes" or y == "Y":
            print()
        else:
            break


# In[16]:


movieApp()

