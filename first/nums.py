my_list = ['a', 'b', [1, 2, 3], 'd']
a,b,c,d = my_list
print(a,b,c)

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
print(sum(filter(lambda x: isinstance(x, int), list_1)))
print(list(filter(lambda x: isinstance(x, str) and 'a' in x, list_1)))
print([x for x in list_1 if isinstance(x, str) and 'a' in x])

family_1=input([])
family_2=input([])
if len(family_2)>len(family_1):
    print(family_2)

else:
    print(family_1)
