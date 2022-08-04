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
my_fruit_list=my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show =my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)




streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")


fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)






import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('The user entered ', add_fruit)



