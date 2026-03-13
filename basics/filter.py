# filter is used to filter out items from an array as per condition specified by a funtion

natural_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_even(num):
    return True if num % 2 == 0 else False


even_nums = list(filter(is_even, natural_nums))
print(even_nums)

#another way could be by using lambda
odd_nums = list(filter((lambda x : True if x%2 == 1 else False), natural_nums))
print(odd_nums)