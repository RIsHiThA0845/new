import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()
#BASE_URL=os.getenv("BASE_URL")
BASE_URL1=os.getenv("BASE_URL1")
 
st.title("Item Manager")
 
st.header("Add Item")
name = st.text_input("Name")
price = st.number_input("Price", min_value=0.0)
 
if st.button("Save"):
    data = {"name": name, "price": price}
    res = requests.post(f"{BASE_URL1}/item", json=data)
    st.write(res.json())
 

st.header("All Items")
res = requests.get(f"{BASE_URL1}/items")
if res.status_code == 200:
    st.json(res.json())
 