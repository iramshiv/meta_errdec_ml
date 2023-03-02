import csv
import timeit

import pandas as pd

decimal1 = set(['d', '.'])
integer1 = set(['d'])
string1 = set(['s'])
alpha1 = set(['d', 's', 'S', '.'])

datetime = [line.strip() for line in open('./lookup/trifacta_DataTimePattern.txt')]
datetime_1 = ['d/dd', 'dd/dd', 'dddd/dd/dd', 'dddd/d/dd', 'dd/dd/dd', 'dd/dd/d',
              'd/dd', 'dd/dd', 'dd:dd', 'd:dd', 'dd:dd:dd', 'd:dd:dd', 'd:d:dd', 'dd/sss/dddd']

list1 = []
dt = []


def data_inference(db_filename, index_col):
    df3 = pd.read_csv(f'./metadata/date_pattern_{db_filename}.csv')

    f = f'./metadata/data_pattern_{db_filename}.csv'
    f1 = f'./metadata/top_datapat_{db_filename}.csv'
    f2 = f'./metadata/data_type_{db_filename}.csv'
    f3 = f'./data/{db_filename}.csv'

    df_f3 = pd.read_csv(f3, low_memory=False)

    xx = (df_f3.infer_objects().dtypes != object)
    yy = [i for i, xx in enumerate(xx) if xx]
    column_names_1 = df_f3.columns[yy]
    co = []
    co.clear()
    for ccx in column_names_1:
        co.append(ccx)

    for c in co:
        if str(df_f3[c].infer_objects().dtypes) == 'int64':
            dt.append('integer')
            print(c + "----> integer")
        elif str(df_f3[c].infer_objects().dtypes) == 'float64':
            dt.append('decimal')
            print(c + "----> integer")
        elif str(df_f3[c].infer_objects().dtypes) == 'bool':
            dt.append('boolean')
            print(c + "----> bool")
        elif str(df_f3[c].infer_objects().dtypes) == 'datetime64':
            dt.append('DateTime')
            print(c + "----> DateTime")
        elif str(df_f3[c].infer_objects().dtypes) == 'string':
            dt.append('string')
            print(c + "----> String")

    starttime = timeit.default_timer()

    with open(f2, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(df_f3.columns)
        writer.writerows([dt])

    x = (df_f3.dtypes == object)
    y = [i for i, x in enumerate(x) if x]
    column_names = df_f3.columns[y]

    df_f1 = pd.read_csv(f1, low_memory=False)

    for c in column_names:

        u = prof(df_f1, c)
        #print(u)

        if set(u) == string1:
            print(c + "----> string")
            dt.append('string')
            # dft[c+'_datatype'] = 'string'
        elif set(u) == integer1:
            print(c + "----> integer")
            # dft[c+'_datatype'] = 'int64'
            # dt = 'int64'
            dt.append('integer')
        elif set(u) == decimal1:
            print(c + "----> decimal")
            # dft[c+'_datatype'] = 'decimal'
            # dt = 'decimal'
            dt.append('decimal')
        elif datetime_bool(unique_date_pattern(c, df3), datetime) == 'True':
            print(c + "----> DateTime")
            # print('unique_dat', unique_date_pattern(c, df3))
            # dft[c+'_datatype'] = 'DateTime'
            # dt = 'DateTime'
            dt.append('DateTime')
        elif intersection(set(unique_date_pattern(c, df3)), set(datetime)) > 0:
            print(c + '------>DateTime')
            # dft[c+'_datatype'] = 'DateTime'
            # dt = 'DateTime'
            dt.append('DateTime')
        elif intersection(set(split_date(c, df3)), set(datetime_1)) > 2:
            print(c + '------>DateTime')
            # dft[c+'_datatype'] = 'DateTime'
            # dt = 'DateTime'
            dt.append('DateTime')
        elif any(cs.isalnum() for cs in c):
            print(c + '----------> AlphaNum')
            # dft[c+'_datatype'] = 'AlphaNum'
            # dt = 'AlphaNum'
            dt.append('AlphaNum')
        else:
            print(c + '--------> DataTypeViolation')
            # dft[c+'_datatype'] = 'DataTypeViolation'
            # dt = 'DataTypeViolation'
            dt.append('DataTypeViolation')

    print("\n The time for Data Inference is :", timeit.default_timer() - starttime)

    with open(f2, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(df_f3.columns)
        writer.writerows([dt])


def prof(dd, col):
    list1.clear()

    for x in dd[col]:
        if pd.isnull(x) or pd.isna(x):
            pass
        elif x == 'S':
            pass
        else:
            for xc in str(x):
                if xc not in list1:
                    list1.append(xc)
    return list1


def datetime_bool(list11, list2):
    result = any(item in list11 for item in list2)
    # print(result)
    return str(bool(result))


un_list2 = []


# Find unique values
def unique_date_pattern(list2, df3):
    un_list2.clear()
    # print(df3[list2].dropna())
    for x in df3[list2].dropna():
        if x not in un_list2:
            un_list2.append(x.replace('-', '/'))
    # print('Date', un_list2)
    return un_list2


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return len(lst3)


un_list_2 = []


def split_date(list2, df3):
    un_list_2.clear()
    # print(df3[list2].dropna())
    for x in df3[list2].dropna():
        if x not in un_list_2:
            x = x.replace('-', '/')
            x = x.split()
            for xx in x:
                # x = set(xx)
                # print('x2', xx)
                # x = x & x
                # print('x3', xx)
                un_list_2.append(xx)
    # print('split', un_list_2)
    return un_list_2
