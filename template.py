import time

from timer import Timer

class Template:
    def __init__(self) -> None:
        try:
            self._name = input("Template name: ")
            if not self.isValidName(self._name):
                raise ValueError("Invalid template name. Please use alphanumeric characters.")

            self._workTime = self.getValidTime("Work length in minutes: ")
            self._breakTime = self.getValidTime("Break length in minutes: ")
        except ValueError as e:
            print(e)
            raise

    def editWorkTime(self) -> None:
        try:
            new_time = self.getValidTime(f"Current work length: {self._workTime} minutes. Enter the new time: ")
            self._workTime = new_time
            print(f"Work time is now {self._workTime} minutes.")
        except ValueError as e:
            print(e)

    def editBreakTime(self) -> None:
        try:
            new_time = self.getValidTime(f"Current break length: {self._breakTime} minutes. Enter the new time: ")
            self._breakTime = new_time
            print(f"Break time is now {self._breakTime} minutes.")
        except ValueError as e:
            print(e)

    def editTemplateName(self) -> None:
        try:
            new_name = input(f"Change name of {self._name} to: ")
            if self.isValidName(new_name):
                print(f"Template name changed from {self._name} to {new_name}!")
                self._name = new_name
            else:
                raise ValueError("Invalid template name. Please use alphanumeric characters.")
        except ValueError as e:
            print(e)

    def isValidTime(self, time: str) -> bool:
        try:
            time = int(time)
            return 1 <= time <= 120
        except ValueError:
            return False

    def isValidName(self, name: str) -> bool:
        return 1 < len(name) < 15 and name.isalnum()

    def getValidTime(self, prompt: str) -> int:
        while True:
            try:
                time_input = input(prompt)
                if self.isValidTime(time_input):
                    return int(time_input)
                print("Invalid time. Please enter a value between 1 and 120 minutes.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
