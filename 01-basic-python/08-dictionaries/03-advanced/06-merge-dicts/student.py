# Write your code here

# def merge_dicts(dict1, dict2):
#     new_dict = {}
#     for k,v in dict1.items():
#         for i,j in dict2.items():
#             if k == i:
#                 new_dict[i] = j
#             else:
#                 new_dict[k] = v
#                 new_dict[i] = j
#     return new_dict

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}