import multiprocessing as multi
import day12_lib as lib

INPUT_FILENAME = "input_12.txt"


def main():
    records = lib.parse_input(INPUT_FILENAME)
    springs, conditions = map(tuple, zip(*records))
    springs = tuple(["?".join([s] * 5) for s in springs])
    conditions = tuple([c * 5 for c in conditions])
    records = zip(springs, conditions)

    pool = multi.Pool(processes=12)
    arrangement_count = sum(list(pool.starmap(lib.count_arrangements, records)))
    print(arrangement_count)


if __name__ == "__main__":
    main()