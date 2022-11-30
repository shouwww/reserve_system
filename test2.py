import streamlit as st
import time
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
 
# データフレームを作成
df = pd.DataFrame([
  ["0001", "John", "Engineer"],
  ["0002", "Lily", "Sales"]],
  columns=['id', 'name', 'job'])
 
df.to_csv("test.csv")

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)
# data
data = px.data.iris()

for i in range(1, 5):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

'''
template = st.sidebar.selectbox("Template", list(pio.templates.keys()))
# body
st.write(px.scatter(data, x="sepal_width", y="sepal_length", template=template))
'''
def rand_df(r=10, c=5):
    df = pd.DataFrame(
        np.random.randn(r, c),
        columns=('col %d' % i for i in range(c)))
    return df
dataframe = rand_df(c=10, r=8)
dataframe.to_csv('test2.csv')
st.dataframe(dataframe)

df = pd.read_csv('test2.csv', index_col= 0)
choose_title = st.multiselect('title', df.columns.values)
st.write(type(choose_title))
st.write(choose_title)
st.write(px.line(x=["a","b","c"], y=[1,3,2], title="sample figure"))
# plot_line = px.line(data_frame=df, x=df.index, y=df['Close'], title="Close")
# https://data-analytics.fun/2021/06/11/plotly-line-chart/
plot_line = px.line(data_frame=df, x=df.index, y=choose_title, title="test")
st.write(plot_line)
data = []
for col in df.columns:
  if col in choose_title:
    data.append(go.Scatter(x=df.index,
              y=df[col],
              name=col))
#for col in df.columns:
  #if col != 'Date':
  #  data.append(go.Scatter(x=df['Date'],y=df[col],name=col))
go_fig = go.Figure(data)
st.write(go_fig)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")