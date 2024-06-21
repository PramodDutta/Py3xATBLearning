import time


def note_time_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Time Taken - " + str(end_time - start_time))
    return wrapper


@note_time_decorator
def logs_function():
    time.sleep(5)
    print("print the logs of time taken")


@note_time_decorator
def reporting_function():
    time.sleep(2)
    print("print the logs of time taken")
