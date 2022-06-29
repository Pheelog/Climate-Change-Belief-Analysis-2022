import streamlit as st
import joblib,os
import base64

with open('styles/about.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.markdown("<div class='about-head'> About Us </div>", unsafe_allow_html=True)

st.markdown('''<p class='about-body'> Polaroids is an institution that makes sense of data using machine learning methods
                                       to provide solutions that improve lives. Our mission is to drive changes that lead to a greener earth.
                                       </p>''', unsafe_allow_html=True)

st.markdown(
    f"""
        <div class="each-image">
            <div class="img-cont">
                <img class="team-img" src="data:image/png;base64,{base64.b64encode(open('resources/imgs/pheelo.jpeg', "rb").read()).decode()}">
            </div>
            <p class="team-name">Philip Ogunmola</p>
        </div>
        <div class="each-image">
            <div class="img-cont">
                <img class="team-img" src="data:image/png;base64,{base64.b64encode(open('resources/imgs/abdul.jpeg', "rb").read()).decode()}">
            </div>
            <p class="team-name">Abubakar Abdulkadir</p>
        </div>
        <div class="each-image">
            <div class='img-cont'>
                <img class="team-img" src="data:image/png;base64,{base64.b64encode(open('resources/imgs/joseph.jpeg', "rb").read()).decode()}">
            </div>
            <p class="team-name">Joseph Mugo</p>
        </div>
        <div class="each-image">
            <div class='img-cont'>
                <img class="team-img" src="data:image/png;base64,{base64.b64encode(open('resources/imgs/rogers.jpeg', "rb").read()).decode()}">
            </div>
            <p class="team-name">Rogers Mugambi</p>
        </div>
        <div class="each-image">
            <div class='img-cont'>
                <img class="team-img" src="data:image/png;base64,{base64.b64encode(open('resources/imgs/nana.jpeg', "rb").read()).decode()}" />
            </div>
            <p class="team-name">Adewale Nana</p>
        </div>
        <div class="each-image">
            <div class='img-cont'>
                <img class="team-img" src="data:image/png;base64,{base64.b64encode(open('resources/imgs/philip.jpeg', "rb").read()).decode()}">
            </div>
            <p class="team-name">Philip Wambua</p>
        </div>
    """,
    unsafe_allow_html=True
)
