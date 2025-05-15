
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px

# Sample user credentials
USER_CREDENTIALS = {
    'johndoe': {'password': '1234', 'name': 'John Doe'},
    'janedoe': {'password': '5678', 'name': 'Jane Doe'}
}

def authenticate(username, password):
    user = USER_CREDENTIALS.get(username)
    return user and user["password"] == password

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login UI
if not st.session_state.logged_in:
    st.set_page_config(page_title="Login | Easy Money", layout="centered")
    st.title("🔐 Easy Money Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            if authenticate(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.name = USER_CREDENTIALS[username]["name"]
                st.success(f"✅ Welcome, {st.session_state.name}!")
            else:
                st.error("❌ Invalid username or password")
    st.stop()

# Render dashboard when logged in
st.set_page_config(page_title="Easy Money Dashboard", layout="wide")

# Sidebar
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Dashboard", "Portfolio", "Reports", "Settings"],
        icons=["speedometer", "briefcase", "bar-chart", "gear"],
        menu_icon="cash-coin",
        default_index=0,
        orientation="vertical"
    )
    st.markdown("---")
    st.write("**Logged in as:**")
    st.write(st.session_state.name)

# Header
st.markdown("# 💰 Easy Money Dashboard")
st.markdown(f"Welcome, {st.session_state.name}! Here's your personalized financial overview.")

# Metric Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Investment", "$25,000", "+5%")
col2.metric("Total Returns", "$1,250", "+7.1%")
col3.metric("Active Plans", "3")
col4.metric("Last Updated", "2025-05-15")

st.markdown("---")

# Charts
col5, col6 = st.columns(2)

# Sample chart data
data = pd.DataFrame({
    'Date': pd.date_range(start='2025-01-01', periods=10, freq='M'),
    'Value': [25000, 26000, 27000, 26800, 27500, 28500, 29000, 29500, 30000, 31000]
})
fig = px.line(data, x='Date', y='Value', title='📈 Portfolio Growth Over Time')
col5.plotly_chart(fig, use_container_width=True)

sector_data = pd.DataFrame({
    'Sector': ['Technology', 'Healthcare', 'Finance', 'Energy'],
    'Allocation': [40, 25, 20, 15]
})
fig2 = px.pie(sector_data, names='Sector', values='Allocation', title='📊 Sector Allocation')
col6.plotly_chart(fig2, use_container_width=True)

# Table
st.markdown("## Recent Transactions")
tx_data = pd.DataFrame({
    'Date': pd.date_range(start='2025-04-01', periods=5),
    'Type': ['Buy', 'Sell', 'Buy', 'Buy', 'Dividend'],
    'Amount': [5000, 2500, 3000, 2000, 150],
    'Asset': ['Mutual Fund A', 'Stock B', 'ETF C', 'Bond D', 'Stock B']
})
st.dataframe(tx_data, use_container_width=True)

# Footer
st.markdown("---")
st.caption("🧠 Easy Money Client Dashboard | Powered by Streamlit")
