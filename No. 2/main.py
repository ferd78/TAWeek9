from circle import Circle
from cylinder import Cylinder

def main():
    circle = Circle()
    print(circle.toString(), f"Area: {circle.getArea()}", sep='\n')
    print()

    circle.setRadius(4.0)
    circle.setColor("cyan")
    print(circle.toString(), f"Area: {circle.getArea()}", sep='\n')
    print()

    cyl = Cylinder()
    print(cyl.toString(), f"Area: {cyl.getArea()}, Volume: {cyl.getVolume()}", sep='\n')
    print()
    
    cyl.setRadius(5.0)
    cyl.setColor("blue")
    cyl.setHeight(6.0)
    print(cyl.toString(), f"Area: {cyl.getArea()}, Volume: {cyl.getVolume()}", sep='\n')



if __name__ == '__main__':
    main()