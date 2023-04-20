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
phone_row = st.row_widget(label='Phone Number')
country_code = phone_row.selectbox('Country Code', country_codes)
phone_number = phone_row.text_input('Phone Number')
email = st.text_input('Email')
website = st.text_input('Website')
requirement = st.text_area('Requirement')
rate_row = st.row_widget(label='Rate Quoted')
rate = rate_row.number_input('Rate')
currency = rate_row.selectbox('Currency', currencies)
amount_row = st.row_widget(label='Total Quotation Amount')
amount = amount_row.number_input('Amount')
amount_currency = amount_row.selectbox('Currency', currencies)
timeline = st.text_input('Timeline')
status = st.selectbox('Deal Status', ['Open', 'Close'])

# Add the lead to the CSV file when the submit button is clicked
if st.button('Submit'):
    phone_number = country_code + phone_number
    rate_quoted = str(rate) + currency
    total_quotation_amount = str(amount) + amount_currency
    save_data(name, phone_number, email, website, requirement, rate_quoted, currency, timeline, status, total_quotation_amount)
    st.write('Data saved to CSV file!')
