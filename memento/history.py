class History:
    def __init__(self):
        self.__states=[]
    
    def push(self, state):
        self.__states.append(state)

    def pop(self):
        lastIndex = len(self.__states) - 1
        last_state = self.__states[lastIndex]
        self.__states = self.__states[:-1]
        return last_state