import streamlit as st
import pickle
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()


retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=49341459ac683876652d2b85d5b8ef29&language=en-US'
    
    try:
        
        response = session.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        
        if data.get('poster_path'):
            return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
        else:
            
            return "https://via.placeholder.com/500x750?text=No+Poster+Found"
            
    except Exception as e:
        
        return "https://via.placeholder.com/500x750?text=API+Error"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    
    for i in movies_list:
        
        actual_movie_id = movies.iloc[i[0]].movie_id 
        
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(actual_movie_id))
        
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:', 
    movies['title']
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5) 


    title_css = """
    <div style="height: 60px; display: flex; align-items: flex-end; justify-content: center; margin-bottom: 10px;">
        <p style="text-align: center; font-size: 14px; font-weight: bold; margin: 0; line-height: 1.2; word-wrap: break-word;">{}</p>
    </div>
    """
    
    with col1:
        st.markdown(title_css.format(names[0]), unsafe_allow_html=True)
        st.image(posters[0])
    with col2:
        st.markdown(title_css.format(names[1]), unsafe_allow_html=True)
        st.image(posters[1])
    with col3:
        st.markdown(title_css.format(names[2]), unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        st.markdown(title_css.format(names[3]), unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        st.markdown(title_css.format(names[4]), unsafe_allow_html=True)
        st.image(posters[4])