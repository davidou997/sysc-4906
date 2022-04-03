import sys
import os
import pandas as pd


def clean(filename, export_name):
    loaded = load_file(filename)
    extracted_dict = {
        'WEIGHT': [],  # Weight
        'AGE': [],  # Age
        'SEX': [],  # Sex
        'MART_STAT': [],  # Marital Status
        'HOUS_INC': [],  # Household Income
        'HOUS_SIZ': [],  # Household Size
        'IND_INC': [],  # Individual Income
        'OFF_LANG': [],  # Knowledge of Official Languages
        'HOME_LANG': [],  # Home Language
        'POB': [],  # Place of Birth
        'ETHN': [],  # Ethnicity
        'CITZ_SHIP': [],  # Citizenship
        'IMM_STAT': [],  # Immigration Status
        'PROV': [],  # Province
        'HIGH_EDU': [],  # Highest Level of Education
        'EMP_STAT': []  # Employment Status
    }

    extracted_dict['WEIGHT'] = extract_weight(loaded)
    extracted_dict['AGE'] = extract_age(loaded)
    extracted_dict['SEX'] = extract_sex(loaded)
    extracted_dict['MART_STAT'] = extract_sex(loaded)
    extracted_dict['HOUS_INC'] = extract_house_income(loaded)
    extracted_dict['HOUS_SIZ'] = extract_house_size(loaded)
    extracted_dict['IND_INC'] = extract_house_size(loaded)
    extracted_dict['OFF_LANG'] = extract_official_lang(loaded)
    extracted_dict['HOME_LANG'] = extract_home_lang(loaded)
    extracted_dict['POB'] = extract_pob(loaded)
    extracted_dict['ETHN'] = extract_ethnic(loaded)
    extracted_dict['CITZ_SHIP'] = extract_citz_stat(loaded)
    extracted_dict['IMM_STAT'] = extract_imm_stat(loaded)
    extracted_dict['PROV'] = extract_prov(loaded)
    extracted_dict['HIGH_EDU'] = extract_edu(loaded)
    extracted_dict['EMP_STAT'] = extract_emp_stat(loaded)

    extracted_df = pd.DataFrame.from_dict(extracted_dict)
    cleaned_df = sanitize(extracted_df)
    export_file(cleaned_df, export_name)


def extract_weight(loaded_df):
    """
    Extracts the weights of each row.
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the weights of each row
    """
    weights = []
    columns = loaded_df.columns
    col_name = ""

    print('Extracting Weights')

    if "WEIGHTP" in columns:
        col_name += "WEIGHTP"
    elif "WEIGHT" in columns:
        col_name += "WEIGHT"
    else:
        print("No Age Column Detected")
        sys.exit(0)

    weights = loaded_df[col_name].tolist()

    print('Weights extracted')

    return weights


def extract_age(loaded_df):
    """
    Extracts the age from each row and bins it. The format is the following:
    -1 - Invalid value
    1 - 0 to 9
    2 - 10 to 19
    3 - 20 to 29
    4 - 30 to 39
    5 - 40 to 49
    6 - 50 - 59
    7 - 60 - 69
    8 - 70 - 79
    9 - 80 and over

    :param loaded_df: The loaded dataframe from the file
    :return: A list of the weights
    """
    ages = []
    columns = loaded_df.columns
    col_name = ""

    print('Extracting Age')

    if "AGEGRP" in columns:
        col_name += "AGEGRP"
    elif "AGEP" in columns:
        col_name += "AGEP"
    else:
        print("No Age Column Detected")
        sys.exit(0)

    for age in loaded_df[col_name].tolist():
        if col_name == "AGEGRP":
            if age <= 3:  # 0 to 9
                ages.append(1)
            elif age <= 7:  # 10 to 19
                ages.append(2)
            elif age <= 9:  # 20 to 29
                ages.append(3)
            elif age <= 11:  # 30 to 39
                ages.append(4)
            elif age <= 13:  # 40 to 49
                ages.append(5)
            elif age <= 15:  # 50 to 49
                ages.append(6)
            elif age <= 17:  # 60 to 69
                ages.append(7)
            elif age <= 19:  # 70 to 79
                ages.append(8)
            elif age <= 21:  # 80 and above
                ages.append(9)
            else:  # Not applicable
                ages.append(-1)
        else:
            if age < 10:  # 0 to 9
                ages.append(1)
            elif age < 20:  # 10 to 19
                ages.append(2)
            elif age < 30:  # 20 to 29
                ages.append(3)
            elif age < 40:  # 30 to 39
                ages.append(4)
            elif age < 50:  # 40 to 49
                ages.append(5)
            elif age < 60:  # 50 to 59
                ages.append(6)
            elif age < 70:  # 60 to 69
                ages.append(7)
            elif age < 80:  # 70 to 79
                ages.append(8)
            elif age >= 80:  # 80 and above
                ages.append(9)
            else:  # Not applicable
                ages.append(-1)

    print('Age extracted')

    return ages


