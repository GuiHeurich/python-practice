import timeit
import random
from random import randrange
from functions import last

def ranges():
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
    return [
    list_a[-1],
    list_b[-1],
    list_c[-1],
    list_d[-1],
    list_e[-1],
    list_f[-1],
    list_g[-1],
    list_h[-1],
    list_i[-1],
    list_j[-1],
    list_k[-1],
    list_l[-1],
    list_m[-1],
    list_n[-1],
    list_o[-1],
    list_p[-1],
    list_q[-1],
    list_r[-1],
    list_s[-1]
    ]

def times():
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

    time_a = timeit.timeit(lambda: last(list_a))
    time_b = timeit.timeit(lambda: last(list_b))
    time_c = timeit.timeit(lambda: last(list_c))
    time_d = timeit.timeit(lambda: last(list_d))
    time_e = timeit.timeit(lambda: last(list_e))
    time_f = timeit.timeit(lambda: last(list_f))
    time_g = timeit.timeit(lambda: last(list_g))
    time_h = timeit.timeit(lambda: last(list_h))
    time_i = timeit.timeit(lambda: last(list_i))
    time_j = timeit.timeit(lambda: last(list_j))
    time_k = timeit.timeit(lambda: last(list_k))
    time_l = timeit.timeit(lambda: last(list_l))
    time_m = timeit.timeit(lambda: last(list_m))
    time_n = timeit.timeit(lambda: last(list_n))
    time_o = timeit.timeit(lambda: last(list_o))
    time_p = timeit.timeit(lambda: last(list_p))
    time_q = timeit.timeit(lambda: last(list_q))
    time_r = timeit.timeit(lambda: last(list_r))
    time_s = timeit.timeit(lambda: last(list_s))

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

def run_last():
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

    print("LAST")
    time_a = print(timeit.timeit(lambda: last(list_a)))
    time_b = print(timeit.timeit(lambda: last(list_b)))
    time_c = print(timeit.timeit(lambda: last(list_c)))
    time_d = print(timeit.timeit(lambda: last(list_d)))
    time_e = print(timeit.timeit(lambda: last(list_e)))
    time_f = print(timeit.timeit(lambda: last(list_f)))
    time_g = print(timeit.timeit(lambda: last(list_g)))
    time_h = print(timeit.timeit(lambda: last(list_h)))
    time_i = print(timeit.timeit(lambda: last(list_i)))
    time_j = print(timeit.timeit(lambda: last(list_j)))
    time_k = print(timeit.timeit(lambda: last(list_k)))
    time_l = print(timeit.timeit(lambda: last(list_l)))
    time_m = print(timeit.timeit(lambda: last(list_m)))
    time_n = print(timeit.timeit(lambda: last(list_n)))
    time_o = print(timeit.timeit(lambda: last(list_o)))
    time_p = print(timeit.timeit(lambda: last(list_p)))
    time_q = print(timeit.timeit(lambda: last(list_q)))
    time_r = print(timeit.timeit(lambda: last(list_r)))
    time_s = print(timeit.timeit(lambda: last(list_s)))

if __name__ == '__main__':
    run_last()
