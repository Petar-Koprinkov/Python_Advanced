def grocery_store(**kwargs):
    result = ""
    sorted_dict = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
    for key, value in sorted_dict:
        result += f"{key}: {value}\n"

    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print()
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
