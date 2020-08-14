class Queue:
    def __init__(self):
        self._container = []
        self._size = 0

    def enqueue(self, value) -> None:
        """"""
        self._container = [value] + self._container
        self._size += 1

    def dequeue(self):
        """"""
        if self._size == 0:
            return -1

        self._size -= 1
        return self._container.pop()

    def empty(self) -> bool:
        return self._size == 0

