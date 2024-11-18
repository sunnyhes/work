import streamlit as st
import pandas as pd

if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]
with st.sidebar:
    st.caption(f'{ID}님 접속중')
data = pd.read_csv("서울주차장.csv")

st.title('우리 차 어디 주차하지?')


#data = data.copy().fillna(0)
data.loc[:,'size'] = 1.5*(data['주차구획수'])
data


color = {'노외':'#f2aeea',
         '노상':'#4b62c9'}
data.loc[:,'color'] = data.copy().loc[:,'주차장유형'].map(color)


st.map(data, latitude="위도",
       longitude="경도",
       size="size",
       color="color",
       zoom=10)
