import streamlit as st
import joblib,os
import base64
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open('styles/climate.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.markdown("<div class='about-head'> The Weather Data </div>", unsafe_allow_html=True)

# display distribution
st.markdown('''<div class='sub-head'> 
                More Tweets for the Support of Man-made Climate
            </div>''', unsafe_allow_html=True)
st.markdown('''<div class='sub-body'> 
                <p class="sub-par">
                    There are more tweets in support of the belief of man-made Climate Change. 
                    Infact more than half of the entire tweets.
                </p>
            </div>''', unsafe_allow_html=True)
st.image('resources/imgs/distribution.jpg')



# display distribution
st.markdown('''<div class='sub-head'> 
                What are the Key Hashtags in Climate Tweets
            </div>''', unsafe_allow_html=True)
st.image('resources/imgs/hashtags.jpg')
st.markdown('''<div class='sub-body'> 
                <p class="sub-par">
                    There are events and situations which influences the conversations around climate change. A look at the 
                    Hashtags gives an insight into such events. Before the flood is a popular hashtag used in pro climate change tweets. 
                    This refers to a 2016 documentary where actor Leonardo DiCaprio meets with scientists, activists and world leaders to
                    discuss the dangers of climate change and possible solutions.
                    In the anti climate change tweets, MAGA (Make America great again) is the top popular hashtag. 
                    It is a slogan that was often used by Donald Trump during his campaign for elections in 2016. 
                    This soon became a trending hashtag to use to show support for Donald Trump.,
                </p>
            </div>''', unsafe_allow_html=True)



# display distribution
st.markdown('''<div class='sub-head'> 
                What are the Key Handles in Climate Tweets?
            </div>''', unsafe_allow_html=True)
st.markdown('''<div class='sub-body'> 
                <p class="sub-par">
                    The conservation of climate has been a motion which started long ago. Some institutions and individuals
                    have been on the fore-front of the movement. A look at the handles in each tweet.
                </p>
            </div>''', unsafe_allow_html=True)
st.image('resources/imgs/hashtags.jpg')


# display distribution
st.markdown('''<div class='sub-head'> 
                Retweets
            </div>''', unsafe_allow_html=True)
st.markdown('''<div class='sub-body'> 
                <p class="sub-par">
                    The term retweet refers to a reposted tweet. Most times people retweet posts which they agree with. In some instances
                    though, people can retweet a tweet with a quote showing their reservations. The sentiment for man-made climate change 
                    has about twice more retweets than other sentiments.
                </p>
            </div>''', unsafe_allow_html=True)
st.image('resources/imgs/retweets.jpg')