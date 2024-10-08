# This program display information about a car model

def car_dictionary(name, manufacturer, **car_info):
    car_info['name'] = name
    car_info['manufacturer'] = manufacturer
    return(car_info)

car_info = car_dictionary('Ram 1500', 'Dodge',
                          Color = 'Black',
                          Year = 2011,
                          Truck = 'Yes')

for quality, info in car_info.items():
    print(f"\t{quality}: {info}")
print("\n")