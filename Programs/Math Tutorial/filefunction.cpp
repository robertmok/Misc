#include <iostream>
#include <fstream>
#include <string>
using namespace std;


//Program for creating Binary files and storing a value

int main () {
int num=0;
    ofstream file ("fraction.bin", ios::binary); //write to file 
    file.write(reinterpret_cast<const char *>(&num), sizeof(num)); 
    file.close (); 
  cout << "num b4:"<< num << endl;
  
  
  //ifstream myFile ("file.bin"); //read from file
//   int test;
//    myFile.read(reinterpret_cast<char*>(&test), sizeof(int));
//	myFile.close();
//  cout << "test:" << test << endl;
  system ("pause");
  return 0;
}
