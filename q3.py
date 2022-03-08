class List(list):
    # Constructor - initialize with the super() function:
    def __init__(self, input_list: list):
        super(List, self).__init__(input_list)

    # Operator [] getter:
    def __getitem__(self, key):
        # If key is a single index we can use the original getter:
        if isinstance(key, int):
            return super(List, self).__getitem__(key)

        # If key is a tuple we need to iterate over it and get the index of each level:
        current_data = self
        for index in key:
            current_data = current_data[index]

        return current_data

    # Operator [] setter:
    def __setitem__(self, key, value):
        # If key is a single index we can use the original setter:
        if isinstance(key, int):
            return super(List, self).__setitem__(key, value)

        # If key is a tuple we need to iterate over it and get the levels one by one,
        # We need to get to the len(key)-2 index and then change the value of the last item:
        current_data = self
        for index in range(len(key) - 1):
            current_data = current_data[key[index]]
        current_data[key[len(key) - 1]] = value


if __name__ == '__main__':
    # Tests:
    l = List([[1, 2], [[3, 4], [5, 6]]])
    print(l)
    print(l[0, 1])
    print(l[1])
    print(l[1, 0, 1])
    l[0, 1] = 777
    print(l)
    print(l[0,1])
    l.append(5)
    l.reverse()
    print(l.index(5))
    print(l)

    # Expected output:
    # [[1, 2], [[3, 4], [5, 6]]]
    # 2
    # [[3, 4], [5, 6]]
    # 4
    # [[1, 777], [[3, 4], [5, 6]]]
    # 777
    # 0
    # [5, [[3, 4], [5, 6]], [1, 777]]
