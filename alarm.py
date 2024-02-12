from tkinter import *
import datetime
import time
import winsound
import threading


def Threading():
    t1 = threading.Thread(target=alarm)
    t1.start()


def alarm():
    while True:
        if hour.get() ==minute.get() == second.get() == '00':
            state.config(text="Please, select time!" , bg="black")
            break
        else:
            state.config(text="Alarm Started" , bg="black")
            userTime = f"{hour.get()}:{minute.get()}:{second.get()}"
            time.sleep(1)
            currentTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(userTime , currentTime)
            if userTime == currentTime:
                state.config(text="Time to wake up!")
                winsound.PlaySound(r"C:\Users\Hp\Desktop\alarmProj\mixkit-retro-game-emergency-alarm-1000.wav", winsound.SND_ALIAS)
                
                hour.set(hours[0])
                minute.set(minutes[0])
                second.set(seconds[0])
                print("Time to wake up!")
                break

master = Tk()

master.geometry('400x250')
master.title("Alarm Clock")

iconFrame = PhotoImage(file=r"C:\Users\Hp\Desktop\alarmProj\alarm_clock_PNG80.png")
master.iconphoto(False, iconFrame)

appTitle = Label(master, text="Alarm Clock" , font=("century 20 bold"))
appTitle.pack()

setTimeLabel = Label(master, text="Set Time" , font=("century 15"))
setTimeLabel.pack(pady = 10)

frame = Frame(master)
frame.pack()

hour = StringVar(master)
#hours = ('00', '01', '02','03','04','05',
#        '06','07','08','09','10','11','12','13','14',
#        '15','16','17','18','19','20','21','22','23','24')

hours = []
for num in range(0 , 25):
    if num <= 9:
        num = '0' + str(num)
    hours.append(num)

hrs = OptionMenu(frame , hour , *hours)
hrs.pack(side=LEFT)
hrs.config(font=("century 13") ,fg="white" , background="black")
hour.set(hours[0])


minute = StringVar(master)
minutes = []
for num in range(0 , 61):
    if num <= 9:
        num = '0' + str(num)
    minutes.append(num)

mins = OptionMenu(frame , minute , *minutes)
mins.pack(side=LEFT)
mins.config(font=("century 13") ,fg="white" , background="black")
minute.set(minutes[0])


second = StringVar(master)
seconds = []
for num in range(0 , 61):
    if num <= 9:
        num = '0' + str(num)
    seconds.append(num)

secs = OptionMenu(frame , second , *seconds)
secs.pack(side=LEFT)
secs.config(font=("century 13") ,fg="white" , background="black")
second.set(seconds[0])


btn = Button(master , text="Start Alarm" , font=('century 14 bold') , fg="white" , bg="black", command=Threading)
btn.pack(pady = 10)


state = Label(master , font=("century 10 bold") , fg="white")
state.pack()

master.mainloop()