from src import finder, indexer, parameters


def main():
    time1 = indexer.create_index(parameters.DATA_PATHS, "data/index.json", parameters.PART)
    print("Time to create index:", time1)
    time2, answer = finder.find("data/index.json", parameters.TOP, parameters.TO_FIND, parameters.PART)
    print("Time to find:", time2)
    print("Time summary:", time1 + time2)
    print("Result:")
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()