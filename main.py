import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('https://raw.githubusercontent.com/khushalj/Sales-Collection/main/client_secret_330242038577-me3o3fff5phglev87nhpggt4eo603b5t.apps.googleusercontent.com.json', scope)
client = gspread.authorize(creds)
sheet_name = "SalesLeads1"
worksheet_name = "Sheet1"
worksheet = client.open(sheet_name).worksheet(worksheet_name)

# Define form inputs
st.sidebar.title("Sales Lead Form")
st.sidebar.write("Enter the following details:")
name = st.sidebar.text_input("Name")
col1, col2 = st.sidebar.beta_columns([1, 2])
with col1:
    country_codes = ["+91", "+1", "+44"]
    country_code = st.selectbox("Country Code", country_codes)
with col2:
    phone_number = st.number_input("Phone Number", step=1)
email = st.sidebar.text_input("Email ID")
website = st.sidebar.text_input("Website")
requirement = st.sidebar.text_area("Requirement")
col3, col4 = st.sidebar.beta_columns([2, 1])
with col3:
    rate_quoted = st.number_input("Rate Quoted")
with col4:
    currencies = ["₹", "$"]
    currency = st.selectbox("Currency", currencies)
quotation_amount = st.sidebar.number_input("Total Quotation Amount")
timeline = st.sidebar.date_input("Timeline")
deal_status = st.sidebar.radio("Deal Status", options=["Open", "Close"])

# Define form submission action
def on_submit():
    name = st.session_state.name
    phone_number = st.session_state.country_code + str(int(st.session_state.phone_number))
    email = st.session_state.email
    website = st.session_state.website
    requirement = st.session_state.requirement
    rate_quoted = str(st.session_state.rate_quoted) + st.session_state.currency
    quotation_amount = st.session_state.quotation_amount
    timeline = st.session_state.timeline.strftime("%m/%d/%Y")
    deal_status = st.session_state.deal_status
    
    # Create a new row in the Google Sheet with the form data
    row = [name, phone_number, email, website, requirement, rate_quoted, quotation_amount, timeline, deal_status]
    worksheet.append_row(row)
    
    st.success('Form submitted successfully!')

# Add form submission button
st.sidebar.button("Submit", on_click=on_submit)
