import streamlit as st
import pandas as pd

# Create a function to save the data to a CSV file
def save_data(name, phone, email, website, requirement, rate, currency, timeline, status, amount):
    data = pd.read_csv('leads.csv')
    new_data = pd.DataFrame({'Name': [name], 'Phone': [phone], 'Email': [email], 'Website': [website], 
                             'Requirement': [requirement], 'Rate Quoted': [rate], 'Currency': [currency], 'Timeline': [timeline], 
                             'Deal Status': [status], 'Total Quotation Amount': [amount]})
    data = data.append(new_data, ignore_index=True)
    data.to_csv('leads.csv', index=False)

# Create a list of country codes
country_codes = ['+1', '+44', '+61', '+91']

# Create a list of currencies
currencies = ['₹', '$']

# Create a Streamlit app
st.title('Lead Management System')
st.write('Enter your lead information below:')

# Create input fields for name, phone, email, website, requirement, rate, currency, timeline, status, and amount
name = st.text_input('Name')
phone_col, currency_col = st.columns(2)
with phone_col:
    phone = st.number_input('Phone', format='%d', step=1)
with currency_col:
    currency = st.selectbox('Currency', currencies)
country_code_col, phone_col = st.columns(2)
with country_code_col:
    country_code = st.selectbox('Country Code', country_codes)
with phone_col:
    phone_number = st.text_input('Phone Number')
email = st.text_input('Email')
website = st.text_input('Website')
requirement = st.text_area('Requirement')
rate_col, amount_col = st.columns(2)
with rate_col:
    rate = st.number_input('Rate Quoted')
with amount_col:
    amount = st.number_input('Total Quotation Amount')
timeline = st.text_input('Timeline')
status = st.selectbox('Deal Status', ['Open', 'Close'])

# Add the lead to the CSV file when the submit button is clicked
if st.button('Submit'):
    phone_number = country_code + phone_number
    rate_quoted = str(rate) + currency
    total_quotation_amount = str(amount) + currency
    save_data(name, phone_number, email, website, requirement, rate_quoted, currency, timeline, status, total_quotation_amount)
    st.write('Data saved to CSV file!')
