class Cookie:
    def __init__(self, color):
        self.color = color
        
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        
    def __str__(self) -> str:
        return "Cookie is " + self.color
                
cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print(cookie_one)
print(cookie_two)

cookie_two.set_color('red')

print(cookie_two)