def extract_sex(loaded_df):
    """
    Extracts the sex of each row. The coded values are as follows:
    1 - Male
    2 - Female
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the sex values
    """
    sexes = []
    columns = loaded_df.columns
    col_name = ""

    print('Extracting Sex')

    if "Sex" in columns:
        col_name += "Sex"
    elif "SEX" in columns:
        col_name += "SEX"
    elif "SEXP" in columns:
        col_name += "SEXP"
    else:
        print("No Sex Column Detected")
        sys.exit(0)

    sexes = loaded_df[col_name].tolist()

    print('Sex extracted')

    return sexes


def extract_marital(loaded_df):
    """
    Extracts the marital statuses of each row. The coded values are the following:
    -1 - Invalid value
    1 - Single
    2 - Married
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the marital status
    """
    mart_stats = []
    columns = loaded_df.columns
    col_name = ""

    print('Extracting Marital Status')

    if "MarStH" in columns:
        col_name += "MarStH"
    elif "MARST" in columns:
        col_name += "MARST"
    elif "MARSTLP" in columns:
        col_name += "MARSTLP"
    else:
        print("No Marital Status Column Detected")
        sys.exit(0)

    single_cats = [1, 3, 4, 5]
    if col_name == "MarStH":
        single_cats = [1, 3, 4, 5, 6]

    for mart_stat in loaded_df[col_name].tolist():
        if mart_stat in single_cats:  # Single
            mart_stats.append(1)
        elif mart_stat == 2:  # Married
            mart_stats.append(2)
        else:
            mart_stats.append(-1)  # Not available

    print('Marital Status extracted')

    return mart_stats


def extract_house_income(loaded_df):
    """
    Extracts the household income of each row. The coded values are the following:
    -1 - Invalid value
    1 - Less than 25k
    2 - 25k to 49,999
    3 - 50k to 74,999
    4 - 75k to 99,999
    5 - 100k and over
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the household income
    """
    hous_incs = []
    columns = loaded_df.columns
    col_name = ""

    print('Extracting Household Income')

    if "HHInc" in columns:
        col_name += "HHInc"
    elif "HHINC" in columns:
        col_name += "HHINC"
    elif "HHINCP" in columns:
        col_name += "HHINCP"
    else:
        print("No Household Income Column Detected")
        sys.exit(0)

    for hous_inc in loaded_df[col_name].tolist():
        if col_name == "HHINCP":
            if hous_inc < 10:  # less than 25k
                hous_incs.append(1)
            elif hous_inc < 15:  # 25k to 49,999
                hous_incs.append(2)
            elif hous_inc < 20:  # 50k to 74,999
                hous_incs.append(3)
            elif hous_inc < 22:  # 75k to 99,999
                hous_incs.append(4)
            elif hous_inc < 99:  # over 100k
                hous_incs.append(5)
            else:  # invalid value
                hous_incs.append(-1)
        elif col_name == "HHINC":
            if hous_inc < 10:  # less than 25k
                hous_incs.append(1)
            elif hous_inc < 15:  # 25k to 49,999
                hous_incs.append(2)
            elif hous_inc < 20:  # 50k to 74,999
                hous_incs.append(3)
            elif hous_inc < 23:  # 75k to 99,999
                hous_incs.append(4)
            elif hous_inc <= 28:  # over 100k
                hous_incs.append(5)
            else:  # invalid value
                hous_incs.append(-1)
        else:
            if hous_inc < 10:  # less than 25k
                hous_incs.append(1)
            elif hous_inc < 15:  # 25k to 49,999
                hous_incs.append(2)
            elif hous_inc < 20:  # 50k to 74,999
                hous_incs.append(3)
            elif hous_inc < 25:  # 75k to 99,999
                hous_incs.append(4)
            elif hous_inc <= 33:  # over 100k
                hous_incs.append(5)
            else:  # invalid value
                hous_incs.append(-1)

    print('Household Income extracted')

    return hous_incs


