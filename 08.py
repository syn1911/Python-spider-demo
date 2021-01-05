class Car():
    # 方法的初始化
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    # 普通汽车都满足，为足电动车不满足
    def fill_gas_tank(self):
        print("我可装500L的油")


# 继承
class ElectricCar(Car):
    # 使用父类的初始化
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 子类去扩展
        self.lala=70
    def desc_batteryDemo(self):
        print("tesla is very important")

    def fill_gas_tank(self):
        print("我是电动车，我怎么可能有油箱来着？？？")

my = ElectricCar('tesla', 'model s', 2016)
print(my.get_descriptive_name())
print(my.desc_batteryDemo())

print(my.fill_gas_tank())


# 将实例当作属性
# 抽取特有的方法，作为属性，从而简化某些类

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def desc_battery_line(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class EleAuoCar(Battery):
    def __init__(self,make,model,year):
        super.__init__(make,model,year)
        # 引入对象
        self.battery_size=Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.desc_battery_line()