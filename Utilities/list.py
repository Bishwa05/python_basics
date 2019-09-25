numbers = [5, 2, 1, 5, 7, 4]
numbers.insert(0, 10)
print(numbers)
numbers.remove(2)
print(numbers)
numbers.pop()
print(numbers)
print (50 in numbers)
print(numbers.count(5))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)

#To remove duplicate

numbers = [2,2,4,6,3,4, 6,1]
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)

