import functools
import re
import webbrowser

import pandas as pd


def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red'
    return 'color: % s' % color


def dmv_dom(df1, xxx, db_filename, li, p):
    template = """"
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <head>
    <p> <b> f </b> </p>
    <p> coun </p>
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

    x = df1.style.set_properties(**{'border': '1.3px solid green', 'color': 'black'}).highlight_null(color='yellow') \
        .hide_index().applymap(color_negative_red, subset=pd.IndexSlice[li, [p]])
    classes = 'table table-striped table-bordered table-hover table-sm'
    html = template % x.to_html(classes=classes)
    html = re.sub("<p> <b> f </b> </p>", f'<p> <b> Domain Constraints : {p} </b> </p>', html)
    html = re.sub("<p> coun </p>", f'<p> <b> Total Domain constraint Values: {xxx} </b> </p>', html)
    text_file = open(f"./view_error/{db_filename}_view_domain.html", "w", encoding="utf-8")
    text_file.write(html)
    text_file.close()
    pa = f"file:///C:/Users/Sethu/PycharmProjects/errorDetection_Metadata/view_error/{db_filename}_view_domain.html"
    webbrowser.open(pa, new=2)


