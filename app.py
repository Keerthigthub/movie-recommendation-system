import streamlit as st
import pickle

st.title("Movie Recommendation System")

movie_list = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movie_list.iloc[i[0]].title)

    return recommended_movies


selected_movie = st.selectbox(
    "Select a movie",
    movie_list['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)