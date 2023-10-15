import pickle
import streamlit as st

import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import nltk


# First some helper functions:
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


def tweet_to_input(tweet,tokenizer=tokenizer):
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




# ok load the pickled files

with open('../pickles/arjun_model_3.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
    
with open('../pickles/tokenizer_arjun_v1.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)
    
# 

# Create a title for our app
st.title("Which author do you write like?")

# Get user input
user_text = st.text_input('Please copy-paste the tweet in question: ', max_chars = 280)

# Get the prediction

pred_prob = model.predict(tweet_to_input(user_text,tokenizer=tokenizer))

# Display prediction
st.write(f'Our model thinks this is {pred_prob*100}% probabilty regarding a disaster')