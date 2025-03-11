import streamlit as st

st.header("Calculator")

def calc():
    First_number=st.number_input("Enter the first number ")
    opratore=st.text_input("Enetr the opratore ")
    Second_number=st.number_input("Enter the second number ")

    if opratore=="+":
        return First_number+Second_number
    elif opratore=="-":
        return First_number-Second_number
    elif  opratore=="*":
        return First_number*Second_number
    elif opratore=="/":
        if Second_number<=0:
            return "Divison by Zero Error"
        return First_number/Second_number
    else:
        return "Invalid opratore"
    

res=calc()
   
if st.button("submit"):

    st.success(f"result:{res}")
