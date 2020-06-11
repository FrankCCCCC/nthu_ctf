gcc -z execstack -fno-stack-protector -no-pie hackme.c -o hackme
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

nasm -f elf64 assembly.asm . // this will generate assembly.o file
ld -m elf_x86_64 -s -o assembly assembly.o . //this will generate our final binary 
chmod +x assembly //to make our binary executable 
ls -l assembly //just to make sure everything is ok with the compiled file
./assembly . //executing our binray to test if it's working, if so we'll see something like this

objdump -d ./shellcode|grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'