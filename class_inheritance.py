

class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Aaaaah...")
            self.hungry = False
        else:
            print("No, thanks.")

class SongBird(Bird):
    def __init__(self):
        self.song = 'LaLaLa'
        super(SongBird, self).__init__()

    def sing(self):
        print(self.song)

bird_one = SongBird()
bird_one.sing()
bird_one.eat()
bird_one.eat()
print("isinstance(bird_one, SongBird):", isinstance(bird_one, SongBird))
print("issubclass(SongBird, Bird):", issubclass(SongBird, Bird))