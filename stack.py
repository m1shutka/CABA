class Stack():

    def push(self, list, object):
        list.append(object)

    def pop(self, list):
        if self.is_empty(list):
            return None

        result = list[len(self.list) - 1]
        list = list[: len(list) - 1]
        return list

    def get(self, list):
        if self.is_empty(list):
            return None
        result = list[len(list) - 1]
        return result

    def is_empty(self, list):
        return True if len(list) == 0 else False