import pandas as pd
import streamlit as st
import random
from datetime import datetime
@st.cache
def load_data():
    df = pd.read_csv("data/rated_answers.csv")
    return df
df = load_data()

st.title('Bot Survey')

votes = pd.read_csv("data/votes.csv")
answer = '-'
if 'count' not in st.session_state:
    st.session_state.count = 0

if 'no' not in st.session_state:
    st.session_state.no = random.randrange(df.shape[0])

if 'ses' not in st.session_state:
    st.session_state.ses = random.randrange(1000000)    
    
st.write('Select the best answer to the question, taking into account relevancy and accuracy.')
st.write('Survey Answered : ', st.session_state.count)
no = st.session_state.no
print(st.session_state.no)
print(no)
st.header("Question: "+df.iloc[no]['Question'])
thing1 = ["-"]
thing2 = [df.iloc[no]['Answer_Model1'],df.iloc[no]['Answer_Model2'],df.iloc[no]['Answer_Model3']]
#SHUFFLING A SINGLE LIST DOESNT WORK, PLEASE EXCUSE MESS
ra = random.randint(1,2)
# if ra==1:
#     thing2 = [df.iloc[no]['Answer_Model1'],df.iloc[no]['Answer_Model2'],df.iloc[no]['Answer_Model3']]
# elif ra==2:
#     thing2 = [df.iloc[no]['Answer_Model1'],df.iloc[no]['Answer_Model3'],df.iloc[no]['Answer_Model2']]
# elif ra==3:
#     thing2 = [df.iloc[no]['Answer_Model2'],df.iloc[no]['Answer_Model1'],df.iloc[no]['Answer_Model3']]
# elif ra==4:
#     thing2 = [df.iloc[no]['Answer_Model2'],df.iloc[no]['Answer_Model3'],df.iloc[no]['Answer_Model1']]
# elif ra==5:
#     thing2 = [df.iloc[no]['Answer_Model3'],df.iloc[no]['Answer_Model1'],df.iloc[no]['Answer_Model2']]
# elif ra==6:
#     thing2 = [df.iloc[no]['Answer_Model3'],df.iloc[no]['Answer_Model2'],df.iloc[no]['Answer_Model1']]
thing3 = thing1+thing2
print(thing3)
answer = st.radio("Answer", thing3)
if (answer != '-'):
    ans=''
    print(answer)
    if (answer == df.iloc[no]['Answer_Model1']):
        ans = 'Model1'
        votes['Vote1'].iloc[no] = votes['Vote1'].iloc[no] + 1
    elif (answer == df.iloc[no]['Answer_Model2']):
        ans = 'Model2'
        votes['Vote2'].iloc[no] = votes['Vote2'].iloc[no] + 1
    elif (answer == df.iloc[no]['Answer_Model3']):
        ans = 'Model3'
        votes['Vote3'].iloc[no] = votes['Vote3'].iloc[no] + 1
    print("we got this far!")
    ts = pd.read_csv("data/timestamps.csv")
    current_time = datetime.now().strftime("%d/%m/%y %H:%M")
    new = {'Time':current_time, 'Count':st.session_state.count, 'Number':st.session_state.no, 'Session':st.session_state.ses}
    ts = ts.append(new,ignore_index=True)
    ts.to_csv("data/timestamps.csv", index=False)
    st.session_state.count += 1
    st.session_state.no = random.randrange(df.shape[0])
    votes.to_csv("data/votes.csv", index=False)
    st.button('Next')
    