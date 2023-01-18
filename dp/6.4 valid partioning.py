"""
6.4 You are given a string of n characters s[1...n], which you believe to be a corrupted text document
in which all punctuation has vanished (so that it looks something "itwasthebestoftimes..."). You wish
to reconstruct the document using a dictionary, which is available in the form of a Boolean function
dict(.):
for any string w,
    dict(w) = true if w is a valid word, false otherwise
(a) Give a dynamic programming algorithm that determines whether the string s[.] can be reconstituted
    as a sequence of valid words. The running time should be at most O(n^2), assuming calls to dict take
    unit time.
(b) In the event that the string s is valid, make your algorithm output the corresponding sequence of
    words.
"""

def valid(s, d):
    n = len(s)
    d = set(d)
    opt = [False] * (n+1)
    opt[0]=True
    for i in range(n+1):
        for j in range(i):
            if s[j:i] in d:
                opt[i] = opt[i-(i-j)]
    return opt[n]

d = [ "i", 'it', 'was', 'the', 'best', 'of', 'times' ]
s = "itwasthebest"
print(s, "is valid?:",valid(s,d))

s = "iathebest"
print(s, "is valid?:", valid(s,d)) # should be false