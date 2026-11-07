class Character:
    def __init__ (self,Name,XPosition,YPosition):
        self.Name=Name#STRING 
        self.XPosition=XPosition#INTEGER
        self.YPosition=YPosition#INTEGER

    def GetXPosition(self):
        return self.XPosition

    def GetYPosition(self):
        return self.YPosition

    def SetXPosition(self,value):
        self.XPosition+=value
        if self.XPosition>=10000:
            self.XPosition=10000
        if self.XPosition<=0:
            self.XPosition=0
    def SetYPosition(self,value):
        self.YPosition+=value
        if self.YPosition>=10000:
            self.YPosition=10000
        if self.YPosition<=0:
            self.YPosition=0
    def Move(self,string):
        if string=="up":
            self.YPosition+=10
        if string=="down":
            self.YPosition-=10                
        if string=="left":
            self.XPosition-=10    
        if string=="right":
            self.XPosition+=10
Jack=Character('Jack',50,50)
class BikeCharacter(Character):
    def __init__ (self,Name,XPosition,YPosition):
        super().__init__ (Name,XPosition,YPosition)

    def Move(self,string):
        if string=="up":
            self.YPosition+=20
        if string=="down":
            self.YPosition-=20                
        if string=="left":
            self.XPosition-=20    
        if string=="right":
            self.XPosition+=20
Karla=BikeCharacter('Karla',100,50)
CharacterChoice = input("Which character do you want to move? jack/karla: ").lower()
Direction = input("Which direction? up/down/left/right: ").lower()
if CharacterChoice=='karla':
    Karla.Move(Direction)
    print(f'Karlas new position is X ={Karla.XPosition}, Y ={Karla.YPosition}')
if CharacterChoice=='jack':
    Jack.Move(Direction)
    print(f'Jack new position is X ={Jack.XPosition}, Y ={Jack.YPosition}')

              