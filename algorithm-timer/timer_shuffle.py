import sys
import timeit
import random
from random import randrange
from functions import shuffle

def shuffle_times():
    list_a = list(range(10001))
    list_b = list(range(15001))
    list_c = list(range(20001))
    list_d = list(range(25001))
    list_e = list(range(30001))
    list_f = list(range(35001))
    list_g = list(range(40001))
    list_h = list(range(45001))
    list_i = list(range(50001))
    list_j = list(range(55001))
    list_k = list(range(60001))
    list_l = list(range(65001))
    list_m = list(range(70001))
    list_n = list(range(75001))
    list_o = list(range(80001))
    list_p = list(range(85001))
    list_q = list(range(90001))
    list_r = list(range(95001))
    list_s = list(range(100001))

    time_a = timeit.timeit(lambda: shuffle(list_a), number=1)
    time_b = timeit.timeit(lambda: shuffle(list_b), number=1)
    time_c = timeit.timeit(lambda: shuffle(list_c), number=1)
    time_d = timeit.timeit(lambda: shuffle(list_d), number=1)
    time_e = timeit.timeit(lambda: shuffle(list_e), number=1)
    time_f = timeit.timeit(lambda: shuffle(list_f), number=1)
    time_g = timeit.timeit(lambda: shuffle(list_g), number=1)
    time_h = timeit.timeit(lambda: shuffle(list_h), number=1)
    time_i = timeit.timeit(lambda: shuffle(list_i), number=1)
    time_j = timeit.timeit(lambda: shuffle(list_j), number=1)
    time_k = timeit.timeit(lambda: shuffle(list_k), number=1)
    time_l = timeit.timeit(lambda: shuffle(list_l), number=1)
    time_m = timeit.timeit(lambda: shuffle(list_m), number=1)
    time_n = timeit.timeit(lambda: shuffle(list_n), number=1)
    time_o = timeit.timeit(lambda: shuffle(list_o), number=1)
    time_p = timeit.timeit(lambda: shuffle(list_p), number=1)
    time_q = timeit.timeit(lambda: shuffle(list_q), number=1)
    time_r = timeit.timeit(lambda: shuffle(list_r), number=1)
    time_s = timeit.timeit(lambda: shuffle(list_s), number=1)

    return [
    round(time_a, 2),
    round(time_b, 2),
    round(time_c, 2),
    round(time_d, 2),
    round(time_e, 2),
    round(time_f, 2),
    round(time_g, 2),
    round(time_h, 2),
    round(time_i, 2),
    round(time_j, 2),
    round(time_k, 2),
    round(time_l, 2),
    round(time_m, 2),
    round(time_n, 2),
    round(time_o, 2),
    round(time_p, 2),
    round(time_q, 2),
    round(time_r, 2),
    round(time_s, 2)
    ]

def run_shuffle():
    list_a = list(range(10000))
    list_b = list(range(15000))
    list_c = list(range(20000))
    list_d = list(range(25000))
    list_e = list(range(30000))
    list_f = list(range(35000))
    list_g = list(range(40000))
    list_h = list(range(45000))
    list_i = list(range(50000))
    list_j = list(range(55000))
    list_k = list(range(60000))
    list_l = list(range(65000))
    list_m = list(range(70000))
    list_n = list(range(75000))
    list_o = list(range(80000))
    list_p = list(range(85000))
    list_q = list(range(90000))
    list_r = list(range(95000))
    list_s = list(range(100000))

    print("SHUFFLE")
    print(timeit.timeit(lambda: shuffle(list_a), number=1))
    print(timeit.timeit(lambda: shuffle(list_b), number=1))
    print(timeit.timeit(lambda: shuffle(list_c), number=1))
    print(timeit.timeit(lambda: shuffle(list_d), number=1))
    print(timeit.timeit(lambda: shuffle(list_e), number=1))
    print(timeit.timeit(lambda: shuffle(list_f), number=1))
    print(timeit.timeit(lambda: shuffle(list_g), number=1))
    print(timeit.timeit(lambda: shuffle(list_h), number=1))
    print(timeit.timeit(lambda: shuffle(list_i), number=1))
    print(timeit.timeit(lambda: shuffle(list_j), number=1))
    print(timeit.timeit(lambda: shuffle(list_k), number=1))
    print(timeit.timeit(lambda: shuffle(list_l), number=1))
    print(timeit.timeit(lambda: shuffle(list_m), number=1))
    print(timeit.timeit(lambda: shuffle(list_n), number=1))
    print(timeit.timeit(lambda: shuffle(list_o), number=1))
    print(timeit.timeit(lambda: shuffle(list_p), number=1))
    print(timeit.timeit(lambda: shuffle(list_q), number=1))
    print(timeit.timeit(lambda: shuffle(list_r), number=1))
    print(timeit.timeit(lambda: shuffle(list_s), number=1))

if __name__ == '__main__':
    run_shuffle()
