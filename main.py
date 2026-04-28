def get_full_name(first_name : str, last_name : str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))


def get_name_with_age(name : str, age : int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


from typing import Any

def some_functions(data : Any):
    print(data)
    
    
#Generic Types
