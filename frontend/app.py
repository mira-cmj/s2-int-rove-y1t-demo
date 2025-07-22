import streamlit as st
import requests

st.title("Rewards Redemption Optimizer")

st.write("Find the best-value travel redemptions for your airline miles!")

origin = st.text_input("Origin Airport Code (e.g., JFK)")
destination = st.text_input("Destination Airport Code (e.g., LAX)")
date = st.date_input("Travel Date")

if st.button("Search"):
    if origin and destination and date:
        params = {
            "origin": origin,
            "destination": destination,
            "date": date.strftime("%Y-%m-%d")
        }
        try:
            response = requests.get("http://localhost:8000/search", params=params)
            data = response.json()
            st.write("Results:", data.get("results", []))
        except Exception as e:
            st.error(f"Error contacting backend: {e}")
    else:
        st.warning("Please fill in all fields.")