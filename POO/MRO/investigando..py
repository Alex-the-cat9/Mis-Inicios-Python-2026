class A:
    def hablar(self):
        print("A")
class B(A):
     pass
class F:
    def hablar(self):
        print("F")
     
class C(F):
    pass
class D(B,C):
        pass

d = D()
d.hablar()
print(D.mro())
class A:
    def hablar(self):
        print("A")

class B(A):
    def hablar(self):
        print("B")

class D(A, B):
    pass