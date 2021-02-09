## MODULE WITH FUNCTIONS USED FOR THE ANALYSIS





"-------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Standard library imports


## Third party imports

import Levenshtein


## Local application imports

from utils.catalog_completion_params import (
    pres_types
)





"-------------------------------------------------------------------------------"
#########################
## Ancillary functions ##
#########################


## Calculating relative levenshtein distances
def rel_leveshtein(txt1, txt2):
    """
    """

    return (1 - Levenshtein.distance(txt1, txt2)/len(txt1))



## Filling information about the medicine contents
def fill_meds_info(row):
    """
    """

    if (row["pres_type"] in pres_types) & (row["idm"] != -1):

        # print(row["medicamento"])

        if isinstance(pres_types[row["pres_type"]]["pres"], str) == False:

            if row["pres_dims_gen"] in pres_types[row["pres_type"]]["pres"]:
                res = pres_types[row["pres_type"]]["pres"][row["pres_dims_gen"]].format(row["pres_dims"], pres_types[row["pres_type"]]["name"])

            else:
                res = pres_types[row["pres_type"]]["pres"]["others"].format(pres_types[row["pres_type"]]["name"], row["pres_dims"])

        elif pres_types[row["pres_type"]]["pres_txt"] == "name-num":
            res = pres_types[row["pres_type"]]["pres"].format(pres_types[row["pres_type"]]["name"], row["pres_dims"])

        else:
            res = pres_types[row["pres_type"]]["pres"].format(row["pres_dims"], pres_types[row["pres_type"]]["name"])

    else:
        res = "no_success"

    return res



## Specifying how the medicine is administered
def fill_meds_adm(row):
    """
    """

    if (row["pres_type"] in pres_types) & (row["idm"] != -1):

        res = pres_types[row["pres_type"]]["adm"]

    else:
        res = "TBD"

    return res
