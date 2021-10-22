import functools
def addTwoDigits(n):
    """
    You are given two strings pattern and s. The first string pattern contains only the symbols 0 and 1, and the second string s contains only lowercase English letters.

Let's say that pattern matches a substring s[l..r] of s if the following 3 conditions are met:

they have equal length;
for each 0 in pattern the corresponding letter in the substring is a vowel;
for each 1 in pattern the corresponding letter is a consonant.
Your task is to calculate the number of substrings of s that match pattern.
    """
    list2=[]
    with open("text.txt",'r+') as f:
        list1=f.readlines()
    mydict={}
    for item in list1:
        #item.strip()
        list2.append(item.strip().split(","))

    print(list2)
    list3=[]
    for i in range(1,len(list2)):
      list3.append(dict(zip(list2[i],list2[0])))
    print(list3)
    list1 = [int(ch) for ch in str(n)]
    sum2=functools.reduce(lambda x,y:x+y ,list1)
    list1 =[int(ch) for ch in str(n)]
    x=list(map(lambda x:x**2,[2,3,4,5,6,7,8]))
    print(x)
    print(sum2)
    sum1 =0
    for item in list1:
        sum1=sum1+item
        print(sum1)
    return sum1
if __name__=="__main__":
    print(addTwoDigits(29))
