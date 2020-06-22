#include <iostream>
#include <string.h>

char* Decrypt(char *param_1)
{
  uint key;
  char *pchar;
  
  key = 0x7b1;
  pchar = param_1;
  while (*pchar != '\0') {
    key = key * 7 & 0xffff;
    *pchar = (char)(*pchar + ((char)((int)key / 10) * '\n' - (char)key));
    pchar = pchar + 1;
  }
  return param_1;
}

int main()
{
    const char string[] = "Gtu.}\'uj{fq!p{$";
    char buffer[256];
    memset(buffer, 0x0, sizeof(buffer));
    memcpy(buffer, string, sizeof(string));
    std::cout << Decrypt(buffer) << std::endl;
    return 0;
}