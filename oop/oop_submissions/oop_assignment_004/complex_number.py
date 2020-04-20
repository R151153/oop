import math
class ComplexNumber:
    def __init__(self,real_num=0,imaginary_num=0):
        if isinstance(real_num,str) and isinstance(imaginary_num,str): 
            raise ValueError("Invalid value for real and imaginary part")
        elif isinstance(real_num,str):
            raise ValueError("Invalid value for real part")
        elif isinstance(imaginary_num,str):
            raise ValueError("Invalid value for imaginary part")
        self._real_part=real_num
        self._imaginary_part=imaginary_num
    @property
    def real_part(self):
        return self._real_part
    @property
    def imaginary_part(self):
        return self._imaginary_part
    def conjugate(self):
        return ComplexNumber(self.real_part,-self.imaginary_part)
    def __add__(self,other):
        return ComplexNumber(self._real_part+other._real_part,self._imaginary_part+other._imaginary_part)
    def __sub__(self,other):
        return ComplexNumber(self._real_part-other._real_part,self._imaginary_part-other._imaginary_part)
    def __mul__(self,other):
        return ComplexNumber(self._real_part*other._real_part-self._imaginary_part*other._imaginary_part,
        self._real_part*other._imaginary_part+self._imaginary_part*other._real_part)
    def __truediv__(self,other):
        k=pow(other._real_part,2)+pow(other._imaginary_part,2)
        return ComplexNumber(round((self._real_part*other._real_part+self._imaginary_part*other._imaginary_part)/k,2),
        round((self._imaginary_part*other._real_part- other._imaginary_part*self._real_part)/k,2))
    def __eq__(self, other):
        return self._real_part == other._real_part and self._imaginary_part == other._imaginary_part
    def __abs__(self):
        return round(math.sqrt(pow(self._real_part,2)+pow(self._imaginary_part,2)),3)
    def __str__(self):
        complex_number="{}+{}i".format(self.real_part,self.imaginary_part)
        complex_number=complex_number.replace("+-","-")
        return complex_number