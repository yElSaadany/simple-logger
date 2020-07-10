import sys
import inspect
import datetime


class Logger:
    def __init__(self, name="default", to_file=False, only_to_file=False):
        self.name = name
        self.file = to_file if to_file else None
        self.only_to_file = only_to_file
        print(f'Logger "{self.name}" started.')

    def get_date_and_time(self, date: bool, time: bool):
        if date or time:
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tmp = current_datetime.split(" ")
        date = f"{tmp[0]}->" if date else ""
        time = f"{tmp[1]}->" if time else ""

        return date, time

    def log(self, msg_type, msg, calling_function=True, date=True, time=True):
        #
        calling_function = (
            f"{inspect.getouterframes(inspect.currentframe(), 2)[1].function}->"
            if calling_function
            else ""
        )

        date, time = self.get_date_and_time(date, time)
        self._log(msg_type, date, time, calling_function, msg)

    def debug(self, msg, calling_function=True, date=True, time=True):
        calling_function = (
            f"{inspect.getouterframes(inspect.currentframe(), 2)[1].function}->"
            if calling_function
            else ""
        )
        date, time = self.get_date_and_time(date, time)

        self._log("DEBUG", date, time, calling_function, msg)

    def write_to_file(self, complete_msg: str):
        try:
            with open(self.file, "a") as log_file:
                log_file.write(complete_msg + "\n")
        except TypeError:
            raise TypeError(
                'You need to specify the name of the log file with "to_file=" argument\n'
            )

    def _log(self, type: str, date: str, time: str, calling_function: str, msg: str):
        complete_msg = f"{self.name}-{type}->{date}{time}{calling_function}{msg}"

        if self.only_to_file:
            self.write_to_file(complete_msg)
        elif self.file:
            self.write_to_file(complete_msg)
            print(complete_msg)
        else:
            print(complete_msg)
