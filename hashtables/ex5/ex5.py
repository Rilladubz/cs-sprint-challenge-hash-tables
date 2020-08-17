# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    files_list = {}

    def split(word):
        count = 0
        split_word = [char for char in word]

        for each in split_word:
            if each == '/':
                count += 1

        return count

    for each in files:
        count = split(each)
        if each.split('/', )[count] not in files_list:
            files_list[each.split("/", )[count]] = each
        elif each.split('/', )[count] in files_list:
            files_list[each.split('/', )[count] + "two"] = each

    return_list = {}

    for query in queries:
        query2 = query + "two"
        if query in files_list:
            return_list[query] = files_list[query]
        if query2 in files_list:
            return_list[query2] = files_list[query2]

    return_vals = [each[1] for each in return_list.items()]

    return return_vals


if __name__ == "__main__":
    # files = [
    #     '/bin/foo',
    #     '/bin/bar',
    #     '/usr/bin/baz',
    #     '/bin/foo',
    #     '/bin/bar',
    #     '/usr/bin/baz'
    # ]
    # queries = [
    #     "foo",
    #     "qux",
    #     "baz"
    # ]

    files = []

    for i in range(500000):
        files.append(f"/dir{i}/file{i}")

    for i in range(500000):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    queries = []

    for i in range(1000000):
        queries.append(f"nofile{i}")

    queries += [
        "file3490",
        "file256",
        "file999999",
        "file8192"
    ]

    print(finder(files, queries))
