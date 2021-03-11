from regex_cls import SumNums

import os

# importing a function in the fave_apps_funcs.py module in MyFuncs package
if 'C:\\Users\\welcome\\Desktop\\MyFuncs' not in os.sys.path:
    os.sys.path.append('C:\\Users\\welcome\\Desktop\\MyFuncs')

from fave_app_funcs import num_inp

prompt = "\nHow many operations do you wish to carry out?\n>\t"
num = num_inp(prompt)

objs = {}
for n in range(num):

    while True:
        obj = SumNums()

        txt = obj.open_file()

        obj.sum_nums(txt)

        break

