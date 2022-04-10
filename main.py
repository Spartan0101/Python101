# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script..
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
test = 1/2

print(type(test))
# type() -> gives you the variable type
print("hello \n world")
print(len('hello'))
# String indexing and sliceing
myString = "Hello World"
print(myString[1] + myString[-1])
print(myString[2:])
print(myString[:6])
print(myString[2:7:2])
print(myString[::-1])
print(myString.upper())
x = "Hi this is a string"
print(x.split())
print(x.split('i'))
print('This is a string {}'.format('INSERTED'))
print('{2} {0} {1}'.format('Electric','Car','Expensive'))

name = 'Jode'
print(f'Hello, my friend {name}')

#lists

my_list = [1,2,3]
my_list = ['String', 1 , 23.2]
print(len(my_list))
print(my_list[0])
another_list = ['String2', 12]
print(my_list + another_list)
my_list[0] = 'ALL CAPS'
print(my_list)
my_list.append('Six')
print(my_list)
my_list.pop()
print(my_list)
new_list = ['a', 'x', 'g', 'o', 'e']
new_list.sort()
my_sorted_list = new_list
print(my_sorted_list)
my_sorted_list.reverse()
print(my_sorted_list)

#Dictionaries

my_dict = {'key1': 'Honda', 'key2': 'Civic'}
prices_lookup = {'apple':2.99, 'Oranges':5.99}
print(prices_lookup['apple'])
d = {'k1': 123,'k2': [0, 1, 2]}
print(d['k2'])
d = {'k1':100, 'k2':200, 'k3':300}
d['k4'] =400
print(d)
d['k1'] = 'NEW VALUE'
print(d)
print(d.keys())
print(d.items())
print(d.values())

#TUPLES , key difference from lists, they are immutability

t = (1,2,3)
my_tuple = [1,2,3]
print(type(t))
t = ('a','b','c')
print(t.count('a'))
print(t.index('a'))

#Sets - unordered collection of unique elements

myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset)
#if adding duplicate it won't be displayed
mylisttwo = [1,1,1,2,2,2,3,3,3]
print(set(mylisttwo))

