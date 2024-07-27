#importing functions directly from another files

def lbs_to_kg(weight):
    return weight*0.45


def kg_to_lbs(weight):
    return weight//0.45

# def find_max(list):
#     maximum=list[0]
#     for i in list:
#         if maximum<i:
#             maximum=i
#     return maximum

def maximum(list):
    maximum1=list[0]
    for i in list:
        if maximum1<i:
            maximum1=i
    return maximum1 