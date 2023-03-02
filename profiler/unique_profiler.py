# Total Number of rows
import timeit

from csv_write import csv_writ_id


def number_rows(df):
    no_of_rows = len(df.index)
    # print(no_of_rows)
    return no_of_rows


index_column = {}


# Find Index column
def find_index_column(df, db_filename):
    index_columnn = ''
    n = number_rows(df)
    yx = []

    for c in df.columns:
        l = df[c].nunique()
        index_column.update({c: l})
    #print(index_column)

    val = [x for x, y in index_column.items() if int(y / n) == 1]
    if len(val) == 1:
        return val, df, db_filename
    elif len(val) > 1:
        for x1 in range(len(val)):
            yx.append(f' {x1} for {val[x1]}')
        print('One or more columns with 100% Uniqueness, Set index column to continue\n')
        try:
            xx = input(f"Please choose column as index: {yx}: ")
            y = [val[int(xx)]]
            return y, df, db_filename
        except:
            print('Error')
            xx = input(f"Please choose column as index: {yx}: ")
            y = [val[int(xx)]]

    else:
        print('No column with 100% Uniqueness found.... \n Generating id colummn, please wait...')
        col = 'id'
        fname = f"./data/{db_filename}_pk.csv"
        df = csv_writ_id(fname, df, col)
        return [col], df, f"{db_filename}_pk"

