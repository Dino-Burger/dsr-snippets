# Plotly Express is now a sublibrary of Plotly:
import plotly.express as px

import pandas as pd

gapminder = px.data.gapminder()


# plot number 1: classical gapminder plot
fig_1 = px.scatter(
    gapminder, 
    x='gdpPercap', 
    y='lifeExp', 
    color='continent', 
    size='pop', 
    size_max=80, 
    log_x=True, 
    hover_name='country', 
    animation_frame='year',
    )

fig_1.write_html(
    file='classical_gapminder.html', 
    include_plotlyjs='cdn',
    config=dict(displaylogo=False),
)

# plot number 2: gdp ranking
gapminder_fig_2 = gapminder.groupby('year').apply(
    lambda x: x.sort_values(
        ["gdpPercap"], 
        ascending = False,
    ).head(10)
).reset_index(drop=True)

fig_2 = px.bar(
    gapminder_fig_2, 
    x='gdpPercap', 
    y='country', 
    animation_frame='year', 
    orientation='h', 
    range_x=[0,100000], 
    animation_group='country', 
    color='gdpPercap', 
    color_continuous_scale=px.colors.sequential.Magma,
)
fig_2.update_yaxes({'automargin':False})

fig_2.write_html(
    file='gdp_ranking.html', 
    include_plotlyjs='cdn',
    config=dict(displaylogo=False),
)
