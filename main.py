from insertion import insertion
from merge import merge_sort
from hybrid_sort import hybrid_sort
from random import randint
from timeit import default_timer

if __name__ == '__main__':

    number = int(input('please enter amount of animals : '))
    Array = [randint(1, number) for _ in range(number)]
    Array2 = Array.copy()
    Array3 = Array.copy()

    print('-------------------------- INSERTION ------------------------------------')
    insertion_start = default_timer()
    insertion(Array)
    insertion_end = default_timer()
    print(Array)
    print(f'the time is: {insertion_end - insertion_start}')
    print('---------------------insertion----------------------')
    print('\n\n')
    print('------------------------------- MERGE -----------------------------')
    merge_start = default_timer()
    merge_sort(Array2, 0, number - 1)
    merge_end = default_timer()
    print(Array2)
    print(f'the time is: {merge_end - merge_start}')
    print('------------------------------------merge-----------------------------------')

    print('\n\n')
    print('--------------------------- HYBRID ---------------------------------')
    k = int(input('please enter your limit: ')) #that is for determining the limit
    hybrid_start = default_timer()
    Array3 = hybrid_sort(Array3, k)
    hybrid_end = default_timer()
    print(Array3)
    print(f'the time is {hybrid_end - hybrid_start}')

    print('--------------------------------------hybrid-----------------------------------')