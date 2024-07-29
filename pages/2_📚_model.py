<<<<<<< HEAD
import streamlit as st
import pandas as pd
import pickle
import requests
import mechanicalsoup
from bs4 import BeautifulSoup



st.set_page_config(
    page_title='Movie Recommendations App',
    page_icon="🎬",
    layout='wide',
    initial_sidebar_state='expanded'
)
st.markdown("""
    <style>    
        .image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 40%;
        hight:100px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

def fetch_poster(movie_id, movie_title):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=6f21acf7e97b7c4d771392ba29999fca&language=en-US")
    data = response.json()
    if 'poster_path' in data and data['poster_path']:
        poster = 'http://image.tmdb.org/t/p/w500/' + data['poster_path']
    else:
        browser = mechanicalsoup.Browser()
        url = 'https://www.themoviedb.org/'
        page = browser.get(url)
        page_html = page.soup
        form = page_html.select('form')[0]
        film_search = form.select('input')[0]
        film_search['value'] = movie_title
        login = browser.submit(form, url)
        login_url = login.url
        request = requests.get(login_url).text
        soup = BeautifulSoup(request, 'html.parser')
        f1 = soup.find('div', class_='search_results movie').find("div", class_='poster').find('img')
        poster = f1.get('src')
    return poster

similarity = pickle.load(open('models/similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Assuming the DataFrame has a 'movie_id' column
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from website
        try:
            recommended_posters.append(fetch_poster(movie_id, recommended_movies[-1]))
        except KeyError:
            continue
    return recommended_movies, recommended_posters

movies = pd.read_csv('data/raw/recommend_data.csv')
st.title('🎬 Movie Recommendation System')
st.markdown("""
            <img src='https://th.bing.com/th/id/OIG3.sjI6_FjgDMYfstkIkRXe?w=1024&h=1024&rs=1&pid=ImgDetMain' class='image'>""",unsafe_allow_html=True)
select_movie_name = st.selectbox('Select a movie to recommend', options=movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(select_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0],)
        st.image(posters[0],width=150)
    with col2:
        st.text(names[1])
        st.image(posters[1],width=150)
    with col3:
        st.text(names[2])
        st.image(posters[2],width=150)
    with col4:
        st.text(names[3])
        st.image(posters[3],width=150)
    with col5:
        st.text(names[4])
        st.image(posters[4],width=150)
=======
import streamlit as st
import pandas as pd
import pickle
import requests
import mechanicalsoup
from bs4 import BeautifulSoup



st.set_page_config(
    page_title='Movie Recommendations App',
    page_icon="🎬",
    layout='wide',
    initial_sidebar_state='expanded'
)
st.markdown("""
    <style>    
        .image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 40%;
        hight:100px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

def fetch_poster(movie_id, movie_title):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=6f21acf7e97b7c4d771392ba29999fca&language=en-US")
    data = response.json()
    if 'poster_path' in data and data['poster_path']:
        poster = 'http://image.tmdb.org/t/p/w500/' + data['poster_path']
    else:
        browser = mechanicalsoup.Browser()
        url = 'https://www.themoviedb.org/'
        page = browser.get(url)
        page_html = page.soup
        form = page_html.select('form')[0]
        film_search = form.select('input')[0]
        film_search['value'] = movie_title
        login = browser.submit(form, url)
        login_url = login.url
        request = requests.get(login_url).text
        soup = BeautifulSoup(request, 'html.parser')
        f1 = soup.find('div', class_='search_results movie').find("div", class_='poster').find('img')
        poster = f1.get('src')
    return poster

similarity = pickle.load(open('models/similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Assuming the DataFrame has a 'movie_id' column
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from website
        try:
            recommended_posters.append(fetch_poster(movie_id, recommended_movies[-1]))
        except KeyError:
            continue
    return recommended_movies, recommended_posters

movies = pd.read_csv('data/raw/recommend_data.csv')
st.title('🎬 Movie Recommendation System')
st.markdown("""
            <img src='https://th.bing.com/th/id/OIG3.sjI6_FjgDMYfstkIkRXe?w=1024&h=1024&rs=1&pid=ImgDetMain' class='image'>""",unsafe_allow_html=True)
select_movie_name = st.selectbox('Select a movie to recommend', options=movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(select_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0],)
        st.image(posters[0],width=150)
    with col2:
        st.text(names[1])
        st.image(posters[1],width=150)
    with col3:
        st.text(names[2])
        st.image(posters[2],width=150)
    with col4:
        st.text(names[3])
        st.image(posters[3],width=150)
    with col5:
        st.text(names[4])
        st.image(posters[4],width=150)
>>>>>>> e1ddd1ea8b1198d4cd20417f4165fa0c77a36171
