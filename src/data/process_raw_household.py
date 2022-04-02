import pandas as pd
import os


def read_file():
    """
    Reads the CSV file taken from the following document: "Household Total Income Groups (22) in Constant (2015)
    Dollars, Household Type Including Census Family Structure (11), Household Size (7), Ages of Household Members (
    18), Number of Earners in the Household (6) and Year (2) for Private Households of Canada, Provinces and
    Territories, Census Metropolitan Areas and Census Agglomerations, 2006 Census - 20% Sample Data and 2016 Census -
    100% Data"

    :return: None
    """
    chunk_size = 10 ** 6
    print("Reading...")
    curr_path = os.path.dirname(__file__) + '\\..\\..\\data\\raw\\'
    raw = pd.read_csv(curr_path + '98-400-X2016097_English_CSV_data.csv', chunksize=chunk_size)
    print("Converting to Dataframe...")
    df = pd.concat(raw, ignore_index=True)
    return df


def get_canada_rows_raw(df):
    """
    Retreives all rows containing "Canada" as the geolocation
    :param df: The raw dataframe
    :return: A dataframe with "Canada" geolocation only
    """
    canada_only = df[df['GEO_NAME'].str.contains('Canada')]

    return canada_only


def filter_canada(canada_only):
    """
    Cleans the data and gives the columns new column names to be more readable. Separates the total and singular
    categories inside the 'DIM: Ages of household members (18)' column.
    :param canada_only: A dataframe with "Canada" geolocation only
    :return: None
    """
    print("Filtering Canada...")
    canada_filtered = pd.DataFrame()
    age_range_categories = ['0 to 5 years', '0 to 17 years', '65 years and over']
    canada_filtered["Household Type"] = canada_only["DIM: Household type including census family structure (11)"]
    canada_filtered["Household Size"] = canada_only["DIM: Household size (7)"]

    beginning = "Total - Households by number of persons aged "
    age_range_category_column = []
    category_index = 0
    category_next_index = category_index + 1
    category_curr_str = beginning + age_range_categories[category_index]
    category_next_str = beginning + age_range_categories[category_next_index]
    for index in range(len(canada_only.index)):
        curr_cat = canada_only.at[index, 'DIM: Ages of household members (18)']
        if not curr_cat == category_next_str:
            age_range_category_column.append(category_curr_str)
        else:
            age_range_category_column.append(category_next_str)

            category_count = len(age_range_categories)

            category_index += 1
            if category_index >= category_count:
                category_index = 0

            category_next_index = category_index + 1
            if category_next_index >= category_count:
                category_next_index = 0

            category_curr_str = beginning + age_range_categories[category_index]
            category_next_str = beginning + age_range_categories[category_next_index]

    canada_filtered["Ages Range Category"] = age_range_category_column
    canada_filtered["Number of Household Members in Age Range Category"] = canada_only[
        "DIM: Ages of household members (18)"]
    canada_filtered["Number of Earners in Household"] = canada_only["DIM: Number of earners in the household (6)"]
    canada_filtered["Household Income"] = canada_only["DIM: Household total income groups (22)"]
    canada_filtered["Value in 2015"] = canada_only["Dim: Year (2): Member ID: [1]: 2015 (Note: 4)"]
    canada_filtered["Value in 2005"] = canada_only["Dim: Year (2): Member ID: [2]: 2005 (Note: 5)"]

    canada_filtered = canada_filtered[~canada_filtered['Number of Earners in Household'].str.contains('1 earner or more')]
    return canada_filtered


def separate_totals(canada_filtered):
    """
    Separates the filtered file into a file containing all the totals and a file without the totals
    :param canada_filtered: A dataframe that has been filtered and renamed columns
    :return: A dataframe with no total information and a dictionary with dataframes that each are organized by a total
    """
    print("Removing Totals")
    total_str = "Total"
    median_str = "Median"
    columns = ['Household Type', 'Household Size', 'Number of Household Members in Age Range Category',
               'Number of Earners in Household', 'Household Income']
    no_total = canada_filtered
    by_totals = {}
    for column in columns:
        no_total = no_total[~no_total[column].str.contains(total_str)]
        no_total = no_total[~no_total[column].str.contains(median_str)]
        by_totals[column] = canada_filtered.copy(deep=True)
        by_totals[column] = by_totals[column][by_totals[column][column].str.contains(total_str)]

    return no_total, by_totals


def read_no_totals():
    path = os.path.dirname(__file__) + '\\..\\..\\data\\processed\\Canada - Processed, No Totals.csv'
    chunk_size = 10 ** 6
    no_totals_raw = pd.read_csv(path, chunksize=chunk_size)
    no_totals = pd.concat(no_totals_raw, ignore_index=True)
    # household_types = no_totals['Household Type'].unique()
    ages_range_types = no_totals['Ages Range Category'].unique()

    # print(len(household_types) * len(ages_range_types))

    census_families = no_totals[no_totals['Household Type'].str.contains('Census family households')]
    for ages_range_type in ages_range_types:
        temp = census_families[census_families['Ages Range Category'].str.contains(ages_range_type)]
        row = temp[temp['Value in 2015'] == temp['Value in 2015'].max()]
        print(row)


if __name__ == "__main__":
    # raw_df = read_file()  # Get Raw
    # canada_raw = get_canada_rows_raw(raw_df)  # Remove non-Canada totals
    # canada_filter = filter_canada(canada_raw)
    # no_totals, by_totals = separate_totals(canada_filter)
    #
    # path = os.path.dirname(__file__) + '\\..\\..\\data\\processed\\'
    #
    # no_totals.to_csv(path + "Canada - Processed, No Totals.csv")
    # for key in by_totals.keys():
    #     by_totals[key].to_csv(path + "Canada - Processed, Totals of " + key + ".csv")
    read_no_totals()
