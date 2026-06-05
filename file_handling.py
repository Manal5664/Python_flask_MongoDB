# ============================================
# WORKING WITH FILES & REGULAR EXPRESSIONS
# # ============================================
# ython mein file read karne ke advantages:

# Data access: File se text, CSV, JSON, logs, ya config data easily read kar sakte hain.
# Automation: Manual kaam kam hota hai, jaise reports read karna, records process karna, ya logs analyze karna.
# Large data handling: Python files se large data step-by-step read kar sakta hai, poori file memory mein load karna zaroori nahi.
# Reusability: Ek baar file mein data save ho jaye to program baar baar use kar sakta hai.
# Data analysis: File read karke data cleaning, calculations, charts, aur machine learning mein use kar sakte hain.
# Easy syntax: Python mein open(), read(), readline(), aur readlines() se file reading simple hoti hai.

# ============================================
# 1. INTRODUCTION TO FILE HANDLING
# ============================================
# File Handling ka matlab hai Python ki madad se files ko
# open, read, write aur close karna.

# File Open Karna (Read Mode)
file = open("file.txt", "r")

# File Close Karna
file.close()


# Recomenmded Method: with statement
# Is method mein file automatically close ho jati hai.

with open("file.txt", "r") as file:
    data = file.read()
    print(data)


# ============================================
# 2. READING TEXT FILES
# ============================================


# Ek Line Read Karna

with open("file.txt", "r") as file:
    line = file.readline()

print(line)


# Sab Lines List Mein Read Karna

with open("file.txt", "r") as file:
    lines = file.readlines(2)

print(lines)


# ============================================
# 3. WRITING TEXT FILES
# ============================================
# "w" mode nayi file banata hai ya purani file ka
# content overwrite kar deta hai.

with open("file.txt", "w") as file:
    file.write("I am learning Python")


# ============================================
# APPENDING DATA TO A FILE
# ============================================
# "a" mode file ke end mein data add karta hai.

with open("file.txt", "a") as file:
    file.write("\nI am learning File Handling")


# ============================================
# 4. WORKING WITH CSV FILES
# ============================================
# CSV = Comma Separated Values


import csv


# CSV File Read Karna

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# CSV File Write Karna

with open("std.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age"])
    writer.writerow(["Ali", 20])
    writer.writerow(["Sara", 22])


# ============================================
# 5. INTRODUCTION TO REGULAR EXPRESSIONS (REGEX)
# ============================================
# Regex text ko search aur manipulate karne ke liye use hota hai.

import re


# ============================================
# 6. SEARCH A WORD
# ============================================
# re.search() kisi text mein word dhoondta hai.

text = "I love Python"

result = re.search("Python", text)

print(result)


# ============================================
# 7. FIND ALL MATCHES
# ============================================
# re.findall() tamam matching values return karta hai.

text = "cat bat rat"

result = re.findall("at", text)

print(result)


# ============================================
# 8. FIND DIGITS
# ============================================
# \d ka matlab hai digit (0-9)

text = "My age is 25"

result = re.findall(r"\d", text)

print(result)


# ============================================
# 9. EXTRACT EMAIL ADDRESS
# ============================================
# Regex ki madad se email extract kar sakte hain.

text = "Contact: manal@gmail.com"

email = re.findall(r"\S+@\S+", text)

print(email)


# ============================================
# 10. REPLACE TEXT
# ============================================
# re.sub() kisi text ko replace karta hai.

text = "I like python"

new_text = re.sub("python","Java", text)

print(new_text)


# ============================================
# COMMON REGEX SYMBOLS
# ============================================
#
# \d  -> Digit (0-9)
# \w  -> Letter, Digit, Underscore
# \s  -> Space
# .   -> Any Character
# +   -> One or More Occurrences
# *   -> Zero or More Occurrences
# ^   -> Start of String
# $   -> End of String
#
# ============================================


# ============================================
# REAL-WORLD EXAMPLE
# ============================================
# File Handling -> File Read Karega
# Regex -> Data Extract Karega
# CSV -> Data Spreadsheet Format Mein Save Karega
#
# Example:
#
# Ali is 20 years old
# Sara is 22 years old
# Ahmed is 19 years old
#
# Regex age numbers extract kar sakta hai.
# CSV unko table format mein save kar sakta hai.
# ============================================