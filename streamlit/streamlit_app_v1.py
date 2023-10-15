import pickle
import streamlit as st
from operator import mod

from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import nltk




# some helper functions:
# tweet_cleaner() does some initial cleaning of the tweet
# tweet_to_input() gets the cleaned tweet ready to put in the model 

def tweet_cleaner(tweet , remove_usernames = True):
  '''
  made for cleaning the tweet

  input: tweet: an uncleaned tweet with a 'string datatype
         remove_usernames: bool if usernames should be included or not. even if included, @ symbol is removed

  output: cleaned tweet with all stopwords removed

  '''
  #first remove usernames
  if remove_usernames:
    tweet = re.sub('@[^\s]+','',tweet)

  # remove urls
  tweet = re.sub('http[^\s]+','',tweet)
  tweet = re.sub('https[^\s]+','',tweet)
  tweet = re.sub('www[^\s]+','',tweet)

  # just capture words
  pattern = r'\b[a-zA-Z]+\b'

  # including new stopwords unique to tweets. and adding them to nltk
  stops = nltk.corpus.stopwords.words('english')
  new_stop_words = ["ha", "wa", "http", "s", "https", "com", "'s", "' s", "'ll", "' ll", "' d", "'d", "'re", "' re", "co", "amp", "url"]
  stops.extend(new_stop_words)

  # Gets list of words from re.findall() and filters out stop words and 1 letter words
  list_of_words = [x.lower() for x in re.findall(pattern, tweet) if (x not in stops) and (len(x)>1)]

  return ' '.join(list_of_words)


def tweet_to_input(tweet,tokenizer):
  '''
  Function that transforms asingle tweet(string) into an input for the model that was trained with a particular tokenizer
  input: tweet = single tweet that is a string
         tokenizer = tensorflow tokenizer used to train the model that we are getting predicitons from

  output: input array for model of shape (,max_padded_sequence_length)  aka (1,25) for this particular model

  requires:
            - tweet_cleaner() custom function
            - tensorflow.keras.preprocessing.Tokenizer object that was used in model training
            - pad_sequences() function from tensorflow.keras.preprocessing.sequence

  '''

  cleaned_tweet = list(map(tweet_cleaner,[tweet]))

  sequence = tokenizer.texts_to_sequences(cleaned_tweet)

  padded_array = pad_sequences(sequence, maxlen=25)

  return padded_array





# Define the background image URL
background_image_url = 'https://www.computerhope.com/jargon/t/twitter.png'

# Create custom HTML and CSS to set the background image as a cover
page_bg = f"""
<style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
    }}
</style>
"""

## Adding a falling animation
flow = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
          @keyframes falling {
            from {
              transform: translateY(-10%);
              opacity: 3;
            }
            to {
              transform: translateY(100%);
              opacity: 5;
            }
          }
        
          .raindrop {
            position: absolute;
            display: inline-block;
            font-size: 180px;
            animation: falling 20s linear infinite;
            right: 30%;
          }
        
        </style>
        </head>
        <body>
          <div class="rain-container">
            <div class="raindrop">☠️🏴‍☠️</div>
          </div>
        </body>
        </html>
        """
        
st.markdown(flow, unsafe_allow_html=True)


# Apply the custom CSS to the app
st.markdown(page_bg, unsafe_allow_html=True)


# load the pickled files

with open('../pickles/arjun_model_3.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
    
with open('../pickles/tokenizer_arjun_v1.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)
    

# Title for our app
st.title("Tweet Recognition")
st.subheader('Is a tweet about a real disaster?')

# Get user input

user_txt = st.text_area('Enter a disaster tweet here to check whether it\'s real or not: ', max_chars = 280)


if st.button('Submit'):
  if len(user_txt) > 0:
    pred_prob = model.predict(tweet_to_input(user_txt,tokenizer=tokenizer))[0][0]
    
    if pred_prob > 0.8:
        st.write(f"This disaster notification is: REAL! Please stay safe!")
    elif pred_prob > 0.4:
        st.write(f"This disaster notification might be: REAL. Please work with your local news channel to learn more.")
    else:
        st.write(f"This tweet is: NOT REAL. Please enjoy your day!")
   
  else:
    st.write('Please enter a text to check whether or not it\'s about a real disaster.')

    

