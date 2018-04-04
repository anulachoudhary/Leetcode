
class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node %s>" % self.data


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root=%s>" % self.root

    # Print nodes in bread first
    # But every level should be printed alternate order
    #                     a
                      
    #          b                     c 

    #   d           e           f         g  

    # h    i     j    k      l    m     n    o 

    # sample: regular BFS: a, b, c, d, e, f, g, h, i, j, k, l, m, n, o
    # alternate BFS:       a, c, b, d, e, f, g, o, n, m, l, k, j, i, h 
    def alternate_bread_first_search(self):
        pass



if __name__ == "__main__":
    # f = Node("F")
    # g = Node("G")
    # c = Node("C", [f, g])
    
    # e = Node("E")
    # d = Node("D")
    # b = Node("B", [d, e])
    
    # a = Node("A", [b, c])

    # tree = Tree(a)
    # result = tree.get_nodes("B")
    # result == [b2, b1]

    print "main"