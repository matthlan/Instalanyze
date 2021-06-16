import streamlit as st
import numpy as np
import pandas as pd

import json

import plotly.express as px

import emojis
"""
# Insta DM Analyser
Analyze your instagram conversations easily to learn about you and your friends
"""

def show_data(data):
    #create users list
    users = [u["name"].encode('latin-1').decode('utf-8') for u in data["participants"]]


    #data_frame containing messages
    df = pd.DataFrame(data["messages"])

    #decode unicdode special characters
    df["sender_name"] = df["sender_name"].apply(lambda x: x.encode('latin-1').decode('utf-8'))
    df["content"] = df["content"].apply(lambda x: str(x).encode('latin-1').decode('utf-8'))


    df["date"] = pd.to_datetime(df["timestamp_ms"], unit='ms')
    df["total_message"] = 1

    st.markdown('## {} and {} conversation :'.format(*users))

    

 

    

    """
    ### Messages sended by day by user
    """
    for user in users:
        df.loc[df['sender_name'] == user, user] = 1  

    d2 = df.resample('D', on='date').sum()
    st.plotly_chart(px.line(d2[[*users, "total_message"]]))


    """
    ### Proportion of messages sent by users
    """
    d3 = df.groupby(pd.Grouper(key="sender_name")).sum()
    fig = px.pie(d3,values='total_message', names=d3.index)
    st.plotly_chart(fig)

    """
    ### Most used emoji
    """
    d4 = df[(df["content"] != "nan") & (df["content"] != "Liked a message")]
    all_text = ' '.join(d4['content']).lower()
    all_emoji = ' '.join(list(emojis.iter(all_text)))
    most_used_emoji = pd.Series(all_emoji.split()).value_counts()[:10][::-1]
    print(most_used_emoji)
    fig = px.bar(most_used_emoji, orientation='h')
    fig.update_layout(xaxis_title="Emoji", yaxis_title="Uses")
    st.plotly_chart(fig)
   



file = st.file_uploader('Upload your JSON file')


if st.button('Analyze'):
    text = file.read()
    #data = json.load(file)
    data = json.loads(text)
    show_data(data)

