
from operator import mod
import streamlit as st
import pickle

# @st.cache
def load_model():
  with open('Polina_Model.pkl', 'rb') as f:
    the_model = pickle.load(f)
  return the_model

model = load_model()

st.title("Tweet Recognition")

st.subheader('Is a tweet about a real disaster?')

txt = st.text_area('Enter a disaster tweet here to check whether it\'s real or not: ').strip()

if st.button('Submit'):
  if len(txt) > 0:
    pred = model.predict([txt])[0]
    if pred > 0.8:
        st.write(f"This disaster notification is: REAL! Please stay safe!")
    elif pred > 0.5:
        st.write(f"This disaster notification might be: REAL. Please work with your local news channel to learn more.")
    else:
        st.write(f"This tweet is: NOT REAL. Please enjoy your day!")
   
  else:
    st.write('Please enter a text to check whether or not it\'s about a real disaster.')