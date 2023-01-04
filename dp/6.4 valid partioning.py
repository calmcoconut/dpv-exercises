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
	return False

d = [ 'it', 'was', 'the', 'best', 'of', 'times' ]
s = "itwasthebestoftimes"
print(s, "is valid?:",valid(s,d))

s = "ithebest"
print(s, "is valid?:", valid(s,d)) # should be false