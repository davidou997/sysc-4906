import sys
import os
import pandas as pd


def clean(filename):
    loaded = load_file(filename)
    cleaned_dict = {
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

    cleaned_dict['WEIGHT'] = extract_weight(loaded)
    cleaned_dict['AGE'] = extract_age(loaded)
    cleaned_dict['SEX'] = extract_sex(loaded)
    cleaned_dict['MART_STAT'] = extract_sex(loaded)
    cleaned_dict['HOUS_INC'] = extract_house_income(loaded)
    cleaned_dict['HOUS_SIZ'] = extract_house_size(loaded)
    cleaned_dict['IND_INC'] = extract_house_size(loaded)
    cleaned_dict['OFF_LANG'] = extract_official_lang(loaded)
    print(len(cleaned_dict['WEIGHT']))
    print(len(cleaned_dict['AGE']))
    print(len(cleaned_dict['SEX']))
    print(len(cleaned_dict['MART_STAT']))
    print(len(cleaned_dict['HOUS_INC']))
    print(len(cleaned_dict['HOUS_SIZ']))
    print(len(cleaned_dict['IND_INC']))
    print(len(cleaned_dict['OFF_LANG']))
    print(f'total size: {len(loaded.index)}')


def extract_weight(loaded_df):
    """
    Extracts the weights of each row.
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the weights of each row
    """
    weights = []
    columns = loaded_df.columns
    col_name = ""

    if "WEIGHTP" in columns:
        col_name += "WEIGHTP"
    elif "WEIGHT" in columns:
        col_name += "WEIGHT"
    else:
        print("No Age Column Detected")
        sys.exit(0)

    weights = loaded_df[col_name].tolist()
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

    if "AGEGRP" in columns:
        col_name += "AGEGRP"
    elif "AGE" in columns:
        col_name += "AGE"
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

    return ages


def extract_sex(loaded_df):
    """
    Extracts the sex of each row. The coded values are as follows:
    1 -  Male
    2 - Female
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the sex values
    """
    sexes = []
    columns = loaded_df.columns
    col_name = ""

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

    return mart_stats


def extract_house_income(loaded_df):
    """
    Extracts the household income of each row. The coded values are the following:
    -1 - Invalid value
    1 - Less than 25k
    2 - 25k to 49,999
    3 - 50k to 74,999
    4 - 75k to 99,999
    5 - Over 100k
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the household income
    """
    hous_incs = []
    columns = loaded_df.columns
    col_name = ""

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
    return hous_sizes


def extract_ind_income(loaded_df):
    """
    Extracts the individual income of each row. The coded values are the following:
    -1 - Invalid value
    1 - Less than 0 (net loss)
    2 - 0 to 24,999
    3 - 25k to 49,999
    4 - 50k to 74,999
    5 - 75k to 99,999
    6 - Over 100k
    7 - Not applicable (the person is under 15 years of age)
    :param loaded_df: The dataframe loaded from the file
    :return: A list containing the new values of the individual income
    """
    ind_incs = []
    columns = loaded_df.columns
    col_name = ""
    max_val = 0

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
            ind_incs.append(7)
        else:  # invalid value
            ind_incs.append(-1)
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

    return off_langs


def extract_home_lang(loaded_df):
    # TODO
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
    home_langs = []
    columns = loaded_df.columns
    col_name = ""

    return home_langs


def extract_pob():
    # TODO
    pobs = []

    return pobs


def extract_ethnic():
    # TODO
    ethnics = []

    return ethnics


def extract_citz_stat():
    # TODO
    citz_stats = []

    return citz_stats


def extract_imm_stat():
    # TODO
    imm_stats = []

    return imm_stats


def extract_prov():
    # TODO
    provs = []

    return provs


def extract_edu():
    # TODO
    edus = []

    return edus


def extract_emp_stat():
    # TODO
    emp_stats = []

    return emp_stats


def load_file(filename):
    """
    Loads the csv file specified by the filename parameter in the data/raw folder and returns a dataframe with that data
    :param filename: The name of the file to be loaded from the data/raw folder
    :return: A dataframe of the loaded csv file
    """
    path = os.path.dirname(os.path.realpath(__file__)) + '\\..\\..\\data\\raw\\' + filename
    if not os.path.exists(path):
        print(f'There is no file name "{filename}" in the data/raw folder.')
        sys.exit(0)

    print(f"Loading file {filename}...")

    chunk_size = 10 ** 6
    loaded_raw = pd.read_csv(path, chunksize=chunk_size)
    loaded_df = pd.concat(loaded_raw, ignore_index=True)

    print("File loaded")

    return loaded_df


def sanitize(extracted_df):
    # TODO
    print('extract')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('You must provide a filename.')
        sys.exit(0)

    clean(sys.argv[1])
