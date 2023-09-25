import time

class Stopwatch:
    def __init__(self):
        self.start_time = None   # Время начала работы секундомера
        self.pause_time = None   # Время начала паузы (если была)
        self.paused_duration = 0 # Общая продолжительность паузы
        
    def start(self):
        self.start_time = time.time()
        print("Секундомер запущен.")
    
    def pause(self):
        if not self.start_time:
            print("Ошибка: Секундомер еще не запущен.")
            return

        if self.pause_time:
            print("Ошибка: Секундомер уже находится в режиме паузы.")
            return

        self.pause_time = time.time()
        print("Секундомер приостановлен.")
    
    def resume(self):
        if not self.start_time:
            print("Ошибка: Секундомер еще не запущен.")
            return

        if not self.pause_time:
            print("Ошибка: Секундомер не находится в режиме паузы.")
            return
        
        self.paused_duration += time.time() - self.pause_time
        self.pause_time = None
        print("Секундомер возобновлен.")
    
    def stop(self):
        if not self.start_time:
            print("Ошибка: Секундомер еще не запущен.")
            return
        
        elapsed_time = time.time() - self.start_time - self.paused_duration
        self.start_time = None
        self.pause_time = None
        self.paused_duration = 0
        print("Секундомер остановлен.")
        print("Прошло времени: {:.2f} секунд.".format(elapsed_time))


stopwatch = Stopwatch()

stopwatch.start()
time.sleep(2)

stopwatch.pause()
time.sleep(1)

stopwatch.resume()
time.sleep(3)

stopwatch.stop()