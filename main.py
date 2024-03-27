import time
import threading

from timer import Timer
from template import Template
from session import Session
from gui import GUI

if __name__ == "__main__":
    gui = GUI()
    template = Template()
    session = Session(template)
    timerThread = threading.Thread(target=session.startNextTimer)
    timerThread.start() 
    time.sleep(3)
    session.pauseResumeTimer()
    time.sleep(3)
    session.pauseResumeTimer()
    time.sleep(3)
    # session.rewindTimer()
    # time.sleep(3)
    # session.pauseResumeTimer()
    # time.sleep(3)
    # session.skipTimer()
    # time.sleep(3)
    
    
# toDo:
# - implement a callback function or event handling 
#   mechanism to notify external code when the timer ends
# - split classes into individual files 