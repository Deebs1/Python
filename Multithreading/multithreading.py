import time
import threading

# def calc_square(numbers):
#     print("calculate square numbers")
#     for n in numbers:
#         time.sleep(1)
#         print('square:',n*n)
#
# def calc_cube(numbers):
#     print("calculate cube of numbers")
#     for n in numbers:
#         time.sleep(1)
#         print('cube:',n*n*n)
#
# arr = [2,3,8,9]
#
# t = time.time()
# # print(t)
#
# t1= threading.Thread(target=calc_square, args=(arr,))
# t2= threading.Thread(target=calc_cube, args=(arr,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# # print(time.time())
# print("done in : ",time.time()-t)
# print("Hah... I am done with all my work now!")


def calc(number):
    print(number)

for i in range(10):
    th = threading.Thread(target = calc, args = (2,))
    th.start()

print(threading.active_count())