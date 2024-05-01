import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt


data = pd.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Month"]= data["Timestamp"].dt.strftime("%Y-%m")
month_average_course=data.groupby(["Month", "Course Name"]).mean().unstack()


def app():
    wp = jp.QuasarPage()
    wp.title = 'Course Reviews Analysis'
    main_div = jp.Div(classes="q-pa-md")
    wp.add(main_div)

    jp.QDiv(a=main_div, text="Analysis of Course Reviews", classes="text-h4 text-center q-mb-md")
    jp.QDiv(a=main_div, text="These graphs represent the course analysis", classes="text-h6 text-center q-mb-md")




    chart_options = {
        "title": {"text": f"Average Ratings Over Time"},
        "xAxis": {"categories": [str(month) for month in month_average_course.index]},
        "yAxis": {"title": {"text": "Average Rating"}},
        "plotOptions": {
            "areaspline": {"fillOpacity": 0.5}
        },
        "series": [{
            "name": v1,
            "data": [v2 for v2 in month_average_course[v1]]
        } for v1 in month_average_course.columns],
        "responsive": {
            "rules": [{
                "condition": {"maxWidth": 500},
                "chartOptions": {
                    "legend": {"layout": "horizontal", "align": "center", "verticalAlign": "bottom"}
                }
            }]
        }
    }

    jp.HighCharts(a=main_div, options=chart_options, classes="q-ma-md")

    return wp

jp.justpy(app)
