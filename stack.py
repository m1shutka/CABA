class Stack():
    def __init__(self):
        self.__stk = []

    def push(self, object):
        self.__stk.append(object)

    def pop(self):
        if self.is_empty():
            return None

        result = self.__stk[len(self.__stk) - 1]
        self.__stk = self.__stk[: len(self.__stk) - 1]
        return result

    def get(self):
        if self.is_empty():
            return None
        result = self.__stk[len(self.__stk) - 1]
        return result

    def is_empty(self):
        return True if len(self.__stk) == 0 else False

    def get_elems(self):
        return self.__stk


if __name__ == '__main__':
    s = Stack()
    s.push('1')
    print(s.is_empty())
    s.push('2')
    s.push('3')
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())