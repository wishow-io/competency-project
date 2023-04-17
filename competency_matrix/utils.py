## utils to manipulate and access nested dictionaries 

# util  : from a dict with all users get a dict of each competency level by user, by family of competency
def get_dict_by_user_by_family(dict):
    for i in dict:
        for j in dict[i]:
            dict[i][j] = {
                "values": list(dict[i][j].values()),
                "keys":list(dict[i][j].keys())
                }  
            dict_by_user_by_family = dict[i][j]
            return dict_by_user_by_family
        

