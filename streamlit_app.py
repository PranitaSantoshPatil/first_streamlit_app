import streamlit
streamlit.title('My parents new healthy diner')


streamlit.header('Breakfast Menu')
streamlit.text('Omega3 and blueberry oatmeal')
streamlit.text('Kale,spinach and rocket smoothei')
streamlit.text('🥚 🐔Hard-boiled free range egg')
streamlit.text('Avacado Toast')
streamlit.header('🥭🍌Biuld Your Own Fruit Smoothie🥝')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
