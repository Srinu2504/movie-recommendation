import pickle
import streamlit as st
import requests
with open("style.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=eaf5fc3171c5ff3f8c611e98c9d63530&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = mvs[mvs['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = mvs.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(mvs.iloc[i[0]].title)
    
    return recommended_movie_names,recommended_movie_posters
    
st.header('Movie Recommendation System')
mvs = pickle.load(open('mvs_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = mvs['title'].values
selected_movie = st.selectbox(
    "Type or select a movie",
    movie_list
)

if st.button('Search Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])

    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col4, col5, col6 = st.columns(3)
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col7, col8, col9 = st.columns(3)
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col8:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col9:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
   
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col10,col11,col12 = st.columns(3)
    
    with col10:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
   



