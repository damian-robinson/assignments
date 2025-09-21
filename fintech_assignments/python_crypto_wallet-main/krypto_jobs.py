# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# From `crypto_wallet.py import the functions generate_account, get_balance, and send_transaction
from crypto_wallet import generate_account, get_balance, send_transaction

# Database of KryptoJobs2Go candidates including their name, digital address, rating and hourly cost per Ether.
candidate_database = {
    "Lane": [
        "Lane",
        "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0",
        "4.3",
        0.20,
        "Images/lane.jpeg",
    ],
    "Ash": [
        "Ash",
        "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396",
        "5.0",
        0.33,
        "Images/ash.jpeg",
    ],
    "Jo": [
        "Jo",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "4.7",
        0.19,
        "Images/jo.jpeg",
    ],
    "Kendall": [
        "Kendall",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "4.1",
        0.16,
        "Images/kendall.jpeg",
    ],
}

# A list of the KryptoJobs2Go candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]


def get_people():
    """Display the database of KryptoJobs2Go candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("KryptoJobs2Go Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

# Streamlit application headings
st.markdown("# KryptoJobs2Go!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
st.sidebar.write(get_balance(account.address))

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox("Select a Person", people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the KryptoJobs2Go candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the KryptoJobs2Go candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the KryptoJobs2Go candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the KryptoJobs2Go candidate's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")

# Calculate total `wage` for the candidate by multiplying the candidate’s hourly ate from the
# candidate database (`candidate_database[person][3]`) by the value of the `hours` variable
wage = candidate_database[person][3] * hours

# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(wage)

if st.sidebar.button("Send Transaction"):

    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    send_transaction(account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# Writes KryptoJobs2Go candidates to the Streamlit page
get_people()

# 3. On the resulting webpage, select a candidate that you would like to hire
# from the appropriate drop-down menu. Then, enter the number of hours that you
# would like to hire them for. (Remember, you do not have a lot of ether in
# your account, so you cannot hire them for long!)

# 4 Click the Send Transaction button to sign and send the transaction with
# your Ethereum account information. If the transaction is successfully
# communicated to Ganache, validated, and added to a block,
# a resulting transaction hash code will be written to the Streamlit
# application sidebar.

# 5. Navigate to the Ganache accounts tab and locate your account (index 0).
# * Take a screenshot of the address, balance, and transaction (TX) count.
# Save this screenshot to the README.md file of your GitHub repository for
#  this Challenge assignment.

# 6. Navigate to the Ganache transactions tab and locate the transaction.
# * Click the transaction and take a screenshot of it.
# Save this screenshot to the README.md file of your GitHub repository for
#  this Challenge assignment.
