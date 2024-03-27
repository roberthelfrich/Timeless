import time

from timer import Timer
from template import Template


class Session:
    def __init__(self, template: Template) -> None:
        try:
            length = self.getValidInput("Work sessions: ")
            self._workTimer = Timer(template._workTime)
            self._breakTimer = Timer(template._breakTime)
            self._currentTimer = self._workTimer
            self._length = int(length)
            self._remainingLength = self._length
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
            print("\n" + "Timer has been skipped!")
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
                print("\n" + "Timer paused!")
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