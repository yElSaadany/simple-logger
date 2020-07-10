import sys
import inspect
import datetime


class Logger:
    def __init__(self, name="default", to_file=False, only_to_file=False):
        self.name = name
        self.file = to_file if to_file else None
        self.only_to_file = only_to_file
        print(f'Logger "{self.name}" started.')

    def debug(self, msg, calling_function=True, date=True, time=True):
        calling_function = (
            f"{inspect.getouterframes(inspect.currentframe(), 2)[1].function}->"
            if calling_function
            else ""
        )
        if date or time:
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tmp = current_datetime.split(" ")
            date = f"{tmp[0]}->" if date else ""
            time = f"{tmp[1]}->" if time else ""
        print(f"{self.name}-DEBUG->{date}{time}{calling_function}{msg}")
