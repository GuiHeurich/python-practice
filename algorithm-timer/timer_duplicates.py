import timeit
from functions import find_duplicate

def ranges():
    list_a = 10001
    list_b = 15001
    list_c = 20001
    list_d = 25001
    list_e = 30001
    list_f = 35001
    list_g = 40001
    list_h = 45001
    list_i = 50001
    list_j = 55001
    list_k = 60001
    list_l = 65001
    list_m = 70001
    list_n = 75001
    list_o = 80001
    list_p = 85001
    list_q = 90001
    list_r = 95001
    list_s = 100001
    return [
    list_a,
    list_b,
    list_c,
    list_d,
    list_e,
    list_f,
    list_g,
    list_h,
    list_i,
    list_j,
    list_k,
    list_l,
    list_m,
    list_n,
    list_o,
    list_p,
    list_q,
    list_r,
    list_s
    ]

def times():
    list_a = list(range(5001)) * 2
    list_b = list(range(7501)) * 2
    list_c = list(range(10001)) * 2
    list_d = list(range(12501)) * 2
    list_e = list(range(15001)) * 2
    list_f = list(range(17501)) * 2
    list_g = list(range(20001)) * 2
    list_h = list(range(22501)) * 2
    list_i = list(range(25001)) * 2
    list_j = list(range(27501)) * 2
    list_k = list(range(30001)) * 2
    list_l = list(range(32501)) * 2
    list_m = list(range(35001)) * 2
    list_n = list(range(37501)) * 2
    list_o = list(range(40001)) * 2
    list_p = list(range(42501)) * 2
    list_q = list(range(45001)) * 2
    list_r = list(range(47501)) * 2
    list_s = list(range(50001)) * 2

    time_a = timeit.timeit(lambda: find_duplicate(list_a), number=1)
    time_b = timeit.timeit(lambda: find_duplicate(list_b), number=1)
    time_c = timeit.timeit(lambda: find_duplicate(list_c), number=1)
    time_d = timeit.timeit(lambda: find_duplicate(list_d), number=1)
    time_e = timeit.timeit(lambda: find_duplicate(list_e), number=1)
    time_f = timeit.timeit(lambda: find_duplicate(list_f), number=1)
    time_g = timeit.timeit(lambda: find_duplicate(list_g), number=1)
    time_h = timeit.timeit(lambda: find_duplicate(list_h), number=1)
    time_i = timeit.timeit(lambda: find_duplicate(list_i), number=1)
    time_j = timeit.timeit(lambda: find_duplicate(list_j), number=1)
    time_k = timeit.timeit(lambda: find_duplicate(list_k), number=1)
    time_l = timeit.timeit(lambda: find_duplicate(list_l), number=1)
    time_m = timeit.timeit(lambda: find_duplicate(list_m), number=1)
    time_n = timeit.timeit(lambda: find_duplicate(list_n), number=1)
    time_o = timeit.timeit(lambda: find_duplicate(list_o), number=1)
    time_p = timeit.timeit(lambda: find_duplicate(list_p), number=1)
    time_q = timeit.timeit(lambda: find_duplicate(list_q), number=1)
    time_r = timeit.timeit(lambda: find_duplicate(list_r), number=1)
    time_s = timeit.timeit(lambda: find_duplicate(list_s), number=1)

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

def run_duplicates():
    list_a = list(range(5001)) * 2
    list_b = list(range(7501)) * 2
    list_c = list(range(10001)) * 2
    list_d = list(range(12501)) * 2
    list_e = list(range(15001)) * 2
    list_f = list(range(17501)) * 2
    list_g = list(range(20001)) * 2
    list_h = list(range(22501)) * 2
    list_i = list(range(25001)) * 2
    list_j = list(range(27501)) * 2
    list_k = list(range(30001)) * 2
    list_l = list(range(32501)) * 2
    list_m = list(range(35001)) * 2
    list_n = list(range(37501)) * 2
    list_o = list(range(40001)) * 2
    list_p = list(range(42501)) * 2
    list_q = list(range(45001)) * 2
    list_r = list(range(47501)) * 2
    list_s = list(range(50001)) * 2

    print("FIND DUPLICATE")
    time_a = print(timeit.timeit(lambda: find_duplicate(list_a), number=1))
    time_b = print(timeit.timeit(lambda: find_duplicate(list_b), number=1))
    time_c = print(timeit.timeit(lambda: find_duplicate(list_c), number=1))
    time_d = print(timeit.timeit(lambda: find_duplicate(list_d), number=1))
    time_e = print(timeit.timeit(lambda: find_duplicate(list_e), number=1))
    time_f = print(timeit.timeit(lambda: find_duplicate(list_f), number=1))
    time_g = print(timeit.timeit(lambda: find_duplicate(list_g), number=1))
    time_h = print(timeit.timeit(lambda: find_duplicate(list_h), number=1))
    time_i = print(timeit.timeit(lambda: find_duplicate(list_i), number=1))
    time_j = print(timeit.timeit(lambda: find_duplicate(list_j), number=1))
    time_k = print(timeit.timeit(lambda: find_duplicate(list_k), number=1))
    time_l = print(timeit.timeit(lambda: find_duplicate(list_l), number=1))
    time_m = print(timeit.timeit(lambda: find_duplicate(list_m), number=1))
    time_n = print(timeit.timeit(lambda: find_duplicate(list_n), number=1))
    time_o = print(timeit.timeit(lambda: find_duplicate(list_o), number=1))
    time_p = print(timeit.timeit(lambda: find_duplicate(list_p), number=1))
    time_q = print(timeit.timeit(lambda: find_duplicate(list_q), number=1))
    time_r = print(timeit.timeit(lambda: find_duplicate(list_r), number=1))
    time_s = print(timeit.timeit(lambda: find_duplicate(list_s), number=1))

if __name__ == '__main__':
    run_duplicates()
