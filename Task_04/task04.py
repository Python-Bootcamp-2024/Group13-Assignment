import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Load data
wine_df = pd.read_csv('Win_df.csv')

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = html.Div([
    html.H1("Wine Insights Dashboard", style={'textAlign': 'center'}),
    dcc.Tabs([
        dcc.Tab(label='Country Analysis', children=[
            dcc.Graph(id='country-bar-chart'),
            html.Label("Select a Metric"),
            dcc.Dropdown(
                id='metric-dropdown',
                options=[
                    {'label': 'Average Rating', 'value': 'Rating'},
                    {'label': 'Average Price', 'value': 'Price'}
                ],
                value='Rating'
            )
        ]),
        dcc.Tab(label='Wine Style Analysis', children=[
            dcc.Graph(id='wine-style-pie-chart'),
        ]),
        dcc.Tab(label='Alcohol vs Price', children=[
            dcc.Graph(id='alcohol-price-scatter'),
        ]),
        dcc.Tab(label='Interactive Data Filter', children=[
            html.Label("Filter by Country"),
            dcc.Dropdown(
                id='country-filter',
                options=[{'label': country, 'value': country} for country in wine_df['Country'].unique()],
                value=wine_df['Country'].unique()[0]
            ),
            dcc.Graph(id='filtered-bar-chart')
        ])
    ])
])

# Callbacks
@app.callback(
    Output('country-bar-chart', 'figure'),
    Input('metric-dropdown', 'value')
)
def update_country_bar_chart(metric):
    fig = px.bar(
        wine_df.groupby('Country')[metric].mean().reset_index(),
        x='Country', y=metric,
        title=f"Average {metric} by Country"
    )
    return fig



@app.callback(
    Output('wine-style-pie-chart', 'figure'),
    Input('country-filter', 'value')
)
def update_wine_style_pie_chart(country):
    filtered_data = wine_df[wine_df['Country'] == country]
    fig = px.pie(
        filtered_data, names='Wine style',
        title=f"Wine Styles in {country}"
    )
    return fig



@app.callback(
    Output('alcohol-price-scatter', 'figure'),
    Input('country-filter', 'value')
)
def update_alcohol_price_scatter(country):
    filtered_data = wine_df[wine_df['Country'] == country]
    fig = px.scatter(
        filtered_data, x='Alcohol content', y='Price',
        color='Country', size='Rating',
        title="Alcohol Content vs Price"
    )
    return fig



@app.callback(
    Output('filtered-bar-chart', 'figure'),
    Input('country-filter', 'value')
)
def update_filtered_bar_chart(country):
    filtered_data = wine_df[wine_df['Country'] == country]
    fig = px.bar(
        filtered_data, x='Wine style', y='Rating',
        title=f"Ratings of Wine Styles in {country}"
    )
    return fig

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
