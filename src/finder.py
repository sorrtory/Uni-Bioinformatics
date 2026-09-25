import json
import time
import os

from src.vectorize import vectorize

SAME_EXP = 1
SAME_COEF = 1
ONLY_CHECK_EXP = 3
ONLY_CHECK_COEF = 5
ONLY_ITEM_EXP = 2
ONLY_ITEM_COEF = 2

candid = []


def difference(check_vector: dict, item: dict, barrier: int) -> int:
    diff = 0
    keys_check = set(check_vector.keys())
    keys_item = set(item.keys())
    for key in keys_check.intersection(keys_item):
        diff += ((check_vector[key] - item[key]) * SAME_COEF) ** SAME_EXP
        if diff > barrier:
            return 10**10
    for key in keys_check.difference(keys_item):
        diff += (check_vector[key] * ONLY_CHECK_COEF) ** ONLY_CHECK_COEF
        if diff > barrier:
            return 10**10
    for key in keys_item.difference(keys_check):
        diff += (item[key] * ONLY_ITEM_COEF) ** ONLY_ITEM_EXP
        if diff > barrier:
            return 10**10
    return diff

def find_pos(num: int) -> int:
    global candid
    low = 0
    high = len(candid)
    while True:
        middle = (low + high) // 2
        if low == high:
            return low
        if candid[middle][0] > num:
            high = middle
            continue
        if candid[middle][0] < num:
            low = middle + 1
            continue
        return middle
    return -1


def find(index_folder_path: str, top: int, check:str, part: int) -> tuple[float, list]:
    global candid
    count = 0
    start = time.time()
    check_vector = vectorize(check, part)
    cur_min = 10**10
    iterations = 0
    for index_path in os.listdir(index_folder_path):
        with open(f"{index_folder_path}/{index_path}", mode="r") as f:
            data = json.load(f)
            if (iterations // 100000) == 1:
                print(100000 * count + iterations, time.time() - start)
                iterations -= 100000
                count += 1
            for key, item in data.items():
                iterations += 1
                diff = difference(check_vector, item, cur_min)
                if len(candid) < top:
                    candid += [[diff, key]]
                    candid.sort()
                else:
                    if cur_min > diff:
                        index = find_pos(diff)
                        if index != -1:
                            candid.insert(index, [diff, key])
                            candid.pop(-1)
                            cur_min = candid[-1][0]
    end = time.time()
    return end - start, candid