import time
from io import TextIOWrapper

from src.vectorize import vectorize

def parse_input(kt):
    kt = kt.split("\n>")
    sl = {}
    for elem in kt:
        key = (elem[10:elem.find(" ")].strip("|")
               + elem[elem.find("OS=") + 2:elem.find("OX=") - 1])
        value = elem[elem.find("\n") + 1:].replace("\n", "")
        sl[key] = value
    return sl

def write(file_stream: TextIOWrapper, key: str, domains: dict, is_first: bool):
    string = (f'{'{' if is_first else ",\n"}'
              f'{f'"{key}"' if is_first else f'\t"{key}"'}'
              f':\n\t\t{str(domains).replace("'", '"')}')
    file_stream.write(string)

def create_index(file: str, out_path: str, part: int) -> float:
    with open(file) as f:
        kt = f.read()
        data = parse_input(kt)
        result_file = open(out_path, mode="w")
        startind = time.time()
        is_first = True
        for key, value in data.items():
            domains = vectorize(value, part)
            write(result_file, key, domains, is_first)
            is_first = False
        endind = time.time()
        print("}", file=result_file)
        result_file.close()
    return endind - startind