import dash
import plotly.express as px
import pandas as pd
import io
import requests
import calendar

# Data exploration
# -------------------------------------------------------

githubpath = 'https://raw.githubusercontent.com/Luizagurdeva/dashlesson/Delivery1'
githubpath = requests.get("https://raw.githubusercontent.com/Luizagurdeva/dashlesson/Delivery1").content

df = pd.read_excel(githubpath + "my_shop_data.xlsx"), 

print(df[:5])