class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queue_list = []

    def put(self, elem):
        self.__queue_list.append(elem)


    def get(self):
        try:
            elem = self.__queue_list[0]
            del self.__queue_list[0]
            return elem
        except:
            raise QueueError


class SuperQueue(Queue):

    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        if len(self._Queue__queue_list) > 0 :
            return False
        else:
            return True

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
