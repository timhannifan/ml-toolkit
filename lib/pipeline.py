'''
Class for building and executing a machine learning pipeline
'''

from collections import deque


class Pipeline:
    '''
    Class for building and executing a machine learning pipeline
    '''
    def __init__(self, params=None):
        self.dq = deque()
        self.dq.clear()

        self.last_result = None

        if params is not None:
            if isinstance(params, list):
                for p in params:
                    self.add(p)
            elif isinstance(params, str):
                self.add(params)

    def clear(self):
        '''
        Clears all contents of pipeline
        Input: none
        Returns: nothing
        '''
        self.dq.clear()

    def add(self, new_task):
        '''
        Adds new_task to the pipeline.

        Input:
            new_task (object): the class/object to be added
        Returns: nothing
        '''
        print('Adding item to pipeline', type(new_task))
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
        Input: none
        Returns: bool
        '''
        if (len(self.dq) == 0):
            return True
        return False

    def execute(self):
        '''
        Pipeline execution method. Executes each component sequentially
        Input: none
        Returns: last result of the pipeline or None if pipeline fails
        '''
        next_task = self.get_next_task()
        counter = 0
        while next_task is not None:
            print('Starting task:', type(next_task))
            try:
                if counter == 0:
                    # First run requires Reader to already be loaded.
                    self.last_result = next_task.execute()
                else:
                    # Otherwise load the next task with previous results
                    next_task.load_input(self.last_result)
                    self.last_result = next_task.execute()
                next_task = self.get_next_task()
                counter += 1
            except:
                print('Pipeline failed during task:', next_task)
                return None
        return self.last_result
