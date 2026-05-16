# Data Structures
# Lists 
# A list is an ordered collection that can be changed (mutable)
# =========================
# 1. LIST (Mutable, Ordered)
# =========================

print("===== LIST OPERATIONS =====")

fruits = ["apple", "banana", "mango"]
print("Original List:", fruits)

# INSERT (Add)
fruits.append("orange")
print("After Insert:", fruits)

# ACCESS (Read)
print("Access item:", fruits[0])

# UPDATE
fruits[1] = "grapes"
print("After Update:", fruits)

# DELETE
fruits.remove("mango")
print("After Delete:", fruits)


# =========================
# 2. TUPLE (Immutable, Ordered)
# =========================

print("\n===== TUPLE OPERATIONS =====")

colors = ("red", "green", "blue")
print("Original Tuple:", colors)

# ACCESS (Read only)
print("Access item:", colors[1])

# UPDATE (NOT DIRECTLY POSSIBLE → workaround)
temp_list = list(colors)
temp_list[1] = "yellow"
colors = tuple(temp_list)
print("After Update (converted):", colors)

# DELETE (NOT DIRECTLY POSSIBLE → workaround)
temp_list = list(colors)
temp_list.remove("blue")
colors = tuple(temp_list)
print("After Delete (converted):", colors)


# =========================
# 3. SET (Unordered, Unique)
# =========================

print("\n===== SET OPERATIONS =====")

A = {1, 2, 3}
print("Original Set:", A)

# INSERT (Add)
A.add(4)
print("After Add:", A)

# ACCESS (No indexing → only loop)
print("Access items:")
for item in A:
    print(item)

# UPDATE (remove + add)
A.remove(2)
A.add(20)
print("After Update:", A)

# DELETE
A.remove(1)
print("After Delete:", A)


# =========================
# 4. DICTIONARY (Key-Value)
# =========================

print("\n===== DICTIONARY OPERATIONS =====")

student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}
print("Original Dictionary:", student)

# INSERT (Add)
student["city"] = "Karachi"
print("After Insert:", student)

# ACCESS
print("Access name:", student["name"])

# UPDATE
student["age"] = 21
print("After Update:", student)

# DELETE
del student["grade"]
print("After Delete:", student)