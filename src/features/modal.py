import math
import os
import pandas as pd
import matplotlib.pyplot as plt

filename_2016 = 'PUMF_2016_clean.csv'
filename_2006 = 'PUMF_2006_clean.csv'
filename_2001 = 'PUMF_2001_clean.csv'
filename_1996 = 'PUMF_1996_clean.csv'
path_base = os.path.dirname(os.path.realpath(__file__)) + '/../../data/processed/'


def load_data():
    filename_2016 = 'PUMF_2016_clean.csv'
    filename_2006 = 'PUMF_2006_clean.csv'
    filename_2001 = 'PUMF_2001_clean.csv'
    filename_1996 = 'PUMF_1996_clean.csv'
    path_base = os.path.dirname(os.path.realpath(__file__)) + '/../../data/processed/'
    chunk_size = 10 ** 6

    cleaned_2016 = pd.concat(pd.read_csv(path_base + filename_2016, chunksize=chunk_size), ignore_index=True)
    cleaned_2006 = pd.concat(pd.read_csv(path_base + filename_2006, chunksize=chunk_size), ignore_index=True)
    cleaned_2001 = pd.concat(pd.read_csv(path_base + filename_2001, chunksize=chunk_size), ignore_index=True)
    cleaned_1996 = pd.concat(pd.read_csv(path_base + filename_1996, chunksize=chunk_size), ignore_index=True)

    return {
        '1996': cleaned_1996,
        '2001': cleaned_2001,
        '2006': cleaned_2006,
        '2016': cleaned_2016
    }


def top_modals(cleaned_df):
    columns = cleaned_df.drop(columns=['WEIGHT']).columns.tolist()
    top = cleaned_df.groupby(columns).size().reset_index(name='Count').sort_values('Count', ascending=False).head(1)

    return top


def top_modals_over_20(cleaned_df):
    columns = cleaned_df.drop(columns=['WEIGHT']).columns.tolist()
    over_20 = cleaned_df[cleaned_df['AGE'] >= 3]
    top = over_20.groupby(columns).size().reset_index(name='Count').sort_values('Count', ascending=False).head(1)

    return top


def top_modals_working(cleaned_df):
    columns = cleaned_df.drop(columns=['WEIGHT']).columns.tolist()
    working = cleaned_df[(cleaned_df['AGE'] >= 3) & (cleaned_df['AGE'] <= 6)]
    top = working.groupby(columns).size().reset_index(name='Count').sort_values('Count', ascending=False).head(1)

    return top


def top_modals_imm(cleaned_df):
    columns = cleaned_df.drop(columns=['WEIGHT']).columns.tolist()
    imm = cleaned_df[cleaned_df['IMM_STAT'] != 1]
    top = imm.groupby(columns).size().reset_index(name='Count').sort_values('Count', ascending=False).head(1)
    return top


def top_modals_over_20_imm(cleaned_df):
    columns = cleaned_df.drop(columns=['WEIGHT']).columns.tolist()
    over_20 = cleaned_df[cleaned_df['AGE'] >= 3]
    imm = over_20[over_20['IMM_STAT'] != 1]
    top = imm.groupby(columns).size().reset_index(name='Count').sort_values('Count', ascending=False).head(1)
    return top


def top_modals_working_imm(cleaned_df):
    columns = cleaned_df.drop(columns=['WEIGHT']).columns.tolist()
    working = cleaned_df[(cleaned_df['AGE'] >= 3) & (cleaned_df['AGE'] <= 6)]
    imm = working[working['IMM_STAT'] != 1]
    top = imm.groupby(columns).size().reset_index(name='Count').sort_values('Count', ascending=False).head(1)
    # print(top3)
    # plottest(top3)
    return top


def top_modals_non_imm(cleaned_df):
    columns = cleaned_df.drop(columns=['WEIGHT']).columns.tolist()
    imm = cleaned_df[cleaned_df['IMM_STAT'] == 1]
    top = imm.groupby(columns).size().reset_index(name='Count').sort_values('Count', ascending=False).head(1)

    return top