def extract_house_size(loaded_df):
    """
    Extracts the household size of each row. The coded values are the following:
    -1 - Invalid value
    1 - 1 person
    2 - 2 people
    3 - 3 people
    4 - 4 people
    5 - Over 4 people
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the household size
    """
    hous_sizes = []
    columns = loaded_df.columns
    col_name = ""

    print('Extracting Household Size')

    if "HHSIZE" in columns:
        col_name += "HHSIZE"
    elif "UNITSP" in columns:
        col_name += "UNITSP"
    else:
        print("No Household Size Column Detected")
        sys.exit(0)

    for hous_size in loaded_df[col_name].tolist():
        if hous_size == 1:  # 1 person
            hous_sizes.append(1)
        elif hous_size == 2:  # 2 people
            hous_sizes.append(2)
        elif hous_size == 3:  # 3 people
            hous_sizes.append(3)
        elif hous_size == 4:  # 4 people
            hous_sizes.append(4)
        elif hous_size <= 7:  # over 4 people
            hous_sizes.append(5)
        else:  # invalid value
            hous_sizes.append(-1)

    print('Household Size extracted')

    return hous_sizes


def extract_ind_income(loaded_df):
    """
    Extracts the individual income of each row. The coded values are the following:
    -1 - Invalid value
    0 - Not applicable (the person is under 15 years of age)
    1 - Less than 0 (net loss)
    2 - 0 to 24,999
    3 - 25k to 49,999
    4 - 50k to 74,999
    5 - 75k to 99,999
    6 - Over 100k
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the individual income
    """
    ind_incs = []
    columns = loaded_df.columns
    col_name = ""
    max_val = 0

    print('Extracting Individual Income')

    if "TotInc" in columns:
        col_name += "TotInc"
        max_val = 1586814
    elif "TOTINC" in columns:
        col_name += "TOTINC"
        max_val = 1285586
    elif "TOTINCP" in columns:
        col_name += "TOTINCP"
        max_val = 200000
    else:
        print("No Individual Income Column Detected")
        sys.exit(0)

    for ind_inc in loaded_df[col_name].tolist():
        if ind_inc < 0:  # net loss
            ind_incs.append(1)
        elif ind_inc < 25000:  # 0 to 24,999
            ind_incs.append(2)
        elif ind_inc < 50000:  # 25k to 49,999
            ind_incs.append(3)
        elif ind_inc < 75000:  # 50k to 74,999
            ind_incs.append(4)
        elif ind_inc < 100000:  # 75k to 99,999
            ind_incs.append(5)
        elif ind_inc <= max_val:  # over 100k
            ind_incs.append(6)
        elif ind_inc == 99999999:  # the person is under 15 years of age
            ind_incs.append(0)
        else:  # invalid value
            ind_incs.append(-1)

    print('Individual Income extracted')

    return ind_incs


def extract_official_lang(loaded_df):
    """
    Extracts the knowledge of the official languages of each row. The coded values are the following:
    -1 - Invalid value
    1 - English only
    2 - French only
    3 - Both
    4 - Neither
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the knowledge of the official languages
    """
    off_langs = []
    columns = loaded_df.columns
    col_name = ""
    valid_vals = [1, 2, 3, 4]

    print('Extracting Knowledge of Official Languages')

    if "KOL" in columns:
        col_name += "KOL"
        max_val = 1586814
    elif "OLNP" in columns:
        col_name += "OLNP"
        max_val = 1285586
    else:
        print("No Knowledge of the Official Languages Column Detected")
        sys.exit(0)

    off_langs = [ind_inc if ind_inc in valid_vals else -1 for ind_inc in loaded_df[col_name].tolist()]

    print('Knowledge of Official Languages extracted')

    return off_langs


