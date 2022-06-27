"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib,os
    
# The main function where we will build the actual app
def main():
    with open('styles/opiniate.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    # create the header banner
    st.image('resources/imgs/logo.png')
    st.markdown('<div class="sub-class"> Weather Sentiment Application </div>', unsafe_allow_html=True)
    st.markdown('<a href="Prediction" class="action-button"> Make Predictions </div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()