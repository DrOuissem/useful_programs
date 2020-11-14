def question1():
    n=1
    s=0
    while n<10:
        s+=n #s=45
        n+=1 #n=10
    print(s)
#question1()
#question1()

#fruits=['Orange','Banana','Coconut','Strawberry']
#print(fruits[0:4])
#print(fruits[-1:-4:-2])

def question2():
    fruits=['Orange','Banana','Coconut']
    n=-1
    f=fruits[n]
    while f!="Banana":
        n=n-1 #n=-1 -1 = -2
        f=fruits[n] #f='Banana'
        print(f)

#question2()

def question3():
    l=['abc','bcb','aab','oooo','123','1221']
    res=[]
    for word in l:
        if len(word)>=3 and word[0]==word[-1]:
            res.append(word)
    print("The number of strings that fulfill the conditions in the following\n"
          "list",l,"is:",len(res),"\n And the strings are :",res)
#question3()

def palindrome(word):
    for c in range(0,len(word)//2):
        if word[c]!=word[-1-c]:
            print("No")
            return
    print("Yes")

#word='abccba'


def palindrome2(word):
    reverse=word[::-1]
    if reverse == word:
        print("Yes")
    else:
        print("No")

#palindrome2('abcba1')

def create_palindrome(word):
    res=word
    for c in range(1,len(word)):
        res+=word[-1-c]
    return res

print(create_palindrome('hi'))