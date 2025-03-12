from src.divine import *

print("----------------------------")

value = Layout().validate(None)
print(f"value: {type(value)}")

print("----------------------------")

value = Empty() + 2
print(f"(new) value: {value}")

print("----------------------------")

print(Layout().validate.__doc__)

print("----------------------------")

value = Empty() + 2
print(f"(new) value: {value.half}")

print("----------------------------")

layout = Layout()
layout.maxy = None
layout.maxx = layout.maxy + 20
print(f"layout.maxx: {layout.maxx}")

print("----------------------------")

layout.begy = 20
layout.begx = 20
print(layout.has_begyx)
print(layout.has_maxyx)
print(layout.has_allyx)