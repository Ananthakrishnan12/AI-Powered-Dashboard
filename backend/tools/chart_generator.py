import plotly.express as px

def create_bar_chart(df,x,y):
    fig=px.bar(df,x=x,y=y)
    return fig


def create_line_chart(df,,x,y):
    fig=px.line(df,x,y)
    return fig


def create_pie_chart(df,column):
    fig=px.pie(df,names=column)
    return fig