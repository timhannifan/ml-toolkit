'''
Class for building and executing a machine learning pipeline
'''

from collections import deque
import reader

class Pipeline:
    '''
    Class for representing a way to compress and decompress text data.
    '''
    def __init__(self, params=None):
        self.dq = deque()
        self.last_result = ''

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
        print('adding item to pipeline', type(new_task))
        self.dq.append(new_task)

    def get_next_task(self):
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

    def execute(self):
        '''
        Kicks off the pipeline
        '''
        print('Starting pipeline ---------------------------')
        next_task = self.get_next_task()
        print('Starting w task', type(next_task))
        last_result = self.last_result

        while next_task is not None:
            print('Starting next task:', type(next_task))
            if last_result != '':
                next_task.load(last_result)
            last_result = 'a'
            # last_result = next.execute()
            # print(type(last_result))
            # print('Completing task', type(next_task))
            next_task = self.get_next_task()

    def peek(self):
        return self.dq[0]

    def clear(self):
        self.dq.clear()

    def extend(self, tasks):
        self.dq.extend(tasks)

    def prioritize(self, task):
        self.dq.appendleft(task)