def extract_home_lang(loaded_df):
    """
    Extracts the home language of each row. The coded values are the following:
    -1 - Invalid value
    1 - English only
    2 - French only
    3 - Both
    4 - Other
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the home language
    """
    home_langs = []
    columns = loaded_df.columns
    col_name_main = ""
    col_name_en = ""
    col_name_fr = ""

    print('Extracting Home Language')

    if "HLNP" in columns:
        col_name_main = "HLNP"
    elif "HLNPA" in columns:
        col_name_main = "HLNPA"
    elif "HLANO" in columns and "HLAFR" in columns and "HLAEN" in columns:
        col_name_main = "HLANO"
        col_name_en = "HLAFR"
        col_name_fr = "HLAEN"
    else:
        print("No Home Language Column(s) Detected")
        sys.exit(0)

    col_main = loaded_df[col_name_main].tolist()
    col_en = []
    col_fr = []

    if col_name_en:
        col_en = loaded_df[col_name_en].tolist()

    if col_name_fr:
        col_fr = loaded_df[col_name_fr].tolist()

    for index in range(len(col_main)):
        home_lang = col_main[index]
        if col_name_main == "HLANO":
            if home_lang == 0:
                home_lang_en = col_en[index]
                home_lang_fr = col_fr[index]
                if home_lang_en == 0 and home_lang_fr == 0:
                    home_langs.append(3)
                elif home_lang_en == 0 and home_lang_fr == 1:
                    home_langs.append(1)
                elif home_lang_en == 1 and home_lang_fr == 0:
                    home_langs.append(2)
                else:
                    home_langs.append(4)
                print('check en fr')
            elif not home_lang == 88:
                home_langs.append(4)
            else:
                home_langs.append(-1)
        else:
            if home_lang == 1:
                home_langs.append(1)
            elif home_lang == 2:
                home_langs.append(3)
            elif home_lang == 3:
                home_langs.append(3)
            elif not home_lang == 98 and not home_lang == 99:
                home_langs.append(4)
            else:
                home_langs.append(-1)

    print('Home Language extracted')

    return home_langs


def extract_pob(loaded_df):
    """
    Extracts the place of birth of each row. The coded values are the following:
    -1 - Invalid value
    1 - Born inside Canada
    2 - Born outside Canada
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the place of birth
    """
    pobs = []
    columns = loaded_df.columns
    col_name = ""

    print('Extracting Place of Birth')

    if "POBP" in columns:
        col_name = "POBP"
    elif "POB" in columns:
        col_name = "POB"
    else:
        print("No Place of Birth Column(s) Detected")

    num_uniq = loaded_df[col_name].nunique()

    for pob in loaded_df[col_name].tolist():
        if col_name == "POBP":
            if num_uniq == 41:
                if pob <= 10 or (pob >= 33 and pob <= 35):  # Inside Canada
                    pobs.append(1)
                elif pob <= 40:  # Outside Canada
                    pobs.append(2)
                else:  # invalid value
                    pobs.append(-1)
            elif num_uniq == 13:
                if pob < 6:  # Inside Canada
                    pobs.append(1)
                elif pob <= 12:  # Outside Canada
                    pobs.append(2)
                else:  # invalid value
                    pobs.append(-1)
        else:
            if num_uniq == 28:
                if pob == 1:  # Inside Canada
                    pobs.append(1)
                elif pob <= 27:  # Outside Canada
                    pobs.append(2)
                else:  # invalid value
                    pobs.append(-1)
            elif num_uniq == 33:
                if pob == 1:  # Inside Canada
                    pobs.append(1)
                elif pob <= 32:  # Outside Canada
                    pobs.append(2)
                else:  # invalid value
                    pobs.append(-1)

    print('Place of Birth extracted')

    return pobs


