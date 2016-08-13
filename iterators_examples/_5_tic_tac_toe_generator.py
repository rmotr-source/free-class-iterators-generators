def tic_tac_toe():
    words = ['tic', 'tac', 'toe']
    for word in words:
        yield word

for elem in tic_tac_toe():
    print(elem)