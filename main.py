import os
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import base64


courses_list = pickle.load(open('courses.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(course):
    index = courses_list[courses_list['course_name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_course_names = []
    for i in distances[1:7]:
        course_name = courses_list.iloc[i[0]].course_name
        recommended_course_names.append(course_name)

    return recommended_course_names

with open('download.jpeg','rb') as image_file:
    encoded_string = base64.b64encode(image_file.read())
st.markdown(f"""<style>
            .stApp {{
                background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
                background-size: cover
            }}
            </style>""",unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #8e44ad;'>Recommendation System for future skills</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #2980b9;'>Find similar courses from a dataset of over 3,000 courses from Coursera!</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #2980b9;'>Web App created by TEAM 32</h3>", unsafe_allow_html=True)


course_list = courses_list['course_name'].values
selected_course = st.selectbox(
    "Type or select a course you like :",
    courses_list
)

if st.button('Show Recommended Courses'):
    st.write("Recommended Courses based on your interests are :")
    recommended_course_names = recommend(selected_course)
    st.text(recommended_course_names[0])
    st.text(recommended_course_names[1])
    st.text(recommended_course_names[2])
    st.text(recommended_course_names[3])
    st.text(recommended_course_names[4])
    st.text(recommended_course_names[5])
    st.text(" ")
    st.markdown("<h4 style='text-align: center; color: red;'>Copyright reserved by team 32</h4>", unsafe_allow_html=True)