import time

class Template:
    def __init__(self) -> None:
        self._name = input("Template name: ")
        if not self.isValidName(self._name):
            raise ValueError("Invalid template name. Please use alphanumeric characters.")

        self._workTime = self.getValidTime("Work length in minutes: ")
        self._breakTime = self.getValidTime("Break length in minutes: ")

    def editWorkTime(self) -> None:
        new_time = self.getValidTime(f"Current work length: {self._workTime} minutes. Enter the new time: ")
        self._workTime = new_time
        print(f"Work time is now {self._workTime} minutes.")

    def editBreakTime(self) -> None:
        new_time = self.getValidTime(f"Current break length: {self._breakTime} minutes. Enter the new time: ")
        self._breakTime = new_time
        print(f"Break time is now {self._breakTime} minutes.")

    def editTemplateName(self) -> None:
        new_name = input(f"Change name of {self._name} to: ")
        if self.isValidName(new_name):
            print(f"Template name changed from {self._name} to {new_name}!")
            self._name = new_name
        else:
            raise ValueError("Invalid template name. Please use alphanumeric characters.")

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
            time_input = input(prompt)
            if self.isValidTime(time_input):
                return int(time_input)
            print("Invalid time. Please enter a value between 1 and 120 minutes.")

class Timer:
    def __init__(self, duration: int) -> None:
        self._duration = int(duration)
        self._remainingDuration = self._duration
        self._paused = True
        
    def startTimer(self) -> None:
        self.resumeTimer()
        while self._remainingDuration > 0:
            if not self._paused:
                time.sleep(1)
                self._remainingDuration -= 1
        print("\nTimer has ended!")
        
    def hasEnded(self) -> bool:
        if self._remainingDuration == 0:
            return True
        else:
            return False
        
    def endTimer(self) -> None:
        self._remainingDuration = 0
        
    def resetTimer(self) -> None:
        self._remainingDuration = self._duration
        
    def pauseTimer(self) -> None:
        self._paused = True
        
    def resumeTimer(self) -> None:
        self._paused = False
    
    
class Session:
    def __init__(self, template:Template) -> None:
        # Set ammount of work sessions for this session, each work session except the last one will be followed by a break
        length = input("Work sessions: ")
        # Initialize two timers, one for work and one for break
        self._workTimer = Timer(template._workTime) 
        self._breakTimer = Timer(template._breakTime)
        # Set the current timer to workTimer, as the session will start with a bout of work
        self._currentTimer = self._workTimer
        self._length = int(length)
        self._remainingLength = self._length
        self.startNextTimer()
            
            
    def startNextTimer(self) -> None:
        if not self._remainingLength == 0:
            self._remainingLength -= 1
        else: 
            print("Session has ended!")
            return
        self._currentTimer.startTimer()
        while not self._currentTimer.hasEnded(): 
            mins, secs = divmod(self._currentTimer._remainingDuration, 60)
            print(f"{mins:02}:{secs:02}", end="\r")
        self.switchCurrentTimer()
        self.startNextTimer()
        
    def switchCurrentTimer(self):
        self._currentTimer = self._workTimer if self._currentTimer == self._breakTimer else self._breakTimer

    def skipTimer(self) -> None:
        self._currentTimer.endTimer()
        self.startNextTimer()
        print("Timer has been skipped!")
        
    def rewindTimer(self) -> None:
        if self._remainingLength < self._length:
            self._currentTimer.resetTimer()
            self._currentTimer.pauseTimer()
            print("Timer has been rewinded!")
        else:
            print("Cannot rewind timer!")

    def pauseResumeTimer(self) -> None:
        if self._currentTimer._paused:
            self._currentTimer.resumeTimer()
            print("Timer resumed!")
        else:
            self._currentTimer.pauseTimer()
            print("Timer paused!")
        
        

            
if __name__ == "__main__":
    template = Template()
    session = Session(template)
    
    


# toDo:
# - fix timer not showing 
# - try: except: clauses for better error management 
# - implement a callback function or event handling 
#   mechanism to notify external code when the timer ends
# - invalid input handling for Session class (getValidInput())
# - split classes into individual files 
