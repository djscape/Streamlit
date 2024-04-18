import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

"""col1, col2, col3 = st.columns(3)
col1.metric('Temperature', '70 ˚F', '1.2 ˚F')
col2.metric('Wind', '9 mph', '-8%')
col3.metric('Humidity', '86%', '4%')

st.metric(label='Temp_Seoul', value='20 ˚C', delta='1.2 ˚C')
st.metric(label='Temp_Busan', value='19 ˚C', delta='-0.8 ˚C')
st.metric(label='Temp_Daegu', value='25 ˚C', delta='3.4 ˚C', delta_color='inverse')
st.metric(label='Temp_Suwon', value='21 ˚C', delta='-1.5 ˚C', delta_color='normal')
st.metric(label='Temp_Ulsan', value='20 ˚C', delta='2.0 ˚C', delta_color='off')

st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

add_sidebar = st.sidebar.selectbox(
    'Favorite food?',
    ('Apple', 'Banana', 'Pop corn')
)

if add_sidebar == 'Apple':
    st.write('YOU Choose APPLE!')
elif add_sidebar == 'Banana':
    st.write('YOU Choose BANANA!')
else:
    st.write('YOU Choose POP CORN!')

with st.sidebar:
    add_radio = st.radio(
        'choose a language',
        ('English', 'Korean', 'Python')
    )
    if add_radio == 'Python':
        st.write('God Python')
    elif add_radio == 'English':
        st.write('English!')
    else:
        st.write('YOU Choose K-Language!')"""