#1
# a=[1,2,4]
# a_iter=iter(a)
# print(next(a_iter))
# print(next(a_iter))
# print(next(a_iter))
#1.1
# for iter in a_iter:
    # print(iter)

#2
# b=[32,2,9,0,6,43]
# b_iter=iter(b)
#
# while True:
#     try:
#         print(next(b_iter))
#     except StopIteration:
#        print("tugadi")
#        break
#3
f=open('test.py')
print(next(f))
print(next(f))

f=open('test2.py')
while True:
    try:
        print(next(f))
    except StopIteration:
       print("tugadi")
       break
#4
class Counter:
    def __init__(self, start, stop):
        self.start = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start < self.stop:
            return self.start
        raise StopIteration


a = Counter(1, 10)
for item in a:
    print(item)
