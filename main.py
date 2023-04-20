import streamlit as st
import pandas as pd
import numpy as np
import pycountry

# Create a dictionary of country codes and names
country_dict = {country.alpha_2: country.name for country in pycountry.countries}

# Create a list of tuples for the country code dropdown
country_codes = [f'{code} ({country_dict[code]})' for code in country_dict.keys()]

# Create a Streamlit app
st.title('Lead Form')
st.write('Enter your lead information below:')

# Create input fields for name, phone number, email, website, requirement, rate quoted, timeline, deal status, and total quotation amount
name = st.text_input('Name')
phone_country_code = st.selectbox('Phone Country Code', country_codes)
phone_number = st.number_input('Phone Number', value=0)
email = st.text_input('Email')
website = st.text_input('Website')
requirement = st.text_input('Requirement')
rate_quoted = st.number_input('Rate Quoted', value=0.0)
timeline = st.text_input('Timeline')
deal_status = st.selectbox('Deal Status', ['Open', 'Close'])
total_quotation_amount = st.number_input('Total Quotation Amount', value=0.0)

# Extract the country code from the dropdown value
country_code = phone_country_code.split()[0]

# Create a button to submit the form
if st.button('Submit'):
    # Store the data in a Pandas DataFrame
    data = {
        'Name': [name],
        'Phone Number': [f'{country_code}{phone_number}'],
        'Email': [email],
        'Website': [website],
        'Requirement': [requirement],
        'Rate Quoted': [rate_quoted],
        'Timeline': [timeline],
        'Deal Status': [deal_status],
        'Total Quotation Amount': [total_quotation_amount]
    }
    df = pd.DataFrame(data)
    
    # Save the data to a Google Sheet
    # (Replace with your own credentials and sheet URL)
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/your_sheet_id/edit#gid=0')
    worksheet = sh.get_worksheet(0)
    worksheet.append_row(df.values.tolist()[0])
    
    # Display a success message
    st.success('Lead data saved successfully!')
