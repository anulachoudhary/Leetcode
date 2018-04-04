def get_indices(sum, number_list):

    number_index_pair = {}
    list_of_tuples = []
    for i, number in enumerater(number_list):
        second_number = sum - number 