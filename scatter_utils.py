import pandas as pd
import plotly.express as px

def generate_scatter(df, x_col, y_col, color_col=None, size_col=None):
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        color=color_col,
        size=size_col,
        hover_data=df.columns,
        template='plotly_white'
    )
    fig.update_layout(width=800, height=600)
    return fig
