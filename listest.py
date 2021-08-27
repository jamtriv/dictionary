foo = (1, 2, 4, 8, 16)
print(foo)
bar = tuple(x + 1 for x in foo)
print(bar)