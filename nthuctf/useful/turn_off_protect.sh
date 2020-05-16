gcc -z execstack -fno-stack-protector -no-pie hackme.c -o hackme
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space