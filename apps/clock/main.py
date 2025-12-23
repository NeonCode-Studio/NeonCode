import time

def run():
    print("Neon Clock")
    for i in range(5):  # wyświetla czas 5 razy
        print(time.strftime("%H:%M:%S"))
        time.sleep(1)
