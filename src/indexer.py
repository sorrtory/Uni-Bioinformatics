import os
import time
from io import TextIOWrapper

from src.vectorize import vectorize

def parse_input(kt):
    kt = kt.split("\n>")
    answer = []
    for elem in kt:
        key = (elem[10:elem.find("OX=") - 1]).replace("|", "").replace('"', "")
        value = elem[elem.find("\n") + 1:].replace("\n", "")
        answer += [[key, value]]
    return answer

def write(file_stream: TextIOWrapper, key: str, domains: dict, is_first: bool):
    string = (f'{'{' if is_first else ",\n"}'
              f'{f'"{key}"' if is_first else f'\t"{key}"'}'
              f':\n\t\t{str(domains).replace("'", '"')}')
    file_stream.write(string)

def create_index(file: str, dir_path: str, part: int, amount: int) -> float:
    startind = time.time()
    for filename in os.listdir(dir_path):
        os.remove(f"{dir_path.rstrip("/")}/{filename}")
    with open(file) as f:
        kt = f.read()
        entries = kt.count(">")
        all_data = parse_input(kt)
        for i in range(amount):
            data = all_data[i * (entries // amount):(i + 1) * (entries // amount)]
            write_path = dir_path + "index" + str(i) + ".json"
            result_file = open(write_path, mode="w")
            is_first = True
            for key, value in data:
                domains = vectorize(value, part)
                write(result_file, key, domains, is_first)
                is_first = False
            print("}", file=result_file)
            result_file.close()
    endind = time.time()
    return endind - startind