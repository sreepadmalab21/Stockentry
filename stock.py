import streamlit as st
import datetime
import numpy as np
import pandas as pd
import os
from PIL import Image
img = Image.open('images/sreepadma logo.jpg")
#st.image(img,width=150)
col1, col2, col3 = st.columns([4,6,1])
with col1:
 st.write("")
with col2:
 st.image(img,width=150)
with col3:
 st.write("")
st.title("Sreepadma AquaFlora Stock Details")
col1,col2=st.columns(2)
with col1:
 date_input=st.date_input('Date')
type_list = ['PIR Production', 'Export','Initiation','Import','Contamination','Greenhouse','Discard']
crop_list=['RANACULUS', 'MOSS', 'STAUROGYNE','CRYPTOCORYNE','SYNGONIUM','HYGROPHYLLA','ANUBIAS','BUCEPHALANDRA','AGLONEMA','ALTERNENDRA','CREPIDOMANES FERN','GLOSSOSTIGMA','LAGNENDRA','LUDWIGIA REPENS','ELEOCHARIS','MICRANTHEMUM','ROTALA','ECHINODORUS','RICCARDIA']
with col2:
 type = st.multiselect("Type ", options=type_list)
 type = str(type)[2:-2]
col1,col2=st.columns(2)
with col1:
 #crop = st.selectbox('Crop',('RANACULUS', 'MOSS', 'STAUROGYNE','CRYPTOCORYNE'))
 crop = st.multiselect("Crop", options=crop_list)
 crop=str(crop)[2:-2]
with col2:
 #clone=st.selectbox('Clone',options=['SR1', 'RN1', 'CR1','CR21'])
 clone = st.multiselect("Clone", options=['SR1', 'RN1', 'CR1','CR21','CR121A','CR21','CR21A','CR103','CR103A','CR141','CR161','CR181','CR201','CR221','CR221A','CR241','CR261','CR241A','CR181A',
'CR21C','HP1','HP21','HP41','HP81','SR22','SGJ','AR1A','AG1', 'AG21','AGSRC','MC1','MS41','MS61','MS81','MS101','ASIE','AS1F','AS51F','AS51G','AS51I','AS51J','AS151A','AS151I','AS201A','AS201F','AS251D','AS251E','AS251F','AS251G','AS251H','AS251I','AS251K','AS401','AS401A',
'AS301','AS301E','AS301F','AS301I','AS301J','AS301K','AS301L','AS301M','AS301N','AS301O','AS351','AS351A','AS351C','BC61','BC1','BC21','BC41','CR121C','CR121D','CF1','AG21A','AG21C','GE1','AR1','CR22','CR22A','BC1 Z','BC41 Z', 'CR121','CR41','CR61','CR81','CR102','CR141A','BC81','BC101','CR261A','CM1','AS451','CR201A','CR201C','AS151J'])
 clone=str(clone)[2:-2]
col1,col2,col3,col4=st.columns(4)
with col1:
 used_LTD=st.multiselect("Used LTD", options=range(53))
 used_LTD=str(used_LTD)[1:-1]
 #used_LTD=st.selectbox("Used LTD",(range(53)))
with col2:
 used_stage = st.multiselect("Used stage",options= ("M", "M2", "S", "R", "INI","M3","MA","MN","MB"))
 used_stage=str(used_stage)[2:-2]
 #used_stage=st.selectbox("Used stage",("M","M2","S","R","INI"))
with col3:
 used_cultures=st.text_input("Used Cultures")
with col4:
 used_status=st.text_input("Used status")
col1,col2,col3,col4=st.columns(4)
with col1:
 produced_cultures=st.text_input("Produced cultures")
with col2:
 produced_stage=st.multiselect("Produced stage ",options= ("M","M2","S","R","INI","MA","MN","MB"))
 produced_stage = str(produced_stage)[2:-2]
with col3:
 operator=st.multiselect("Operator",options= ("NJK","SGS","ANJ","SKM","OMR","SST"))
 operator = str(operator)[2:-2]
with col4:
 produced_status=st.text_input("Produced status")

no_of_bottles=st.text_input("Number of bottles")

button1=st.button("Submit")


result_df= pd.DataFrame(data=[[date_input, type, crop, clone,used_LTD,used_stage,used_status,used_cultures,produced_cultures,produced_stage,produced_status,operator,no_of_bottles]],columns=["date", "type", "crop", "clone","Used LTD","Used Stage","Used status","used cultures","produced cultures","produced stage","produced status","operator","no of bottles"])
if button1:
 if os.path.isfile('stocksheet.xlsx'):
   df_fetch = pd.read_excel('stocksheet.xlsx')
   df_final = df_fetch.append(result_df)
   df_final.to_excel('stocksheet.xlsx', index=False)
 else:
   result_df.to_excel('stocksheet.xlsx')




