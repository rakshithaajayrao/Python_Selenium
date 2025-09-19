# List #Ordered, mutable, allows duplicates

fruits = ['apple', 'banana', 'cherry']
fruits.append('date')
print(fruits)  # ['apple', 'banana', 'cherry', 'date']

#Tuple # Ordered, immutable, allows duplicates
person = ('Alice', 30, 'Engineer')
print(person[0])  # Alice

# Set # Unordered, mutable, no duplicates
unique_numbers = {1, 2, 3, 2, 1}
unique_numbers.add(4)
print(unique_numbers)  # {1, 2, 3, 4}

# Dictionary # Key-value pairs, mutable, keys must be unique
student = {'name': 'Bob', 'age': 22, 'major': 'CS'}
student['age'] = 23
print(student)  # {'name': 'Bob', 'age': 23, 'major': 'CS'}