def extract_ethnic(loaded_df):
    """
    Extracts the ethnic origins of each row. The coded values are the following:
    -1 - Invalid value
    1 - European
    2 - Middle Eastern
    3 - South Asian
    4 - East Asian
    5 - African/South American
    6 - Multiple origins
    7 - Aboriginal
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the ethnic origins
    """
    # TODO
    ethnics = []
    columns = loaded_df.columns
    col_name = ""
    num_unique = 0

    print('Extracting Ethnic Origins')

    if 'ETHNICRP' in columns:
        col_name = 'ETHNICRP'
    elif 'ETHNICRA' in columns:
        col_name = 'ETHNICRA'
    elif 'ETHDER' in columns:
        col_name = 'ETHDER'
    else:
        print('No Citizenship Status column Detected')
        sys.exit(0)

    num_unique = loaded_df[col_name].nunique()

    for ethnic in loaded_df[col_name].tolist():
        if col_name == "ETHDER":
            if num_unique == 49:
                if ethnic == 40 or 4 <= ethnic <= 23 or 34 <= ethnic <= 36:  # European
                    ethnics.append(1)
                elif ethnic == 28:  # Middle Eastern
                    ethnics.append(2)
                elif ethnic in [29, 30]:  # South Asian
                    ethnics.append(3)
                elif 31 <= ethnic <= 33:  # East Asian
                    ethnics.append(4)
                elif 24 <= ethnic <= 27:  # African/South American
                    ethnics.append(5)
                elif ethnic in [2, 3] or 37 <= ethnic <= 39 or 41 <= ethnic <= 48:  # Multiple origins
                    ethnics.append(6)
                elif ethnic == 1:  # Aboriginal
                    ethnics.append(7)
                else:
                    ethnics.append(-1)
            else:
                if 4 <= ethnic <= 9 or 13 <= ethnic <= 25 or 27 <= ethnic <= 13:  # European
                    ethnics.append(1)
                elif ethnic == 32 or 34 <= ethnic <= 36:  # Middle Eastern
                    ethnics.append(2)
                elif ethnic == 37 or ethnic == 38:  # South Asian
                    ethnics.append(3)
                elif 39 <= ethnic <= 43:  # East Asian
                    ethnics.append(4)
                elif 10 <= ethnic <= 12 or ethnic == 33:  # African/South American
                    ethnics.append(5)
                elif ethnic in [1, 2, 51] or 44 <= ethnic <= 46:  # Multiple origins
                    ethnics.append(6)
                elif 47 <= ethnic <= 50:  # Aboriginal
                    ethnics.append(7)
                else:  # invalid value
                    ethnics.append(-1)
        elif col_name == 'ETHNICRA':
            if 2 <= ethnic <= 13 or 22 <= ethnic <= 28:  # European
                ethnics.append(1)
            elif ethnic in [14, 16, 30, 31]:  # Middle Eastern
                ethnics.append(2)
            elif ethnic in [17, 32]:  # South Asian
                ethnics.append(3)
            elif 18 <= ethnic <= 21 or ethnic == 33:  # East Asian
                ethnics.append(4)
            elif ethnic in [15, 29, 34, 35]:  # African/South American
                ethnics.append(5)
            elif 37 <= ethnic <= 40 or ethnic in [1, 37, 45]:  # Multiple origins
                ethnics.append(6)
            elif ethnic == 36 or 41 <= ethnic <= 44:  # Aboriginal
                ethnics.append(7)
            else:  # invalid values
                ethnics.append(-1)
        else:
            if 1 <= ethnic <= 13 or ethnic in [15, 30, 31, 35, 44]:  # European
                ethnics.append(1)
            elif ethnic == 14 or 17 <= ethnic <= 19:  # Middle Eastern
                ethnics.append(2)
            elif ethnic == 20:  # South Asian
                ethnics.append(3)
            elif ethnic == 45 or 21 <= ethnic <= 24:  # East Asian
                ethnics.append(4)
            elif ethnic in [16, 25, 26, 46]:  # African/South American
                ethnics.append(5)
            elif 32 <= ethnic <= 34 or 36 <= ethnic <= 43 or ethnic in [28, 29, 47]:  # Multiple origin
                ethnics.append(6)
            elif ethnic == 27:  # Aboriginal
                ethnics.append(7)
            else:
                ethnics.append(-1)

    print('Ethnic Origins extracted')

    return ethnics


