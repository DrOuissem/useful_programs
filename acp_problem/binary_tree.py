
class BTNode:
    __slots__ = ['__value','__parent','__left_child','__right_child']
    def __init__(self,value):
        self.__value=value
        self.__parent=self.__left_child=self.__right_child=None

    def get_value(self):
        return self.__value

    def get_parent(self):
        return self.__parent

    def get_left(self):
        return self.__left_child

    def get_right(self):
        return self.__right_child

    def set_value(self,value):
        self.__value=value

    def set_parent(self,parent):
        self.__parent=parent

    def set_left(self, child):
        self.__left_child = child
        if child is not None:
            child.set_parent(self)

    def set_right(self, child):
        self.__right_child = child
        if child is not None:
            child.set_parent(self)

    def pre_order(self):
        res=[]
        res.append(self.get_value())
        if self.get_left():
            res+=self.get_left().pre_order()
        if self.get_right():
            res+=self.get_right().pre_order()
        return res

    def in_order(self):
        res=[]

        if self.get_left():
            res+=self.get_left().in_order()
        res.append(self.get_value())
        if self.get_right():
            res+=self.get_right().in_order()
        return res

    def post_order(self):
        res = []
        if self.get_left():
            res += self.get_left().post_order()

        if self.get_right():
            res += self.get_right().post_order()
        res.append(self.get_value())
        return res

    def encode(self):
        res=''

        if self.get_left():
            res+='l'
            res+=self.get_left().encode()

        if self.get_right():
            res+='r'
            res+=self.get_right().encode()
        return res

def example_bt():
    A=BTNode('A')
    B = BTNode('B')
    C = BTNode('C')
    D = BTNode('D')
    E = BTNode('E')
    F = BTNode('F')
    G = BTNode('G')

    B.set_left(G)
    B.set_right(E)
    F.set_left(D)
    F.set_right(B)
    A.set_left(F)
    A.set_right(C)

    l1=A.pre_order()
    l2=A.in_order()
    l3=A.post_order()
    print("pre order:",l1)
    print("in order:",l2)
    print("post order:",l3)

if __name__=='__main__':
    example_bt()
