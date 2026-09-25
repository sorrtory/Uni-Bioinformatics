import json


def test(result: list, path_to_small_index: str) -> tuple[int, int]:
    js = json.load(open(path_to_small_index, mode="r"))
    c = 0
    for elem in result:
        if elem[1] in js:
            c += 1
    return c, len(js)