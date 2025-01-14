import streamlit as st

# Set page title and favicon
st.set_page_config(page_title='Hotel Booking Cancellation Predictor', page_icon=':hotel:')

# Add CSS styles
st.markdown(
    """
    <style>
    body {
        background-color: #F0F0F0;
    }
    .header {
        font-size: 40px;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
        margin-bottom: 30px;
    }
    .subheader {
        font-size: 24px;
        font-weight: bold;
        color: #FF5733;
        margin-bottom: 10px;
    }
    .content {
        font-size: 18px;
        margin-bottom: 20px;
    }
    .cta-button {
        display: inline-block;
        padding: 10px 20px;
        background-color: #FF5733;
        color: #FFFFFF;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .cta-button:hover {
        background-color: #E64A19;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Header
st.markdown('<div class="header">Welcome to the Hotel Booking Cancellation Predictor</div>', unsafe_allow_html=True)

# Introduction
st.markdown('<div class="subheader">Introduction</div>', unsafe_allow_html=True)
st.markdown(
    '''
    <div class="content">
    The Hotel Booking Cancellation Predictor is a machine learning-based tool that helps predict whether a hotel guest is likely to cancel their reservation. By leveraging historical booking data and guest information, our predictor provides valuable insights to hotel management, enabling them to optimize their operations and improve guest satisfaction.
    </div>
    ''',
    unsafe_allow_html=True
)

# Features
st.markdown('<div class="subheader">Features</div>', unsafe_allow_html=True)
st.markdown(
    '''
    <div class="content">
    - Accurate cancellation predictions based on guest information and booking details<br>
    - User-friendly interface for inputting guest features<br>
    - Real-time predictions to assist in decision-making<br>
    - Helps optimize hotel revenue management and resource allocation
    </div>
    ''',
    unsafe_allow_html=True
)

# Call-to-Action
st.markdown(
    '''
    <div class="content">
    Ready to try out the Hotel Booking Cancellation Predictor? Click the button below to get started!
    </div>
    ''',
    unsafe_allow_html=True
)
st.markdown('<a href="/Cancellation_Prediction" target="_self" class="cta-button">Get Started</a>', unsafe_allow_html=True)

# About Us
st.markdown('<div class="subheader">About Us</div>', unsafe_allow_html=True)
st.markdown(
    '''
    <div class="content">
    We are a team of data scientists and hotel industry experts dedicated to developing innovative solutions to optimize hotel operations. Our goal is to provide hotels with powerful tools and insights to enhance their guest experience and improve their bottom line.
    </div>
    ''',
    unsafe_allow_html=True
)

# Contact Information
st.markdown('<div class="subheader">Contact Us</div>', unsafe_allow_html=True)
st.markdown(
    '''
    <div class="content">
    If you have any questions, feedback, or inquiries, please feel free to reach out to us:<br>
    Email: info@hotelbookingpredictor.com<br>
    Phone: +1 (123) 456-7890
    </div>
    ''',
    unsafe_allow_html=True
)