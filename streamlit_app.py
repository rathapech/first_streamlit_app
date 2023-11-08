import streamlit
import pandas 

streamlit.title("My Parents New Healthy Diner")

streamlit.header("🥣 Breakfast menu")
streamlit.text("🥗 Omega 3 & Blueberry Oatmeal")
streamlit.text("🐔 Kale, Spinach & Rocket Somothie")
streamlit.text("🥑🍞 Hard-Boiled Free-Range Egg")

streamlit.header("🍌🥭 Build Your Own Menu 🥝🍇")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
