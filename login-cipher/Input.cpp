#include <iostream>

int main()
{
    char passwd_buffer[76];
    scanf("%64[^\n]",passwd_buffer);
    std::cout << passwd_buffer << std::endl;
    return 0;
}