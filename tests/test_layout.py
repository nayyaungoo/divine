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