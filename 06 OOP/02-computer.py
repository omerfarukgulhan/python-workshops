class Computer():
    def __init__(self, cpu, gpu, ram, ssd):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.ssd = ssd

    def show_information(self):
        print("cpu: {}\ngpu: {}\nram: {}\nssd: {}".format(
            self.cpu, self.gpu, self.ram, self.ssd))

    def turn_on(self):
        print("PC turned on.")

    def turn_off(self):
        print("PC turned off.")

    def open_app(self, app):
        print("{} opened.".format(app))


pc = Computer("5600x", "RTX 2060", "16 GB", "1 Tb")
pc.show_information()
pc.turn_on()
pc.open_app("Spotify")
pc.turn_off()
