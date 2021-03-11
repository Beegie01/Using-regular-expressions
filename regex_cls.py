import re
import os

# importing a function in the fave_apps_funcs.py module in MyFuncs package
if 'C:\\Users\\welcome\\Desktop\\MyFuncs' not in os.sys.path:
    os.sys.path.append('C:\\Users\\welcome\\Desktop\\MyFuncs')

from fave_app_funcs import password_inp

class SumNums:

    def __init__(self):
        self.filename = None
        self.filepath = None
        self.result = None
        self.total = None


    def path_inp(self):
        while True:
            prompt1, prompt2 = '\nPlease enter name of file\n>\t', '\nPlease enter file path seperated by double backward slashes\n>\t'
            filename, f_path = password_inp(prompt1), password_inp(prompt2)

            return f_path, filename


    def open_file(self):
        '''
        to ensure that the given file path is in working condition
        retrieves the text from file in a string format
        and stores in a variable named 'txt'

        :returns --> file content in string format variable
        '''

        while True:
            # collect the filename/with path
            fp, f = self.path_inp()

            f_path = str(fp) + '\\' + str(f)

            with open(f_path, 'r', encoding='utf-8') as f:
                try:
                    txt = f.read()

                    # check to see if file was successfully copied
                    print(txt)
                    break
                except OSError:
                    print("ERROR!!!:\nPlease ensure that double backward slashes are given in file path")
                    continue

        self.filename, self.filepath = f, fp

        return txt


    def sum_nums(self, text):
        '''
        A function that reads through a file and sums up all the numbers contained within

        '''


        # compile the search pattern for strictly digits
        pattern = r'[0-9]+'

        # list all occurrences
        result = re.findall(pattern, text)

        # convert each number in the result back into an integer format
        numbers = [int(n) for n in result]
        self.result = numbers

        print(f"{len(numbers)} numbers found!\nMinimum 10 numbers: {sorted(numbers)[:10]}\nMaximum 10 numbers: {sorted(numbers)[-10:]}\
        \nNumbers Total: {sum(numbers)}")

        self.total = sum(self.result)

        return self.total