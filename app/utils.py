import os 
from constants import *

# util  : from a dict with all users get a dict of each competency level by user, by family of competency
def get_dict_by_user_by_family(dict):
    # mock data : all_users_competencies_score
    for i in dict:
        for j in dict[i]:
            dict[i][j] = {
                "values": list(dict[i][j].values()),
                "keys": list(dict[i][j].keys())
            }
            dict_by_user_by_family = dict[i][j]
            return dict_by_user_by_family


