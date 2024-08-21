from math import pi

def circle_area(radius):
        if radius < 0 :
            raise ValueError("Radius cant be semble")
        return pi*radius**2

#r_list = [2, 0, -3, 2 + 3j, True, [2], 'seven']
#message = 'Площа округи с радіусом {radius} --> {area}'

#for r in r_list:
      #  s = circle_area(r)
      #  print(message.format(radius = r, area  = s ))