# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:16:58 2024

@author: USER
"""

# calculator_app.py

import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

st.title("Basic Calculator")

operation = st.selectbox("Choose an operation:", ("Add", "Subtract", "Multiply", "Divide"))
num1 = st.number_input("Enter first number:", format="%.2f")
num2 = st.number_input("Enter second number:", format="%.2f")

if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    
    st.write("The result is:", result)
