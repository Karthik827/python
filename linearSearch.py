def linearSearch(numbers_list,number_to_find):
    for index,element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

if __name__ == '__main__':
    numbers_list = [12,14,6,5,35,45,68,90]
    number_to_find = 35

    index = linearSearch(numbers_list,number_to_find)
    print(f'Number is found at {index} using linear search')