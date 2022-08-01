# There is string s = "Python Bootcamp". Write the code that hashes string.


def str_to_hash(test_str):
    return hash(test_str)


s = 'Python Bootcamp'


if __name__ == "__main__":
    s_hash = str_to_hash(s)
    print(f'Hash value for "{s}": {s_hash}')


