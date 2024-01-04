#include <iostream>

using namespace std;

int main()
{
    char a, b;
    string str, str2, str3;
    cin >> str >> str2;
    
    str3 = str[str.size()-1] - '0' + str2[str2.size()-1] - '0';
    str.pop_back(); str2.pop_back();
    a = str3[0] / 10;
    str3[0] = (str3[0]%10) + '0';
    
    while (str.size() > 0 || str2.size() > 0)
    {
        b = 0;
        if (str.size())
        {
            b = str[str.size()-1] - '0';
            str.pop_back();
        }
        if (str2.size())
        {
            b = b + str2[str2.size()-1] -'0';
            str2.pop_back();
        }
        b = b + a;
        
        a = b/10;
        b = (b%10) + '0';
        str3 = b + str3;
    }
    
    if (a > 0)
    {
        a = a + '0';
        str3 = a + str3;
    }
    
    cout << str3;
    return 0;
}