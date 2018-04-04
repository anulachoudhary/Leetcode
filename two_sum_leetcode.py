def two_sum(list_of_numbers, sum):
    # Because we need a reverse mapping of number to index, we create a dictionary
    # where the key is the number and the value is the index
    number_to_index = {}

    # A result list to hold tuples of two indices
    list_of_index_tuples = []



    # insert in dict => number : index
    for index, number in enumerate(list_of_numbers):
        # Key is number, Value is index
        number_to_index[number] = index



    # Iterate over the list of numbers to check
    for index_from_list, first_number in enumerate(list_of_numbers):
        # Figure out the difference of sum and each number
        second_number = sum - first_number

        # Now check if this number exists in the dictionary, so get value
        index_of_second_number_from_dictionary = number_to_index.get(second_number, -1)

        # -1 means default value, which means second_number is not in dictionary
        if index_of_second_number_from_dictionary != -1:
            # Insert a tuple inlist
            list_of_index_tuples.append((index_from_list, index_of_second_number_from_dictionary))

            # After finding a pair (i, j), we need to make sure we dont find (j, i)
            # So we need to remove these entries from dictionary
            # To remove entries, we will simply find first_number and second_number in dictionary
            # and remove them :)
            del number_to_index[first_number]
            del number_to_index[second_number]



    return list_of_index_tuples




if __name__ == "__main__":

    input = [3, 6, 8, 10, 7, 5, 2, 1,15, 19, 20]

    list_of_answers = two_sum(input, 15)

    print list_of_answers
two_sum.py
Open with
Displaying two_sum.py.