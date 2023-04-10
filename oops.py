#oops concepts;-
#1.Classes and objects   (blue print to create objects)  
#2.Inheritance           (types)
#3.Polymerphism          (many forms)
#4.Abstraction          (data hiding)
#5.Encapsulation         (winding of data members and data methods) 


class Sagar:
    print("this is class")
    def display(self):
        a=10
        b=12
        print(a,b)                   #this is class
obj=Sagar()                          #10 12
obj.display()

class Sagar:
    d=12
    def display(self):
        a=10
        b=12
        print(a,b)                   #10 12    obj=object
obj=Sagar()                          #12       obj.d=object.variable
obj.display()
print(obj.d)

#init
class Mobile:
    def __init__(self,Brand,Battery,Ram,Camera,Price):
        self.Brand=Brand
        self.Battery=Battery
        self.Ram=Ram
        self.Camera=Camera
        self.Price=Price
    def display(self):
        print("Brand:",self.Brand)                                      #Brand: apple
        print("Battery:",self.Battery)                                  #Battery: 4000mah
        print("Ram:",self.Ram)                                          #Ram: 8gb
        print("Camera:",self.Camera)                                    #Camera: 48mp
        print("Price:",self.Price)                                      #Price: 90000
obj=Mobile("apple","4000mah","8gb","48mp","90000")
obj.display()




