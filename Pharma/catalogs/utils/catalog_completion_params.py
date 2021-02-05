## MODULE WITH PARAMTERES FOR MEDICINE CATALOG





## Similarity teshold for review
lev_low_tr = 0.5
lev_high_tr = 0.65





## LIST OF THE DIFFERENT TYPES OF PRESENTATIONS
pres_types = {
    "TAB": {
        "name": "tableta(s)",
        "pres": "presentación con {} {}",
        "adm": "Oral",
        "pres_txt": "num-name"
    },
    "CAP": {
        "name": "capsula(s)",
        "pres": "presentación con {} {}",
        "adm": "Oral",
        "pres_txt": "num-name"
    },
    "PZA": {
        "name": "pieza(s)",
        "pres": {
            "#": "{} {}",
            "others": "{} de {}"
        },
        "adm": "TBD"
    },
    "CRE": {
        "name": "crema en presentación",
        "pres": "{} de {}",
        "adm": "TBD",
        "pres_txt": "name-num"
    },
    "SOL": {
        "name": "solución(es)",
        "pres": "{} de {}",
        "adm": "TBD",
        "pres_txt": "name-num"
    },
    "TUB": {
        "name": "tubo(s)",
        "pres": "{} de {}",
        "adm": "TBD",
        "pres_txt": "name-num"
    },
    "COM": {
        "name": "comprimido(s)",
        "pres": "presentación con {} {}",
        "adm": "TBD",
        "pres_txt": "num-name"
    },
    "GEL": {
        "name": "gel(es)",
        "pres": {
            "#": "{} {}",
            "others": "{} en presentación de {}"
        },
        "adm": "TBD",
    },
    "BOT": {
        "name": "bote(s)",
        "pres": {
            "#": "{} {}",
            "others": "{} de {}"
        },
        "adm": "TBD",
    },
    "SOB": {
        "name": "sobre(s)",
        "pres": {
            "#": "{} {}",
            "others": "{} de {}"
        },
        "adm": "Oral",
    },
    "SUS": {
        "name": "suspensión(es)",
        "pres": {
            "#": "{} {}",
            "others": "{} de {}"
        },
        "adm": "TBD",
    },
    "FRA": {
        "name": "frasco",
        "pres": "{} de {}",
        "adm": "TBD",
        "pres_txt": "name-num"
    },
    "AMP": {
        "name": "ampolleta(s)",
        "pres": {
            "#": "{} {}",
            "others": "{} de {}"
        },
        "adm": "TBD",
    },
    "GRA": {
        "name": "grageas",
        "pres": "{} {}",
        "adm": "TBD",
        "pres_txt": "num-name"
    },
    "GOT": {
        "name": "gotero",
        "pres": "{} de {}",
        "adm": "TBD",
        "pres_txt": "name-num"
    },
    "CAJ": {
        "name": "caja",
        "pres": "{} con {} unidad(es)",
        "pres_txt": "name-num",
        "adm": "TBD",
    },
    "BLI": {
        "name": "blister(s)",
        "pres": {
            "#": "{} {}",
            "others": "{} de {}"
        },
        "adm": "TBD",
    },
    "BTE": {
        "name": "bote(s)",
        "pres": "{} de {}",
        "pres_txt": "name-num",
        "adm": "TBD",
    },
}





## List of identified mistakes
mistakes_id = {
    "cap_wl": [402, 405, 682, 963, 1092, 1119, 1139, 1955, 1991],
    "caj_wl": [19, 450, 469, 1095],
    "tab_wl": [813, 818, 819, 927, 956, 1055, 1580, 1724, 1800],
    "man_notes": [24, 31, 115, 154, 307, 364, 372, 450, 632, 646, 675, 941, 1400, 1458, 1677, 1779, 1886, 2143],
}
