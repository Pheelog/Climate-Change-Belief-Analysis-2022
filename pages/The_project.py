import streamlit as st
import joblib,os
import base64

with open('styles/project.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.markdown("<div class='about-head'> Weather Sentiment Analysis </div>", unsafe_allow_html=True)
st.markdown('''<div class='sub-head'> 
                The Project
            </div>''', unsafe_allow_html=True)
            
st.markdown('''<div class='sub-body'> 
                <p class="sub-par">
                    Many companies are built around lessening their environmental impact or carbon footprint.
                    They offer products and services that are environmentally friendly and sustainable, in line with their values and ideals.
                    As such, they would like to determine how people perceive climate change and whether or
                    not they believe it is a real threat. This would add to their market research efforts in
                    gauging how their product/service may be received. 
                </p>
                <p class="sub-par">
                    With this context, this notebook provides a walthrough on the creation of a Machine Learning model
                    that is able to classify whether or not a person believes in climate change based on their novel tweet data.
                    Providing an accurate and robust solution to this task gives companies access to a broad base of consumer sentiment,
                    spanning multiple demographic and geographic categories - thus increasing their insights and informing future
                    marketing strategies.
                </p>
            </div>''', unsafe_allow_html=True)

st.image('resources/imgs/climate.jpg')

st.markdown('''<div class='sub-head'> 
                The Problem
            </div>''', unsafe_allow_html=True)
st.markdown('''<div class='sub-body'> 
                <p class="sub-par">
                    The fashion industry has a destructive effect on the climate. By estimation, the fashion industry accounts for 
                    about 8% of the total CO<sub>2</sub> global emission - greater than international flights, maritime and shipping
                    industries combined. This is because people want to change clothes as quickly as possible and there is a need to match 
                    supply with the growing demand of clothes.
                </p>
            </div>''', unsafe_allow_html=True)

st.markdown('''<div class='sub-head'> 
                Our Client: Petit Pli
            </div>''', unsafe_allow_html=True)
st.markdown('''<div class='sub-body'> 
                <p class="sub-par">
                    Petit Pli is an institution which makes clothes that grow. This products makes it possible to reduce the need for new 
                    clothing by pregnant women or growing children.
                </p>
                <p class="sub-par">
                    Petit Pli needs to market this product to a suitable market. Hence they need a market where there is a sentiment which 
                    believes in climate change. These target markets are where they can maximize sales due to the belief of the people which
                    should tally with the objective of the product - ecologically friendly.
                </p>
            </div>''', unsafe_allow_html=True)
            
st.markdown('''<div class='sub-head'> 
                Our Solution: Opiniate 1.0
            </div>''', unsafe_allow_html=True)
st.markdown('''<div class='sub-body'> 
                <p class="sub-par">
                    Opiniate 1.0 is a web application for sentiment analysis. This application will allow our client to enter tweets collected  
                    from persons in a Geolocation and get the climate sentiment estimate of the environment. This will allow our Client to
                    decide on the environments where they can invest efforts and resources to maximize revenue.
                </p>
            </div>''', unsafe_allow_html=True)
