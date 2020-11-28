import main4

if __name__=='__main__':
    s1=main4.Student("Amal Saleh",21,2,123123,1231233,4.5)
    s2 = main4.Student("Mohamed Saleh", 22, 1, 3123123, 1031233, 5)
    s3 = main4.Student("Khaled David", 22, 1, 3123123, 1031233, 3)
    s4 = main4.Student("Mona Abdallah", 22, 2, 3123123, 1031233, 4)
    l=[s1,s2,s3,s4]
    l2=sorted(l,reverse=True)
    for s in l2:
        print(s)



