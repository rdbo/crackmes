#include <iostream>

ulong GetKey(char *param_1)
{
    uint uVar1;
    ulong key;
    int DAT_00104010;
    char* DAT_00104028;
    
    if (param_1 != (char *)0x0) {
      DAT_00104010 = 0x7b1;
      DAT_00104028 = param_1;
    }
    if (*DAT_00104028 == '\0') {
      key = 0;
    }
    else {
      uVar1 = (uint)(DAT_00104010 * 7 >> 0x1f) >> 0x10;
      DAT_00104010 = (DAT_00104010 * 7 + uVar1 & 0xffff) - uVar1;
      key = (ulong)(uint)((int)*DAT_00104028 + ((DAT_00104010 / 10) * 10 - DAT_00104010));
      DAT_00104028 = DAT_00104028 + 1;
    }
    return key;
}

int main()
{
    ulong key = GetKey((char*)"fhz4yhx|~g=5");
    std::cout << "[*] Output of GetKey(\"fhz4yhx|~g=5\"): " << key << "  ==  " << (char)key << std::endl;
    key = GetKey(0);
    std::cout << "[*] Output of GetKey(0): " << key << "  ==  " << (char)key << std::endl;
    return 0;
}