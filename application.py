import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

application = app.server

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

html.Div(children='''
        This is Dash running on Elastic Beanstalk.
    '''),

dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ['left', 'center', 'right'], 'y': [3,7,6], 'type': 'bar', 'name': 'category 1'},
                {'x': ['left', 'center', 'right'], 'y': [4,2,5], 'type': 'bar', 'name': 'category 2'},
            ],
            'layout': {
                'title': 'Graph Title',
                'xaxis':{'title':'x-axis label'},
                'yaxis':{'title':'y-axis label'},
            }
        }
    )
])

if __name__ == '__main__':

    application.run(debug=True, port=8080)
