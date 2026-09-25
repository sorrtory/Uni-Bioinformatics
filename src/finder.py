import json
import time

from src.vectorize import vectorize

SAME = 1
ONLY_CHECK = 7
ONLY_ITEM = 3

def difference(check_vector: dict, item: dict) -> int:
    diff = 0
    keys_check = set(check_vector.keys())
    keys_item = set(item.keys())
    for key in keys_check.intersection(keys_item):
        diff += (check_vector[key] - item[key]) ** SAME
    for key in keys_check.difference(keys_item):
        diff += check_vector[key] ** ONLY_CHECK
    for key in keys_item.difference(keys_check):
        diff += item[key] ** ONLY_ITEM
    return diff

def find(index_path: str, top: int, check:str, part: int) -> tuple[float, list]:
    start = time.time()
    check_vector = vectorize(check, part)
    with open(index_path, mode="r") as f:
        data = json.load(f)
        candid = []
        for key, item in data.items():
            candid += [[difference(check_vector, item), key]]
        candid.sort()
    end = time.time()
    return end - start, candid[:top]