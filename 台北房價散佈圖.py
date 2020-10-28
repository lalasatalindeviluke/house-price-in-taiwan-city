import pandas as pd
import plotly.express as px
from plotly.offline import plot

taipei = pd.read_csv("D:\\暑期程式工作坊\\台北市.csv",
                     usecols=[1,3,9,13,14,15,16])
taipei = taipei.dropna()
taipei = taipei[taipei["屋齡"] <= 50]

fig = px.scatter(taipei, x="建物移轉總面積平方公尺", y="總價元",
                 title="房價-坪數總覽", color="鄉鎮市區",
                 animation_frame="屋齡")
fig.write_html("D:\\.spyder-py3\\python file\\台北房價散佈圖.html")
plot(fig)
