import streamlit as st
import pandas as pd

# Load country codes from CSV file
country_codes = pd.read_csv('https://raw.githubusercontent.com/khushalj/Sales-Collection/main/Country%20Codes.csv')

# Define input fields for name, phone number, email, website, requirement, rate quoted, timeline, deal status, and total quotation amount
name = st.text_input('Name')
phone_number = st.number_input('Phone Number', format='%d', step=1)
country_code = st.selectbox('Country Code', country_codes['Code'])
email = st.text_input('Email ID')
website = st.text_input('Website')
requirement = st.text_area('Requirement')
rate_quoted = st.number_input('Rate Quoted', format='%f')
timeline = st.date_input('Timeline')
deal_status = st.selectbox('Deal Status', ['Open', 'Close'])
total_quotation_amount = st.number_input('Total Quotation Amount', format='%f')

# Add the data to a pandas DataFrame
data = {'Name': [name],
        'Phone Number': [str(country_code) + str(phone_number)],
        'Email ID': [email],
        'Website': [website],
        'Requirement': [requirement],
        'Rate Quoted': [rate_quoted],
        'Timeline': [timeline],
        'Deal Status': [deal_status],
        'Total Quotation Amount': [total_quotation_amount]}
df = pd.DataFrame(data)

# Display the data in a table
st.write(df)
