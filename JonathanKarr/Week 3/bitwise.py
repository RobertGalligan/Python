print(3 & 4)    #this is an and gate they both have to be ones to be true
#  00000011   00000100
#  00000000

print (3 | 4)   #this is an or gate that compares both numbers and if there is a one it will accept it as true
#  00000011   00000100
#  00000111
print(3^5)      #this is an xor gate.
#  00000011
#  00000101
# =00000110

print(~21)
# 21 is 00010101 so not 21 is -22 11101010

print(~-21)
# -21 is 11101011 so not -21 is 20 00010100

print(17<<1)
# 17 is 00010001, so left shift 1 is 00100010 is 34

print(17>>1)
# 17 is 00010001, so right shift 1 is 00001000 is 8
