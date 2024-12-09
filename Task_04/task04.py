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

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
