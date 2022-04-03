import pandas as pas
import os
import matplotlib.pyplot as ply

file_excel1 = os.path.dirname(os.path.realpath(__file__)) + '\\..\\..\\data\\processed\\' + "1996_cleaned_data.csv"
file_excel2 = os.path.dirname(os.path.realpath(__file__)) + '\\..\\..\\data\\processed\\' + "2001_cleaned_data.csv"
file_excel3 = os.path.dirname(os.path.realpath(__file__)) + '\\..\\..\\data\\processed\\' + "2006_cleaned_data.csv"
file_excel4 = os.path.dirname(os.path.realpath(__file__)) + '\\..\\..\\data\\processed\\' + "2016_cleaned_data.csv"

read_file1 = pas.read_csv(file_excel1)
read_file2 = pas.read_csv(file_excel2)
read_file3 = pas.read_csv(file_excel3)
read_file4 = pas.read_csv(file_excel4)
#print(read_file1.columns)

#1996_Printing single with immigration status of either 1: Not an immigrant (ex. a citizen) 2: Immigrant 3: Non-permanent resident (ex. a refugee or a person on a work/study permit)
filter_96_1 = read_file1.loc[(read_file1['MART_STAT'] == 1) & (read_file1['IMM_STAT'] == 1)]
filter_96_2 = read_file1.loc[(read_file1['MART_STAT'] == 1) & (read_file1['IMM_STAT'] == 2)]
filter_96_3 = read_file1.loc[(read_file1['MART_STAT'] == 1) & (read_file1['IMM_STAT'] == 3)]

#1996_Printing Married with immigration status of either 1: Not an immigrant (ex. a citizen) 2: Immigrant 3: Non-permanent resident (ex. a refugee or a person on a work/study permit)
filter_96_11 = read_file1.loc[(read_file1['MART_STAT'] == 2) & (read_file1['IMM_STAT'] == 1)]
filter_96_22 = read_file1.loc[(read_file1['MART_STAT'] == 2) & (read_file1['IMM_STAT'] == 2)]
filter_96_33 = read_file1.loc[(read_file1['MART_STAT'] == 2) & (read_file1['IMM_STAT'] == 3)]

#2001_Printing single with immigration status of either 1: Not an immigrant (ex. a citizen) 2: Immigrant 3: Non-permanent resident (ex. a refugee or a person on a work/study permit)
filter_01_1 = read_file2.loc[(read_file2['MART_STAT'] == 1) & (read_file2['IMM_STAT'] == 1)]
filter_01_2 = read_file2.loc[(read_file2['MART_STAT'] == 1) & (read_file2['IMM_STAT'] == 2)]
filter_01_3 = read_file2.loc[(read_file2['MART_STAT'] == 1) & (read_file2['IMM_STAT'] == 3)]

#2001_Printing Married with immigration status of either 1: Not an immigrant (ex. a citizen) 2: Immigrant 3: Non-permanent resident (ex. a refugee or a person on a work/study permit)
filter_01_11 = read_file2.loc[(read_file2['MART_STAT'] == 2) & (read_file2['IMM_STAT'] == 1)]
filter_01_22 = read_file2.loc[(read_file2['MART_STAT'] == 2) & (read_file2['IMM_STAT'] == 2)]
filter_01_33 = read_file2.loc[(read_file2['MART_STAT'] == 2) & (read_file2['IMM_STAT'] == 3)]

#2006_Printing single with immigration status of either 1: Not an immigrant (ex. a citizen) 2: Immigrant 3: Non-permanent resident (ex. a refugee or a person on a work/study permit)
filter_06_1 = read_file3.loc[(read_file3['MART_STAT'] == 1) & (read_file3['IMM_STAT'] == 1)]
filter_06_2 = read_file3.loc[(read_file3['MART_STAT'] == 1) & (read_file3['IMM_STAT'] == 2)]
filter_06_3 = read_file3.loc[(read_file3['MART_STAT'] == 1) & (read_file3['IMM_STAT'] == 3)]

#2006_Printing Married with immigration status of either 1: Not an immigrant (ex. a citizen) 2: Immigrant 3: Non-permanent resident (ex. a refugee or a person on a work/study permit)
filter_06_11 = read_file3.loc[(read_file3['MART_STAT'] == 2) & (read_file3['IMM_STAT'] == 1)]
filter_06_22 = read_file3.loc[(read_file3['MART_STAT'] == 2) & (read_file3['IMM_STAT'] == 2)]
filter_06_33 = read_file3.loc[(read_file3['MART_STAT'] == 2) & (read_file3['IMM_STAT'] == 3)]

#2016_Printing single with immigration status of either 1: Not an immigrant (ex. a citizen) 2: Immigrant 3: Non-permanent resident (ex. a refugee or a person on a work/study permit)
filter_16_1 = read_file2.loc[(read_file4['MART_STAT'] == 1) & (read_file2['IMM_STAT'] == 1)]
filter_16_2 = read_file2.loc[(read_file4['MART_STAT'] == 1) & (read_file2['IMM_STAT'] == 2)]
filter_16_3 = read_file2.loc[(read_file4['MART_STAT'] == 1) & (read_file2['IMM_STAT'] == 3)]

#2016_Printing Married with immigration status of either 1: Not an immigrant (ex. a citizen) 2: Immigrant 3: Non-permanent resident (ex. a refugee or a person on a work/study permit)
filter_16_11 = read_file4.loc[(read_file4['MART_STAT'] == 2) & (read_file4['IMM_STAT'] == 1)]
filter_16_22 = read_file4.loc[(read_file4['MART_STAT'] == 2) & (read_file4['IMM_STAT'] == 2)]
filter_16_33 = read_file4.loc[(read_file4['MART_STAT'] == 2) & (read_file4['IMM_STAT'] == 3)]




