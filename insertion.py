import random
from time import perf_counter
import timeit

def insertion(ArrayList: list) -> list:
    l = len(ArrayList)
    for i in range(1, len(ArrayList)):
        key = ArrayList[i]
        j = i - 1

        while j >= 0 and key < ArrayList[j]:
            ArrayList[j + 1] = ArrayList[j]
            j -= 1
        ArrayList[j + 1] = key



if __name__ == "__main__":
    n = int(input("please enter amount of your animals: "))

    ArrayList= [random.randint(1, n) for i in range(n)]

    
