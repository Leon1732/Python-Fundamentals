from duo import ChadianCar

my_tesla = ChadianCar('Benz', 'E350L', 2017)
print(my_tesla.get_car_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