def top_modals_over_20_non_imm(cleaned_df):
    columns = cleaned_df.drop(columns=['WEIGHT']).columns.tolist()
    over_20 = cleaned_df[cleaned_df['AGE'] >= 3]
    imm = over_20[over_20['IMM_STAT'] == 1]
    top = imm.groupby(columns).size().reset_index(name='Count').sort_values('Count', ascending=False).head(1)

    return top


def top_modals_working_non_imm(cleaned_df):
    columns = cleaned_df.drop(columns=['WEIGHT']).columns.tolist()
    working = cleaned_df[(cleaned_df['AGE'] >= 3) & (cleaned_df['AGE'] <= 6)]
    imm = working[working['IMM_STAT'] == 1]
    top = imm.groupby(columns).size().reset_index(name='Count').sort_values('Count', ascending=False).head(1)

    return top


def export(df, filename):
    df.to_csv(path_base + filename, index=False)


def eduvsinc(df):
    temp = {
        "EDU": df['HIGH_EDU'],
        "INC": df['IND_INC']
    }
    df_temp = pd.DataFrame.from_dict(temp)
    df_temp.plot.scatter(x="EDU", y="INC")
    plt.show()


def vis_ind_inc(df, title):

    yticks = range(0, df['IND_INC'].max() + 1)
    df.plot(x="YEAR", y="IND_INC", title=title,kind='bar',xlabel='Year',ylabel='Individual Income Code',yticks=yticks)
    plt.tight_layout()
    plt.show()


def main():
    cleaned = load_data()
    modals = {}
    modals_over_20 = {}
    modals_working = {}
    modals_imm = {}
    modals_over_20_imm = {}
    modals_working_imm = {}
    modals_non_imm = {}
    modals_over_20_non_imm = {}
    modals_working_non_imm = {}
    for key in cleaned.keys():
        modals[key] = top_modals(cleaned[key])
        modals_over_20[key] = top_modals_over_20(cleaned[key])
        modals_working[key] = top_modals_working(cleaned[key])
        modals_imm[key] = top_modals_imm(cleaned[key])
        modals_over_20_imm[key] = top_modals_over_20_imm(cleaned[key])
        modals_working_imm[key] = top_modals_working_imm(cleaned[key])
        modals_non_imm[key] = top_modals_non_imm(cleaned[key])
        modals_over_20_non_imm[key] = top_modals_over_20_non_imm(cleaned[key])
        modals_working_non_imm[key] = top_modals_working_non_imm(cleaned[key])

    parts = {
        'REG': {
            'REG': modals,
            'OVER20': modals_over_20,
            'WORKING': modals_working
        },
        'IMM': {
            'REG': modals_imm,
            'OVER20': modals_over_20_imm,
            'WORKING': modals_working_imm
        },
        'NONIMM': {
            'REG': modals_non_imm,
            'OVER20': modals_over_20_non_imm,
            'WORKING': modals_working_non_imm
        }
    }

    combined = {}

    for key in parts.keys():
        part = parts[key]
        for type in part.keys():
            cat = part[type]
            combined_arr = []
            for year in cat.keys():
                df = cat[year]
                df['YEAR'] = [year]
                combined_arr.append(df)
            combined_df = pd.concat(combined_arr)
            combined[key + type] = combined_df
            export(combined_df, key+type+'.csv')

    for key in combined.keys():
        title = 'Individual Income - '
        if "REG" in key[:3]:
            title += 'Overall'
        elif "IMM" in key[:3]:
            title += 'Immigrants'
        elif "NON" in key[:3]:
            title += 'Non-immigrants'

        if "REG" in key[3:]:
            title += ' (All samples)'
        elif "OVER20" in key[3:]:
            title += ' (Over Age 20)'
        elif "WORKING" in key[3:]:
            title += ' (Working Age)'
        vis_ind_inc(combined[key], title)


if __name__ == "__main__":
    main()
