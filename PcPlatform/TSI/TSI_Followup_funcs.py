## MODULE WITH FUNCTIONS TO PERFORM ANALYSIS ON DATA FROM WORK PLAN
#### Author: Rob (GH: Roberto919)
#### Date: 30 June 2020





'------------------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Python libraries

import plotly.figure_factory as ff
import plotly.express as px

from datetime import *

import json

import pprint as pp


## Ancillary modules

from TSI_Followup_params import *





'------------------------------------------------------------------------------------------'
################
## Functions ##
################


## Pretty print a dictionary and preserving special characters
def json_dump_dict(dictionary):
    """
    Pretty print a dictionary and preserving special characters
        args:
            dictionary (dictionary): dict that will be pretty printed
        returns:
            -
    """

    print(json.dumps(dictionary, indent=4, ensure_ascii=False).encode("utf8").decode())

    return



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
        # print(val)

        spc_n = count_spaces(val)

        if spc_n > spc_o:

            add = sh_list[sh_list.index(val) - 1]
            tag_dict[spc_n] = add

            spc_o = spc_n

            md_list.append(add.strip() + sep + val.strip())


        elif spc_n <= spc_o:

            md_list.append(tag_dict[spc_n].strip() + sep + val.strip())

            spc_o = spc_n

    # pp.pprint(tag_dict)

    # pp.pprint(md_list)


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


    ## Append column with mother-daughter tasks names.
    df["md_names"] = md_list


    ## Reviewing if the new column has only unique values
    rev = df["md_names"].value_counts()
    if len(rev[rev != 1]) == 0:
        print("All mother-daughter names are unique")
    else:
        print("Problem with the mother-daughter: not all are unique")


    ## Extracting mother-daughter relation of activities as a dict
    md_dict = mother_daughter_dict(md_list)


    return md_dict, df



## Formatting dataframe
def format_df(df, version='TSI'):
    """
    Formatting dataframe
        args:
            df (dataframe): df that will be cleaned to leave only columns for the Gantt chart
            version (string): specification of the type of document that will be processed
                options:
                    - "TSI": Advancements according to the provider
                    - "Rob": Review of advancements according to Rob
        returns:
            df (dataframe): cleaned df
    """


    ## Creating column with cleaned tasks names
    df['Tarea_strip'] = df['Nombre de tarea'].str.strip()


    ## Eliminating tasks that don't have a start or end date
    m1 = df['Comienzo.1'].notnull()
    m2 = df['Fin.1'].notnull()
    df = df.loc[(m1 & m2), :]


    ## Adding time to tasks
    df.loc[:, 'Comienzo.1'] = df['Comienzo.1'].apply(lambda x: datetime(x.year, x.month, x.day, 1, 1))
    df.loc[:, 'Fin.1'] = df['Fin.1'].apply(lambda x: datetime(x.year, x.month, x.day, 23, 59))


    ## Eliminating non relevant and non identified columns
    n_rc = []
    for col in df.columns:
        if (col not in def_dict):
            n_rc.append(col)
        else:
            if def_dict[col]['relevant'] == False:
                n_rc.append(col)

    if version=="TSI":
        n_rc.append("RevRob")
        ## Changing "% completado" column to a 100 base
        df['% completado'] = df['% completado']*100
    elif version=="Rob":
        ## Adding column with Rob's review status
        df['RevRobf'] = df['Fin.1'].apply(lambda x: "Atrasada" if x < datetime.now() else "Pendiente")
        m1 = df['% completado'] == 1
        df.loc[m1, 'RevRobf'] = "Terminada"
        m1 = df['RevRob'] == 1
        df.loc[m1, 'RevRobf'] = "Validada"

        n_rc.append("% completado")
        n_rc += ["% completado", "RevRob"]
    else:
        raise NameError('Invalid document')

    df.drop(n_rc, inplace=True, axis=1)


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
def gantt_chart_deprecated(md_dfs, mother_task):
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



## Create Gantt chart based on dataframe
def gantt_chart(md_dfs, mother_task, version="TSI"):
    """
    Create Gantt chart based on dataframe
        args:
            md_dfs (dictionary): dictionary of dataframes filtered based on mother_daughter_dict
            mother_task (string): name of the mother task that will be explored with the gantt chart
            version (string): specification of the type of document that will be processed
                options:
                    - "TSI": Advancements according to the provider
                    - "Rob": Review of advancements according to Rob
        returns:
            - (printed figure)
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


    ## Creating figure depending on the document
    if version == "TSI":
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
    elif version=="Rob":
        ## Creating gantt chart
        fig = px.timeline(
            df,
            y="Task",
            x_start="Start",
            x_end="Finish",
            color="Complete",
            color_discrete_map={
                "Atrasada": "red",
                "Pendiente": "orange",
                "Terminada": "blue",
                "Validada": "green"
            }
        )
        fig.show()


    return



## Print dictionary of all activities based on md_dict
def followup_dict(df):
    """
    Print dictionary of all activities based on md_dict
        args:
            df (dataframe): df with all the info to update dictionary.
        returns:
            res_dict (dictionary): relation of mother-daughter tasks with followup contents.
    """


    ## Copying and adjusting dataframe to leave only relevant information.
    dfx = df.copy()
    dfx.set_index("md_names", inplace=True)
    # dfx.drop(["Comienzo", "Fin", "Comienzo.1", "Fin.1", "Predecesoras", "Nombre de tarea", "Duración", "% completado"], axis=1, inplace=True)
    dfx = dfx.loc[:, ["No.", "RevRob", "Notas_Rob"]]


    ## Creating dictionary with definitions.
    res_dict = dfx.to_dict(orient="index")

    # pp.pprint(res_dict)


    ## Printing json
    json_dump_dict(res_dict)


    # return res_dict
