from joblib import load
import streamlit as st
import numpy as np

model_newHPP=load("newHPP.joblib")

def model(a1,a2,a3,a4,a5,a6,a7):
    l=[a1,a2,a3,a4,a5,a6,a7]
    b=np.array(l).reshape(1,-1)
    n=model_newHPP.predict(b)
    st.write(f"Price of house is : {n[0]}")

if __name__=="__main__":
    st.title("HOUSE PRICE PREDICTION:")
    b1=st.text_input("NO")
    b2=st.text_input("transaction date")
    b3=st.text_input("house age")
    b4=st.text_input("distance to the nearest MRT station")
    b5=st.text_input("number of convenience stores")
    b6=st.text_input("latitude")
    b7=st.text_input("longitute")
    
    if st.button("Click for Predicting Price"):
        model(b1,b2,b3,b4,b5,b6,b7)
        st.success("thanks for using ours service")