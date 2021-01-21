from binary_tree import BTNode
class BSTNode(BTNode):
    def __init__(self,value):
        super().__init__(value)
    def add_value(self,value):
        if value==self.get_value():
            return
        if value<self.get_value():
            if self.get_left() is None:
                new_node=BSTNode(value)
                self.set_left(new_node)
            else:
                self.get_left().add_value(value)
        else:
            if self.get_right() is None:
                new_node=BSTNode(value)
                self.set_right(new_node)
            else:
                self.get_right().add_value(value)

    def delete_value(self,value):
        if value<self.get_value():
            if self.get_left()is not None:
                new_left=self.get_left().delete_value(value)
                self.set_left(new_left)

        elif value>self.get_value():
            if self.get_right() is not None:
                new_right=self.get_right().delete_value(value)
                self.set_right(new_right)
        else:
            if self.get_left() is None and self.get_right() is None:
                return None

            if self.get_left() is None:
                return self.get_right()

            if self.get_right() is None:
                return self.get_left()

            min_value=self.get_right().find_min()
            self.set_value(min_value)
            new_right=self.get_right().delete_value(min_value)
            self.set_right(new_right)

        return self

    def find_min(self):
        if self.get_left() is None:
            return self.get_value()
        else:
            return self.get_left().find_min()

def test_delete_bst():
    bst=BSTNode(10)
    l=[5,15,3,8,14,6,9]
    for value in l:
        bst.add_value(value)
    bst.delete_value(10)
    in_order=bst.in_order()
    print(in_order)


def test_add_bst():
    bst=BSTNode(10)
    l=[5,15,3,8,14,6,9]
    for value in l:
        bst.add_value(value)
    in_order=bst.in_order()
    print(in_order)

if __name__=='__main__':
    #test_add_bst()
    test_delete_bst()