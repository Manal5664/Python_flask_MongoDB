# Conditional Statements (if, elif, else)
# Conditional Statements → decision making in code

marks = int(input("Enter student marks: "))  # student marks

if marks >= 80:
    print("Grade A")  # runs if condition is true
elif marks >= 70:
    print("Grade B")  # runs if first condition is false but this is true
elif marks >= 60:
    print("Grade C")  # runs if above conditions are false but this is true
else:
    print("Fail")  # runs if none of the conditions are true


# Looping Techniques (for loop)
# For loop → used to iterate over a sequence (list, string, range)

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)  # prints each number one by one

# using Range
for i in range(1, 6):
    print(i)  # prints numbers from 1 to 5

# while Loop
# while loop → runs until condition becomes false

count = 1

while count <= 5:
    print(count)  # prints current value of count
    count += 1     # increases count by 1 each time (important or loop will run forever)


# break → stops the loop completely
# continue → skips current iteration and moves to next
# pass → does nothing (placeholder)

for i in range(1, 6):

    if i == 3:
        continue  # skips number 3

    if i == 5:
        break  # stops loop when i becomes 5

    print(i)  # prints numbers except 3 and stops before 5



    # pass

    for i in range(1, 4):
        if i == 2:
            pass  # nothing happens here (used for future code)
        print(i)

# List Comprehension

# List comprehension

# normal way
squares = []
for i in range(1, 6):
    squares.append(i * i)

print(squares)

# same thing using list comprehension
# concise method (recommended)

squares = [i * i for i in range(1, 6)]  # creates list of squares
print(squares)

# List Comprehension with condition
# only even numbers square list

even_squares = [i * i for i in range(1, 11) if i % 2 == 0]
print(even_squares)  # prints squares of even numbers only