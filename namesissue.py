from main import Redash
import pandas as pd
import numpy as np
from collections import Counter


def write_excel(df, filename):
    file_name = 'C:/Users/asus/PycharmProjects/untitled2/' + filename + '.xlsx'
    df.to_excel(file_name)
    return 0


def name_issue_sol(table, columns, chaine):
    df = pd.DataFrame(table)
    for column in columns:
        df['newcol'] = np.where(df[column].apply(lambda x: chaine in x), 1, 0)
    write_excel(df, 'NameIssueSol')
    message = 'DataFrame is written to Excel File successfully.'
    write_excel(df, 'NameIssueSol')
    return message


def name2_issue_sol(table, columns):
    df = pd.DataFrame(table)
    l = []
    for column in columns:
        for i in range(len(df)):
            url = df[column][i].split('.')
            site = url[1]
            l.append(site)
    write_excel(df, 'Name2IssueSol')
    return Counter(l).most_common(10)


redash = Redash(redash_url='http://51.178.128.212:8080', api_key='DLO2Fz3i8ETRpvrG4GnTx6t6Z5RrsXEhY9PD7Pl2')
api_key = 'DLO2Fz3i8ETRpvrG4GnTx6t6Z5RrsXEhY9PD7Pl2'

chainproduct_name = redash.get_fresh_query_result(310, api_key)
name_issue_sol(chainproduct_name, ['name'], 'Michelin')

chainproduct_image_url = redash.get_fresh_query_result(311, api_key)
name2_issue_sol(chainproduct_image_url, ['image_url'])
