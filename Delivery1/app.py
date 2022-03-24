import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 

import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

import numpy as np
import calendar

import structured_data
order = structured_data.get_data()
df_year = structured_data.get_year()
df_month = structured_data.get_month()