import streamlit as st
from src.predict import predict_duplicate

#page config

st.set_page_config(page_title="Duplicate Question Detector",page_icon="❓",layout="centered")

#title
st.title("Duplicate Question Detector ❓")
st.write("Enter two questions and check whether they are duplicates or not")

#input boxes
q1=st.text_area("Question1",placeholder="Enter first question.....")
q2=st.text_area("Question2",placeholder="Enter second question ......")

#prediction button

if st.button("Predict"):
    if q1.strip()== "" or q2.strip()== "":
        st.warning("Please enter both questions ")

    else:
        probability=predict_duplicate(q1,q2)

        st.subheader("Prediction ")

        if(probability>=0.5):
            st.success("Duplicate Question ")

        else:
            st.error("Different Question , not duplicate")

        st.write(f"**Probabaility:**{probability:.4f}")