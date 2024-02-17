"""Class implementing Area of Square shape"""


class Square:
    """Square shape 
    
    Args:
      	length: float
      	
    Attributes:
    	area
    	from_area
    """
    def __init__(self, length):
        self.length = length
        
    def __repr__(self):
        return f"{type(self).__qualname__} ({self.length!r})"
        
    @property
    def area(self) -> float:
        return self.length**2
    
    @classmethod
    def from_area(cls, area: int or float) -> float:
        return cls(area**0.5)


if __name__ == "__main__":
    print(Square.from_area(25))
