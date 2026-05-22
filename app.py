import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df = sns.load_dataset('penguins')
st.title('Penguins Data Analysis')

st.write("### Available Columns in Dataset:")
st.write(list(df.columns))

fig, ax = plt.subplots()
sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species", ax=ax)
st.pyplot(fig)