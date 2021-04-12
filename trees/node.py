class Node: 
    left = None 
    right = None
    data = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '%s' % self.data


