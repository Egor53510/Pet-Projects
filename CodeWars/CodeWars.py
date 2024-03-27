def longest_slide_down(pyramid):
    for i in range(len(pyramid)-2, -1, -1):
        for j in range(len(pyramid[i])):
            pyramid[i][j] += max(pyramid[i+1][j], pyramid[i+1][j+1])
    return pyramid[0][0]

def sum_strings(x, y):
    return str((int(x) if x != "" else 0) + (int(y) if y != "" else 0))

def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    counts = {'n': 0, 's': 0, 'e': 0, 'w': 0}
    for directions in walk:
        counts[directions] += 1
    return counts['n'] == counts['s'] and counts['e'] == counts['w']

def pig_it(text):
    return " ".join([i[1:] + i[0] + "ay" if i.isalpha() else i for i in list(text.split())])

def persistence(n):
    j = 0
    while len(str(n)) > 1:
        k = 1
        for d in str(n):
            k *= int(d)
        n = k
        j += 1
    return j

def DNA_strand(dna):
    complete = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complete[base] for base in dna])

def spin_words(sentence):
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split(" ")])

def rgb(r, g, b):
    return " ".join([str(hex(r).upper()[2:]), str(hex(g).upper()[2:]), str(hex(b).upper()[2:])])
print(rgb(1, 2, 3))