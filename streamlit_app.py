import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title('My parents new healthy diner')


streamlit.header('Breakfast Menu')                                     
streamlit.text('Omega3 and blueberry oatmeal')
streamlit.text('Kale,spinach and rocket smoothei')
streamlit.text('🥚 🐔Hard-boiled free-range egg')
streamlit.text('Avacado Toast')
streamlit.header('🥭🍌Biuld Your Own Fruit Smoothie🥝')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show =my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return (fruityvice_normalized)
streamlit.header("Fruityvice Fruit Advice!")
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
 else:
  back_from_function=get_fruityvice_data(fruit_choice)
  streamlit.dataframe(back_from_function)
except URLerror as e:
  streamlit.error()






#import snowflake.connector


#snowflake related function
streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
   with  my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return  my_cur.fetchall()
#add a button to load the fruit
if streamlit.button('Get Fruit load list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)
   
   
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')")
      return "Thanks for adding "+ new_fruit 
add_my_fruit = streamlit.text_input('What fruit would you like to add?')   
if streamlit.button('Add a fruit to the list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_funcction = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)
   
   
streamlit.write('Thanks for adding ',add_my_fruit)  
   
streamlit.stop()   
   
  

streamlit.write('Thanks for adding ', add_fruit)




