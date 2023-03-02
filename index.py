import shutil
import sys
import time
import timeit
from pathlib import Path
import pandas as pd

from profiler.SparkClean.duplicate_profiler import dup
from profiler.column_PatternLearner import column_Pattern_Learner
from profiler.data_type_profiler import data_inference
from profiler.dmv_pat_prof import dmv_pat
from profiler.dmv_profiler import dmv_profiler
from profiler.domain import domain_role
from profiler.fuzz import fuzz
from profiler.hash_prof import calculate_hash_val
from profiler.length_value import val_length
from profiler.missing_value_profiler import missing_value
from profiler.top3 import top_values, top_pat_dat, top_pat, top_profiler
from profiler.unique_profiler import number_rows, find_index_column
# from user_gen import user_meta
from user_gen import user_meta, gen_meta
from view_error.view_dmv import dmv_view
from view_error.view_dup import dup_view
from view_error.view_null import null_view

print("_______Welcome to Metadata based Error Detection___________", '\n')

# Input Database path

file_path = input("Enter database path: ").strip()

if (file_path == ''):
    print('Please enter a database path: \n')
else:

    db_filename = Path(file_path).stem
    print("-----Database Name: ------  ", db_filename, '\n')

    # Copy to our path
    db_newpath = f"./data/{db_filename}.csv"
    shutil.copy(file_path, db_newpath)
    print('Succesfully added database to the pipeline....', '\n')

    # sample output
    df = pd.read_csv(db_newpath, low_memory=False, delimiter=',')
    print('----------- Sample Data-------------  ', '\n')
    print(df.head(5))

    # Number of row
    no_of_rows = number_rows(df)
    print('-------- Total No. of Rows : --------- ', no_of_rows, '\n')

    # 1. Index Column / PK / Uniquness Profiling
    starttime = timeit.default_timer()
    index_col, df, dmv_path = find_index_column(df, db_filename)
    db_filename = dmv_path
    print(" \n The time for unique column detection is :", timeit.default_timer() - starttime, '\n')
    df = df
    ccc = str(index_col[0])

    print('--------- Index column is: ---------- ', ccc, '\n')
    print('-------- New Sample Data with Unique column index is: -------------- \n')
    print(df.head(5), '\n')

    # DataFrame - with no index Column
    df1 = df.loc[:, ~df.columns.isin(index_col)]
    # print(df1.columns, '\n')

    xcv = int(input('Enter "1" to automatic metadata extraction, "2" for metadata generation customised heuristics'))
    if xcv == 1:

        # 2. Null - missing_value heuristics 'no_null_df can be used for FD/CFD/RFD as its datadframe dropped null values'
        no_null_df = missing_value(df, ccc, dmv_path)


        # Domain check
        xxxx = int(input('Enter "1" to check domain violations, else "0" to skip : '))
        if xxxx == 1:
            domain_role(db_filename, df)
        else:
            pass

        xxxx1 = int(input('Enter "1" to check duplicates, else "0" to skip : '))
        if xxxx1 == 1:
            # Duplicates with hash
            for c in df1.columns:
                print(c)
            cvv = input('Please enter the column name to find duplicates')
            l, hash_dup = calculate_hash_val(db_filename, cvv)

            # Fuzz
            print('\n Fuzz for duplicates is continuing for the same column')
            l_thresh = int(input('Please enter the lower threshold: (default is 90)') or '90')
            u_thresh = int(input('Please enter the upper threshold: (default is 95)') or '95')
            ll, fuzz_dup = fuzz(df, cvv, db_filename, l_thresh, u_thresh)

            total_dup = list(set(l) | set(ll))
            dup_view(df, len(total_dup), db_filename, total_dup)
        else:
            pass

        xxxx2 = int(input('Enter "1" to check duplicates with LSH, else "0" to skip : '))
        if xxxx2 == 1:
            #Duplicates
            for c in range(len(df.columns)):
                print(f'    {c} for {df.columns[c]}')
            op = int(input("\nEnter column number to check for duplicate"))
            dup(db_filename, op)
        else:
            pass

        # 3. DMV - disguised_missing_value heuristics
        dmv, tot = dmv_profiler(dmv_path, df1, ccc)

        # 4. Pattern learner
        column_Pattern_Learner(df, df1, ccc, db_filename)

        # 3.1 DMV pattern
        dmv_1 = dmv_pat(df1, index_col, db_filename)

        all_dmv = [*dmv, *dmv_1]
        print('-----------All DMVs Found-------- \n', all_dmv)

        # 7 top 10 values
        top_val = top_values(index_col, db_filename, all_dmv)

        # 7.1 top 10 patterns
        pat_val = top_pat(index_col, db_filename, all_dmv)

        # 7.2 top 10 data patterns
        dat_val = top_pat_dat(index_col, db_filename, all_dmv)
        print(" \n The time for top 10 pattern generation is :", timeit.default_timer() - starttime, '\n')

        # 5 Data Type Inference -----------------> Third metadata
        data_inference(db_filename, index_col)

        # 6 value_length
        val_length(ccc, db_filename, all_dmv)

        starttime = timeit.default_timer()


        # 8 Top pattern vs values profiler
        print('----- Top pattern versus values to check errors in top values \n')
        top_profiler(db_filename, index_col)

        print('Opening html pages to show all error found')
        null_view(df, df.isna().sum().sum(), db_filename)
        dmv_view(df, tot, db_filename, all_dmv)

    elif xcv == 2:
        #print('Generating value length distribution, please wait.....')
        #val_length(ccc, db_filename, all_dmv)
        gen_meta(db_filename)
    else:
        print('Thank you!')
        exit()