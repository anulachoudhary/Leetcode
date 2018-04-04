# >>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# >>> reverse_alternate_five_item(lst)
# 1 2 3 4 5
# 10 9 8 7 6 
# 11 12 13 14 15
# 20 19 18 17 16 


def reverse_alternate_five_items(lst):
    """

    """
    count = 0
    temp_lst = []
    for item in lst:
        count += 1
        
        temp_lst.append(item)

        if (count % 10 == 0):
            print temp_lst[::-1] 
            temp_lst = []
        
        elif count % 5 == 0:
            print temp_lst
            temp_lst = []
                        















