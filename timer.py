import time
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


            

