'''
    Aula 17 - Metaclasses
    Em Python tudo é um objeto: incluindo classes
    Metaclasses são as "classes" que criam classes.
    type é uma metaclasse(!!!???)
'''

class Meta(type):
    def __new__(mcs, name, bases,namespace):
        if name == 'A':
            return type.__new__(mcs,name,bases,namespace)

class A(metaclass=Meta):
    def fala(self):
        self.b_fala()

class B (A):
    pass

