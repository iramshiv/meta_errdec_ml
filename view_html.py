import webbrowser

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
from IPython.display import HTML, display_html

db_newpath = f"./data/diabetes_pk.csv"

df = pd.read_csv(db_newpath, low_memory=False, delimiter=',')


def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red'
    return 'color: % s' % color

template = """"
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<head>
<p> <b> NULL VALUES </b> </p>
</head>
<style>
th {
    background: #2d2d71;
    color: white;
    text-align: left;
}
</style>
<body>
%s
</body>
"""
f = [1,2,3]
def view(df):
    df = df['Age'].to_frame()
    x = df.style.set_properties(**{'border': '1.3px solid green',
                          'color': 'black'}).highlight_null(color='red').hide_index().applymap(color_negative_red, subset=pd.IndexSlice[f, ['Age']])

    classes = 'table table-striped table-bordered table-hover table-sm'
    html = template % x.to_html(classes=classes)
    text_file = open("i.html", "w")
    text_file.write(html)
    text_file.close()
    webbrowser.open('i.html', new=3)

view(df)

