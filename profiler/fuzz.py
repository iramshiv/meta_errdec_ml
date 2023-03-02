import timeit

from thefuzz import process, fuzz, StringMatcher
import difflib

import pandas as pd
import seaborn as sns

from view_error.view_dup import dup_view


def fuzz(df, col, db_filename, l_thresh, u_thresh):


    #https://www.activestate.com/blog/how-to-implement-fuzzy-matching-in-python/


    list_1 = []
    list2 = []
    i = 0
    for c in df[col].unique():
        list_1.append(c)
    starttime = timeit.default_timer()
    #print(df[column_names[1]].unique())
    for l in df[col].unique():
        #print('Word---:   ',l)
        score = process.extract(l, df[col], limit=4)
        #print(len(score))
        for l1 in range(len(score)):
            #print(int(score[l1][1])>= 90)
            if 90 <= int(score[l1][1]) <= 95:
                #print(score[l1])
                list2.append(score[l1][0])
                i+=1
    #print(list2)
    print('_________ Duplicates Found--------', i, '\n')
    print("\n The time for duplicates detection is :", timeit.default_timer() - starttime, '\n')
    return list2, i
