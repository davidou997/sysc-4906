import pandas as pas
import os

file_excel1 = os.path.dirname(os.path.realpath(__file__)) + '\\..\\..\\data\\processed\\' + "1996_cleaned_data.csv"
file_excel2 = os.path.dirname(os.path.realpath(__file__)) + '\\..\\..\\data\\processed\\' + "2001_cleaned_data.csv"
file_excel3 = os.path.dirname(os.path.realpath(__file__)) + '\\..\\..\\data\\processed\\' + "2006_cleaned_data.csv"
file_excel4 = os.path.dirname(os.path.realpath(__file__)) + '\\..\\..\\data\\processed\\' + "2016_cleaned_data.csv"

read_file1 = pas.read_csv(file_excel1)
read_file2 = pas.read_csv(file_excel2)
read_file3 = pas.read_csv(file_excel3)
read_file4 = pas.read_csv(file_excel4)

#1996)_Printing province with any person that made above 0 income
filter_96_1 = read_file1.loc[(read_file1['PROV'] == 1) & (read_file1['IND_INC'] > 1 )]
filter_96_2 = read_file1.loc[(read_file1['PROV'] == 2) & (read_file1['IND_INC'] > 1 )]
filter_96_3 = read_file1.loc[(read_file1['PROV'] == 3) & (read_file1['IND_INC'] > 1 )]
filter_96_4 = read_file1.loc[(read_file1['PROV'] == 4) & (read_file1['IND_INC'] > 1 )]
filter_96_5= read_file1.loc[(read_file1['PROV'] == 5) & (read_file1['IND_INC'] > 1 )]
filter_96_6 = read_file1.loc[(read_file1['PROV'] == 6) & (read_file1['IND_INC'] > 1 )]
filter_96_7 = read_file1.loc[(read_file1['PROV'] == 7) & (read_file1['IND_INC'] > 1 )]
filter_96_8 = read_file1.loc[(read_file1['PROV'] == 8) & (read_file1['IND_INC'] > 1 )]
filter_96_9 = read_file1.loc[(read_file1['PROV'] == 9) & (read_file1['IND_INC'] > 1 )]
filter_96_10 = read_file1.loc[(read_file1['PROV'] == 10) & (read_file1['IND_INC'] > 1 )]
filter_96_11 = read_file1.loc[(read_file1['PROV'] == 11) & (read_file1['IND_INC'] > 1 )]

#2001_Printing provinces with any person that made above 0 income
filter_01_1 = read_file2.loc[(read_file2['PROV'] == 1) & (read_file2['IND_INC'] > 1 )]
filter_01_2 = read_file2.loc[(read_file2['PROV'] == 2) & (read_file2['IND_INC'] > 1 )]
filter_01_3 = read_file2.loc[(read_file2['PROV'] == 3) & (read_file2['IND_INC'] > 1 )]
filter_01_4 = read_file2.loc[(read_file2['PROV'] == 4) & (read_file2['IND_INC'] > 1 )]
filter_01_5 = read_file2.loc[(read_file2['PROV'] == 5) & (read_file2['IND_INC'] > 1 )]
filter_01_6 = read_file2.loc[(read_file2['PROV'] == 6) & (read_file2['IND_INC'] > 1 )]
filter_01_7 = read_file2.loc[(read_file2['PROV'] == 7) & (read_file2['IND_INC'] > 1 )]
filter_01_8 = read_file2.loc[(read_file2['PROV'] == 8) & (read_file2['IND_INC'] > 1 )]
filter_01_9 = read_file2.loc[(read_file2['PROV'] == 9) & (read_file2['IND_INC'] > 1 )]
filter_01_10 = read_file2.loc[(read_file2['PROV'] == 10) & (read_file2['IND_INC'] > 1 )]
filter_01_11 = read_file2.loc[(read_file2['PROV'] == 11) & (read_file2['IND_INC'] > 1 )]

#2006_Printing province with any person that made above 0 income
filter_06_1 = read_file3.loc[(read_file3['PROV'] == 1) & (read_file3['IND_INC'] > 1 )]
filter_06_2 = read_file3.loc[(read_file3['PROV'] == 2) & (read_file3['IND_INC'] > 1 )]
filter_06_3 = read_file3.loc[(read_file3['PROV'] == 3) & (read_file3['IND_INC'] > 1 )]
filter_06_4 = read_file3.loc[(read_file3['PROV'] == 4) & (read_file3['IND_INC'] > 1 )]
filter_06_5 = read_file3.loc[(read_file3['PROV'] == 5) & (read_file3['IND_INC'] > 1 )]
filter_06_6 = read_file3.loc[(read_file3['PROV'] == 6) & (read_file3['IND_INC'] > 1 )]
filter_06_7 = read_file3.loc[(read_file3['PROV'] == 7) & (read_file3['IND_INC'] > 1 )]
filter_06_8 = read_file3.loc[(read_file3['PROV'] == 8) & (read_file3['IND_INC'] > 1 )]
filter_06_9 = read_file3.loc[(read_file3['PROV'] == 9) & (read_file3['IND_INC'] > 1 )]
filter_06_10 = read_file3.loc[(read_file3['PROV'] == 10) & (read_file3['IND_INC'] > 1 )]
filter_06_11 = read_file3.loc[(read_file3['PROV'] == 11) & (read_file3['IND_INC'] > 1 )]

#2016_Printing province with any person that made above 0 income
filter_16_1 = read_file4.loc[(read_file4['PROV'] == 1) & (read_file4['IND_INC'] > 1 )]
filter_16_2 = read_file4.loc[(read_file4['PROV'] == 2) & (read_file4['IND_INC'] > 1 )]
filter_16_3 = read_file4.loc[(read_file4['PROV'] == 3) & (read_file4['IND_INC'] > 1 )]
filter_16_4 = read_file4.loc[(read_file4['PROV'] == 4) & (read_file4['IND_INC'] > 1 )]
filter_16_5 = read_file4.loc[(read_file4['PROV'] == 5) & (read_file4['IND_INC'] > 1 )]
filter_16_6 = read_file4.loc[(read_file4['PROV'] == 6) & (read_file4['IND_INC'] > 1 )]
filter_16_7 = read_file4.loc[(read_file4['PROV'] == 7) & (read_file4['IND_INC'] > 1 )]
filter_16_8 = read_file4.loc[(read_file4['PROV'] == 8) & (read_file4['IND_INC'] > 1 )]
filter_16_9 = read_file4.loc[(read_file4['PROV'] == 9) & (read_file4['IND_INC'] > 1 )]
filter_16_10 = read_file4.loc[(read_file4['PROV'] == 10) & (read_file4['IND_INC'] > 1 )]
filter_16_11 = read_file4.loc[(read_file4['PROV'] == 11) & (read_file4['IND_INC'] > 1 )]