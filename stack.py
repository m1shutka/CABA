class Stack():
    def __init__(self):
        self.__stk = []

    def push(self, object):
        self.__stk.append(object)

    def pop(self):
        result = self.__stk[len(self.__stk) - 1: len(self.__stk)]
        self.__stk = self.__stk[: len(self.__stk) - 1]
        return result

if __name__ == '__main__':
    s = Stack()
    s.push('1')
    s.push('2')
    s.push('3')
    print(s.pop())