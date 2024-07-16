x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)

# # 2. change the last name of the first student from jordan to bryant
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students[0]['last_name'])
print(students)

# # 3.change messi to andres
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# # 4. change the value 20 in z to 30
z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
print(z)


# 1. iterate through a list of dictionaries
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(some_list):
    i = 0
    while i < len(some_list):
        print(some_list[i])
        i += 1


def iterateDictionary2(key_name, some_list):
    x = 0
    while x < len(some_list):
        print(some_list[x][key_name])
        x += 1

def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list)):

        for key,val in some_list[i].items():
            if key == key_name:

                print(val) 


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in dojo.keys():
        print('--------------')
        print(str(len(dojo[key])) + ' ' + key.upper()) # include the number of entries in the list
        for value in dojo[key]: #print each entry in the list
            print(value)
printInfo(dojo)