import collection 
import math
import sos

# return full path
def path(filename):
    filepath = os.path.realpath(__file__)
    dirpath = os.path.dirname(filepath)
    fullpath = os.path.join(dirpath,filename)
    return fullpath

def line(a,b,x,y):
    import turtle
    turtle.up()
    turtle.goto(a,b)
    turtle.down()
    turtle.goto(x,y)

class vector(collection.Sequence):
    PRECISION = 6
    __slots__ = ('_x','_y','_hash')

    #constructor
    def __init__(self,x,y):
        self._hash = None
        self._x = round(x,self.PRECISION)
        self._y = round(y,self.PRECISION)

    @property
    #getter
    def x(self):
        return self._x


    @x.setter
    def x(self, value):
        if self._hash is not None:
            raise ValueError("Cannot set x after hashing")
        self._x = round(value, self.PRECISION)

    
    @property
    #getter
    def y(self):
        return self._y


    @y.setter
    def y(self, value):
        if self._hash is not None:
            raise ValueError("Cannot set y after hashing")
        self._y = round(value, self.PRECISION)


    def __hash__(self):
        # v.__hash__() = hash(v)
        if self._hash is None:
            pair = (self.x, self.y)
            self._hash = hash(pair)
        
        return self._hash

    def __len__(self):
        return 2
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError
    
    def copy(self):
        type_self = type(self)
        return type_self(self.x, self.y)

    def __eq__(self, other):
        # v == w if v = vector(1,2) w = vector(1,2)
        if isinstance(other, vector):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, vector):
            return self.x != other.x and self.y != other.y
        else:
            return NotImplemented

    def __iadd__(self, other):
        #v.__iadd__(w) -> v += w
        if self._hash is not None:
            raise ValueError("Cannot add a vector after hashing")

        elif isinstance(other, vector):
            self.x += other.x    
            self.y += other.y
        else:
            self.x = other
            self.y = other
        return self

    
    def __add__(self, other):
        copy = self.copy()
        return copy.__iadd__(other)


    __radd__ = __add__

    def move(self, other):
        #move vector by other (n places)
        #v =  vector(1,2) w = vector(3,4) 
        #v.move(w) ==> vector(4,6)
        self.__iadd__(other)


    def __isub__(self, other):
        if self._hash is not None:
            raise ValueError("Cannot subtract a vector after hashing")

        elif isinstance(other, vector):
            self.x -= other.x 
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other

        return self

       

    def __sub__(self, other):
        copy = self.copy()
        return copy.__isub__(other)

    __rsub__ = __sub__ 


    def __imul__(self, other):
        #v.imul__(w) => v *= w
        if self._hash is not None:
            raise ValueError("Cannot multiply a vector after hashing")

        elif isinstance(other, vector):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other.x
            self.y *= other.y
        return self
    

    def __mul__(self, other):
        copy = self.copy()
        return self.__imul__(other)

    __rmul__ = __mul__



    def scale(self, other):
        self.__imul__(other)


    def __itruediv__(self, other):
        if self._hash is not None:
            raise ValueError("Cannot divide a vector after hashing")
        else:
            self.x /= other.x
            self.y /= other.y
        return self

    def __truediv__(self, other):
        copy = self.copy()
        return copy.__itruediv__(other)

    #__rtruediv__ = __truediv__

    def __neg__(self, other):
        copy = self.copy()
        copy.x = -copy.x
        copy.y = -copy.y
        return copy

    def __abs__(self, other):
        return (self.x**2 + self.y**2)**0.5

    def rotate(self, angle):
        #y = ycos(0) + xsin(0)
        #x = xcos(0) - ysin(0)
        if self._hash is not None:
            raise ValueError("cannot rotate vector after hashing")

        radian = (angle * math.pi)/ 180.0
        self.x = (self.x * math.cos(radian) - self.y * math.sin(radian))
        self.y = (self.y * math.cos(radian) + self.x * math.sin(radian))

    def __repr__(self):
        #v.__repr__() = repr(v)
        type_self = type(self)
        name = type_self.__name__
        return '{}({!r},{!r})'.format(name, self.x, self.y)
        