## ANALYZING TELEMEDICINE SURVEY RESULTS - MAIN FILE
#### Author: Rob (GH: Roberto919)
#### Date: 21 July 2020





'------------------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Python libraries

import pandas as pd

import numpy as np

import pprint as pp

from datetime import *
from dateutil.relativedelta import relativedelta

from statistics import median, mean

import os

import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff

import dash
import dash_core_components as dcc
import dash_html_components as html


## Ancillary modules

from TelemedSurvey_params import *
from TelemedSurvey_funcs import *
from TelemedSurvey_app import *





'------------------------------------------------------------------------------------------'
#################
## Main script ##
#################


def main_script_func():


    #### Executing dashboard
    dashboard_layout_new()





'------------------------------------------------------------------------------------------'
###########################
## Executing main script ##
###########################

if __name__ == '__main__':
    main_script_func()
