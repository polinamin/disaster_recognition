# Disaster Tweet Recognition

Twitter/X.com plays a crucial role as a communication platform during emergencies, facilitated by the widespread use of smartphones that allow real-time reporting of critical incidents. Consequently, there is a growing interest among various organizations, such as disaster relief agencies and news outlets, in systematically tracking Twitter for such information.

Our project, led by a team of three consultants, focuses on the development of a tweet classification model capable of distinguishing between tweets related to disasters and those that are not. We have also created a functional prototype using Streamlit, allowing users to input a tweet and receive an instant assessment regarding its relevance to an emergency situation.

Throughout our modeling journey, we explored various machine learning algorithms, including LSTM, Random Forest Classifier, and Logistic Regression classification. In addition, we experimented with advanced techniques, such as Word2Vec, and pretrained embeddings, such as GloVe, to enhance the processing of our data.

For our app, we decided to implement a Bernoulli Naïve Bayes model due to its remarkable balance between accuracy, minimal overfitting, and high sensitivity. This choice reflects our priority in minimizing False Negatives, ensuring that tweets related to genuine disasters are not misclassified as 'safe' tweets.

Our project has not only deepened our understanding of classification and natural language processing (NLP) but has also resulted in a functional prototype that we are proud of. Looking ahead, we aim to further enhance our model and implement it for real-time classification of live-streamed tweets, ensuring rapid identification of disaster-related content with precision and efficiency.

### Software Requirements:
    - Pandas
    - Scikit-learn 
    - NLTK 
    - Numpy 
    - Matplotlib 
    - Seaborn 
    - Streamlit
    - * TensorFlow (Not required) - utilized in marked notebooks(see File Structure below)
    
### Application:

To run the application, install all required libraries above(TF is not required). And run the following command from the local repo **/streamlit** directory:


```console
streamlit run Model_Streamlit.py
```

<img src =images/App_image.PNG/>

### File structure:

- Code folder
    - **disaster_recognition.ipynb** 
        - A thorough walkthrough of our final process. Final Model - Bernoulli Naive Bayes
        - Includes:
            - Exploration of Data with relevant visualizations
            - Various preprocessing techniques - CountVectorizer vs. TFIDF(Term-Frequency-Inverse-Document-Frequency) with other considerations
            - Experimentation with various techniques including: Logistic Regression, Decision Trees, ADA Boosted Random Forest, and Naive Bayes
            - Model Evaluation -Comparing all the models- MNB was chosen for balance between accuracy, minimal overfitting, and high sensitivity
        - Requirements (listed below--under 'Software Requirements')
    - trial and error folder: contains other models and explorations
        - GloVe_LSTM.ipynb 
            - Requires TensorFlow and GloVe Embeddings as described in the top cell of notebook
            - A thorough walkthrough of utilizing GloVe Embeddings to feed corpus into various LSTM Networks. Used in Kaggle competition, however, for this project, we prioritized Sensitivity, therefore, was not chosen for final App
        - Kalpa__notebook.ipynb
            - A thorough walkthrough of preprocessing, visualizations, and more Machine Learning Techniques. Notably, Logistic Regression, Random Forest, KNN, MNB, and Linear SVC. Diligent model Evaluation -- differing preprocessing techniques than the final model used in project
        - Data_Model_NN_Polina.ipynb
            - Requires TensorFlow
            - An Exploration of further LSTM architectures. Additionally, an experimentation and utilization of Word2Vec Embeddings - trained on the corpus of tweets
        - Kalpa_Kaggle folder: contains csv files used/created in the prototyping phase
        
- Data folder
    - train.csv
        - 'id' (*int64*): A unique identifier for each tweet.
        - 'text' (*string*): The textual content of the tweet.
        - 'keyword' (*string*): A hashtag or keyword associated with the tweet, though this field may be empty in some cases.
        - 'location' (*string*): The originating location of the tweet. This field may also be blank.
        - 'target' (*int64*): A binary indicator (1 or 0) that classifies the tweet as either a disaster tweet (1) or a non-disaster tweet (0).
    - test.csv - same as train.csv with no 'target'
    - misc data folder: contains other cleaned data used/created in modeling and prototyping
        
- Images folder
    - Images used /created throughout the project

- Pickles folder
    - **Bernoulli_Model.pkl** - Final pickled model that is used in the Streamlit App
    - trial and error folder: contains other miscellaneous pickled objects used in prototyping phase
 

- Streamlit folder
    - **Model_Streamlit.py** - streamlit App code
    - Files utilized in the App
    - trial and error folder: contains other files NOT used in final application
    
- Submissions folder
    - Files used for an [external kaggle competition](https://www.kaggle.com/competitions/nlp-getting-started/overview)

    
### Data Description:

Data Acquisition: [From this kaggle competition](https://www.kaggle.com/competitions/nlp-getting-started/data) -- future ingestion could be through X.com API

Data Ingestion and Cleaning: Standard practices of tokenization and stop word removal were used. Various techniques were explored including stemming, lemmatization, removal of duplicates, usernames, URLs, and emoticons. Thorough walkthrough found in disaster_recognition.ipynb

Only 'text' feature was used for this prototype. Future versions will include experimentation with other features.

train.csv - 7,613 labeled tweets

test.csv - 3,263 unlabeld tweets


#### Columns:
    - id - a unique identifier for each tweet
    - text - the text of the tweet
    - location - the location the tweet was sent from (may be blank)
    - keyword - a particular keyword from the tweet (may be blank)
    - target - in train.csv only, this denotes whether a tweet is about a real disaster (1) or not (0)



### Model Evaluation:
<img src= images/model_performance.PNG>


### Contributors:

**Polina Minkovski** 
    - [Github](https://github.com/polinamin)
    - [LinkedIn](https://www.linkedin.com/in/polinaminkovski/)
    
**Kalpa Henadhira Arachchige** 
    - [Github](https://github.com/kharindra)
    -[LinkedIn](https://www.linkedin.com/in/kalpa-henadhira/)
    
**Kalyan Lakshmanan** 
    - [Github](https://github.com/polinamin) 
    - [LinkedIn](https://www.linkedin.com/in/kalyanlakshmanan/) 

### Special Thanks
- To our advisors: Musfiqur Rahman, Sonyah Seiden, and Eric Bayless
