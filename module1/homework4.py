immutable_var=(10, 2.13, 'square', 89, 'C')
print(immutable_var)
#immutable_var[0]=18 TypeError: 'tuple' object does not support item assignment Кортеж это не изменяемый объект
mutable_list=[10, 2.13, 'square', 89, 'C']
mutable_list[0]=18
mutable_list[4]='modifed'
print(mutable_list)