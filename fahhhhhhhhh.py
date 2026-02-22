my_dict = {"Doe": "Jane", "Smith": "John", "Jones": "Jane"}
search_value = "Jane"

keys_with_value = [key for key, value in my_dict.items() if value == search_value]
print(keys_with_value)
