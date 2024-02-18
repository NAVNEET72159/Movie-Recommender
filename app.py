import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=dbbbb8361a90872c8e836693a0745815")
    response = response.json()
    poster_path = response['poster_path']
    return "https://image.tmdb.org/t/p/w500/" + poster_path

def get_recommendation(movie):
    index = movies[movies['original_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].original_title)

    return recommended_movie_names,recommended_movie_posters


st.header('Welcome to Movie Recommendation System!')
movies = pickle.load(open('res/movie_list.pkl','rb'))
similarity = pickle.load(open('res/similarity.pkl','rb'))

movie_list = movies['original_title'].values
selected_movie = st.selectbox(
    "Select a Movie",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = get_recommendation(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])