# 类相关
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "：蹲下")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog("zs", 19)
print(my_dog.name)
print(my_dog.age)
# 调用方法

print(my_dog.sit())


# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     # 调用car 的信息
#     def getInfoCar(self):
#         long_name = str(self.year) + "-" + self.make + "-" + self.model
#         return long_name.title()
#
#
# # 调用
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.getInfoCar())

# 指定默认值
# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading='0'
#
#     # 调用car 的信息
#     def getInfoCar(self):
#         long_name = str(self.year) + "-" + self.make + "-" + self.model
#         return long_name.title()
#     # 汽车里程
#     def read_odometer(self):
#      print("This car has " + str(self.odometer_reading) + " miles on it.")
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.read_odometer())
#
# print("直接修改属性的值")
# print("直接修改属性的值")
# my_new_car.odometer_reading='23'
# print(my_new_car.read_odometer())


# 通过方法修改属性

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading='0'

    # 调用car 的信息
    def getInfoCar(self):
        long_name = str(self.year) + "-" + self.make + "-" + self.model
        return long_name.title()
    # 汽车里程
    def read_odometer(self):
     print("This car has " + str(self.odometer_reading) + " miles on it.")


    def write_odo(self,miles):
        self.odometer_reading=miles

my_new_car = Car('audi', 'a4', 2016)
my_new_car.write_odo(20)
print(my_new_car.read_odometer())
