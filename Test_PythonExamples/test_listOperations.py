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
             # Swap elements in String list using replace() + list comprehension
        res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]
        print("List after performing character swaps : " + str(res))

        #Python Program to count unique values inside a list
        a=[1,2,2,2,3,4,5,5,5,5]
        print(len(list(set(a))))

        # Python – List product excluding duplicates
        import functools
        #print(list(map(lambda x:x*x, list(set(a)))))
        print(functools.reduce(lambda x,y: x * y, list(set(a))))

        #Python – Extract elements with Frequency greater than K
        from collections import Counter
        k=3
        mydict=dict(Counter(a))
        print(mydict)
        print({key:val for key,val in mydict.items() if mydict[key]>k })

        # Python program to check if the list contains three consecutive common numbers in Python
        from itertools import groupby
        print([item[0] for item in groupby(a) if len(list(item[1]))>3])

        #Python program to find the Strongest Neighbour
        a=[4,5,1,2,3,8,9,6,7,1]
        print([val for i,val in enumerate(a) if val==max(a[i:])])
        #Python Program to print all Possible Combinations from the three Digits
        a=[1,2,3] #output:(1, 2, 3)(1, 3, 2)(2, 1, 3)(2, 3, 1)(3, 1, 2)(3, 2, 1)
        from itertools import permutations
        print(list(permutations(a,3)))

        # Python – Test if List contains elements in Range #True or False
        test_list = [4, 5, 6, 7, 3, 9]
        # Initialization of range
        i, j = 3, 10
        print(all(item>=i and j>item for item in test_list))


