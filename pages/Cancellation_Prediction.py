import pandas as pd
import numpy as np
from xgboost.sklearn import XGBClassifier
import streamlit as st
import pickle
import os

# Page Configuration
st.set_page_config(
    page_title="Hotel Booking Cancellation Predictor",
    page_icon="🏨",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 20px;
    }
    .title {
        color: #1E3D59;
        text-align: center;
        padding: 20px;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        margin: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #f5f5f5;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
    <h1 class='title'>🏨 Hotel Booking Cancellation Predictor</h1>
    <p style='text-align: center;'>An ML-powered tool to predict booking cancellations</p>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📝 Guest Information")
    st.markdown("---")

def user_input_feature():
    # Grouping related inputs
    st.sidebar.subheader("🔄 Booking History")
    previous_cancellations = st.sidebar.number_input('Previous Cancellations', 
        min_value=0, max_value=26, value=0, step=1,
        help="Number of previous booking cancellations")
    booking_changes = st.sidebar.number_input('Booking Changes', 
        0, 21, 0, 1,
        help="Number of changes made to the booking")

    st.sidebar.subheader("🚗 Facilities")
    required_car_parking_spaces = st.sidebar.number_input('Required Parking Spaces', 
        0, 2, 0, 1,
        help="Number of car parking spaces required")
    total_of_special_requests = st.sidebar.number_input('Special Requests', 
        0, 5, 0, 1,
        help="Total number of special requests made by the guest")

    st.sidebar.subheader("📋 Booking Details")
    country = st.sidebar.selectbox('Country of Origin', 
        ('PRT', 'GBR', 'FRA', 'ESP', 'DEU', 'ITA', 'IRL', 'BEL', 'BRA', 'NLD', 'USA', 'CHE', 'Others'),
        help="Guest's country of origin")
    
    market_segment = st.sidebar.selectbox('Market Segment',
        ('Direct', 'Corporate', 'Online TA', 'Offline TA/TO', 'Groups', 'Complementary', 'Aviation'),
        help="Booking market segment")
    
    deposit_type = st.sidebar.selectbox('Deposit Type',
        ('No Deposit', 'Non Refund', 'Refundable'),
        help="Type of deposit made for the booking")
    
    customer_type = st.sidebar.selectbox('Customer Type',
        ('Transient', 'Contract', 'Transient-Party', 'Group'),
        help="Type of customer")
    
    reserved_room_type = st.sidebar.selectbox('Room Type',
        ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'P'),
        help="Type of room reserved")
    
    days_in_waiting_list = st.sidebar.selectbox('Waiting List Duration',
        ('0', '1 or more day(s)'),
        help="Days the booking was in the waiting list")

    # Create DataFrame
    data = {
        'previous_cancellations': [previous_cancellations],
        'country': [country],
        'market_segment': [market_segment],
        'booking_changes': [booking_changes],
        'required_car_parking_spaces': [required_car_parking_spaces],
        'total_of_special_requests': [total_of_special_requests],
        'deposit_type': [deposit_type],
        'customer_type': [customer_type],
        'reserved_room_type': [reserved_room_type],
        'days_in_waiting_list': [days_in_waiting_list]
    }
    return pd.DataFrame(data)

# Get user input
df_customer = user_input_feature()
df_customer.index = ['value']

# Load model
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, 'hotel_booking_prediction_model.sav')
    model_loaded = pickle.load(open(model_path, 'rb'))
    is_canceled = model_loaded.predict(df_customer)
except Exception as e:
    st.error(f"Error loading model: {str(e)}")

# Display results
col1, col2 = st.columns([4, 2])

# [Previous code remains the same until the display section]

# Display results with better spacing
st.markdown("<br>", unsafe_allow_html=True)

# Adjust column ratio (4:2) and add custom styling for the table
col1, col2 = st.columns([4, 2])

with col1:
    st.markdown("""
        <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-right: 20px;'>
            <h3 style='color: #2c3e50; margin-bottom: 15px;'>📊 Guest Details</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Convert DataFrame to a more readable format with better column names
    df_display = df_customer.transpose()
    df_display.columns = ['Guest Information']
    
    # Rename index for better readability
    index_mapping = {
        'previous_cancellations': 'Previous Cancellations',
        'country': 'Country of Origin',
        'market_segment': 'Market Segment',
        'booking_changes': 'Booking Changes',
        'required_car_parking_spaces': 'Required Parking Spaces',
        'total_of_special_requests': 'Special Requests',
        'deposit_type': 'Deposit Type',
        'customer_type': 'Customer Type',
        'reserved_room_type': 'Room Type',
        'days_in_waiting_list': 'Days in Waiting List'
    }
    df_display.index = df_display.index.map(lambda x: index_mapping.get(x, x))
    
    # Create a custom CSS style for the table
    custom_css = """
        <style>
        .custom-table {
            font-size: 1.1rem !important;
            width: 100% !important;
            margin-bottom: 20px;
        }
        .custom-table th {

            padding: 12px 15px !important;
            font-weight: bold !important;
            text-align: justify !important;
        }
        .custom-table td {
            padding: 12px 15px !important;
            text-align: justify !important;
        }
        .table-container {
            padding: 20px;

            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
    
    # Convert DataFrame to HTML with custom styling
    table_html = df_display.to_html(classes='custom-table', escape=False)
    st.markdown(f"""
        <div class="table-container">
            {table_html}
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px;'>
            <h3 style='color: #2c3e50; margin-bottom: 15px;'>🔮 Prediction Result</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if is_canceled == 1:
        st.markdown("""
            <div style='background-color: #fff3f3; padding: 30px; border-radius: 10px; border: 2px solid #ffcccb;'>
                <h3 style='color: #cc0000; margin:0; font-size: 24px;'>⚠️ High Risk of Cancellation</h3>
                <br>
                <p style='color: #cc0000; font-size: 18px;'>Our ML model predicts that this booking has a high probability of cancellation.</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style='background-color: #f0fff0; padding: 30px; border-radius: 10px; border: 2px solid #90EE90;'>
                <h3 style='color: #006400; margin:0; font-size: 24px;'>✅ Low Risk of Cancellation</h3>
                <br>
                <p style='color: #006400; font-size: 18px;'>Our ML model predicts that this booking is likely to be completed.</p>
            </div>
        """, unsafe_allow_html=True)

# Additional Information Section with better spacing
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-top: 20px;'>
        <h3 style='color: #2c3e50;'>ℹ️ About This Predictor</h3>
        <p style='color: #666666; font-size: 16px;'>
            This ML-powered tool uses advanced machine learning algorithms to predict the likelihood of a hotel booking cancellation 
            based on various guest and booking characteristics. It helps our hotel management team to:
        </p>
        <ul style='color: #666666; font-size: 16px;'>
            <li>Better manage inventory and room allocation</li>
            <li>Optimize overbooking strategies</li>
            <li>Improve revenue management and forecasting</li>
            <li>Make data-driven decisions for operations</li>
        </ul>
        <p style='color: #666666; font-size: 16px;'>
            The model is trained on historical booking data from our Portuguese hotels and is regularly updated to maintain accuracy.
        </p>
    </div>
""", unsafe_allow_html=True)