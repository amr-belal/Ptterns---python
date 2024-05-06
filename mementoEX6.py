class Memento:
    def __init__(self,file , content):
        self.file = file
        self.content= content
    

class CoonstructionX:
    def __init__(self,file_path):
        self.file=file_path
        self.content = ""
    
    def write(self,string):
        self.content+=string
        
    def save(self):
        return Memento(self.file,self.content)
    
    
    def undo(self,memento):
        self.file=memento.file
        self.content=memento.content
        
class ApplyY:
    def save(self,x):
        self.mem=x.save()
    def undo(self,x ):
        x.undo(self.mem)
        
if __name__ =="__main__":
    y=ApplyY()
    
    x=CoonstructionX("File.txt")
    
    x.write("first version") # string variable store this and added to content
    
    print(x.content) # print content after addin string to it 
    
    y.save(x) #save what we did in x "fisrt version "
    
    
    x.write("\n second version") # add second version
    print(x.content) # here we have second version and first version in history
    
    y.undo(x) # undeo second version
    print(x.content) # print first version only after undo
    
#================================================================================================
# GAMECHECKPOINT EXAMPLE

class GameStateMemento(object):
    def __init__(self,player_position,health,inventory):
        self.player_position = player_position
        self.health = health
        self.inventory =inventory
        
class Game :
    def __init__(self) :
        self.player_position=(0,0)
        self.health=100
        self.inventory=[]
        
    def save_checkpoint(self):
        return GameStateMemento(self.player_position,self.health,self.inventory)
    
    def load_checkpoint(self ,checkpoint):
        #restore from memento class
        self.player_position=checkpoint.player_position
        self.health=checkpoint.health
        self.inventory=checkpoint.inventory


game =Game()

checkpoint1=game.save_checkpoint()
game.player_position=(5,5)
game.health-=70
game.inventory =["ak-47","surpressor","scope-8"]

print(checkpoint1.health)
checpoit2=game.save_checkpoint()

game.load_checkpoint(checkpoint1)
print(checpoit2.health)