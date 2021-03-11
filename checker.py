# importing the regular expression module
import re

f_path = 'W:\\EDUCATION\Python Programming\\Coursera_Python Specialization Courses\\3.0_Using Python to Access Web Data\\regex_sum_1138828.txt'
#
# # opening the file handle
# with open(f_path, 'r', encoding='utf-8') as f:
#
# # storing the text content of file in a variable
#     txt = f.read()
#
# # compile the search pattern for strictly digits
# pattern = r'[0-9]+'
#
# # list all occurrences
# result = re.findall(pattern, txt)
#
# # convert each number in the result back into an integer format
# numbers = [int(n) for n in result]
# answer = sum(numbers)
#
# print(answer)

# using list comprehension
print(sum([int(n) for n in re.findall(r'[0-9]+', open(f_path, 'r', encoding='utf-8').read())]))