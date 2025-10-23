import streamlit as st
import pandas as pd

# Set the page title
st.set_page_config(page_title='Loan Default Risk Dashboard')

# Function to define color-coding for risk levels
def color_risk(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for high risk,
    'color: orange' for medium risk, and 'color: green' for low risk.
    """
    if val < 0.3:
        color = 'green'
    elif 0.3 <= val <= 0.6:
        color = 'orange'
    else:
        color = 'red'
    return f'color: {color}'

# Load the data from the CSV file
df = pd.read_csv('loan_default_risk_dashboard/borrower_data.csv')

# Add a title to the dashboard
st.title('Loan Default Risk Dashboard')

# Search and filter functionality by borrower name
name_search = st.text_input('Search by borrower name:')
if name_search:
    df = df[df['Borrower Name'].str.contains(name_search, case=False)]

# Display the data in a table with color-coded risk levels.
# The `st.dataframe` function provides sortable columns by default.
st.dataframe(df.style.applymap(color_risk, subset=['Predicted Default Probability']))
