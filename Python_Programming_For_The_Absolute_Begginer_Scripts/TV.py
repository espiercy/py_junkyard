#TV
#A quick program designed to demonstrate various aspects of chapter 9
#Chapter 9, Challenge 3
#Evan Piercy
#6.5.15


class TV(object):
    """A virtual TV."""
    def __init__(self, power = False, channel = 1, volume = 0):
        print("Time to watch some TV!")
        self.power = power
        self.channel = channel
        self.volume = volume

    def power_switch(self):
        if self.power == False:
            self.power = True
            self.channel = 1
            self.volume = 0
            print("Power turned on.")
        else:
            self.power = False
            print("Power turned off.")

    def change_channel(self, number):
        if self.power == True:
            if 1 <= self.channel <= 100:
                self.channel = number
                print("The channel has been changed to: ", self.channel)
            else:
                print("That's not a valid channel number.")
        else:
            print("Power must be on!")
            
    def change_volume(self, number):
        if self.power == True:
            if 0 <= self.channel <= 100:
                self.channel = number
                print("The volume has been changed to: ", self.channel)
            else:
                print("That's not a valid volume level.")
        else:
            print("Power must be on!")

    def check_settings(self):
        if self.power == True:
            print("TV is on channel ", self.channel)
            print("Volume is set at ", self.volume)
        else:
            print("TV is not on.")

def main():
    tv = TV()
    choice = None
    while choice != "0":
        print\
        ("""
         Time to watch some tv

         0 - Quit
         1 - Turn TV On/Off
         2 - Change Channel
         3 - Change Volume
         """)
        choice = input("Choice: ")
        print()

        #exit
        if choice == "0":
            print("Good-bye.")

        #turn tv on or off
        elif choice == "1":
            tv.power_switch()

        #change channel
        elif choice == "2":
            channel = int(input("What channel would you like to watch?"))
            tv.change_channel(channel)

        #change volume
        elif choice == "3":
            volume = int(input("What volume would you like the TV set at?"))
            tv.change_volume(volume)

#main
main()
input("\n\nPress the enter key to exit.")
