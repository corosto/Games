from laser import Laser
from importing import Importing


class Ship:  # klasa rodzica
    COOLDOWN = 30  # 0.5 sekundy, timeout strzału gracza

    def __init__(self, x, y, health=15):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    # szerokość statku
    def get_width(self):
        return self.ship_img.get_width()

    # wysokość statku
    def get_height(self):
        return self.ship_img.get_height()

    # jeżeli nie strzeliłeś w ostatnim czasie (0.5s) to cool_down_counter jest 0 i możesz strzelić
    # inaczej, inkrementuje się w tej metodzie
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    # jak cooldown na strzał się skończył, to tworzy nowy laser i w move_laser posyła go w dół (dla player)
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x + 20, self.y - 14, self.laser_img)
            self.lasers.append(laser)
            Importing.MISSILE_SOUND.play()
            self.cool_down_counter = 1

    # rysowanie statku i strzałów w oknie gry (dla enemy i boss)
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    # co loop zwiększa cool_down_counter o 1, aż do momentu końca cool_down'u i wtedy wykona się shoot,
    # jak powstał jakiś laser dzięki metodzie shoot, to będzie go przesuwać w dół (dla enemy)
    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(Importing.HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 1
                self.lasers.remove(laser)
