import atexit
import csv
import os
import subprocess
import sys
import timeit
import pandas as pd


from view_error.view_dmv import dmv_view


def dmv_profiler(db_filename, odf, ccc):
    starttime = timeit.default_timer()
    full_path = os.getcwd()
    c = os.system(f"C:/cygwin64/bin/bash --login -c 'cd C:/Users/Sethu/PycharmProjects/errorDetection_Metadata/profiler"
                  f"/FAHES_Code/src; " f" make; ./FAHES ../../../data/{db_filename}.csv ../../../metadata/ 4;'")
    try:
        os.close(c)
    except OSError:
        print('error')


    print("The time for DMV detection is :", timeit.default_timer() - starttime, '\n')
    pathfile = f'./metadata/DMV_{db_filename}.csv'
    df_dmv = pd.read_csv(pathfile, usecols=['DMV', 'Frequency'], low_memory=False)

    DMV = []
    Cout = []

    for c in df_dmv['DMV']:
        DMV.append(c)
    x = 0
    for c in df_dmv['Frequency']:
        x = x + c
        Cout.append(c)

    fl = ["./metadata/" + db_filename + "_error_log.csv", "./metadata/" + db_filename + "_combo_log.csv"]
    i = 0
    for f in fl:
        dffb = pd.read_csv(f)
        # df = df.loc[:, ~df.columns.isin([ccc])]
        li = []
        if i == 0:
            for c in odf.columns:
                li.clear()
                for cc in range(len(odf[c])):
                    if odf[c][cc] in DMV:
                        #print('val', odf[c][cc])
                        if dffb[c][cc] == 0:
                            #print('error', dffb[c][cc])
                            li.append(1)
                    else:
                        #print('nodmv', dffb[c][cc])
                        li.append(dffb[c][cc])
                dffb[c] = pd.Series(li)
                dffb.to_csv(f, index=False)
        else:
            for c in odf.columns:
                li.clear()
                for cc in range(len(odf[c])):
                    if odf[c][cc] in DMV:
                        #print('val', odf[c][cc])
                        if dffb[c][cc] == 0:
                            #print('error', dffb[c][cc])
                            li.append(2)
                        elif dffb[c][cc] == 1:
                            #print('error', dffb[c][cc])
                            li.append(12)
                    else:
                        #print('nodmv', dffb[c][cc])
                        li.append(dffb[c][cc])
                dffb[c] = pd.Series(li)
                dffb.to_csv(f, index=False)

        i += 1

    print('_________ DMVs Found--------', DMV, '\n')
    print('_____Each DMVs Found-------- ', Cout, '\n')
    print('_________ Total Count DMVs Found--------', x, '\n')

    return DMV, x


'''
errorpath = './data/diabetes_pk.csv'
df_err = pd.read_csv(errorpath)



datatype_path = '../metadata/diabetes_pk_datatype.csv'
df_data = pd.read_csv(datatype_path)
# metadata_log = './metadata/diabetes_pk_dmv.csv'
# df_meta = pd.read_csv(metadata_log)

col = []
val = []
freq = []

def convert1(a, b):
    if df_data[a][0] == 'integer':
        # print(int(b))
        return int(b)
    elif df_data[a][0] == 'decimal':
        # print(float(b))
        return float(b)
    elif df_data[a][0] == 'string':
        # print(str(b))
        return str(b)

for i in range(len(df_dmv)):
    col.append(df_dmv['Attribute Name'][i])
    val.append(convert1(df_dmv['Attribute Name'][i], df_dmv['DMV'][i]))
    freq.append(df_dmv['Frequency'][i])

error_list = []

for i in range(len(col)):
    error_list.clear()
    print('col', df_err[col])
    for ix in df_err[col]:

        if ix == val[i]:
            error_list.append('1')
        else:
            error_list.append('0')
    print(error_list)
'''
