Programs = '''
2021 Examples Interview
a. Given string print ch and its occurances as output
example: a="mmmaaannnnnjjuu" Output:"m3a3n5j2u2"
'''


###########################################################################################
###########################################################################################

import re
import os
import sys
import pytest

class Testpracticecases(object):

    @pytest.mark.stringsOp
    def test_stringOperations(self,s="manju is awesome"):
        """program to check whether the string is Symmetrical or Palindrome
        """
        if s == s[::-1]:
           print('True')
        else:
            print('False')

        #Reverse words in a given String in Python
        a=s.split()
        rev_string=""
        rev_string+=" ".join(item for item in a[::-1])
        print(rev_string)

        #Ways to remove i’th character from string in Python
        rem_s=s.replace(s[1],'')#removes all occurences
        rem_s=rem_s=s.replace(s[1],'',1)#removes 1 occurences
        print(s,rem_s)
        #Find length of a string in python (4 ways)
        print("Length of sting is:%s".format(len(s)))

        #Python – Avoid Spaces in string length
        print("Avoid Spaces in string length:",s.strip())
        '''
        Python program to print even length words in a string
        Python – Uppercase Half String
        Python program to capitalize the first and last character of each word in a string
        Python program to check if a string has at least one letter and one number
        Python | Program to accept the strings which contains all vowels
        Python | Count the Number of matching characters in a pair of string
        Python program to count number of vowels using sets in given string
        Python Program to remove all duplicates from a given string
        Python – Least Frequent Character in String
        Python | Maximum frequency character in String
        Python – Odd Frequency Characters
        Python – Specific Characters Frequency in String List
        Python | Frequency of numbers in String
        Python | Program to check if a string contains any special character
        Generating random strings until a given string is generated
        Find words which are greater than given length k
        Python program for removing i-th character from a string
        Python program to split and join a string
        Python | Check if a given string is binary string or not
        Python | Find all close matches of input string from a list
        Python program to find uncommon words from two Strings
        Python | Swap commas and dots in a String
        Python | Permutation of a given string using inbuilt function
        Python | Check for URL in a String
        Execute a String of Code in Python
    '''
    @pytest.mark.parametrize("test_input,expected", [("mmmaaannnjjjuuu", "m3a3n3j3u3")])
    def test_charcount(self,test_input,expected):
        """
        a. Given string print ch and its occurances as output
        example: a="mmmaaannnnnjjuu" Output:"m3a3n5j2u2"
        """
        try:
            import itertools
            res=""
            for item in itertools.groupby(test_input):
                res+=item[0]+str(len(list(item[1])))
            print(res)
            if res!=expected:
                    raise AssertionError(test_input,expected)

        except Exception as e:
             print("Exception as e",e)

    @pytest.mark.parametrize("input_ip", [("10.23.45.56")])
    def test_ipcheck(self, input_ip):
        # 1.Validate the ip adderess
        #input_ip = input('Enter the ip:')
        flag = 0

        pattern = "^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"
        match = re.match(pattern, input_ip)
        if (match):
            field = input_ip.split(".")
            for i in range(0, len(field)):
                if (int(field[i]) < 256):
                    flag += 1
                else:
                    flag = 0
        if (flag == 4):
            print("valid ip")
        else:
            print('No match for ip or not a valid ip')

    #########################################################################################
    @pytest.mark.parametrize("input_mail", [("manju23@gmail.com")])
    def test_mailcheck(self, input_mail):
        # 3.Validate the mail id

        #input_mail =
        pattern = "[^@]+@[^@]+"
        flag = 0
        match = re.match(pattern, input_mail)
        if (match):
            list1 = input_mail.split(".")
            print(list1)
            if (3 >= len(list1) > 1):
                flag = 1
            else:
                flag = 0
        if (flag == 1):
            print("Match found")
        else:
            print("Not a valid mail id")

    #########################################################################################
    @pytest.mark.parametrize("input_num", [("+1243567878")])
    def test_telephone(self,input_num):
        print("Validate US telephone number")
        #input_num = input('Enter the Telephone Number:')
        pattern = "^(\+)?(1)?(\s|-)?((\d{3})(-|\s)?){2}(\d{4})$"
        match = re.match(pattern, input_num)
        if match:
            print("Found telephone number")
        else:
            print("No match ")



    def test_numlines(self):
        # 4.To Count number of lines in file

        with open("text.txt", 'r') as f:
            print(len(f.readlines()))
            # or
        with open("text.txt", 'r') as f:
            print(sum(1 for _ in f))

    ##########################################################################################3

    def test_charfile(self):
        # 5.To count the character in file
        with open("text.txt", 'r') as f:
            count = 0
            for line in f:
                for word in line:
                    for ch in word:
                        count = count + 1
        print('Total characters in file', count)

    #########################################################################################

    def test_wordsfile(self):
        # 6.To count the  words in file
        with open("text.txt", 'r') as f:
            count = 0
            text = f.read()
            list2 = []
            list2 = re.findall("\w+", text)

        print('Total words in file', len(list2))


    def test_trailing(self):
        # 7.To remove trailing spaces in string
        string = "This is my world"
        long_string = ""
        list1 = string.split("\s")
        for i in list1:
            long_string+=i
        print(long_string)

    ###########################################################################################

    def test_endspace(self):
        # 8.To remove end and start spaces in string

        string1 = " This is spaces in begining and end  "
        print(string1)
        print(string1.strip())

    ############################################################################################

    def test_duplicate(self):
        # 9.Duplicate words in files, using sets.

        count = {}
        line = []
        with open("text.txt", 'r')as f:
            data = f.read()
            line = re.findall("\w+", data)

            for word in line:
                if word not in count:
                    count[word] = 1
                else:
                    count[word] += 1

        for word in count:
            # print (count[word])
            if count[word] > 1:
                print("The word {0} has occured {1} times in file".format(word, count[word]))

    ###########################################################################################

    def test_dupchar(self):
        # 10.find duclicate characters and replace in string

        string1 = "ringaringaroses"
        print(string1)
        count = {}
        for ch in string1:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1
                #   string1[ch]=""

        for word in count:
            if count[word] > 1:
                print("The word {0} has occured {1} times in file".format(word, count[word]))

    ###########################################################################################################3

    def test_duplist(self):
        print("To find duplicates in list")
        list1 = [1, 2, 3, 4, 5, 2, 6, 7, 8, 4]
        count = {}
        for num in list1:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        print(count)

        for i in count:
            if (count[i] > 1):
                print("The {0} has occured {1} times".format(i, count[i]))

        # Other way using the bubble sort method
        k = 1
        for i in range(0, len(list1) - 1):
            for j in range(k, len(list1)):

                if (list1[i] == list1[j]):
                    print("Duplicate found:", list1[i])
                    # continue
            k += 1

    #########################################################################################33
    def test_fact1(self):
        # 11.factorial without recoursion

        n = 5
        fact = 1
        while (n > 0):
            if (n == 0) or (n == 1):
                fact *= 1
                break;
            else:
                fact *= n
                n = n - 1
        print("The factorial of number is", fact)

    ###########################################################################################################
    def test_listofdict(self):
        list1 = []
        listall = []
        dict1 = {}
        d = {}

        with open("text2.txt", 'r') as f:
            header = f.readline().strip()
            keys = []
            keys = header.split("\t")
            print(keys)
            for line in f:
                list1 = line.strip().split("\t")
                # print (list1)
                listall.append(list1)

        print(listall)

        # Transpose of listall is mat2
        mat2 = []
        for col in range(0, len(listall[0])):
            mat1 = []
            for row in range(0, len(listall)):
                mat1.append(listall[row][col])
            mat2.append(mat1)
        print('Matrix after transpose', mat2)

        # Dictionay of lists
        for i in range(0, len(keys)):
            d[keys[i]] = mat2[i]
        print(d)

        # list of dictionaries

        list1 = []

        for i in range(0, len(listall)):
            d1 = {}
            for j in range(0, len(listall[0])):
                d1[keys[j]] = listall[i][j]
            print(d1)
            list1.append(d1)
        print(list1)

    '''
    #Using zip,map,and dict
        d = dict(zip(keys, map(list, zip(*listall))))
        print(d)
        list2 = []
        for i in range(0, len(listall)):
            dict1 = dict(zip(keys, listall[i]))
            list2.append(dict1)
        print(list2)
    '''

    #####################################################################################################################

    def test_listofdict1(self):
        import re

        list1 = []
        list2 = []
        listall = []
        keys = []
        dict1 = {}
        d = {}

        with open("test2.txt", 'r') as f:
            for line in f:
                keys = re.findall("\w+", line)
                for item in f:
                    listall.append(re.findall("\w+", item))

        d = dict(zip(keys, map(list, zip(*listall))))
        print(d)



        ################################################################################################################

    def test_Datatypesdemo(self):
        print('hello World')
        # integer variables
        a = 10
        print(a)

        # String Variables
        msg = "Hi this is my first program"
        print(msg)
        # String Operations

        print(len(msg))
        print(msg.capitalize())
        print(msg.isalpha())
        # This converts string into list
        words = msg.split()
        # list variables which stores array of values
        print(words)
        names = ['manju', 'rishi', 'Ravi', 'pavan', 'mom', 'dad']
        values = ['12', '23', '45', '65', '6', '7', '7']
        # print values
        for i in values:
            print(i)
        new_list = words + names
        print(new_list)

        # list operations
        values.append(78)
        print(values)
        # values.extend(34)
        values.insert(3, 64)
        print(values)
        # values.remove(12)
        values.pop()
        print(values)
        # values.index(3,)
        print(values.count(64))
        print(values)
        values.sort(cmp=None, key=None, reverse=False)
        print(values)
        values.reverse()

        print(values)

        # Dictionaries

        states = {'Karnataka': 'KA', 'Delhi': 'DL', 'Madya pradesh': 'MP'}
        print(states)

        print(states['Karnataka'])

        for keys in states:
            print(states[keys])

    ############################################################################################

    def test_squareroot(self):
        num = int(input('Enter the number :'))
        x = num / 2
        i = 1
        flag = 1
        while (i < x):
            if (i * i == num):
                print("{0} is the square root of {1}".format(i, num))
                flag = 0
                break
            i = i + 1
        if (flag == 1):
            print("{0} is not a perfect square".format(num))

    #################################################################################################
    def test_printrangenumbers(self):
        i = 1

        def recur(i):
            if (i < 100):
                print(i)
                i = i + 1
                recur(i)

        recur(1)

    ####################################################################################################3

    def test_listavg(self):
        list2 = [1, 2, 3, 4, 5]
        count = int(input('Enter the number of items you want in list:'))
        list1 = []
        cnt = 0
        for i in range(0, count):
            i = int(input('Enter the number :'))
            list1.append(i)

        for i in list1:
            for j in list2:
                if i == j:
                    cnt = cnt + 1
            if (cnt == 0):
                break

        sum1 = 0
        if (cnt == count):
            for i in list1:
                sum1 = sum1 + i
            print('Average of list items is:', (sum1 / cnt))
        else:
            print("All the given elemnts not present in original list")

    #############################################################################################################

    def test_fib(self, n):
        x = 0
        y = 1
        if (n == 0):
            return 0
        if (n == 1):
            return 1
        if n > 1:
            print(fib(n - 1), fib(n - 2))
            return (fib(n - 1) + fib(n - 2))
        print('Fibonaci series', fib(4))

    ############################################################################################

    def test_fileexists(self):
        # 13.File exists

        if os.path.isfile("text.txt"):
            print("File Exists")
        else:
            print("Not a file")

    ###############################################################################################

    def test_transposematrix(self):
        matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        print('Matrix before transpose', matrix1)
        mat2 = []
        for col in range(0, len(matrix1[0])):
            mat1 = []
            for row in range(0, len(matrix1)):
                mat1.append(matrix1[row][col])
            mat2.append(mat1)
        print('Matrix after transpose', mat2)

        mat4 = [[matrix1[row][col] for row in range(0, len(matrix1))] for col in range(0, len(matrix1[0]))]
        print(mat4)

    ##############################################################################################
    def test_listtoset(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

        s = set(list1)
        print(s)

    #####################################################################################################################
    import unicodecsv

    def test_accesscsv(self):
        print("CSV reading")
        datacsv = [{'firstnam': 'manju', 'sirname': 'thimmareddy', 'hobby': 'writing', 'age': '29'},
                   {'firstnam': 'rishi', 'sirname': 'shereddy', 'hobby': 'dancing', 'age': '3'},
                   {'firstnam': 'ravi', 'sirname': 'chandra', 'hobby': 'reading', 'age': '33'}]

        # Accessing without module

        for ele in datacsv:
            for word in ele:
                print(word, ele[word])

    #####################################################################################################

    def test_reversestr(self):
        string1 = "manju"
        print(string1[::-1])
        '''
        i=0
        j=len(string1)-1
        while(i!=j):
            tmp=string1[i]
            string1[i]=string1[j]
            string1[j]=tmp
            i=i+1
            j=j-1
        print(string1)
        '''

    #############################################################################################

    def test_reversestring(self):
        str1 = input('Enter the String')
        str2 = ""
        # j=0
        i = len(str1) - 1
        while (i >= 0):
            str2 += str1[i]
            # print (str2)
            # j=j+1
            i = i - 1
        print("{0} is original,{1} is reverse of string".format(str1, str2))

    #######################################################################################################

    def test_maxvaluelist(self):
        employment = [23.4, 67.0, 56.7, 23.0, 56.8, 65.6, 76.7, 34.4, 45.6]
        max_value = 0
        index = 0
        for value in range(len(employment)):
            # print("ths country {0} has {1} employmentrate".format(countries[value],employment[value]))
            if (employment[value] > max_value):
                max_value = employment[value]
                index = value
        print("Maximum employment value is {0} has index : {1} ".format(max_value, index))

    ###########################################################################################################
    import os.path
    import os

    def test_findfile(self):
        # path1=os.getcwd()
        search_file = input('Enter the file name:')

        # path1=input('Enter the path u want to search')
        # find(path1)
        # flag=0

        def find(path1):
            flag = 0
            pathname = path1
            dirlist = os.listdir(path1)
            # print (dirlist)
            for file1 in dirlist:
                if file1 == search_file:
                    flag = 1
                    break
            for file1 in dirlist:
                if os.path.isdir(file1) and flag == 0:
                    find(os.path.join(path1, file1))

            if (flag == 1):
                print("File Found in current directory {0}".format(path1))
            else:
                print("File not Found in current directory {0}".format(path1))

            find('C:\\Users')

    ####################################################################################################################333
    def test_read_csv(self, filename):
        list1 = []
        with open(filename, 'r') as f:
            reader = unicodecsv.DictReader(f)
            for row in reader:
                list1.append(row)
                # list1=list(reader)
        print(list1)

    #############################################################################################
    def test_generators_square(self):
        # list1 = []
        def test_square():
            for x in range(1, 100):
                yield (x * x)  # keeps the eleemnt one at time hence performance is much better
                # list1.append(x*x)
                # print(list1)

        numlist1 = [x * x for x in range(1, 25)]  # list comprehension
        numlist2 = (x * x for x in range(25, 50))  # using Generators
        list2 = list(numlist2)  # convert generators to list
        print(list2)
        print(numlist2)  # you cant access eleemnts all at time
        # numlist=square()
        # print(numlist1)

        for num in numlist2:  # Generators ar accessed this way
            print(num)

        list2 = [x for x in range(1, 100) if all(x % j != 0 for j in range(2, x))]
        print("Prime numbers list from 1-100", list2)

        list2 = [x for x in range(1, 100) if x % 3 == 0]
        print("Multiple of 3", list2)

    ##################################################################################################
    def test_seclarmatrix(self):
        list1 = [[8, 2, 3], [3, 4, 5], [6, 7, 8], [56, 67, 78], [23, 34, 12], [1, 11, 23]]

        final = []
        for col in range(0, len(list1[0])):
            tran = []
            for row in range(0, len(list1)):
                tran.append(list1[row][col])
            final.append(tran)
        print(final)

        for i in range(0, len(list1[0])):
            list3 = sorted(final[i])
            print("Second largets in {0} column  is {1}".format(i, list3[len(list3) - 2]))

    #######################################################################################################

    def test_stringlen(self):
        list1 = ['hello', 'anja', 'manjum', 'rishi', 'ravi', 'runr']
        print(sorted(list1))
        cnt = 0
        cnt1 = 0
        for i in list1:
            if len(i) > 2:
                cnt = cnt + 1
                # print(cnt)
                if (i[0] == i[len(i) - 1]):
                    cnt1 = cnt1 + 1
        print(
            "{0} list items have length greater that \"two\" and {1} have first and last character same".format(cnt,
                                                                                                                cnt1))

    ############################################################################################
    ############################################################################################

    def test_sortstirng(self):
        s = "Bobble bolly"
        s1 = 'BALL'
        print(s1.lower().upper())
        c = ''.join(sorted(set(s)))  # sorts the string and keeps them distint
        print(c)
        c1 = ''.join(sorted(s))  # sorts and keep duplicates
        print(c1)
        print(''.join(sorted(set(s.lower()))).strip())  # to get rid of begining and end spaces

        #############################################################################################

    def test_stringmatch(self):
        list1 = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
        list2 = []
        list3 = []
        for i in list1:
            if i[0] == 'x' or i[0] == 'X':
                list2.append(i)
            else:
                list3.append(i)
        # print()
        print(list2 + sorted(list3))

        ################################################################################################

    def test_bubblesort(self):
        list1 = [15, 14, 3, 2, 1, 8, 9, 1, 4, 6, 19, 21, 13, 14, 16]

        for i in range(0, len(list1) - 1):
            for j in range(i + 1, len(list1)):
                if (list1[i] > list1[j]):
                    tmp = list1[j]
                    list1[j] = list1[i]
                    list1[i] = tmp
        print(list1)

        #######################################################################################################################

    def test_tuplesort(self):
        list1 = [(1, 7), (1, 3), (3, 4, 5), (2, 2), (4, 5, 6), (1, 2, 3), (3, 5, 7)]

        for i in range(0, len(list1) - 1):
            for j in range(i + 1, len(list1)):
                if (list1[i][len(list1[i]) - 1] > list1[j][len(list1[j]) - 1]):
                    tmp = list1[j]
                    list1[j] = list1[i]
                    list1[i] = tmp
        print(list1)

        ##############################################################################################

    def test_both_ends(self):
        # +++your code here+++
        s = "manjuisawesome"
        s1 = ''
        if (len(s) <= 2):
            print(' ')
        else:
            s1 = ''.join(s[0])
            s1 += ''.join(s[1])
            s1 += ''.join(s[len(s) - 2])
            s1 += ''.join(s[len(s) - 1])
            print(s1)
            # return s1'''

        ##################################################################################################

    def test_fix_start(self):
        # +++your code here+++
        s = "rishiissmart"
        s1 = list(s)  # string has to converted to list for character teplacement
        count = {}
        print(s.count('r'))  # inbuilt function to count charachter occurances in string
        print(s.rstrip())
        print(s.lstrip())
        print(s.strip())

        # tmp=s[0]
        # s1[0]='M'

        for ch in range(0, len(s1)):
            if s1[ch] not in count:
                count[s1[ch]] = 1
            else:
                count[s1[ch]] = count[s1[ch]] + 1
                # print(s[ch])
                s1[ch] = '*'
        s = ''.join(s1)
        print(s)

        ################################################################################################

    def test_mix_up(self):
        a = input('Enter string 1')
        b = input('Enter second string')
        s1 = list(a)
        s2 = list(b)
        tmp1 = s1[0]
        tmp2 = s1[1]
        s1[0] = s2[0]
        s1[1] = s2[1]
        s2[0] = tmp1
        s2[1] = tmp2
        a = ''.join(s1)
        print(a)
        b = ''.join(s2)
        # print(b)
        print(a + " " + b)
        # print(a)

        #####################################################################################################

    def test_list_merge(self):
        list1 = [1, 2, 3, 4, 5, 6]
        list2 = [4, 5, 6, 7, 8, 9]
        # print(list1.append(list2)) #append complete list inside list
        list1.extend(list2)  # Extend will add eleemnt at end of list,end is  1D list

        print(list1)
        print(sorted(list1))

        # print(sorted(list1+list2))

        #################################################################################################

    def test_conseqdup(self):
        list1 = [1, 2, 2, 3, 4, 5, 5, 6, 7, 2, 3, 5]
        list2 = []
        for i in range(0, len(list1) - 1):
            j = i + 1
            if (list1[i] == list1[j]):
                continue
            else:
                list2.append(list1[i])
        print(list2)

        #####################################################################################################

    def test_front_back(self):
        # +++your code here+++
        a = input('Enetr the string1 :')
        # b=input('Enter the string2 :')
        afront = ""
        aback = ""
        if (len(a) % 2 == 0):
            lena1 = len(a) / 2
            for i in range(0, int(len(a) / 2)):
                afront += a[i]
            for i in range(int((len(a) / 2)), int(len(a))):
                aback += ''.join(a[i])
        else:
            for i in range(0, int(len(a) / 2) + 1):
                afront += ''.join(a[i])
            for i in range(int(len(a) / 2) + 1, int(len(a))):
                aback += ''.join(a[i])
        print(afront, aback)

        return

        ###############################################################################################

    def test_not_bad(self):
        # +++your code here+++
        # refer string.find()
        s = input('Enter the string:')
        s1 = ""
        pat = r"not(\s|\w)+bad"
        re.search(pat, s)
        if (re.search(pat, s)):
            s1 = re.sub(pat, "good", s)
        print(s1)

        ###################################################################################################

    def test_verbing(self):
        s = input('Enter the String')
        if (len(s) > 3 and s[len(s) - 3:len(s)] != 'ing'):
            s += ''.join('ing')
            print(s)
        elif (len(s) > 3) and s[len(s) - 3:len(s)] == 'ing':
            s += ''.join('ly')
            print(s)
        elif (len(s) < 3):
            print('String length less than 3 characters')
            # +++your code here+++

    ###############################################################################################
    def test_rem_dup(self):
        list1 = [1, 2, 3, 3, 3, 4, 5, 5, 1, 2, 1, 1, 1, 3, 3, 3, 4, 5, 5, 1, 2]
        list2 = []
        count = {}

        for i in range(0, len(list1)):
            if list1[i] not in count:
                count[list1[i]] = 1
                list2.append(list1[i])
            else:
                count[list1[i]] += 1
                # del list1[i]
        print(list2)

        ##################################################################################################

    def test_fib(self):
        def fibo(n):
            # n=int(input('Enter the number'))
            if (n == 0):
                return 0
            else:
                x = 0
                y = 1
                for i in range(1, n):
                    z = (x + y)
                    x = y
                    y = z
                return y

        for i in range(10):
            print(fibo(i))

        ###################################################################################################

    def test_special_builtin(self):
        from functools import reduce

        # The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.
        # The pass statement is a null operation; nothing happens when it executes.

        def passdemo():
            pass

        passdemo()
        list1 = [1, 2, 3]
        list2 = [2, 3, 4]
        list3 = [1, 2, 4]
        list4 = [3, 4, 5]

        # lambda is fuction used to create the anynymous fuction without actully creating it,ie it not bound to name
        # at runtime ,it integrated with filter ,map,reduce
        g = lambda x: x * 2

        print("Using the lambda", g(5))

        # The map(aFunction, aSequence) function applies a passed-in function to each item in an
        # iterable object and returns a list containing all the function call results.

        list2 = list(map(lambda x: x ** 2, list1))
        print("List of items with squares using map and lamda", list2)

        def squares(x):
            return (x * x)

        print("List of items with squares using map", list(map(squares, list1)))

        # The built-in filter() function operates on any iterable type (list, tuple, string, etc).
        # It takes a function and an iterable as arguments. filter() will invoke the function on each element of the iterable,
        # and return a new iterable composed of only those elements for which the function returned True.
        print("Filter on true return using Filter", list(filter(lambda x: x % 2 == 0, list1)))

        # Reduce is a really useful function for performing some computation on a list and returning the result integerr.
        # For example, if you wanted to compute the product of a list of integers.
        sum1 = reduce((lambda x, y: x + y), [1, 2, 3, 30])
        print("Sum of list using reduce", sum1)

        product = reduce((lambda x, y: x * y), [1, 2, 3, 30])
        print("Product using the reduce", product)

        # Zip function to traverse 2 list items at time

        list1 = [1, 2, 3]
        list2 = [2, 3, 4]
        for a, b in zip(list1, list2):
            print("items of 2 list", a, b)

        list3 = [list1, list2]
        print(list3)
        print(list(zip(*list3)))  # to transpose the list use zip(*values)

        # print(listb)
        print("sum of lists", reduce(lambda x, y: x + y, list1))

        '''You can roughly think of any and all as series of logical or and and operators, respectively.
        any will return True when atleast one of the elements is Truthy. Read about Truth Value Testing.
        all will return True only when all the elements are Truthy.
        '''
        list2 = [x for x in range(1, 100) if all(x % j != 0 for j in range(2, x))]
        print("Prime numbers list from 1-100", list2)

    def test_quicksort(self):
        array1 = [12, 4, 5, 6, 7, 3, 1, 15]

        def sort(array):
            less = []
            equal = []
            greater = []

            if len(array) > 1:
                pivot = array[0]
                for x in array:
                    if x < pivot:
                        less.append(x)
                    if x == pivot:
                        equal.append(x)
                    if x > pivot:
                        greater.append(x)

                print(less, equal, greater)
                # Don't forget to return something!
                return sort(less) + equal + sort(greater)  # Just use the + operator to join lists
            # Note that you want equal ^^^^^ not pivot
            else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
                return array

        print(sort(array1))

        ####################################################################################################

    def test_rev_list(self):
        array1 = [12, 4, 5, 6, 7, 3, 1, 15]

        print("Reverse of list without any function", array1[::-1])
        print("Reverse of list using builtin reversed", list(reversed(array1)))

        ###############################################################################################

    def test_msort(self, x):
        result = []
        if len(x) < 20:
            return sorted(x)
        mid = int(len(x) / 2)
        y = test_msort(x[:mid])
        z = test_msort(x[mid:])
        i = 0
        j = 0
        while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
        result += y[i:]
        result += z[j:]
        print("Sorted array using merge sort", result)

        #############################################################################################################3

    def test_webscrape(self):
        from bs4 import BeautifulSoup as soup
        from urllib.request import urlopen

        url = "https://www.amazon.com/b/ref=s9_acss_bw_tt_x_sgui_shoul_w?node=16313235011&lo=fashion&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=T6GD9F4805AHQVWZXP88&pf_rd_t=101&pf_rd_p=d847fc3d-f4c2-402b-b544-738f8def323e&pf_rd_i=1045024"

        uclient = urlopen(url)
        page_html = uclient.read()

        uclient.close()
        # soup is created, all the html content is stored in the soup
        page_soup = soup(page_html, "html.parser")

        # We can now print out the HTML content of the page, formatted nicely, using the prettify method on the BeautifulSoup object:
        print(page_soup.prettify())

        # print(page_soup.div)
        container = page_soup.findAll('div', attrs={'class': "name"})
        print(container[0])

    def test_csvread(self):
        print("################Without using modules########################3")
        keys = []

        with open("test.csv", 'r') as f:
            keys = f.readline().strip().split(',')
            print(keys)
            for line in f:
                print(line.strip().split(','))

        import csv
        print("################Using csv modules########################3")
        with open("test.csv", 'r', newline='') as f:
            read = csv.reader(f)
            header = next(read)  # extract the header in csv

            for line in read:
                print(line)

        ###################################################################################3############3
    def test_dicitems(self):
        dict1 = {'one': 1, 'two': 2, 'three': 3}

        for k, v in dict1.items():
            print("key and vales are", k, v)

        for k in dict1.keys():
            print("keys are", k)

        for v in dict1.values():
            print("Values are:", v)

        '''
        As you are in python3 , use dict.items() instead of dict.iteritems()
        iteritems() was removed in python3, so you can't use this method anymore.
        Take a look at Python Wiki (Link)
        In Built-in Changes part, it is stated that
        Removed dict.iteritems(), dict.iterkeys(), and dict.itervalues().
        Instead: use dict.items(), dict.keys(), and dict.values() respectively.
        '''

        # for k,v in dict1.iteritems(): throws an error as its removed in python 3

    ################################################################################################################3
    def test_linearsearch(self):
        list1 = [2, 3, 4, 5, 6, 7, 81, 2, 3, 41]

        num = int(input('enter the number to be searched:'))

        for i in range(0, len(list1)):
            if (num == i):
                flag = 1
                # print("Found")
                break
            else:
                flag = 0
        if (flag == 1):
            print("Found")
        else:
            print("Not found")

    #################################################################################################
    def test_argparserdemo(self):

        parser = argparse.ArgumentParser()

        parser.add_argument("Search_criteria", help="Specify the what based Search")
        parser.add_argument("pattern", help="search pattern")
        parser.add_argument("-o", "--out", help="search option specific")
        args = parser.parse_args()

        print(args.Search_criteria)
        print(args.pattern)

        if int(args.Search_criteria) == 1:
            result = searchbasedonfilename(args.pattern, sys.argv[3])
        elif int(args.Search_criteria) == 2:
            result = searchbasedonfilecontent(args.pattern)
        elif int(args.Search_criteria) == 3:
            result = searchbasedondate(args.pattern)
        elif int(args.Search_criteria) == 4:
            result = searchbasedonsize(args.pattern)
        elif int(args.Search_criteria) == 5:
            result = searchbasedontypeoffile(args.pattern)
        else:
            print("Search criteria range from 1-5")



    ##########################################################################################

    def test_prime(self):
        # 12.Given list ,prime numbers with generators and witout generators

        list1 = [2, 3, 2, 34, 23, 17, 11, 56, 25, 44, 99, 7]

        # Using the list comphrensions

        prime1 = [x for x in list1 if all(x % y != 0 for y in range(2, x))]
        print("Prime numbers {0}".format(prime1))

        # Withouut using comprehensions
        for i in list1:
            if (i == 3) or i == 5 or i == 2:
                print("{0} Prime number".format(i))
                continue
            if (i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
                print("{0} Not prime".format(i))
            else:
                print("{0} is Prime".format(i))

                # other way of doing
        list2 = []
        for i in range(1, 100):
            flag = 0
            for j in range(2, i):
                if (i % j) == 0:
                    flag = 1
                    continue
            if (flag == 0):
                list1.append(i)
        print("{0} Prime number list".format(list1))

    def test_prime(self):
        # 12.Given list ,prime numbers with generators and witout generators

        list1 = [2, 3, 2, 34, 23, 17, 11, 56, 25, 44, 99, 7]

        # Using the list comphrensions

        prime1 = [x for x in list1 if all(x % y != 0 for y in range(2, x))]
        print("Prime numbers {0}".format(prime1))

        # Withouut using comprehensions
        for i in list1:
            if (i == 3) or i == 5 or i == 2:
                print("{0} Prime number".format(i))
                continue
            if (i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
                print("{0} Not prime".format(i))
            else:
                print("{0} is Prime".format(i))

                # other way of doing
        list2 = []
        for i in range(1, 100):
            flag = 0
            for j in range(2, i):
                if (i % j) == 0:
                    flag = 1
                    continue
            if (flag == 0):
                list1.append(i)
        print("{0} Prime number list".format(list1))

