import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt


data = pd.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Month"]= data["Timestamp"].dt.strftime("%Y-%m")
monthly_average=data.groupby(["Month"]).mean()

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent the course analysis", classes="text-p1 text-center q-pa-md")

    hc = jp.HighCharts(a=wp, options={
        "title": {"text": "Course Ratings Over Time"},
        "xAxis": {"categories": [str(day) for day in monthly_average.index]},
        "yAxis": {"title": {"text": "Average Rating"}},
        "series": [{
            "name": "Average Rating",
            "data": list(monthly_average["Rating"])  # Assuming "Rating" is the column containing ratings
        }],
        "responsive": {
            "rules": [{
                "condition": {"maxWidth": 500},
                "chartOptions": {
                    "legend": {"layout": "horizontal", "align": "center", "verticalAlign": "bottom"}
                }
            }]
        }
    })

    return wp

jp.justpy(app)
