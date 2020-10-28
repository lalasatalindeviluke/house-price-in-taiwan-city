import pandas as pd
import plotly.express as px
from plotly.offline import plot
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#整理資料
taipei = pd.read_csv("E:\\SummerWorkshop\\台北市.csv",
                     usecols=[1,3,9,13,14,15,16])
taipei = taipei.dropna()
taipei.insert(0, "城市", "台北市")
taichung = pd.read_csv("E:\\SummerWorkshop\\台中市.csv",
                       usecols=[1,3,9,13,14,15,16])
taichung.insert(0, "城市", "台中市")
kao = pd.read_csv("E:\\SummerWorkshop\\高雄市.csv",
                  usecols=[1,3,9,13,14,15,16])
kao.insert(0, "城市", "高雄市")
#合併三都資料
data = pd.concat([taipei, taichung], ignore_index=True)
data = pd.concat([data, kao], ignore_index=True)
data1 = data[data["屋齡"] <= 50]

mark_values = {x:"%d" %x for x in range(51)}

#----------------------------------------------------------------
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div([
        dcc.Graph(id='our_graph')
    ]),
    html.Div([
        html.Br(),
        dcc.Dropdown(id='city',
            options=[{'label':x, 'value':x} for x in data['城市'].unique()],
            value='台北市',
            multi=False,
            disabled=False,
            clearable=True,
            searchable=True,
            placeholder='Choose City...',
            className='form-dropdown',
            style={'width':"100%"},
            persistence='string',
            persistence_type='memory')
        ]),
    html.Div([
        html.Br(),
        dcc.Slider(
            id='house-age',
            min=0,
            max=50,
            step=1,
            marks=mark_values,
            value=0
            )
        ])
    ])

@app.callback(
    Output('our_graph','figure'),
    [Input('city','value'),
     Input('house-age', 'value')]
)
def update_figure(city_num, age):
    dataa = data[(data["城市"] == city_num) &
                 (data["屋齡"] == age)]
    #如果該城市沒有相應屋齡房屋，則會error
    
    fig = px.scatter(dataa, x="建物移轉總面積平方公尺", y="總價元",
                     title="房價-坪數總覽", color="鄉鎮市區")
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)

