from ctypes import *

m = cdll.LoadLibrary(r".\c_function.dll")
m.foo.restype = c_int
m.foo.argtypes = [c_int, c_int, c_int]
a = m.foo(3, 2, 4)

print(a)