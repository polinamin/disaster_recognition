# Monitoring tweets to determine potential Disasters

Twitter/X.com plays a crucial role as a communication platform during emergencies, facilitated by the widespread use of smartphones that allow real-time reporting of critical incidents. Consequently, there is a growing interest among various organizations, such as disaster relief agencies and news outlets, in systematically tracking Twitter for such information.

Our project, led by a team of three consultants, focuses on the development of a tweet classification model capable of distinguishing between tweets related to disasters and those that are not. We have also created a functional prototype using Streamlit, allowing users to input a tweet and receive an instant assessment regarding its relevance to an emergency situation.

Throughout our modeling journey, we explored various machine learning algorithms, including LSTM, Random Forest Classifier, and Logistic Regression classification. In addition, we experimented with advanced techniques such as Word2Vec and pretrained embeddings, such as GloVe, to enhance the processing of our data.

For our app, we decided to implement a Bernoulli Naïve Bayes model due to its remarkable balance between accuracy, minimal overfitting, and high sensitivity. This choice reflects our priority in minimizing False Negatives, ensuring that tweets related to genuine disasters are not misclassified as 'safe' tweets.

Our project has not only deepened our understanding of classification and natural language processing (NLP) but has also resulted in a functional prototype that we are proud of. Looking ahead, we aim to further enhance our model and implement it for real-time classification of live-streamed tweets, ensuring rapid identification of disaster-related content with precision and efficiency.

### Contributors:

    - Polina Minkovski - [Github](https://github.com/polinamin) [LinkedIn](https://www.linkedin.com/in/polinaminkovski/)
    - Dr. Kalpa Henadhira Arachige - [Github](https://github.com/kalymaan) [LinkedIn](https://www.linkedin.com/in/kalpa-henadhira/)
    - Kalyan Lakshmanan - [Github](https://github.com/polinamin) [LinkedIn](https://www.linkedin.com/in/kalyanlakshmanan/) 

### File structure:

- Code
    - reddit_data_collection.ipynb
        - Explanation and execution of reddit question-answer pair scraping
    - 
    -
    -
- Data
    - train.csv
        - **id** (*int64*): A unique identifier for each tweet.
        - **text** (*string*): The textual content of the tweet.
        - **keyword** (*string*): A hashtag or keyword associated with the tweet, though this field may be empty in some cases.
        - **location** (*string*): The originating location of the tweet. This field may also be blank.
        - **target** (*int64*): A binary indicator (1 or 0) that classifies the tweet as either a disaster tweet (1) or a non-disaster tweet (0).
    - test.csv - same as train.csv with no 'target'
    -
    -
        
- Images - Various images used throughout the project

- Streamlit 
    - reddit_questions1-5.csv - csvs generated from reddit scraping
    -
    -
    -
- Submissions - files used for an [external competition](https://www.kaggle.com/competitions/nlp-getting-started/overview)

### Special Thanks
- To our advisors: Musfiqur Rahman, Sonyah Seiden, and Eric Bayless