#Using Object Orientation approach to create a stack

class Stack:

    def __init__(self):
        self.__stack_list = []

    def push(self,val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object = Stack()

stack_object.push(1)
stack_object.push(2)
stack_object.push(3)


class AddingStack(Stack):

    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self,val):
        self.__sum += val
        Stack.push(self,val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

new_stack_object = AddingStack()

for i in range(5):
    new_stack_object.push(i)
print(new_stack_object.get_sum())

for i in range(5):
    print(new_stack_object.pop())