def extract_citz_stat(loaded_df):
    """
    Extracts the citizenship status of each row. The coded values are the following:
    -1 - Invalid value
    1 - Canadian by Birth
    2 - Canadian by Naturalization
    3 - Other Country
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the citizenship status
    """
    citz_stats = []
    columns = loaded_df.columns
    col_name = ""
    valid_vals = [1, 2, 3]

    print('Extracting Citizenship Status')

    if 'Citizen' in columns:
        col_name = 'Citizen'
    elif 'CITIZEN' in columns:
        col_name = 'CITIZEN'
    elif 'CITIZENP' in columns:
        col_name = 'CITIZENP'
    else:
        print('No Citizenship Status column Detected')
        sys.exit(0)

    citz_stats = [citz_stat if citz_stat in valid_vals else -1 for citz_stat in loaded_df[col_name].tolist()]

    print('Citizenship Status extracted')

    return citz_stats


def extract_imm_stat(loaded_df):
    """
    Extracts the immigration status of each row. The coded values are the following:
    -1 - Invalid value
    1 - Not an immigrant
    2 - Immigrant
    3 - Non-permanent resident
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the immigration status
    """
    imm_stats = []
    columns = loaded_df.columns
    col_name = ""
    num_unique_cols = 0
    valid_vals = [1, 2, 3]

    print('Extracting Immigration Status')

    if 'IMMSTAT' in columns:
        col_name = 'IMMSTAT'
    elif 'IMMPOPP' in columns:
        col_name = 'IMMPOPP'
    else:
        print('No Immigration Status column detected')
        sys.exit()

    temp = loaded_df[col_name]
    num_unique_cols = temp.nunique()

    if num_unique_cols == 4:
        imm_stats = [imm_stat if imm_stat in valid_vals else -1 for imm_stat in temp.tolist()]
    else:
        for imm_stat in temp:
            if imm_stat == 2:  # Non-immigrant
                imm_stats.append(1)
            elif imm_stat == 3:  # Immigrant
                imm_stats.append(2)
            elif imm_stat == 1:  # Non-permanent resident
                imm_stats.append(3)
            else:
                imm_stats.append(-1)

    print('Immigration Status extracted')

    return imm_stats


def extract_prov(loaded_df):
    """
    Extracts the province of each row. The coded values are the following:
    -1 - Invalid value
    1 - Newfoundland
    2 - PEI
    3 - Nova Scotia
    4 - New Brunswick
    5 - Quebec
    6 - Ontario
    7 - Manitoba
    8 - Saskatchewan
    9 - Alberta
    10 - BC
    11 - Territories
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the province
    """
    provs = []
    columns = loaded_df.columns
    col_name = ""

    print('Extracting Provinces')

    if 'PR' in columns:
        col_name = 'PR'
    elif 'PROVP' in columns:
        col_name = 'PROVP'
    else:
        print('No Province column detected')
        sys.exit(0)

    for prov in loaded_df[col_name].tolist():
        if prov == 10:  # Newfoundland
            provs.append(1)
        elif prov == 11:  # PEI
            provs.append(2)
        elif prov == 12:  # Nova Scotia
            provs.append(3)
        elif prov == 13:  # New Brunswick
            provs.append(4)
        elif prov == 24:  # Quebec
            provs.append(5)
        elif prov == 35:  # Ontario
            provs.append(6)
        elif prov == 46:  # Manitoba
            provs.append(7)
        elif prov == 47:  # Saskatchewan
            provs.append(8)
        elif prov == 48:  # Alberta
            provs.append(9)
        elif prov == 59:  # BC
            provs.append(10)
        elif prov == 60 or prov == 70:  # Territories
            provs.append(11)
        else:  # invalid value
            provs.append(-1)

    print('Province extracted')

    return provs


