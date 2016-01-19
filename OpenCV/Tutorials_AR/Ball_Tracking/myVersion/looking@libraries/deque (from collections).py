'''
https://docs.python.org/2/library/collections.html

list-like container with fast appends and pops on either end

class collections.deque([iterable[, maxlen]])
Returns a new deque object initialized left-to-right (using append()) with data from iterable.
If iterable is not specified, the new deque is empty.

Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”).
Deques support thread-safe, memory efficient appends and pops from either side of the deque
with approximately the same O(1) performance in either direction.
'''
from collections import deque


myDoubleEndedQueue = deque('ABC')

for element in myDoubleEndedQueue:
    print(element)

myDoubleEndedQueue.append('Z')  # right append
myDoubleEndedQueue.appendleft('!')  # left append

for element in myDoubleEndedQueue:
    print(element)

myDoubleEndedQueue.extend('123') # app multiple elements at once on the right

lengthQ = len(myDoubleEndedQueue)

print('Length of double ended queue: ' + str(lengthQ))
print('Elements popped L to R:')

for i in range(lengthQ):
    itemPopped = myDoubleEndedQueue.pop() # pop right
    print(itemPopped, end = ', ')
    # items in queue: !, A, B, C, Z, 1, 2, 3
    # popped = rev order ^

