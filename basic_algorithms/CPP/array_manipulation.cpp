
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[]){
	string str="This is a complete sentence.";
	string str1 = "sssw";

	str.insert(10, str1);

    cout << str << endl;
	// cout << "Hello World!" << endl;
	return 0;
}