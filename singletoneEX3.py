import copy

class SingleTone(object):
    values =[]
    
    def __new__(cls):
        return cls
    
    def __init__(self):
        "init magic method"
        
    @staticmethod
    def static_method(self):
        "Static Method for inner variable required"
    
    @classmethod
    def class_method(cls):
        "Class method for class level variable"
        val=cls.values.append(1)
        print(val)
        

print(f"id(SingleTone):\t{id(SingleTone)}")
SingleTone.class_method()
object1 =SingleTone()
print(f"object1:\t{id(object1)}")
object1.class_method()
