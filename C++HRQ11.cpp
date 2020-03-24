#include <sstream>
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

vector<string> parseInts(string str) {
    vector<string> numbers;
    string temp;
    stringstream str_strm(str);
    while(getline(str_strm , temp, ',')){
        numbers.push_back(temp);
    }
    return numbers;
}

int main() {
    string str; 
    cin >> str;
    vector<string> integers = parseInts(str);
    
    for(unsigned int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}


