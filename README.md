Modal Canadian
==============================

The project will analyze Canadian census data
to determine the differences between the characteristics that
encompasses a modal Canadian and average Canadian, and the
changes to the difference over time.

Currently, the data comes from the PUMF files from Carleton University's access of the <odesi> (Ontario Data Documentation, Extraction Service and Infrastructure) database. The data that is currently being used are the PUMF census files from 1996, 2001, 2006, and 2016. Unfortunately, the PUMF census files for 2011 were not available and the PUMF census files for 2021 will not be fully released by the deadline of this project.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

Cleaning Instructions
---
The cleaning process will clean a CSV file in the data/raw folder and export the results as a CSV file in the data/processed folder. The raw CSV files will need to be placed into the data/raw folder to begin with. To clean the raw CSV data in the data/raw folder:
1. Navigate to the src/data folder of the local repository via a terminal
2. Run the following command ```python clean.py [raw_filename] [cleaned_filename]```. Replace ```[raw_filename]``` with the filename of the raw CSV file and ```[cleaned_filename]``` with the name of the exported cleaned CSV file, both without the square brackets. For example, ```python clean.py 2016_raw.csv 2016_cleaned.csv``` would clean the data in a file called 2016_raw.csv and export the cleaned data in to CSV file called 2016_cleaned.csv in the data/processed folder. 


Columns of Cleaned Data
---
### WEIGHT

Represents the amount of people the sample represents in the entire population.

### AGE

Represents the age group the sample is part of. The values of this column are as follows:
- 1: 0-9 years of age
- 2: 10-19 years of age
- 3: 20-29 years of age
- 4: 30-39 years of age
- 5: 40-49 years of age
- 6: 50-59 years of age
- 7: 60-69 years of age
- 8: 70-79 years of age
- 9: 80 years of age and over

### SEX

Represents the sex at birth of the sample. The values of this column are as follows:
- 1: Male
- 2: Female

### MART_STAT

Represents the marital status of the sample. The values of this column are as follows:
- 1: Single
- 2: Married

### HOUS_INC

Represents the household income of the sample. The values of this column are as follows:
- 1: Less than $25k
- 2: $25k to $49,999
- 3: $50k to $74,999
- 4: $75k to $99,999
- 5: $100k and over

### HOUS_SIZ

Represents the household size of the sample. The values of this column are as follows:
- 1: 1 person
- 2: 2 people
- 3: 3 people
- 4: 4 people
- 5: Over 4 people

### IND_INC

Represents the individual income of the sample. This column will not factor in the individual income of samples that are under the age of 15. The values of this column are as follows:
- 0: Not applicable (the sample is under the age of 15)
- 1: Less than $0 (net loss)
- 2: $0 to $24,999
- 3: $25k to $49,999
- 4: $50k to $74,999
- 5: $75k to $99,999
- 6: $100k and over

### OFF_LANG

Represents the knowledge of the official languages of the person, which is whether they are able to communicate with the official languages of Canada (English and French). The values of this column are as follows:
- 1: English only
- 2: French only
- 3: Both English and French
- 4: Neither English or French

### HOME_LANG

Represents the language spoken most often at home of the sample. The values of this column are as follows:
- 1: English only
- 2: French only
- 3: Both English and French
- 4: Other languages

### POB

Represents the place of birth of the sample. The values of this column are as follows:
- 1: Born inside Canada
- 2: Born outside Canada

### ETHN

Represents the ethnic and cultural origins of the sample. The values of this column are as follows:
TODO

### CITZ_SHIP

Represents the citizenship status of the sample. The values of this column are as follows:
- 1: Canadian by birth
- 2: Canadian by naturalization (ex. an immigrant applying for citizenship)
- 3: Citizenship in a different country

### IMM_STAT

Represents the immigration status of the sample. The values of this column are as follows:
- 1: Not an immigrant (ex. a citizen)
- 2: Immigrant
- 3: Non-permanent resident (ex. a refugee or a person on a work/study permit)

### PROV

Represents the current province of residence of the sample. The values of this column are as follows:
- 1: Newfoundland and Labrador
- 2: Prince Edward Island
- 3: Nova Scotia
- 4: New Brunswick
- 5: Quebec
- 6: Ontario
- 7: Manitoba
- 8: Saskatchewan
- 9: Alberta
- 10: British Columbia
- 11: One of the territories

### HIGH_EDU

Represents the highest level of education of the sample. This column will not factor in the education level of samples that are under the age of 15. The values of this column are as follows:
- 0: Not applicable (the sample is under the age of 15)
- 1: No degree (didn't finish high school)
- 2: High school degree
- 3: Certificate or Diploma from trades, college, or university
- 4: University Bachelor's degree
- 5: Degree above bachelor's (Medical, Veternarian, Dental)
- 6: Post graduate (Master's, PhD)

### EMP_STAT

Represents the employment status of the sample. This column will not factor in the employment status of samples that are under the age of 15. The values of this columnare as follows:
- 0: Not applicable (the sample is under the age of 15)
- 1: Employed
- 2: Unemployed
- 3: Not in workforce (ex. retired or never worked, such as housewife/househusband)

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
