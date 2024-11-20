class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue_list = []

    def put(self, elem):
        self.queue_list.append(elem)


    def get(self):
        try:
            elem = self.queue_list[0]
            del self.queue_list[0]
            return elem
        except:
            raise QueueError


class SuperQueue(Queue):

    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        if len(self.queue_list) > 0 :
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
