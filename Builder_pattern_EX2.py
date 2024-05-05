"""
        We use the builder pattern when we know that an object must be created in multiple steps,
        and different representations of the same construction are required
"""
from abc import ABCMeta,abstractmethod

class Ibuilder(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def buildParta():
        "build part a"
        
    @staticmethod
    @abstractmethod
    def buildPartb():
        "build part b"
    
    @staticmethod
    @abstractmethod
    def buildPartc():
        "build part c"

    def get_result():
        "final product"

class Builder(Ibuilder):
    
    def __init__(self):
        self.product = Product()
        
    
    def buildParta(self):
        self.product.parts.append("A")
        return self 
    
    def buildPartb(self):
        self.product.parts.append("B")
        return self 
    
    def buildPartc(self):
        self.product.parts.append("C")
        return self 
    def get_result(self):
        return self.product

        
        
class Product(object):
    def __init__(self):
        self.parts = []
        

class Creator(object):
    
    @staticmethod
    def create():
        
        return Builder() \
            .buildParta()\
            .buildPartb()\
            .buildPartc()\
            .get_result()
        
PRODUCT=Creator.create()
print(PRODUCT.parts)

#================================================================


#The Builder class carries all the same attributes as the target class.
#The Builder class is not immutable.
#The Builder class requires very few arguments to instantiate. Most or all of its attributes start off with default values.
#The Builder offers a mechanism for each attribute that starts with a default value to be rewritten with a different value.
#Finally, the Builder offers a method that creates an instance of the original immutable class whose attributes are copied 
#from the corresponding attributes of the Builder instance.

class Build_house:
    
    def __init__(self,):
        self.parts=[]

class house:
    
    def __init__(self):
        self.build = Build_house()
        
    def set_roof(self):
        self.build.parts.append("oval")
        return self
    

    def set_rooms_num(self):
        self.build.parts.append(5)
        return self

    def set_size(self):
        self.build.parts.append(300)# in meters
        return self    
    
    def get_results(self):
        
        return self.build
    
    
class Creator (object):
    
    @staticmethod
    def create():
        
        return house()\
            .set_roof()\
            .set_rooms_num()\
            .set_size()\
            .get_results()


PRODUCT=Creator.create()
print(PRODUCT.parts)


#================================================================================================

class Computer (object):
    def __init__(self, cpu ,ram, storage ,gpu ):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu =gpu
        
    def __str__(self):
        return f"cpu:{self.cpu}, ram:{self.ram}, storage:{self.storage}, gpu:{self.gpu}"

# interface
from abc import ABCMeta , abstractmethod
class ComputerBuilder(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def cpu(self,cpu):
        pass
    
    @staticmethod
    @abstractmethod
    def ram(self,memory):
        pass
    
    @staticmethod
    @abstractmethod
    def storage(self,storage):
        pass
    
    @staticmethod
    @abstractmethod
    def gpu(self,gpu):
        pass
    
    @staticmethod
    @abstractmethod
    def build(self):
        pass
    

class GamingComputerBuilder(ComputerBuilder):
    
    def cpu(self,cpu):
        self.cpu=cpu
        return self
        
    def ram(self,memory):
        self.ram=memory
        return self
    
    def storage(self,storage):
        self.storage=storage
        return self
    
    def gpu(self,gpu):
        self.gpu=gpu
        return self
    
    def build(self):
        return Computer(self.cpu,self.ram,self.storage,self.gpu)
    

class Director:
    
    def __init__(self,builder):
        self.builder=builder
        
    def Creator(self,cpu,ram,storage,gpu):
        
        self.builder.cpu(cpu)
        self.builder.ram(ram)
        self.builder.storage(storage)
        self.builder.gpu(gpu)
        return self.builder.build()
    
gaming_computer_builder=GamingComputerBuilder()
director = Director(gaming_computer_builder)

gaming_pc = director.Creator("intel i7 ","16 GB ","2TB ", "RTX 4090 Ti ")
print(gaming_pc)

#================================================================================================================================

# class Computer (object):
#     def __init__(self, cpu ,ram, storage ,gpu ):
#         self.cpu = cpu
#         self.ram = ram
#         self.storage = storage
#         self.gpu =gpu
        
#     def __str__(self):
#         return f"cpu:{self.cpu}, ram:{self.ram}, storage:{self.storage}, gpu:{self.gpu}"


# # interface
# from abc import ABCMeta , abstractmethod
# class ComputerBuilder(metaclass=ABCMeta):
#     @staticmethod
#     @abstractmethod
#     def cpu(self,cpu):
#         pass
    
#     @staticmethod
#     @abstractmethod
#     def ram(self,memory):
#         pass
    
#     @staticmethod
#     @abstractmethod
#     def storage(self,storage):
#         pass
    
#     @staticmethod
#     @abstractmethod
#     def gpu(self,gpu):
#         pass
    
#     @staticmethod
#     @abstractmethod
#     def build(self):
#         pass
    

# class GamingComputerBuilder(ComputerBuilder):
#     def __init__(self):
        
#         self.components = []
    
#     def cpu(self,cpu):
#         self.cpu=cpu
#         return self
        
#     def ram(self,memory):
#         self.ram=memory
#         return self
    
#     def storage(self,storage):
#         self.storage=storage
#         return self
    
#     def gpu(self,gpu):
#         self.gpu=gpu
#         return self
    
#     def build(self):
#         return Computer(self.cpu,self.ram,self.storage,self.gpu)
    

# class Director:
    
#     def __init__(self,builder):
#         self.builder=builder
        
#     def Creator(self,cpu,ram,storage,gpu):
        
#         self.builder.components.append(cpu)
#         self.builder.components.append(ram)
#         self.builder.components.append(storage)
#         self.builder.components.append(gpu)
#         return self.builder.build()
    
# gaming_computer_builder=GamingComputerBuilder()
# director = Director(gaming_computer_builder)

# gaming_pc = director.Creator("intel i7 ","16 GB ","2TB ", "RTX 4090 Ti ")
# print(gaming_pc)