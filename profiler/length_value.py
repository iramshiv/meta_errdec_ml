import csv
import timeit

import pandas as pd


def val_length(col, db_filename, dm):
    ff = f'./data/{db_filename}.csv'
    dty = f'./metadata/data_type_{db_filename}.csv'
    fv = pd.read_csv(dty)
    dataty = pd.read_csv(ff)

    n_e = 0

    length_file = f'./metadata/length_{db_filename}.csv'
    in_col = dataty.columns

    with open(length_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(in_col)

    dff = pd.read_csv(length_file)
    coo = dff.columns

    cou = dataty[col].tolist()
    # dd = coo[col]
    # print(dd)
    dff[col] = pd.Series(cou)
    dff.to_csv(length_file, index=False)

    d1 = dataty.loc[:, ~dataty.columns.isin([col])]
    column_n = d1.columns

    starttime = timeit.default_timer()

    for col in column_n:
        val_arr = []
        if fv[col].equals('integer') or fv[col].equals('decimal'):
            val_arr = []
        else:
            for val in d1[col]:
                if pd.isnull(val):
                    #n_e = n_e + 1
                    val_arr.append('')
                elif val in dm:
                    val_arr.append('')
                else:
                    val_arr.append(len(str(val)))

            dff[col] = pd.Series(val_arr)
            dff.to_csv(length_file, index=False)

    print("\n The time for length calculation is :", timeit.default_timer() - starttime, '\n')