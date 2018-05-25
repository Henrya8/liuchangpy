from  math import hypot

class Vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __repr__(self):
        '''
        将对象用字符串函数将被内置函数repr调用
        :return:
        '''
        return 'Vector({0},{1})'.format(self.x,self.y)
    def __abs__(self):
        '''
        求模运算
        :return:
        '''
        return hypot(self.x,self.y)
    def __bool__(self):
        '''
        逻辑运算被bool调用
        :return:
        '''
        return bool(abs(self))
    def __add__(self, other):
        '''
        +运算
        :param other:
        :return:
        '''
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)
    def __mul__(self,scalar):
        '''
        *运算
        :param scalar:
        :return:
        '''
        return Vector(self.x*scalar,self.y*scalar)

print(Vector(5,4)+Vector(1,1))
print( Vector(5,4) * 2 )
print(bool(Vector(0,0)))