def extract_edu(loaded_df):
    """
    Extracts the highest level of education of each row. The coded values are the following:
    -1 - Invalid value
    0 - Not applicable (sample is under the age of 15)
    1 - No degree
    2 - High School degree
    3 - Certificate or diploma from trades, college, or university
    4 - University bachelor's degree
    5 - Degree above bachelor's (Medical, Veterinarian, Dental)
    6 - Post graduate (Masters, PhD)
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the highest level of education
    """
    edus = []
    columns = loaded_df.columns
    col_name = ""

    print('Extracting Highest Education Level')

    if 'DGREEP' in columns:
        col_name = 'DGREEP'
    elif 'HDGREE' in columns:
        col_name = 'HDGREE'
    else:
        print('No Highest Education Level column detected')
        sys.exit(0)

    for edu in loaded_df[col_name].tolist():
        if col_name == 'DGREEP':
            if edu == 1:
                edus.append(1)
            elif edu == 2:  # high school
                edus.append(2)
            elif 3 <= edu <= 5:  # certificate/diploma
                edus.append(3)
            elif edu == 6:  # bachelor's
                edus.append(4)
            elif edu == 7 or edu == 8:  # above bachelor's
                edus.append(5)
            elif edu == 9 or edu == 10:  # post graduate
                edus.append(6)
            elif edu == 99:  # sample is under 15 years of age
                edus.append(0)
            else:  # invalid value
                edus.append(-1)
        else:
            if edu == 1:
                edus.append(1)
            elif edu == 2:  # high school
                edus.append(2)
            elif 3 <= edu <= 8:  # certificate/diploma
                edus.append(3)
            elif edu == 9:  # bachelor's
                edus.append(4)
            elif edu == 10 or edu == 11:  # above bachelor's
                edus.append(5)
            elif edu == 12 or edu == 13:  # post graduate
                edus.append(6)
            elif edu == 99:  # sample is under 15 years of age
                edus.append(0)
            else:  # invalid value
                edus.append(-1)

    print('Highest Education Level extracted')

    return edus


def extract_emp_stat(loaded_df):
    """
    Extracts the employment status of each row. The coded values are the following:
    -1 - Invalid value
    0 - Not applicable (the sample is under the age of 15)
    1 - Employed
    2 - Unemployed
    3 - Not in workforce
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the employment status
    """
    emp_stats = []
    columns = loaded_df.columns
    col_name = ""

    print('Extracting Employment Status')

    if 'LFACT' in columns:
        col_name = 'LFACT'
    elif 'LFACTP' in columns:
        col_name = 'LFACTP'
    else:
        print('No Employment Status column detected')
        sys.exit(0)

    for emp_stat in loaded_df[col_name].tolist():
        if emp_stat < 3:
            emp_stats.append(1)
        elif emp_stat < 11:
            emp_stats.append(2)
        elif emp_stat <= 14:
            emp_stats.append(3)
        elif emp_stat == 99:
            emp_stats.append(0)
        else:
            emp_stats.append(-1)

    print('Employment Status extracted')

    return emp_stats


def load_file(filename):
    """
    Loads the csv file specified by the filename parameter in the data/raw folder and returns a dataframe with that data
    :param filename: The name of the file to be loaded from the data/raw folder
    :return: A dataframe of the loaded csv file
    """
    path = os.path.dirname(os.path.realpath(__file__)) + '/../../data/raw/' + filename

    if not os.path.exists(path):
        print(f'There is no file name "{filename}" in the data/raw folder.')
        sys.exit(0)

    print(f"Loading file {filename}...")

    chunk_size = 10 ** 6
    loaded_raw = pd.read_csv(path, chunksize=chunk_size)
    loaded_df = pd.concat(loaded_raw, ignore_index=True)

    print("File loaded")

    return loaded_df


def export_file(cleaned_df, export_name):
    """
    Exports the cleaned dataframe as a CSV file to the data/processed folder
    :param cleaned_df: The cleaned dataframe
    :param export_name: The name of the exported file
    :return: None
    """
    path = os.path.dirname(os.path.realpath(__file__)) + '/../../data/processed/' + export_name

    print(f'Exporting to file {export_name}')

    cleaned_df.to_csv(path, index=False)

    print('File exported')


def sanitize(extracted_df):
    """
    Drops all rows that have invalid values
    :param extracted_df: The dataframe generated from the data extracted from the loaded file
    :return: A dataframe with no invalid values
    """
    columns = extracted_df.columns
    cleaned_df = extracted_df.copy()

    print('Removing invalid values')
    print(f'Total values before invalid value removal: {len(extracted_df.index)}')

    for column in columns:
        cleaned_df = cleaned_df[cleaned_df[column] != -1]

    print('Invalid values removed')
    print(f'Total values after invalid value removal: {len(cleaned_df.index)}')

    return cleaned_df


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('You must provide:\n1. The name of the file to be processed\n2. The name of cleaned file')
        sys.exit(0)

    clean(sys.argv[1], sys.argv[2])
