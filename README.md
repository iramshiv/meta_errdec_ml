# Introduction

### A Metadata-first approach for error detection ML based pipeline

Real world datasets suffers from various errors. According to Quartz guide to bad data [1], the real-world datasets contain exhaustive references to the errors. The most common real-world errors are, 

1. *Missing Values*: where the values are blank or ‘null’ value.
2. *Disguised Missing Values (DMVs)*: these are worse than missing values as these are arbitrary values to fill the missing values. These can happen due to automated process to handle null values or entered by humans. Usually ‘0’ used for null values, ‘999-999-9999’ used for phone numbers, ‘-’, ‘?’ used for unknown values.
3. *Duplicates*: where the values are redundantly appears more than once due to extra information are mostly entered by human for example in address ‘Restaurant katsu, 7th street, 1st avenue’ can be entered again as ‘Restaurant katsu, 7th St., 1st Avn.’
4. *Misspellings*: which are the most common errors when entered by humans, for example ‘John’ as ‘Jhon’, which also leads to duplicates.
5. *Inconsistent Data*: date formats are inconsistent, for example ‘01/08/90’ and ’09-01-90’, where the month and date are not clear. Also, there is data inconsistency. domain violation, when the date is entered as ‘01/08/90’ and ’01;08;90’ where both are similar date but with different representation.
6. *Domain violations*: where the US phone number formats are stored as, ‘984.565;5476’ instead of ‘984-565-5476’ the valid format.
7. *Garbled Text*: these are the values and the problems arises due to encoding problem which further leads to ‘mojibake’ [50] phenomenon, where the data looks like garbage or ‘���’.

Data preparation takes 80% of time in any data science projects. Detecting errors, is one of the crucial step in the data science workflow. This work aims to detect these develop an error detection pipeline to detect the above mentioned errors based on extracting metadata by leveraging various statistical techniques, tools, and unsupevised learning. It's a non-learning approach based error detection. This work is based on the novel task structure proposed by Visengeriyeva and Abedjan (2020) [2] for mapping data quality issues to metadata using qualitative and quantitative techniques and enhancing the data preparation process to detect data errors through metadata. 

**Typical data-science workflow**

![alt-text](https://github.com/iramshiv/meta_errdec_ml/blob/main/images/1.jpg)

# Objective

This work has three main objectives which are,
1. Demonstrating error detection heuristics from extracted metadata that can signal potential errors.
2. Implementing a basic practical application to generate user-defined metadata from extracted metadata combined with heuristics that can also prove to signal errors.
3. Establishing a pipeline to extract metadata and detect erros.

# Architecture

Our pipeline consists,

1. Profiler: where the metadata are extracted using various techniques.
2. Detetctor: where the error detection heuristics detects errors based on rules or condtions using extrcated metadata.
3. Generator: where the user can generate task-specific metadata using the extracted metadata to siganl further errors.

**Our Architecture**

![alt-text](https://github.com/iramshiv/meta_errdec_ml/blob/main/images/2..jpg)

**Profiler**

![alt-text](https://github.com/iramshiv/meta_errdec_ml/blob/main/images/3.jpg)

Profiler extracts metadata and the detector identifies errors for following tasks,

1. Unique Column / Primary Key  (pandas- nunique() for uniqueness and len() for number of rows)
2. Missing values (Null values) (pandas - isnull())
3. Disguised Missing values (DMVs) (FAHEES [3] and Patterns)
4. Patterns
5. Top values vs patterns (Patterns)
6. Data type inference (Patterns)
7. value length
8. Domain violations (Patterns)
9. duplicates (Fuzz [4], Sparkclean [5])
10. outliers (User-defined generator)
 
**Experimental Environment**

1. Single machine with 2.3 GHz 11th Gen Intel Core i7 processor and 16 GB RAM.
2. PyCharm IDE
3. Windows 11
4. Major libraries: 
  python 3.10, Equation==1.2.01, numpy==1.22.3, pandas==1.4.2, thefuzz==0.19.0
5. Cygwin64 Terminal

**Install packages**

```pip install -r requirements.txt```

**Execution**

Run ```index.py```

**User metadata generator overview**

![alt-text](https://github.com/iramshiv/meta_errdec_ml/blob/main/images/4.jpg)

For metadata generator, example that generates z-value metadata from extracted metadata (value length) to find outliers,

![alt-text](https://github.com/iramshiv/meta_errdec_ml/blob/main/images/z-val.jpg)

# References

[1] Quartz bad data guide: An exhaustive reference to problems seen in real-world data along with suggestions on how to resolve them. GitHub. https://github.com/Quartz/bad-data-guide  Accessed on 2023.01.26

[2] Visengeriyeva, L. Advancing data curation with metadata and statistical relational learning. TU Berlin, DOI: 10.14279/depositonce-9705, 2020.
https://depositonce.tu-berlin.de/items/702522f2-90cf-43cd-971a-99474f48ede3 

[3] https://github.com/daqcri/FAHES_Code

[4] https://github.com/seatgeek/fuzzywuzzy

[5]https://github.com/NYUBigDataProject/SparkClean

**Dataset**

[6]	Diabetes Dataset. https://github.com/daqcri/FAHES_Code/blob/master/Data/pima-indians-diabetes.csv Accessed: 2023-01-10

[7]	Adult Dataset. https://github.com/daqcri/FAHES_Code/blob/master/Data/adult.csv Accessed: 2023-01-10

[8]	Graduation dataset. https://github.com/daqcri/FAHES_Code/blob/master/Data/12252-1.csv

[9]	Restaurant Dataset. https://github.com/DastLab/RENUVER-evaluation-datasets/blob/main/MV-injected/Restaurant/Datasets/restaurant_1037_1.csv  

[10] https://github.com/visenger/clean-and-dirty-data/tree/master/FLIGHTS
