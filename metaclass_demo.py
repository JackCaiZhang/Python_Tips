class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class Logger(metaclass=Singleton):
    def __init__(self):
        self.log = []

    def log_message(self, message):
        self.log.append(message)
        print(f'Logged: {message}')

if __name__ == '__main__':
    logger1 = Logger()
    logger2 = Logger()
    logger1.log_message('Initial configuration!')
    logger2.log_message('Fetched target data successfully!')
    print(logger1 is logger2)