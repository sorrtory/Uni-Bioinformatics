from src import finder, indexer, parameters, correctness


def main():
    time1 = indexer.create_index(parameters.DATA_PATHS, "data/indexes/",
                                 parameters.PART, parameters.AMOUNT)
    print("Time to create index:", time1)
    time2, answer = finder.find("data/indexes", parameters.TOP, parameters.TO_FIND, parameters.PART)
    print("Time to find:", time2)
    print("Time summary:", time1 + time2)
    print("Result:")
    c = 0
    for elem in answer:
        c += 1
        print(c, elem)
    print("Testing:")
    time3 = indexer.create_index("data/data-small.txt", "data/index_test/", parameters.PART, 1)
    test_data = correctness.test(answer, "data/index_test/index0.json")
    print(f"Hit in {test_data[0]}, that is {round(test_data[0] / test_data[1], 3)} accuracy")
    print(f"Time to test:", time3)



if __name__ == "__main__":
    main()