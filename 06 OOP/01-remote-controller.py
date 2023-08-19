import random
import msvcrt


class Controller:
    def __init__(
        self, tv_status="Off", tv_volume=0, channel_list=["Trt"], channel="Trt"
    ):
        print("Creating controller...")

        self.tv_volume = tv_volume

        self.tv_status = tv_status

        self.channel_list = channel_list

        self.channel = channel

    def change_volume(self):
        while True:
            character = input("Volume down: '<' Volume up: '>' Exit: 'q'")

            if character == "<":
                if self.tv_volume != 0:
                    self.tv_volume -= 1
                    print("Volume:", self.tv_volume)
            elif character == ">":
                if self.tv_volume != 32:
                    self.tv_volume += 1
                    print("Volume:", self.tv_volume)
            else:
                print("Volume updated:", self.tv_volume)
                break

    def close_tv(self):
        print("TV turns off.")

        self.tv_status = "Off"

    def open_tv(self):
        print("TV turns on.")
        self.tv_status = "On"

    def __str__(self):
        return "Tv status: {}\nVolume: {}\nChannels: {}\nCurrent channel: {}\n".format(
            self.tv_status, self.tv_volume, self.channel_list, self.channel
        )

    def __len__(self):
        return len(self.channel_list)

    def random_channel(self):
        rand = random.randint(0, len(self.channel_list) - 1)

        self.channel = self.channel_list[rand]

        print("Current channel:", self.channel)

    def add_channel(self, channel):
        print("Channel added: ", channel)
        self.channel_list.append(channel)


Controller = Controller()
print(
    """*******************

Tv App

Options ;

1. Turn tv on.

2. Turn tv off.

3. Tv informations.

4. Number of channels.

5. Add channels.

6. Go to random channel

7. Change volume.

8. 'q' for exit.
*******************"""
)

while True:
    operation = input("Choose option:")
    if operation == "q":
        print("Exiting program...")
        break
    if operation == "1":
        Controller.open_tv()
    elif operation == "2":
        Controller.close_tv()
    elif operation == "3":
        print(Controller)
    elif operation == "4":
        print("Number of channels: ", len(Controller))
    elif operation == "5":
        channellar = input(
            "Enter the channels you want to add, separated by ',': ")
        new_channels = channellar.split(",")
        for i in new_channels:
            Controller.add_channel(i)
        print("Channel list updated.")
    elif operation == "6":
        Controller.random_channel()
    elif operation == "7":
        Controller.change_volume()
    else:
        print("Invalid operation...")
