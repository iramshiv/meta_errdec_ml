import shutil
import sys
import time
import timeit
from pathlib import Path
import pandas as pd

from main import uploader, index_pro, mandatory_meta_pro
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

uploaded = False


# check db path not null
def start(file_path1):
    while file_path1 == '':
        file_path1 = input("Please enter a database path: ").strip()
    return file_path1


# domain initiating function
def domain_start(db_filename, df):
    domain = False
    while not domain:

        try:
            xcv = int(input('Enter "1" to for domain_violations, "0" to skip'))
            if xcv == 1:
                # domain_violations
                domain_role(db_filename, df)
                domain = True
            elif xcv == 0:
                domain = True
                pass
        except ValueError:
            pass


# duplicate initiating function
def dup_start(df1, db_filename, df):
    dup1 = False

    while not dup1:
        try:
            xxxx1 = int(input('Enter "1" to check duplicates, else "0" to skip : '))
            if xxxx1 == 1:
                # Duplicates with hash
                for c in df1.columns:
                    print(c)
                cvv = input('Please enter the column NAME to find duplicates')
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
                # Duplicates with sparkclean, LSH
                for c in range(len(df.columns)):
                    print(f'    {c} for {df.columns[c]}')
                op = int(input("\nEnter column NUMBER to check for duplicate"))
                dup(db_filename, op)
            else:
                pass
            dup1 = True
        except:
            pass


# generator initiating
def gen_init(db_filename):
    gen = False
    while not gen:
        try:
            xcv = int(input("Please enter '1' for Metadata Generation, '0' to skip"))
            if xcv == 1:
                gen_meta(db_filename)
                gen = True
            elif xcv == 0:
                gen = True
                print('------- Thank you ---------')

        except ValueError:
            pass


# initial function --> Enter Profiling
def start2(file_path1):
    if file_path1 != '':
        # upload db to our space
        db_filename, df = uploader(file_path1)
        db_filename = Path(file_path).stem
        # profile for index column
        index_col, df, dmv_path, df1 = index_pro(df, db_filename)
        db_filename = dmv_path
        # Mandatory metadata profiling
        mandatory_meta_pro(df, dmv_path, df1, db_filename, index_col)

        # optional metadata profiling
        # domain violation
        domain_start(db_filename, df)

        # duplicates
        dup_start(df1, db_filename, df)

        gen_init(db_filename)

        uploaded = True


# loop until correct db path
while not uploaded:
    file_path = input("Error! Please enter a database path: ").strip()
    file_path = start(file_path)

    try:
        start2(file_path)
        uploaded = True
    except:
        pass
