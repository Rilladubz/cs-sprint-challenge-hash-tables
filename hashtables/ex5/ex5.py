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
        if each not in files_list:
            files_list[each.split("/", )[count]] = each
    print(files_list)

    return_list = {}

    for query in queries:
        if query in files_list:
            return_list[query] = files_list[query]

    return_vals = [each[1] for each in return_list.items()]

    return return_vals


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]

    print(finder(files, queries))
