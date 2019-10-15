import plotly as py
import pandas as pd

table = pd.read_csv('https://raw.githubusercontent.com/chumo/Data2Serve/master/transition_clusters.csv')

initial_traces = []

for my_color in ['red', 'green', 'blue']:
    initial_traces.append(dict(
        type='scatter', 
        x=table[table.color==my_color].Xi, 
        y=table[table.color==my_color].Yi, 
        mode='markers',
        marker=dict(color=my_color)
    ))

    
final_traces = []

for my_color in ['red', 'green', 'blue']:
    final_traces.append(dict(
        type='scatter', 
        x=table[table.color==my_color].Xf, 
        y=table[table.color==my_color].Yf, 
        mode='markers',
        marker=dict(color=my_color)
    ))

from plotly.subplots import make_subplots

fig = make_subplots(
    rows=1, 
    cols=2, 
    subplot_titles=('f(x) = sin(x)', 'f(x) = cos(x)'), 
    shared_yaxes=True,
)

[fig.append_trace(trace, 1, 1) for trace in initial_traces]
[fig.append_trace(trace, 1, 2) for trace in final_traces]

fig.show()