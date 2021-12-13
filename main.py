import streamlit as st
from Web_Page import Page
from ExplorePage import visualization


mains = st.sidebar.selectbox("Prediction or visualization", ("Prediction","visualization"))

if mains=="Prediction":
    Page()
else:
    visualization()

