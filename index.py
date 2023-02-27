import shutil
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
from profiler.length_value import val_length
from profiler.missing_value_profiler import missing_value
from profiler.top3 import top_values, top_pat_dat, top_pat
from profiler.unique_profiler import number_rows, find_index_column
from user_gen import user_meta

print("_______Welcome to Metadata based Error Detection___________", '\n')

# Input Database path
db_path = input("Enter database path: ").strip()
db_filename = Path(db_path).stem
print("-----Database Name: ------  ", db_filename, '\n')

# Copy to our path
db_newpath = f"./data/{db_filename}.csv"
shutil.copy(db_path, db_newpath)
print('Succesfully added database to the pipeline....', '\n')

# sample output
df = pd.read_csv(db_newpath, low_memory=False, delimiter=',')
print('----------- Sample Data-------------  ', '\n')
print(df.head(5))

# Number of row
no_of_rows = number_rows(df)
print('-------- Total No. of Rows : --------- ', no_of_rows, '\n')

# Index Column / PK / Uniquness Profiling
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

# Null - missing_value heuristics
# no_null_df = missing_value(df, ccc, dmv_path)

# DMV - disguised_missing_value heuristics
dmv, tot = dmv_profiler(dmv_path, df1)

# Pattern learner
# column_Pattern_Learner(df, df1, ccc, db_filename)

# DMV pattern
dmv_1 = dmv_pat(df1, index_col, db_filename)

all_dmv = [*dmv, *dmv_1]

# starttime = timeit.default_timer()
# top 10 values
# top_val = top_values(index_col, db_filename, all_dmv)

# top 10 patterns
# pat_val = top_pat(index_col, db_filename, all_dmv)

# top 10 data patterns
# dat_val = top_pat_dat(index_col, db_filename, all_dmv)
# print(" \n The time for pattern generation is :", timeit.default_timer() - starttime, '\n')

# Data Type Inference -----------------> Third metadata
# data_inference(db_filename, index_col)

# Domain check
# print('\n', df.columns)
# print('\n Please enter column from above to domain check: ')
# coll = input()
# pho = [line.strip() for line in open('./lookup/phone.txt')]
# domain_role(coll, db_filename, pho, df)

#Duplicates
#print('\nEnter column to check for duplicate:')
#for c in range(len(df.columns)):
    #print(f'    {c} for {df.columns[c]}')
#op = input()
#dup(db_filename, op)

#value_length
#val_length(ccc, db_filename, all_dmv)

print("Enter '1' for generating metadata, 2 to exit: ")
o = input()

if o == 1:
    user_meta(db_filename)
elif o == 2:
    print('Thank you!')
    exit()