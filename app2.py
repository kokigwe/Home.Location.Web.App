import streamlit as st
from PIL import Image

st.title("Affordable Home Location App")
st.header("welcome to the home location App")

img=Image.open('IMG-20240629-WA0006 (2).jpg')
st.sidebar.image(img)


st.write("This app will help you locate an affordable home")
st.text_input("Full Name")
st.number_input("Age")

st.radio("Gender",['Male','Female'])
st.radio("Marital Status",['Married','Single','Devorced'])

st.selectbox("City of choice",['New York','London','Paris','Toronto','Berlin','Amsterdam','Rome'])

st.multiselect("House Type",['One Bedroom','Two Bedrooms','Three Bedrooms','Four Bedroom'])
st.text_area("Describe your top priorities")

st.file_uploader("Upload a floorplan you prefer",type=['csv','pdf','doc'])

st.number_input("What is Your Budget")
st.number_input("What kind of House Do you want")
st.date_input("What date do you plan to move in")

st.sidebar.subheader("HOME LOCATOR")
st.checkbox("Please agree to terms and conditions")