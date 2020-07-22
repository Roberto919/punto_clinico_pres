## ANALYZING TELEMEDICINE SURVEY RESULTS - FUNCTIONS FILE
#### Author: Rob (GH: Roberto919)
#### Date: 21 July 2020





'------------------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Python libraries

import pandas as pd


## Ancillary modules

from TelemedSurvey_params import *





'------------------------------------------------------------------------------------------'
#######################
## Generic functions ##
#######################


## Determine difference in years between two dates
def difference_between_years(row):
    """
    Determine difference in years between two dates
    """
    res = relativedelta(datetime.now(), row).years
    return res





'------------------------------------------------------------------------------------------'
##############################
## Imported data processing ##
##############################


## Cleaning imported dataset
def clean_raw_dataset(df):
    """
    Cleaning imported dataset
    """


    ## Adding first two numbers to year in order to complete date
    """
    Adding first two numbers to year in order to complete date
    """
    def fix_date(row):

        if row == '0':
            return '01/01/1900'

        year = int(row.split(sep='/')[2])

        if year > 10 & year < 99:
            fix = '19' + row[-2:]
            res = row[:-2] + fix
        else:
            fix = '20' + row[-2:]
            res = row[:-2] + fix

        return res


    ##


    ## Eliminating non relevant columns
    nrc = [nrc for nrc in df.columns if nrc not in simp_rcol_names]
    df.drop(nrc, axis=1, inplace=True)


    ## Simplifying column names
    df.rename(columns=simp_rcol_names, inplace=True)


    ## Adding column with serial number
    df.insert(0, '#', range(1, df.shape[0] + 1))


    ## Cleaning dirty columns
    df['Ha considerado ofrecer teleconsulta?'] = df['Ha considerado ofrecer teleconsulta?'].apply(lambda x: 'NO' if x == 'No' else x)
    df['Cuenta con plataforma de gestión?'] = df['Cuenta con plataforma de gestión?'].apply(lambda x: 'NO' if x == 'No' else x)
    df['Cuenta con plataforma de teleconsultas?'] = df['Cuenta con plataforma de teleconsultas?'].apply(lambda x: 'NO' if x == 'No' else x)


    return df




'------------------------------------------------------------------------------------------'
######################################################################
## Analysis 1 - Have you considered offering a telemedicine service ##
######################################################################


## Preparing dataset
