from threading import Thread
import time

# def sleepMe(i):
#     print("Поток %i засыпает на 5 секунд.\n" % i)
#     time.sleep(5)
#     print("Поток %i сейчас проснулся.\n" % i)
# for i in range(3):
#     th = Thread(target=sleepMe, args=(i, ))
#     th.start()
# for i in range(1000):
#     print(i)
#     time.sleep(1)

choice = 1
def wait():
    print(f'Поток ждёт ответ 5 секунд.\n')
    time.sleep(5)
    if choice == 1:
        print('Забанен')
    else:
        print('Спасён')
i = 1
th = Thread(target=wait, args=( ))
th.start()
choice = input()