# Словари
my_dict = {"Егор": 2002, "Настя": 1923, "Инга": 1873}
print("Dict:", my_dict)
print("Existing value:", my_dict.get("Егор"))
print("Not existting value:", my_dict.get("Аня"))
my_dict.update({"Alex": 2003,
                "Denis": 1732})
print("Deleted value:", my_dict.pop("Егор"))
print("Modified dictionary:", my_dict)

# Множества
my_set = {1, 2, 3, "class", 233}
print(my_set)
my_set.update([123323424, 23233232])
my_set.remove(2)
print(my_set)
