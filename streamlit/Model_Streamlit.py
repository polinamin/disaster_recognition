
from operator import mod
import streamlit as st
import pickle
import numpy as np

#def local_css(file_name):
#    with open(file_name) as f:
#        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#local_css("style.css")
import base64

#code assist to embed local image as background: https://stackoverflow.com/questions/72582550/how-do-i-add-background-image-in-streamlit
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: contain;
    background-repeat:no-repeat;
    #margin-top: 200px;
    }

    
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

#set_background('Disaster_background.png')


# @st.cache
#def load_model():
#  with open('Polina_Model.pkl', 'rb') as f:
#    the_model = pickle.load(f)
#  return the_model

file_name = pickle.load(open('Polina_Model.pkl','rb'))


model = file_name
#new_title = '<p style="font-family:sans-serif; color:White; font-size: 64px;">Tweet Recognition</p>'
#st.markdown(new_title, unsafe_allow_html=True)
st.title("Tweet Recognition")
#new_subtitle = '<p style="font-family:sans-serif; color:White; font-size: 32px;">Is a tweet about a real disaster?</p>'
#st.markdown(new_subtitle, unsafe_allow_html=True)
st.subheader('Is a tweet about a real disaster?')

txt = st.text_area('Enter a disaster tweet here to check whether it\'s real or not: ').strip()
risk = st.slider('Please enter your risk threshold: ', 0.0, 1.0, 0.1)

pred = model.predict_proba([txt])[0][1]
#preds = pred if pred > risk
st.write(f"Calculated probability that this tweet is a disaster: {np.round(pred*100,2)}%")

if st.button('Submit'):
  if len(txt) > 0:
    if pred >= risk or pred > 0.8:
        st.error(f"This disaster notification is: REAL. Please stay safe!")
    elif pred < risk and risk > 0.8:
        st.success(f"This tweet is: NOT REAL. Please enjoy your day!")
    elif pred < risk and pred > 0.5:
        st.warning(f"This disaster notification might be: REAL. Please work with your [local news channel](https://news.google.com/) to learn more.")
        
    else:
        st.success(f"This tweet is: NOT REAL. Please enjoy your day!")