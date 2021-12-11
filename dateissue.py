
from main import Redash
import pandas as pd


def datetime_column(df, column):
    df[column] = pd.to_datetime(df[column])
    df['month_'+column] = df[column].dt.month
    df['year_'+column] = df[column].dt.year
    return df


def write_excel(df, filename):
    file_name = 'C:/Users/asus/PycharmProjects/untitled2/' + filename + '.xlsx'
    df.to_excel(file_name)
    return 0


def date_issue_sol(table, columns):
    df = pd.DataFrame(table)
    for column in columns:
        df = datetime_column(df, column)
        df = datetime_column(df, column)
        df[column] = df[column].dt.tz_localize(None)
    write_excel(df, 'DateIssueSol')
    return 'DataFrame is written to Excel File successfully.'


redash = Redash(redash_url='http://51.178.128.212:8080', api_key='DLO2Fz3i8ETRpvrG4GnTx6t6Z5RrsXEhY9PD7Pl2')
api_key = 'DLO2Fz3i8ETRpvrG4GnTx6t6Z5RrsXEhY9PD7Pl2'
chainproduct = redash.get_fresh_query_result(309, api_key)
date_issue_sol(chainproduct, ['created', 'updated'])
