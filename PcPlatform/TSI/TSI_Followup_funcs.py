## MODULE WITH FUNCTIONS TO PERFORM ANALYSIS ON DATA FROM WORK PLAN
#### Author: Rob (GH: Roberto919)
#### Date: 30 June 2020





'------------------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Python libraries

import plotly.figure_factory as ff

from datetime import *


## Ancillary modules

from TSI_Followup_params import *





'------------------------------------------------------------------------------------------'
################
## Functions ##
################


## Counting number of preceding white spaces in a string
def count_spaces(xt):
    """
    Counting number of preceding white spaces in a string
        args:
            xt (string): string whose white spaces will be counted
        returns:
            ct (int): number or preceding white spaces
    """
    ct = 0
    for i in xt:
        if i.isspace():
            ct += 1
        else:
            break

    return ct



## Creating list of 'mother-daughter' activities based on list with spacing hierarchy
def mother_daughter_list(sh_list):
    """
    Creating list of 'mother-daughter' activities based on list with spacing hierarchy
        args:
            sh_list: list that orders the hierarchy of activities with spacings
        returns:
            md_list: list with association of mother-daughter activities
    """

    ## Formula initial parameters
    sep = ' --> '
    spc_o = 0
    tag_dict = {
        0: 'Seed',
    }
    md_list = []

    ## Formulation of mother-daughter list
    for val in sh_list:
        print(val)

        spc_n = count_spaces(val)

        if spc_n > spc_o:

            add = sh_list[sh_list.index(val) - 1]
            tag_dict[spc_n] = add

            spc_o = spc_n

            md_list.append(add.strip() + sep + val.strip())


        elif spc_n <= spc_o:

            md_list.append(tag_dict[spc_n].strip() + sep + val.strip())

            spc_o = spc_n


    return md_list



## Creating dictionary of mother activity and daughter activity/activities
def mother_daughter_dict(md_list):
    """
    Creating dictionary of mother activity and daughter activity/activities
        args:
            md_list (list): list with association of mother-daughter activities
        returns:
            md_dict (dictionary): dictionary with a relation of the mother activity and all of its daughter activities
    """

    md_dict = {}
    for v in md_list:

        v_mother = v.split(sep=' --> ')[0]

        if v_mother not in md_dict:

            md_dict[v_mother] = []


            for v2 in md_list:

                if v2.split(sep=' --> ')[0] == v_mother:

                    md_dict[v_mother].append(v2.split(sep=' --> ')[1])


    return md_dict



## Extracting mother_daughter_dict form dataframe
def extract_md_dict(df):
    """
    Extracting mother_daughter_dict form dataframe
        args:
            df (dataframe): df with all the activities that will be mapped in the md_dict
        returns:
            md_dict (dictionary): dictionary with a relation of the mother activity and all of its daughter activities
    """

    ## Getting list of all activities with hierarchical espaces
    activities = list(df["Nombre de tarea"])

    ## Extracting mother-daughter relation of activities as a list
    md_list = mother_daughter_list(activities)

    ## Extracting mother-daughter relation of activities as a dict
    md_dict = mother_daughter_dict(md_list)


    return md_dict



## Formatting dataframe
def format_df(df):
    """
    Formatting dataframe
        args:
            df (dataframe)
    """


    ## Creating column with cleaned tasks names
    df['Tarea_strip'] = df['Nombre de tarea'].str.strip()


    ## Eliminating non relevant and non identified columns
    n_rc = []
    for col in df.columns:
        if (col not in def_dict):
            n_rc.append(col)
        else:
            if def_dict[col]['relevant'] == False:
                n_rc.append(col)

    df.drop(n_rc, inplace=True, axis=1)


    ## Changing "% completado" column to a 100 base
    df['% completado'] = df['% completado']*100


    ## Adding time to tasks
    df.loc[:, 'Comienzo.1'] = df['Comienzo.1'].apply(lambda x: datetime(x.year, x.month, x.day, 1, 1))
    df.loc[:, 'Fin.1'] = df['Fin.1'].apply(lambda x: datetime(x.year, x.month, x.day, 23, 59))


    return df



## Creating dictionary of dataframes filtered based on mother_daughter_dict
def mother_daughter_dfs(md_dict, df):
    """
    Creating dictionary of dataframes filtered based on mother_daughter_dict
        args:
            md_dict (dictionary): dictionary with a relation of the mother activity and all of its daughter activities
        returns:
            md_dfs (dictionary): dictionary of dataframes filtered based on mother_daughter_dict
    """

    md_dfs = {}
    for key in md_dict:
        m1 = df['Tarea_strip'].isin(md_dict[key])
        md_dfs[key] = df.loc[m1, :]

    return md_dfs



## Create Gantt chart based on dataframe
def gantt_chart(md_dfs, mother_task):
    """
    Create Gantt chart based on dataframe
        args:
            md_dfs (dictionary): dictionary of dataframes filtered based on mother_daughter_dict
            mother_task (string): name of the mother task that will be explored with the gantt chart
        returns:
            - (print figure)
    """


    ## Selecting dataframe that will be converted into a gantt chart
    df = md_dfs[mother_task]


    ## Columns that will be considered and renamed for the gantt chart
    rename_gant = []
    for def_col in def_dict:
        if (def_dict[def_col]['relevant']) & ('gantt_name' in def_dict[def_col]):
            rename_gant.append(def_col)


    ## Eliminating columns not relevant for gantt chart and renaming relevant columns
    for col in df.columns:

        if col not in rename_gant:
            df.drop(col, inplace=True, axis=1)
        else:
            df.rename(columns={col: def_dict[col]['gantt_name']}, inplace=True)


    ## Creating gantt chart
    fig = ff.create_gantt(
                df,
                colors=['#333F44', '#93e4c1'],
                index_col='Complete',
                show_colorbar=True,
                bar_width=0.2,
                showgrid_x=True,
                showgrid_y=True,
                title=mother_task
                )
    fig.show()


    return
