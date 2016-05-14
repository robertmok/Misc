#include <iostream>
#include <string>
#include <conio.h>
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
using namespace std;

#ifndef GAMEF_H
#define GAMEF_H

//header file
//game functions

class fract{  // multiply
      public:
	  	 int lowest, highest; 	 
	  	 fract (int Getlowest, int Gethighest){  //constructor with 2 parameters
		 	   lowest = Getlowest;
			   highest = Gethighest;
         }	 
         virtual void rdm (float& num1, float& num2, float& num3, float& num4) {          
			  srand((unsigned)time(0)); //seed time
    		  int num; 
    		  int range =(highest-lowest)+1; 
    		  for(int index = 0; index < 6; index++){ //random 6 numbers 
        	  		  num = lowest+int(range*rand()/(RAND_MAX + 1.0)); //make numbers more random
					  if (index == 0 || index > 4) 
					  	 num1 = num;
					  else if (index == 1)
					  	 num2 = num;
					  else if (index == 2)
					  	   num3 = num;
					  else
					  	  num4 = num; 
			  }
     }
};

class decimal{ //add and subtract
	  public:
		 void rdm (float& num1, float& num2, float& ans){
 		      srand((unsigned)time(0)); //seed time
    		  int random_integer = rand(); 
	   		  //cout << random_integer << "odd even test" << endl; //test
			  if (random_integer % 2 == 0){   //even number
			  	 srand((unsigned)time(0));  //seed time
    			 float num; 
    			 for(int index=0; index<4; index++){ //random 4 numbers
       			 		 num = (rand() % (100-1)) / 100.0; //divide random numbers by 100 to give you numbers with two decimal places 
			 				//cout << num << "random decimal test" << endl; //test
				  		  if (index == 2 || index == 4)
				  	 	  	 num1 = num;
		  			      else 
                             num2 = num;
		          }
		          cout << "What is " << num1 << " + " << num2 << " ?" << endl;
		          ans = num1 + num2;
		          cout << ans << "ans" << endl; //test
				  }
               else {
   		          float num; 
    			 for(int index=0; index<4; index++){  //odd number //random 4 numbers
       			 		 num = (rand() % (100-1)) / 100.0; //divide random numbers by 100 to give you numbers with two decimal places
			 				//cout << num << "random decimal test" << endl; //test
				  		  if (index == 2 || index == 4) 
				  	 	  	 num1 = num;
		  			      else 
                             num2 = num;
		          }
		          cout << "What is " << num1 << " - " << num2 << " ?" << endl;
		          ans = num1 - num2;
		          cout << ans << "ans" << endl; //test
				  }
	  }
};

class expon : public fract {  //inheritance from base class fract
	  public:	 
	  	 expon (int Getlowest, int Gethighest) : fract (Getlowest, Gethighest){  //derived constructor with 2 parameters
		 	   lowest = Getlowest;
			   highest = Gethighest;
         }	 
  		 void rdm(float& num1, float& num2, float& num3, float& num4){  //implements virtual fuction in base class
  		 	  srand((unsigned)time(0)); //seed time
		  	  int num; 
		  	  int range = (highest-lowest)+1; 
		  	  for(int index = 0; index < 4; index++){ //random 4 numbers 
    	  		  num = lowest+int(range*rand()/(RAND_MAX + 1.0));  //makes numbers more random
				  if (index == 2 || index == 4)
				  	 num1 = num;
				  else 
				  	 num2 = num;
		          }
        }
};


void check (float& uans, float& ans, int& score){ //check answer function
	 if (uans == ans) //if correct
	 	score = score+1; //score plus 1
     else
     	 score = score+0;
		 }
		 
#endif		 
		 
		 
