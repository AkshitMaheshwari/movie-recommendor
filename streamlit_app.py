import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url  = 'https://api.themoviedb.org/3/movie/{}?api_key=b9045ddab3be581991d33f6ee1d57753&languange=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movie_index = movies_list1[movies_list1['title'] == movie].index[0]
    distances = sim[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:5]
    recommended_movies =[]
    recommended_movies_posters =[]
    for i in movies_list:
        movie_id = movies_list1.iloc[i[0]].id
        # Search Poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies_list1.iloc[i[0]].title)
    return recommended_movies,recommended_movies_posters
st.header('Movie Recommender System')
sim = pickle.load(open('sim.pkl','rb'))
movies_list1 = pickle.load(open('movies.pkl','rb'))
movies = movies_list1['title'].values
# st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Type or Select a Movie name form dropdown: ",
movies)

if st.button('Show Recommendations'):
    recommended_movies,recommended_movies_posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5  = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movies_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movies_posters[1])
    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movies_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movies_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movies_posters[4])
