import streamlit as st
import pandas as pd
from model import recommend

# Assuming you have a music dataset df with columns 'Song', 'Artist', 'Genres', 'Tags'

st.title('Music Recommender System')

# Sample music dataset (replace this with your actual data)
df = pd.read_csv('tmdb_5000_movies.csv')

selected_song = st.selectbox('Select a song:', df['original_title'])

if st.button('Get Recommendations'):
    recommendations = recommend(selected_song)
    st.write(recommendations)
