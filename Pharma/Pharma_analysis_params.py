## ANALYSIS OF DRUG SELLING OPPORTUNITIES - PARAMETERS FILE
#### Author: Rob (GH: Roberto919)
#### Date: 9 July 2020





'------------------------------------------------------------------------------------------'
#############
## Imports ##
#############

from datetime import *





'------------------------------------------------------------------------------------------'
################
## Parameters ##
################


## Metmorfina pricing

metmorfina_pricing = {
    'Walmart': { #### (850 [mg] - 30 [tablets]) [https://super.walmart.com.mx/medicamentos-de-patente/metformina-medimart-850-mg-30-tabletas/00750222629370]
        p1: 50,
        p1_a: 50
    },
    'Farmacias_del_ahorro': { #### (850 [mg] - 60 [tablets]) [https://super.walmart.com.mx/medicamentos-de-patente/metformina-medimart-850-mg-30-tabletas/00750222629370]
        p1: 158,
        p1_a: 158/2
    },
    'Farmacias_san_pablo': { #### (850 [mg] - 60 [tablets]) [https://www.farmaciasanpablo.com.mx/medicamentos/genericos/m---n---o---p/metformina-850-mg/p/000000000060090039]
        p1: 104.5,
        p1_a: 104.5/2
    },
}
