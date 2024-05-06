# class ComplexCars :
#     def __init__(self):
#         pass
    
#     def cars(self,car_name):
#         return f"ComplexCar {car_name}"
    

# class Car_families(object):
#     Car_family={}
    
#     def __new__(cls,name,car_family_id):
        
#         try:
#             obj=cls.Car_family[car_family_id]
            
#         except KeyError:
#             obj = object.__new__(cls)
#             cls.Car_family[car_family_id] = obj
            
#         return obj
    
#     def set_car_info(self,car_info):
        
#         cg = ComplexCars()
#         self.car_info = cg.cars(car_info)
        
#     def get_car_info(self):
        
#         return self.car_info
    
# if __name__ == "__main__":
#     car_data = (("a",1,"audi"),("a",2,"ferarri"),("c",1,"audi"))
#     car_family_objects = []
    
#     for i in car_data:
#         obj=Car_families(i[0],i[1])
#         obj.set_car_info(i[2])
#         car_family_objects.append(obj)
        
#     for i in car_family_objects:
#         print(f"od : {str(id(i))}")
#         print(i.get_car_info())
        
        
#================================================================================================

class TreeType(object):
    def __init__(self, name,color,texture):
        self.name = name
        self.color = color
        self.texture = texture
    
    def render(self,x,y):
        print( f"tree name {self.name} , tree at({x},{y}) , tree color {self.color}, texture: {self.texture}")
        
class Tree(object):
    
    def __init__(self,x,y,tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type
    
    def render(self):
        self.tree_type.render(self.x,self.y)

class TreeFactory(object):
    
    tree_types={}
    
    @staticmethod
    def get_tree_type(name,color,texture):
        
        key=(name,color,texture)
        if key not in TreeFactory.tree_types:
            TreeFactory.tree_types[key]=TreeType(name ,color ,texture)
        
        return TreeFactory.tree_types[key]

if __name__ == "__main__":
    factory = TreeFactory()
    
    tree1 = Tree(1,2 ,factory.get_tree_type("maple","red","smooth"))
    tree1.render()
    print(id(tree1))
    
    tree2 = Tree(3,4 ,factory.get_tree_type("oak","Green","rough"))
    tree2.render()
    print(id(tree2))
    
    tree3 = Tree(2,3,factory.get_tree_type("maple","yellow","smooth"))
    tree3.render()
    print(id(tree1))
    



# class ComplexCar:
#     def __init__(self,name ,color ):
        
#         self.name = name
#         self.color = color
        
    
#     def form (self,car_id):
#         print(f"car name {self.name} , car ID {car_id} , color: {self.color}")
        
# class Car:
    
#     def __init__(self,car_id,car_type):
#         self.car_id=car_id
#         self.car_type= car_type
        
#     def form(self):
#         self.car_type.form(self.car_id)
    
# class CarFactory:
    
#     car_types= {}
#     @staticmethod
#     def get_car_types(name ,color):
#         key=(name,color)
#         if key not in CarFactory.car_types:
#             CarFactory.car_types[key]=ComplexCar(name,color)
#         return CarFactory.car_types[key]
    
# if __name__ == "__main__":
    
#     factory=CarFactory()
#     car1= Car(1 ,factory.get_car_types("audi","black"))
#     car1.form()
#     print(id(car1))
#     car2= Car(2 ,factory.get_car_types("Ferarri","black")) 
#     car2.form()
#     print(id(car2))
    
#     car3= Car(2 ,factory.get_car_types("audi","black"))
#     car3.form()
#     print(id(car3))
    