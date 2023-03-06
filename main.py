import shutil
import timeit
from pathlib import Path
import pandas as pd

from profiler.column_PatternLearner import column_Pattern_Learner
from profiler.data_type_profiler import data_inference
from profiler.dmv_pat_prof import dmv_pat
from profiler.dmv_profiler import dmv_profiler
from profiler.length_value import val_length
from profiler.missing_value_profiler import missing_value
from profiler.top3 import top_values, top_pat, top_pat_dat, top_profiler
from profiler.unique_profiler import number_rows, find_index_column


# uploading the db path
def uploader(file_path):
    db_filename = Path(file_path).stem


    # Copy to our path
    db_newpath = f"./data/{db_filename}.csv"
    shutil.copy(file_path, db_newpath)
    print('Succesfully added database to the pipeline....', '\n')

    # sample output
    df = pd.read_csv(db_newpath, low_memory=False, delimiter=',')
    print("-----Database Name: ------  ", db_filename, '\n')
    print('----------- Sample Data-------------  ', '\n')
    print(df.head(5))

    return db_newpath, df


# unqiue column profiling connection
def index_pro(df, db_filename):
    # Number of row
    no_of_rows = number_rows(df)
    print('-------- Total No. of Rows : --------- ', no_of_rows, '\n')

    # 1. Index Column / PK / Uniquness Profiling
    starttime = timeit.default_timer()
    index_col, df, dmv_path = find_index_column(df, db_filename)
    print(" \n The time for unique column detection is :", timeit.default_timer() - starttime, '\n')

    df = df
    ccc = str(index_col[0])

    print('--------- Index column is: ---------- ', ccc, '\n')
    print('-------- New Sample Data with Unique column index is: -------------- \n')
    print(df.head(5), '\n')

    # DataFrame - with no index Column
    df1 = df.loc[:, ~df.columns.isin(index_col)]
    # print(df1.columns, '\n')

    return index_col, df, dmv_path, df1


def mandatory_meta_pro(df, dmv_path, df1, db_filename, index_col):
    ccc = str(index_col[0])
    # missing value profiler
    no_null_df = missing_value(df, ccc, dmv_path)

    # DMV - disguised_missing_value - FAHES
    dmv, tot = dmv_profiler(dmv_path, df1, ccc)

    # Pattern learner
    column_Pattern_Learner(df, df1, ccc, db_filename)

    # DMV pattern
    dmv_1 = dmv_pat(df1, index_col, db_filename)
    all_dmv = [*dmv, *dmv_1]
    print('-----------All DMVs Found-------- \n', all_dmv)

    starttime = timeit.default_timer()
    # top values
    top_val = top_values(index_col, db_filename, all_dmv)

    # top patterns
    pat_val = top_pat(index_col, db_filename, all_dmv)

    # top data patterns
    dat_val = top_pat_dat(index_col, db_filename, all_dmv)

    print(" \n The time for top 10 pattern generation is :", timeit.default_timer() - starttime, '\n')

    # Data Type Inference
    data_inference(db_filename, index_col)

    # value_length
    val_length(ccc, db_filename, all_dmv)

    starttime = timeit.default_timer()

    # Top pattern vs values profiler
    print('----- Top pattern versus values to check errors in top values \n')
    top_profiler(db_filename, index_col)

