import time

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

class Timer:
    def __init__(self, duration: int) -> None:
        try:
            self._duration = int(duration) # * 60 INGORE! Will be uncommented once testing is complete
            self._remainingDuration = self._duration
            self._paused = True
        except ValueError:
            raise ValueError("Invalid duration. Please enter a valid integer for the timer duration.")

    def startTimer(self) -> None:
        try:
            self.resumeTimer()
            while self._remainingDuration >= 0:
                if not self._paused:
                    mins, secs = divmod(self._remainingDuration, 60)
                    time_format = '{:02d}:{:02d}'.format(mins, secs)
                    print(f"Time remaining: {time_format}" + "\r", end="")
                    time.sleep(1)
                    self._remainingDuration -= 1
            print("\nTimer has ended!")
        except ValueError:
            raise ValueError("Invalid duration. Please enter a valid integer for the timer duration.")

    def hasEnded(self) -> bool:
        return self._remainingDuration <= 0

    def endTimer(self) -> None:
        self._remainingDuration = 0

    def resetTimer(self) -> None:
        self._remainingDuration = self._duration

    def pauseTimer(self) -> None:
        self._paused = True

    def resumeTimer(self) -> None:
        self._paused = False

class Session:
    def __init__(self, template: Template) -> None:
        try:
            length = self.getValidInput("Work sessions: ")
            self._workTimer = Timer(template._workTime)
            self._breakTimer = Timer(template._breakTime)
            self._currentTimer = self._workTimer
            self._length = int(length)
            self._remainingLength = self._length
            self.startNextTimer()
        except ValueError as e:
            print(e)
            raise

    def startNextTimer(self):
        if self._remainingLength == 0:
            print("Session has ended!")
            return
        self._currentTimer.startTimer()
        while not self._currentTimer.hasEnded():
            time.sleep(1)
        print(f"Session {self._length - self._remainingLength + 1} of {self._length} completed!")
        self._remainingLength -= 1
        self._currentTimer.resetTimer()
        self.switchCurrentTimer()
        self.startNextTimer()

    def switchCurrentTimer(self):
        self._currentTimer = self._workTimer if self._currentTimer == self._breakTimer else self._breakTimer

    def skipTimer(self) -> None:
        try:
            self._currentTimer.endTimer()
            self.startNextTimer()
            print("Timer has been skipped!")
        except ValueError as e:
            print(e)

    def rewindTimer(self) -> None:
        try:
            if self._remainingLength < self._length:
                self._currentTimer.resetTimer()
                self._currentTimer.pauseTimer()
                print("Timer has been rewound!")
            else:
                raise ValueError("Cannot rewind timer!")
        except ValueError as e:
            print(e)

    def pauseResumeTimer(self) -> None:
        try:
            if self._currentTimer._paused:
                self._currentTimer.resumeTimer()
                print("Timer resumed!")
            else:
                self._currentTimer.pauseTimer()
                print("Timer paused!")
        except AttributeError:
            print("Timer has not started yet. Please start the timer first.")

    def getValidInput(self, prompt: str, min_value: int = 1, max_value: int = 10) -> int:
        while True:
            try:
                input_value = int(input(prompt))
                if min_value <= input_value <= max_value:
                    return input_value
                else:
                    print(f"Invalid input. Please enter a value between {min_value} and {max_value}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

            
if __name__ == "__main__":
    template = Template()
    session = Session(template)
    time.sleep(3)
    session.pauseResumeTimer()
    time.sleep(5)
    session.pauseResumeTimer()
    
    


# toDo:
# - try: except: clauses for better error management 
# - implement a callback function or event handling 
#   mechanism to notify external code when the timer ends
# - invalid input handling for Session class (getValidInput())
# - split classes into individual files 
