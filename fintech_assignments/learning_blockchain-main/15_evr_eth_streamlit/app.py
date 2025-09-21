# Streamlit Application

# Imports
import streamlit as st

# Import the functions from ethereum.py
from ethereum import generate_account
from web3 import Web3

# Update httpprovider with RPC URL
#
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Instantiate generate_account(w3) as account
account = generate_account(w3)


################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Automating Ethereum with Streamlit!")
st.text("\n")
st.markdown("## Ethereum Account Address:")

# Write the Ethereum account address to the Streamlit page
st.write(account.address)
