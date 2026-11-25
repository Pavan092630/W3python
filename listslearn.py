shopping_list = ["apple", "banana", "cherry"]
another_shopping_list = shopping_list
print(id(another_shopping_list))
print(id(shopping_list))
shopping_list += ["Watermelon"]
print(shopping_list)
print(id(shopping_list))
a = b = c = d = e = shopping_list
b.append("mint")
print(a)
print(b)
print(c)
print(d)
print(e)
print(shopping_list)
even = [x for x in range(1,10) if x % 2 == 0]
print(even)
odd = [x for x in range(10) if x % 2 != 0]
print(odd)
print()
print(min(odd))
print(max(odd))
print(sum(odd))
print()
print(min(even))
print(max(even))
print(sum(even))
print()
print("mississippi".count("iss"))
print("mississippi".count("s"))


