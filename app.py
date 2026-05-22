import streamlit as st
import seaborn as sns
 
st.title("My First Streamlit App")
st.write("Hello, welcome to my app!")
 
df= sns.load_dataset("tips")
 
a = sns.relplot(x="total_bill", y="tip", data=df)
 
st.pyplot(a)