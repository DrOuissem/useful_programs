from binary_search_tree import *
def solve_problem(inputfile):
    shapes=set()
    f=open(inputfile,'r')
    line1=f.readline()
    numbers=line1.split()
    n=int(numbers[0])
    k=int(numbers[1])
    lines=f.readlines()
    for line in lines:
        l=line.split()
        l=list(map(int,l))
        bst=BSTNode(l[0])
        for i in range(1,len(l)):
            bst.add_value(l[i])
        shape=bst.encode()
        shapes.add(shape)
    print(len(shapes))
if __name__=='__main__':
    textfile='input2.txt'
    solve_problem(textfile)