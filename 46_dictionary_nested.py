"""
Nested Dictionary

1. Nested Dictionary: Nesting Dictionary means putting a dictionary inside another dictionary.
2. It's a collection of dictionary into one single dictionary

"""

course = {
    "python": {"duration": "3 month", "fees": "9000"},
    "php": {"duration": "2 month", "fees": "4000"},
    "java": {"duration": "4 month", "fees": "8000"}
}

# print(course['python'])
# print(course['python']["duration"])

# for i in course:
#     print(i, course[i])

# for j,k in course.items():
#     print(j, k)
#
# for a,b in course.items():
#     print(a, b['duration'], b["fees"])


# course["java"]["fees"] = 20000
#
# print(course)

del course["python"]["duration"]
print(course)
