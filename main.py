import json
import time
import pickle

PART = 3
ALPHABET = {'M', 'R', 'B', 'U', 'Q', 'W', 'G', 'P', 'L', 'D', 'E', 'T', 'Z', 'N', 'X', 'F',
            'Y', 'V', 'A', 'I', 'S', 'H', 'K', 'O', 'C'}


def parseinput(kt):
    kt = kt.split("\n>")
    sl = {}
    for elem in kt:
        key = elem[10:elem.find(" ")].strip("|")
        value = elem[elem.find("\n") + 1:].replace("\n", "")
        sl[key] = value
    return sl

with open("uniprot_sprot.fasta") as f:
    kt = f.read()
    sl = parseinput(kt)
    index = {}
    startind = time.time()
    for key, value in sl.items():
        domains = {}
        for t in range(PART):
            for i in range(len(value) // PART + 1):
                batch = value[i * PART + t:i * PART + PART + t]
                if len(batch) < 3:
                    continue
                domains[batch] = domains.get(batch, 0) + 1
            index[key] = domains
    endind = time.time()
    print("Time to make index: ", endind - startind)
    startwr = time.time()
    json.dump(index, open("out.json", mode="w"))
    endwr = time.time()
    print("Time to write index: ", endwr - endind)
    startrd = time.time()
    sl = json.load(fp=open("out.json", mode="r"))
    print(sl["001R_FRG3G"])
    endrd = time.time()
    print("Timt to read index: ", endrd - startrd)
