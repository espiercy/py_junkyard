from struct import *

packed_data = pack( 'iif',4,2,3.6 )

print(packed_data)

unpacked_data = unpack('iif', packed_data)

print(unpacked_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iifi'))