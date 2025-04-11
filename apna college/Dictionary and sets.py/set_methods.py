# Set methods
Info = {"Kashvi",21, "Delhi","Female" , 23}
#set is mutable but set ke elements immutable h

# set.add(el) - to add an element in the set
Info.add("Yuvraj")
Info.add(21)
print(Info)

# set.remove(el) - t0 remove an element in the set
Info.remove("Delhi")
print(Info)
# agr koi value hum remove krna chahe jo exist nhi krti to it gives KeyError:__
# set ke andr saari values hashable values hoti h, hashable values mtlb jinka hash run krne pr same aaye
# agr koi list dalege set mein jo ki mutable hota to pure set ki hashable value change hojaygi jisse prob aaygi

# set.clear() - it empties the set
# Info.clear()
# print(Info)

# set.pop() - to remove a random value
print(Info.pop()) # koi bhi random value
