
id_test = 2
family_test = 'Test Family'

all_users_competencies_score = {"1": {
    "Debugging & Observability": {
        "Debugging": "1",
        "Observability": "4"
    },

    "Quality & testing": {
        "écriture de code": "4",
        "testing": "3"
    },

    "Software design & architecure ": {
        "understanding code": "2"
    },
},

    "2": {

    "Debugging & Observability": {
        "Debugging": "3",
        "Observability": "5"
    },

    "Quality & testing": {
        "écriture de code": "3",
        "testing": "2"
    },

    "Software design & architecure ": {
        "understanding code": "2"
    },
}
}

user_level = {
    "Debugging": 1,
    "Observability": 4,
    "écriture de code": 3,
    "testing": 2,
    "understanding code": 2
}

user_level_by_family = {

    "Debugging & Observability": {
        "Debugging": "3",
        "Observability": "5"
    },

    "Quality & testing": {
        "écriture de code": "3",
        "testing": "2"
    },

    "Software design & architecure ": {
        "understanding code": "2"
    },
}


target_comparison = {
    "target": {
        "skill1": 4,
        "skill2": 3,
        "skill3": 3,
        "skill4": 5,
        "skill5": 4
    },
    "profiles": [
        {
            "name": "jean",
            "skills": {
                "skill1": 4,
                "skill2": 2,
                "skill3": 2,
                "skill4": 5,
                "skill5": 5
            }
        },
        {
            "name": "marie",
            "skills": {
                "skill1": 5,
                "skill2": 5,
                "skill3": 5,
                "skill4": 0,
                "skill5": 4
            }
        },
        {
            "name": "marc",
            "skills": {
                "skill1": 4,
                "skill2": 3,
                "skill3": 4,
                "skill4": 4,
                "skill5": 4
            }
        }
    ]
}
