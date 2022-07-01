# Streamlit dependencies
import streamlit as st
import joblib, os
import ipywidgets as widgets
import pandas as pd
from sklearn.linear_model import RidgeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
import re
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import feature_selection
from sklearn.feature_selection import f_classif
import base64
    
# The main function where we will build the actual app
def main():

    #loading the styles
    with open('styles/prediction.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
            
    st.sidebar.write("1: Pro - This tweet supports the belief of man-made climate change")
    st.sidebar.write("2: News - This tweet links to factual news about climate change")
    st.sidebar.write("0: Neutral - This tweet neither supports nor refutes the belief of man-made climate change")
    st.sidebar.write("-1: Anti - This tweet does not believe in man-made climate change")
    
    st.sidebar.markdown(f'''<img class="logo-down" src="data:image/png;base64,
                            {base64.b64encode(open('resources/imgs/logo.png', "rb").read()).decode()}">''', unsafe_allow_html=True)
        
    st.markdown("<div class='about-head'> Make Classification </div>", unsafe_allow_html=True)
    
    st.info("You can classify single tweets by typing in the text area. Or you can load a file of tweets to classify multiple tweets")
    
    tweet = st.text_area("Enter Tweet")
    
    file = st.file_uploader("Or Upload a CSV file", type='csv', accept_multiple_files=False)
    
    sample = st.checkbox(label="Or Use our Test Dataset", value=False)
    
    col1, col2, col3 = st.columns([1,1,1])
    
    with col1:
        ridge = st.button("Ridge Classifier")
        
    with col2:
        bayes = st.button("Bayes Classifier")
        
    with col3:
        sgdc = st.button("SGDC Model")
        
    # The preprocessing function
    def clean_data(text):
        # change the case of all the words in the text to lowercase 
        text = text.lower()
        
        # Remove links from the text
        url = re.compile(r'https?://\S+|www\.\S+')
        text =  url.sub(r'', text)
        
        # remove punctuation
        text = "".join([x for x in text if x not in string.punctuation])
        
        # Remove Emojis - Emoji Reference : https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b
        emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)
        return text

    # Apply the clean_data function
    def clean(df_test):
        df_test['message'] = df_test['message'].apply(clean_data)
        return df_test

    # Dropping unwanted features
    def drop_unwanted(dataframe, unwanted_features):
        df = dataframe.drop(unwanted_features,  axis='columns')
        return df
    
    # Vectorize dataset     
    def vectorize_data(test):
        vectorizer =  joblib.load(open(os.path.join("resources/vectorizer.pkl"),"rb"))
        test_data = vectorizer.transform(test)
        return test_data
    
    def feature_selection(df):
        selector_kbest = feature_selection.SelectKBest(score_func=f_classif, k=95000)
        train_x_new = selector_kbest.fit_transform(df)
        valid_x_new = selector_kbest.transform(validation_x)
                
    # The wrapper preprocessing function
    def preprocess(file, sample, tweet):
        if tweet != "":
            df_data = pd.DataFrame({"message":tweet, "tweetid":12345}, index=[0])
            
        elif file != None:
            df_data = pd.read_csv(file)
            
        elif sample == True:
            df_data = pd.read_csv("resources/test_with_no_labels.csv")
            
        
        df_tweet_id = df_data["tweetid"]
        df_data = clean(df_data)
        df_data = drop_unwanted(df_data, ['tweetid'])
        df_data = vectorize_data(df_data["message"])
           
        return df_data, df_tweet_id
    
    def make_prediction(model, df):
        sentiment_dict = categories = {'1':'Pro', '2':'News', '0':'Neutral', '-1':'Anti'}
        predict = model.predict(df)
        result = [sentiment_dict[str(x)] for x in predict]
        return result
    
    # Classification Logic
    model = RidgeClassifier()   # default model
    clicked = False
    
    if ridge:
        model = joblib.load(open(os.path.join("models/ridge.pkl"),"rb"))
        clicked = True
    elif bayes:
        model = joblib.load(open(os.path.join("models/bayes.pkl"),"rb"))
        clicked = True
    elif sgdc:
        model = joblib.load(open(os.path.join("models/sgdc.pkl"),"rb"))
        clicked = True
   
    
    if clicked:
        data, index = preprocess(file, sample, tweet)
        predict = make_prediction(model, data)
        result = pd.DataFrame({'tweetid':index, 'sentiment':predict})
        
        if tweet != "":
            st.success("The sentiment is {}".format(result['sentiment'][0]))
        else:
            st.dataframe(result.head())
            result = result.to_csv().encode('utf-8')
            st.download_button('Download Result', data=result, file_name='result.csv', mime='text/csv')
        
if __name__ == '__main__':
    main()
