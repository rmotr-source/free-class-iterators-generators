class SimpleIterator(object):
    # Params?
    def __iter__(self):
        return self
        
    def __next__(self):
        return 1
        
    next = __next__

s = SimpleIterator()
iterator = iter(s)

print(next(iterator))
print(next(iterator))