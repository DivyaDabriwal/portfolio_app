import streamlit as st
import csv

st.set_page_config(layout="wide")

content = ("""Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 Donec eget luctus quam. Maecenas pharetra consequat diam consequat 
 dignissim. Aliquam pharetra mattis libero, eu imperdiet augue posuere
  varius. Integer a venenatis lectus. Curabitur suscipit volutpat dui. 
  Donec condimentum nec quam eu posuere. In convallis eleifend dolor, 
  eget gravida nulla congue id. Maecenas massa eros, pretium ac magna 
  viverra, vehicula consectetur felis. Quisque et dapibus arcu, a gravida
   quam.""")

col1 , col2 = st.columns(2)

with col1:
    st.image('files/images/photo.png')
with col2:
    st.title('Ardit Sulce')
    st.info(content)

st.write('Below you can find some of the apps I have built in Python, Feel free to contact me!')

csv_file_content = []
with open('files/data.csv') as file:
    csv_file = csv.DictReader(file, delimiter=';')
    for i in csv_file:
        csv_file_content.append(i)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for row in csv_file_content[:10]:
        st.header(row['title'])
        st.image('files/images/' + row['image'])
        st.write(row['description'])
        st.link_button('Source Code', row['url'])

with col4:
    for row in csv_file_content[10:]:
        st.header(row['title'])
        st.image('files/images/' + row['image'])
        st.write(row['description'])
        st.link_button('Source Code', row['url'])