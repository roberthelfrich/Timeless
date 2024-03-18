import time
import tkinter as tk

class Timer:
    def __init__(self, duration) -> None:
        self.duration = duration
        self.remaining_time = duration
        self.paused = False

    def start(self):
        while self.remaining_time > 0:
            if not self.paused:
                mins, secs = divmod(self.remaining_time, 60)
                print(f"{mins:02}:{secs:02}", end="\r") # end="\r" ensures that the print() statement gets updated on the same line each time 
                time.sleep(1)
            self.remaining_time -= 1

        print("\nTimer has ended!")

    def pauseResume(self): # Pauses the timer if it was going, resumes it if it was paused 
        if self.paused == False:
            self.paused = True
        elif self.paused == True:
            self.paused = False

    def get_time(self):
        mins, secs = divmod(self.remaining_time, 60)
        return f"{mins:02}:{secs:02}"


def get_work_duration():
    while True:
        try: 
            work_duration = int(input("Enter work duration in minutes: "))
            if work_duration > 0:
                return work_duration * 60
            else:
                print("Please enter a positive duration.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

class TimerGUI:
    def __init__(self):
        root = tk.Tk()
        self.root = root
        root.geometry("500x250")
        root.title("Timeless")

        startButton = tk.Button(root, text='Start/Stop', font=("Times New Roman", 12),)
        startButton.pack(side="bottom")

        self.root.mainloop()

    
    
if __name__ == "__main__": # This line ensures the following code will only run if the script is executed directly
    # Timer logic  
    work_duration = get_work_duration()
    timer = Timer(work_duration)
    timer.start()
    # GUI 'logic'
    timerGUI = TimerGUI() 


    
