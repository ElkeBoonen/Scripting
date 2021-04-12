import threading, time

def TakeANap():
    time.sleep(5)
    print('Wake up!')

print('Start of program.')

thread = threading.Thread(target=TakeANap)
thread.start()

print('End of program.')
