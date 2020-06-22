#include <iostream>

int DAT_0;
char* DAT_1;

ulong GetKey(char *param_1)
{
    uint uVar1;
    ulong key;
    
    if (param_1 != (char *)0x0) {
      DAT_0 = 0x7b1;
      DAT_1 = param_1;
    }
    if (*DAT_1 == '\0') {
      key = 0;
    }
    else {
      uVar1 = (uint)(DAT_0 * 7 >> 0x1f) >> 0x10;
      DAT_0 = (DAT_0 * 7 + uVar1 & 0xffff) - uVar1;
      key = (ulong)(uint)((int)*DAT_1 + ((DAT_0 / 10) * 10 - DAT_0));
      DAT_1 = DAT_1 + 1;
    }

    std::cout << (char)key;
    return key;
}

void CheckPassword(char* param_2)
{
    int key;
    key = GetKey(param_2);
    while (key != 0) {
        key = GetKey(0);
    }

    std::cout << std::endl;
}

int main()
{
    char passwd_string[] = "fhz4yhx|~g=5";
    CheckPassword((char*)passwd_string);
    return 0;
}