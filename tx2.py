class CustomList(list):
    def sum_all(self):
        return sum(self)
    def max_value(self):
        return max(self)
    def __getitem__(self, key):
        if not isinstance(key,int):
            raise KeyError('key must be an integer')
        if key < 0 or key >= len(self):
            raise IndexError('index out of range')
        return super().__getitem__(key)

my_list = CustomList([1, 2, 3, 4, 5])
print(my_list.sum_all())  # 15
print(my_list.max_value())  # 5
print(my_list[2])  # 3
