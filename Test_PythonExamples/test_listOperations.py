import pytest

class Testlistpracticecases(object):
    def test_listOperations(self,a=[1,2,3,4,5,6]):

        #Python program to interchange first and last elements in a list
        print([a[-1]]+a[1:len(a)-1]+[a[0]])
        #Python program to swap two elements in a list
        a[4],a[2]=a[2],a[4]
        print('List after swaping:%s',a)

        #Python – Swap elements in String list
        test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

        print("The original list is : " + str(test_list))

            # Swap elements in String list
            # using replace() + list comprehension
        res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]
        print("List after performing character swaps : " + str(res))

        #Python Program to count unique values inside a list
        a=[1,2,2,2,3,4,5,5,5,5]
        print(len(list(set(a))))
        # Python – List product excluding duplicates
        import functools
        #print(list(map(lambda x:x*x, list(set(a)))))
        print(functools.reduce(lambda x,y: x * y, list(set(a))))
        #print(product)

        """ 
                    
            Python Program to count unique values inside a list
            Python – List product excluding duplicates
            Python – Extract elements with Frequency greater than K
            Python – Test if List contains elements in Range
            Python program to check if the list contains three consecutive common numbers in Python
            Python program to find the Strongest Neighbour
            Python Program to print all Possible Combinations from the three Digits
        """

