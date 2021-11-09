import pytest

class Teststringspractice(object):
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

        #Python program to print even length words in a string
        print([item for item in s.split() if len(item)%2==0])

        #Python – Uppercase Half String
        i=len(s)//2
        print(s[:i].upper()+s[i:])

        #Python program to capitalize the first and last character of each word in a string
        a=[item[0].upper()+item[1:len(item)-2]+item[len(item)-1].upper() for item in s.split()]
        print(a)

        #Python | Convert numeric words to numbers
        help_dict = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'zero': '0'
        }

        # initializing string
        test_str = "zero four zero one"
        print("".join(help_dict[item] for item in test_str.split()))
        #Python | Word location in String
        test_str = 'geeksforgeeks is best for geeks'

                  # printing original string
        print("The original string is : " + test_str)
                  # initializing word
        wrd = 'best'

        for i,val in enumerate(test_str.split()):
            if val == wrd:
                print('index of search string:',i)
        #Python | Consecutive characters frequency
            import itertools
            test_str = "geekksforgggeeks"
            print("The original string is : " + test_str)# printing original string
            res=""
            res +="".join(i+str(len(list(j))) for i, j in itertools.groupby(test_str))
            print("The Consecutive characters frequency : " + str(res))  # printing result
        '''
        String slicing in Python to rotate a string
        s = "GeeksforGeeks"
        d = 2

        Output: Left
        Rotation: "eksforGeeksGe"
        Right
        Rotation: "ksGeeksforGee"
        '''
        s = "GeeksforGeeks"
        d=2
        print("Left rotation by 2:",s[d:]+s[0:d])
        print("Right rotation by 2:", s[len(s)-2:] + s[0:len(s)-2])

        #String slicing in Python to check if a string can become empty by recursive deletion
        str1 = "GEEGEEKSKSLKGEEKSeirietGEEKS"
        sub_str = "GEEKS"
        str2=""
        x=1
        while x<=len(str1) and len(str1)!=0:
            str1=str1.replace(sub_str,"")
            x=x+1
            print(str1,x)

        if len(str1)==0:
            print("After replacement:",len(str1),True)
        else:
            print("After replacement:", str1, False)

        '''
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