'''
Class for building and executing a machine learning pipeline
'''

from collections import deque


class Pipeline:
    '''
    Class for representing a way to compress and decompress text data.
    '''
    def __init__(self, params=None):
        self.dq = deque()

        if params is not None:
            if isinstance(params, list):
                for p in params:
                    self.add(p)
            elif isinstance(params, str):
                self.add(params)

    def add(self, new_task):
        '''
        Adds new_task to the pipeline.

        Input:
        new_task (object): the class/object to be added
        Returns: nothing
        '''
        self.dq.append(new_task)

    def next(self):
        '''
        Pops the first task in the queue

        Input: none
        Returns: next task or None
        '''
        try:
            return self.dq.popleft()
        except IndexError:
            return None

    def is_empty(self):
        '''
        Checks whether queue is empty. Returns True/False
        '''
        if (len(self.dq) == 0):
            return True
        return False

    def go(self):
        '''
        Kicks off the pipeline
        '''
        next_task = self.next()

        while next_task is not None:
            #next_task.go()
            print('running a task from go')
            next_task = self.next()

    def peek(self):
        return self.dq[0]

    def clear(self):
        self.dq.clear()

    def extend(self, tasks):
        self.dq.extend(tasks)

    def prioritize(self, task):
        self.dq.appendleft(task)