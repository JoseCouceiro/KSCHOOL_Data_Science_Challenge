import os
import time
import streamlit as st
import pandas as pd

# Display
st.title('Exercise 5')
st.markdown('**Top arrival airports in the world**')
st.markdown('Please, select the year and the number of airports to be displayed:')
top_number = st.slider('Number of airports', min_value=10, max_value=200, step=10)
year = st.number_input('Select a year between 2013 and 2020', min_value=2013, max_value=2020)
st.write('Selected year', year)
with st.spinner('Calculating...'):
    time.sleep(5)


# Calculations
bookings_sample = pd.read_csv(os.path.join('data', 'bookings.csv.bz2'), sep='^', chunksize=100000)

list_iterations = []
for chunk in bookings_sample:
    iteration = chunk[chunk['year']==year].groupby('arr_port').sum()[['pax']]
    list_iterations.append(iteration)

data_concat = pd.concat(list_iterations).groupby('arr_port').sum()[['pax']]
solution = data_concat.sort_values(by = 'pax', ascending = False).head(top_number).to_json()

# Display solution
st.success('Data ready!')
st.json(solution)

