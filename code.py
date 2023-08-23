def create_freq_dict(a):
    """Creates a frequency dictionary of input string a"""
    b = dict()
    for c in a:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def function2(a):
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

function2(create_freq_dict('ATCTGACGCGCGCCGC'))
