class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.oil = 1000
    def forward(self):
        self.oil -= 50
        print(self.brand, self.color, self.model, "차량 전진중입니다! 현재 기름양 :", self.oil)
    def reverse(self):
        #self.oil = self.oil - 30
        self.oil -= 30
        print(self.brand, self.color, self.model, "차량 후진중입니다! 현재 기름양 :", self.oil)

class ElectricCar(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        self.battery = 100
    def forward(self):
        self.battery -= 10
        print(self.brand, self.model, self.color, "차량이 전진합니다. 남은 충전잔량:", self.battery)
    def reverse(self):
        self.reverse -= 5
        print(self.company, self.model, self.color, "차량이 후진합니다. 남은 충전잔량:", self.battery)


hyundai = Car("현대", "아반떼", "흰색")
hyundai.forward()
hyundai.reverse()
bmw = Car("bmw", "530D", "검은색")
bmw.forward()
bmw.reverse()
audio = Car("audio", "A7", "붉은색")
audio.forward()
audio.reverse()