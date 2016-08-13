class TicTacToe(object):
    def __init__(self):
        self.words = ['tic', 'tac', 'toe']
        self.idx = 0

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx == len(self.words):
            raise StopIteration()
        word = self.words[self.idx]
        self.idx += 1
        return word

    next = __next__