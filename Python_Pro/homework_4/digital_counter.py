def print_message_reaching_limit(func):
    def wrapper(self, *args, **kwargs):
        if self.current >= self.end:
            print('Current is reaching the limit')
        func(self, *args, **kwargs)
    return wrapper


class DigitalCounter:
    def __init__(self, start=0, end=100, current=None):
        self.start = start if type(start) is int else 0
        self.end = end if type(end) is int else 100
        self.current = start if current is None else current

    @print_message_reaching_limit
    def increase(self):
        if self.current < self.end:
            self.current += 1

    def get_current_value(self) -> int:
        return self.current
