import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/ {}?api_key=cb27cce51af498cbb59fc109c2a4abeb&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]


    recommended=[]
    recommended_posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].id
        recommended.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended,recommended_posters


movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('.\similarity.pkl','rb'))


movies_list = movies['title'].values

st.header('Movie Recommendation System')

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies_list
)

if st.button('Show Recommendation'):
    names,posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 =  st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
