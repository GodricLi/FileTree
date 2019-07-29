# _*_ coding=utf-8 _*_


class Node(object):
    def __init__(self, name, t='dir'):
        self.name = name
        self.t = t
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


class FileSystemTree(object):
    def __init__(self):
        self.root = Node('/')
        self.now = self.root

    def mkdir(self, name):
        if name[-1] != '/':
            name += '/'
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name[-1] != '/':
            name += '/'
        if name == '../':
            self.now = self.now.parent
            return
        for chi in self.now.children:
            self.now = chi
            return
        raise ValueError('%s not exists' % name)
