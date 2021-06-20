import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self, no):
        real=self.real+no.real
        imaginary=self.imaginary+no.imaginary
        return Complex(real,imaginary)
    def __sub__(self, no):
        real=self.real-no.real
        imaginary=self.imaginary-no.imaginary
        return Complex(real,imaginary)
    def __mul__(self, no):
        z1=complex(self.real, self.imaginary)
        z2=complex(no.real, no.imaginary)
        z3=z1*z2
        real=z3.real
        imaginary=z3.imag
        return Complex(real,imaginary)
        
    def __truediv__(self, no):
        z1=complex(self.real, self.imaginary)
        z2=complex(no.real, no.imaginary)
        z3=z1/z2
        real=z3.real
        imaginary=z3.imag
        return Complex(real,imaginary)
    def mod(self):
        res=abs(complex(self.real,self.imaginary))
        real=res
        imaginary=0
        return Complex(real,imaginary)
