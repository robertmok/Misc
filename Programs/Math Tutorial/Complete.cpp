#include <iostream>
#include <string>
#include <conio.h>
#include <windows.h>
#include "tutool.h"
#include "gamef.h"
#include <fstream>
using namespace std;

//program start

int main()
{
 	//variables
 	int choice1 = 0, choice2 = 0, choice3 = 0, loop = 0, exp = 0, col = 0, quit = 0;
	int choice4 = 0, loop2 = 0, loop3 = 0, loop4 = 0, loop5 = 0, choice5 = 0;
	float ans = 0;
	int dm = 0, nm = 0, loop8 = 0, loop9 = 0, mainloop = 0;
	string tex;
    tutool tool;
    cout << "Welcome to Grade 6 Math Tutorial!" << endl;
 
 while (mainloop == 0){

//reset all values for new run
 int choice1 = 0, choice2 = 0, choice3 = 0, loop = 0, exp = 0, col = 0, quit = 0;
 int choice4 = 0, loop2 = 0, loop3 = 0, loop4 = 0, loop5 = 0, choice5 = 0;
 float ans = 0;
 int dm = 0, nm = 0, loop9 = 0; // loop8 = 0 //mainloop = 0;	   
 	   
 while (loop2 == 0){
    tex = "1) Tutorials";
    col = 2; //green color
    tool.color(tex, col); //color function
    tex = "2) Game";
    col = 14; //yellow color
    tool.color(tex, col); //color function
    tex = " ";
    col = 15; //white color
    tool.color(tex, col); //color function
    //cin >> choice1;
     if (!(cin >> choice1)) { //if input is not an integer
	 	cout << "Error, please select again!" << endl; 
   		cin.clear(); // clear the error
		// clear the input stream
	    cin.ignore(numeric_limits <streamsize>::max(), '\n');
		}  
    else {
	    if (choice1 == 1 || choice1 == 2){ 
	       loop2 = 1;
	       system("CLS"); //clear screen
		   }
	    else {
	 	   cout << "Error, please select again!" << endl;
	 	   cin.clear(); // clear the error
		   // clear the input stream
	       cin.ignore(numeric_limits <streamsize>::max(), '\n');
	 	   system ("pause"); //pause window
	 	   system ("CLS"); //clear screen
		   }
	   }
}

if (choice1 == 2){
   loop = 1;
   }
 	   while (loop == 0){
 		     if (choice1 == 1){
                 cout << "List of Tutorials" << endl;
                 tex = "1) Decimal Numbers";
                 col = 11; //cyan color 
                 tool.color(tex, col); //color function
                 //cout << "Press 1 to pick Decimal Numbers" <<endl;
                 tex = "2) Exponents"; 
                 col = 10; //green color
                 tool.color(tex, col); //color function
                 //cout << "Press 2 to pick Exponents" << endl;
                 tex = "3) Fractions";
                 col = 12; //red color
                 tool.color(tex, col); //color function
                 //cout << "Press 3 to pick Fractions" << endl;
                 tex = " ";
                 col = 15; //white color 
                 tool.color(tex, col); //color function
                 //cin >> choice2;
 		          }
            if (!(cin >> choice2)) { //if input is not an integer
			 	cout << "Error, please select again!" << endl;
		   		cin.clear(); // clear the error
				// clear the input stream
			    cin.ignore(numeric_limits <streamsize>::max(), '\n');
				}  
		    else {																										
 	 		   if (choice2 == 1 || choice2 == 3)
			   	  		   loop = 1;
	  		   else{
                 cout << "Error, please pick again" << endl;
                 cin.clear(); // clear the error
				// clear the input stream
			    cin.ignore(numeric_limits <streamsize>::max(), '\n');
				 system ("pause"); //pause window
				 system ("CLS"); //clear screen
				 } 
  		 }    
 		          
//===============================================================================================
             if (choice2 == 1){
                 loop = 1;
                 system("CLS"); //clear screen
                 cout << "Introduction to Decimal Numbers" << endl;
                 cout << "Press any key to continue after each instruction!" << endl;
                 tool.line (); //class function
                 cout << "Decimal numbers is a method of writing fractions without a numerator and a denominator" << endl;
                 cout << "For example: 1 / 2 can be written as 0.5" << endl;
                 cout << "or 2 / 5 can be written as 0.4\n";
                 tool.line (); //class function
                 cout << "A number that is less then 1, write a ZERO before your decimal point like this:" << endl;
                 cout << "0.5 but not .5\n";
				 tool.enter (); //class function
				 
				 while (loop3 == 0){
    				 cout << "Lessons" << endl;
    				 tex = "1) Adding Decimals";
                     col = 11; //cyan color
                     tool.color(tex, col); //color function
    				 //cout << "Press 1 to learn adding decimals" << endl;
    				 tex = "2) Subtracting Decimals";
    				 col = 10; //green color
    				 tool.color(tex, col); //color function
    				 //cout << "Press 2 to learn subtracting decimals" << endl;
    				 tex = "3) Multiplying Decimals";
    				 col = 12; //red color
    				 tool.color(tex, col); //color function
    				 //cout << "Press 3 to learn dividing decimals" << endl;
    				 tex = " ";
    				 col = 15; //white color 
    				 tool.color(tex, col); //color function
    				 cout << "Your choice is: " << endl;
    				 //cin >> choice3;
    				 if (!(cin >> choice3)) { //if input is not an integer
       					 	cout << "Error, please select again!" << endl;
 						    cin.clear(); // clear the error
    						// clear the input stream
    						cin.ignore(numeric_limits <streamsize>::max(), '\n');
							}  
     	             else {
	    				 if (choice3 == 1 || choice3 == 2 || choice3 == 3){
	                        loop3 = 1;
	    				    system("CLS"); //clear screen
	                        }
				         else {
	                        cout << "Error, please select again!" << endl;
	                        cin.clear(); // clear the error
    						// clear the input stream
    						cin.ignore(numeric_limits <streamsize>::max(), '\n');
	                        system ("pause"); //pause window
	                        system ("CLS"); //clear screen
	                        }
						}
              } 
				 
//------------------------------------------------------------------------------------------------
				 if (choice3 == 1){
	                 cout << "Adding Decimals" << endl;
	                 tool.line (); //class function
	                 cout << "Adding decimals is just like adding whole numbers" << endl;
	                 cout << "All you have to do is to line up the decimal points" << endl;
					 tool.line (); //class function
					 cout << "Example: What is 0.0005 +  254.0001 ?" << endl;
					 cout << "Write the first number on top of the second number so that the decimal points lined up" << endl;
					 cout << "Then start adding the columns starting from the right side" << endl;
					 cout << "   0.0005" << endl;
					 cout << " 254.0001" << endl;
					 cout << "+________" << endl;
					 cout << " 254.0006" << endl;
					 tool.line (); //class function
					 cout << "Now you have a try!" <<endl;
					 cout << "Add 50.55 + 100.20 + 810.01" << endl;
					 ans = 50.55 + 100.20 + 810.01;
					 tool.check (ans, exp); //class function
					 if (exp == 1){
					 	cout << "The answer to the question:" << endl;	 
					 	cout << "  50.55" << endl;
					 	cout << " 100.20" << endl;
					 	cout << " 810.01" << endl;
					 	cout << "+______" << endl;
					 	cout << " 960.76" << endl;
						}
					 if (exp == 2)
	    	            cout << "Your answer is correct" << endl;
	    	         tool.line (); //class function
					 cout << "You have completed Adding Decimals Tutorial!" << endl;
					 tex = "1) Continue to next lesson";
					 tool.qloop (tex, mainloop, quit); //class function
		 			 if (quit == 1) {
			 		   choice3 = 2;
                       system("CLS"); //clear screen
					   } 
				 }
					 
//------------------------------------------------------------------------------------------------					 
				 if (choice3 == 2){
				 	 cout << "Subtracting Decimals" << endl;
	                 tool.line (); //class function
	                 cout << "Subtracting decimals is just like adding decimal numbers" << endl;
	                 cout << "All you have to do is to line up the decimal points just like adding them" << endl;
					 tool.line (); //class function
					 cout << "Example: What is 156.99 - 42.73?" << endl;
					 cout << "Write the first number on top of the second number so that the decimal points lined up" << endl;
					 cout << "Then start subtracting the columns starting from the right side" << endl;
					 cout << " 156.99" << endl;
					 cout << "  42.73" << endl;
					 cout << "-______" << endl;
					 cout << " 114.26" << endl;
					 tool.line (); //class function
					 cout << "Now you have a try!" <<endl;
					 cout << "Subtract 9846.59 - 6213.21 - 132.11 - 0.02 " << endl;
					 ans = 9846.59 - 6213.21 - 132.11 - 0.02;
					 exp = 0;
					 tool.check (ans, exp); //class function
					 if (exp == 1){
					 	cout << "The answer to the question:" << endl;	 
					 	cout << " 9846.59" << endl;
					 	cout << " 6213.21" << endl;
					 	cout << "  132.11" << endl;
					 	cout << "    0.02" << endl;
					 	cout << "-_______" << endl;
					 	cout << " 3501.25" << endl;
						}
					 if (exp == 2)
	    	            cout << "Your answer is correct" << endl;
	    	         tool.line (); //class function 
					 cout << "You have completed Subtracting Decimals Tutorial!" << endl; 
					 tex = "1) Continue to Next Lesson";    
					 tool.qloop (tex, mainloop, quit); //class function
		 			 if (quit == 1) {
			 		   choice3 = 3;
                       system("CLS"); //clear screen
					   }
				 }
//------------------------------------------------------------------------------------------------					 
				 if (choice3 == 3){
				 	 cout << "Multiplying Decimals" << endl;
	                 tool.line (); //class function
	                 cout << "Multiplying decimals is just like multiplying whole numbers" << endl;
	                 cout << "All you have to do is to line up the decimal points just like subtracting them" << endl;
					 tool.line (); //class function
					 cout << "Example: What is 25.06 x 0.4 ?" << endl;
					 cout << "Write the first number on top of the second number" << endl;
					 cout << "  25.06" << endl;
					 cout << "    0.4" << endl;
					 cout << "x_______" << endl;
					 tool.line (); //class function
					 cout << "Then start multiplying the columns starting from the right side" << endl;
					 cout << "4 x 6 is 24, 24 is larger than 10 so place 2 on top of 0 like this:" << endl;
					 cout << "     2 " << endl;
					 cout << "  25.06" << endl;
					 cout << "    0.4" << endl;
					 cout << "x______" << endl;
					 cout << "      4" << endl;
					 tool.line (); //class function
					 cout << "4 x 0 is 0, then add 2 and 0 to give you 2:" << endl;
					 cout << "     2 " << endl;
					 cout << "  25.06" << endl;
					 cout << "    0.4" << endl;
					 cout << "x______" << endl;
					 cout << "     24" << endl;
					 tool.line (); //class function
					 cout << "4 x 5 is 20, 20 is larger than 10 so place 2 on top of 2 like this:" << endl;
					 cout << "  2  2 " << endl;
					 cout << "  25.06" << endl;
					 cout << "    0.4" << endl;
					 cout << "x______" << endl;
					 cout << "   0 24" << endl;
					 tool.line (); //class function
					 cout << "4 x 2 is 8, then add 8 and 2 to give you 10:" << endl;
					 cout << "  2  2 " << endl;
					 cout << "  25.06" << endl;
					 cout << "    0.4" << endl;
					 cout << "x______" << endl;
					 cout << " 100 24" << endl;
					 tool.line (); //class function
					 cout << "Notice that we didn't put the decimal in the answer in the first step" << endl;
					 cout << "Now we count the number of decimal places and place the decimal point in the answer" << endl;
					 cout << "25.06 has two decimal places, 0.4 has one decimal place." << endl;
					 cout << "The total decimal places is three decimal places" << endl;
					 cout << "Therefore the decimal point is between the two zeros like this:" << endl;
					 cout << "  2  2 " << endl;
					 cout << "  25.06" << endl;
					 cout << "    0.4" << endl;
					 cout << "x______" << endl;
					 cout << " 10.024" << endl;
					 tool.line (); //class function
					 cout << "Now you have a try!" <<endl;
					 cout << "What is 31.22 x 0.6 " << endl;
					 ans = 31.22*0.6;
					 exp = 0;
					 tool.check (ans, exp); //class function
					 if (exp == 1){
					 	cout << "The answer to the question:" << endl;
						cout << "   1 1 " << endl;
					 	cout << "  31.22" << endl;
					 	cout << "    0.6" << endl;
					 	cout << "x_______" << endl;
					 	cout << " 18.732" << endl;
						}
					 if (exp == 2)
	    	            cout << "Your answer is correct" << endl;
	    	         tool.enter ();
	    	         cout << "Now we are going to learn a more harder multiplication!" << endl;
	    	         cout << "Example: What is  0.156 x 0.21 ?" << endl;
	    	         cout << "Write the first number on top of the second number" << endl;
					 cout << "  0.156 " << endl;
					 cout << "   0.21" << endl;
					 cout << "x______" << endl;
					 tool.line (); //class function
                     cout << "Then start multiplying the columns starting from the right side" << endl;
					 cout << "1 x 6 is 6" << endl;
					 cout << "        " << endl;
					 cout << "  0.156 " << endl;
					 cout << "   0.21" << endl;
					 cout << "x______" << endl;
					 cout << "      6" << endl;
					 tool.line (); //class function
	    	         cout << "1 x 5 is 5" << endl;
					 cout << "        " << endl;
					 cout << "  0.156 " << endl;
					 cout << "   0.21" << endl;
					 cout << "x______" << endl;
					 cout << "     56" << endl;
					 tool.line (); //class function
	    	         cout << "1 x 1 is 1" << endl;
					 cout << "        " << endl;
					 cout << "  0.156 " << endl;
					 cout << "   0.21" << endl;
					 cout << "x______" << endl;
					 cout << "    156" << endl;
					 tool.line (); //class function
	    	         cout << "We have multiplied all the digits with 1" << endl;
	    	         cout << "Now we multiply all the digits with 2" << endl;
	    	         cout << "But when we write the answer, we have to write it one digit to the left like this:" << endl;
	    	         cout << "2 x 6 is 12, 12 is larger than 10 so we place 1 on top of 5" << endl;
				     cout << "     1  " << endl;
					 cout << "  0.156 " << endl;
					 cout << "   0.21" << endl;
					 cout << "x______" << endl;
					 cout << "    156" << endl;
	    	         cout << "     2 " << "We place 2 one digit to the left" <<endl;
	    	         tool.line (); //class function
 	    	         cout << "2 x 5 is 10, then we add 10 and 1 which is 11, 11 is larger than 10 so we place 1 on top of 1" << endl;
				     cout << "    11  " << endl;
					 cout << "  0.156 " << endl;
					 cout << "   0.21" << endl;
					 cout << "x______" << endl;
					 cout << "    156" << endl;
	    	         cout << "    12 " <<endl;
	    	         tool.line (); //class function
 	    	         cout << "2 x 1 is 2, then we add 2 and 1 which is 3" << endl;
				     cout << "    11  " << endl;
					 cout << "  0.156 " << endl;
					 cout << "   0.21" << endl;
					 cout << "x______" << endl;
					 cout << "    156" << endl;
	    	         cout << "   312 " <<endl;
	    	         tool.line (); //class function
 	    	         cout << "We have multiplied every digit with 2" << endl;
 	    	         cout << "Now we add up the answers starting from the right column" << endl;
 	    	         cout << "6 plus nothing is 6, 5 plus 2 is 7, 1 plus 1 is 2, nothing plus 3 is 3" << endl;
				     cout << "    11  " << endl;
					 cout << "  0.156 " << endl;
					 cout << "   0.21" << endl;
					 cout << "x______" << endl;
					 cout << "    156" << endl;
	    	         cout << "   312 " << endl;
	    	         cout << "+______" << endl;
 	  				 cout << "   3276" << endl;  	         
 	    	         tool.line (); //class function
 	    	         cout << "Now we count the decimal places" << endl;
 	    	         cout << "0.156 has three decimal places, 0.21 has two decimal places" << endl;
 	    	         cout << "The total decimal places is five decimal places" << endl;
 	    	         cout << "     11  " << endl;
					 cout << "   0.156 " << endl;
					 cout << "    0.21" << endl;
					 cout << "x_______" << endl;
					 cout << "     156" << endl;
	    	         cout << "    312 " << endl;
	    	         cout << "+_______" << endl;
 	  				 cout << " 0.03276" << endl;  	
 	    	         cout << "Now you have a try!" <<endl;
					 cout << "What is 0.206 x 0.35 " << endl;
					 ans = 0.206*0.35;
					 exp = 0;
					 tool.check (ans, exp); //class function
					 if (exp == 1){
					 	cout << "The answer to the question:" << endl;
						cout << "   1  3 " << endl;
					 	cout << "   0.206" << endl;
					 	cout << "    0.35" << endl;
					 	cout << "x_______" << endl;
					 	cout << "    1030" << endl;
					 	cout << "    618 " << endl;
					 	cout << "+_______" << endl;
					 	cout << "  0.0721" << endl;
						}
					 if (exp == 2)
	    	            cout << "Your answer is correct" << endl;
 	    	         tool.line (); //class function
					 cout << "You have completed multiplying Decimals Tutorial!" << endl;     
					 tex = "1) Continue to Learning Exponents"; 
					 tool.qloop (tex, mainloop, quit); //class function
		 			 if (quit == 1) {
			 		   choice2 = 2;
                       system("CLS"); //clear screen
					   }
				}
         }
//================================================================================================     
              if (choice2 == 2) {
                 loop = 1;
                 system("CLS"); //clear screen
                 cout << "Introduction to Exponents" << endl;
                 cout << "Press any key to continue after each instruction!" << endl;
                 tool.line (); //class function
                 cout << "Exponents is  a way of writing a repeated multiplication of the same number." << endl;
                 cout << "For example: 2x2x2 can be written as 2^3" << endl;
                 cout << "or 5x5x5x5 can be written as 5^4" << endl;
                 tool.line (); //class function
                 cout << "The exponent tells how many times the base number is used as a factor" << endl;
                 cout << "For example: 4^3, this tells used that 4 is used as a factor for 3 times" << endl;
                 cout << "Therefore 4^3 = 4x4x4 which equals to 64" << endl;
				 tool.enter (); //class function
				 
				 while (loop4 == 0){
    				 cout << "Lessons" << endl;
    				 tex = "1) The Square of a number";
                     col = 11; //color cyan
                     tool.color(tex, col); //color function
    				 tex = "2) The cube of a number";
    				 col = 10; //color green
    				 tool.color(tex, col); //color function
    				 tex = "3) Evaluating exponents";
    				 col = 12; //color red
    				 tool.color(tex, col); //color function
    				 tex = " ";
    				 col = 15;
    				 tool.color(tex, col); //color function
    				 cout << "Your choice is: " << endl;
    				 //cin >> choice4;
    				 if (!(cin >> choice4)) {
       					 	cout << "Error, please select again!" << endl;
 						    cin.clear(); // clear the error
    						// clear the input stream
    						cin.ignore(numeric_limits <streamsize>::max(), '\n');
							}  
     	             else {
	    				 if (choice4 == 1 || choice4 == 2 || choice4 == 3){
	                         loop4 = 1;
	    				     system("CLS"); //clear screen
	                         }
	                     else {
	                         cout << "Error, please try again!";
	                         cin.clear(); // clear the error
    						 // clear the input stream
    						 cin.ignore(numeric_limits <streamsize>::max(), '\n');
	                         system("pause"); //pause window
	                         system("CLS"); //clear screen
	                         }
						 }
              }
//------------------------------------------------------------------------------------------------
                  if (choice4 == 1){
	                 cout << "The Square of a Number" << endl;
	                 tool.line (); //class function
	                 cout << "The square of a number is basically any number to the power of 2" << endl;
	                 cout << "of any number multiplied by itself twice" << endl;
					 tool.line (); //class function
					 cout << "Example: What is 4^2 ?" << endl;
					 cout << "The exponent tells us that 4 is used as a factor for 2 times" << endl;
					 cout << "Therefore multiply 4 by itself twice" << endl;
					 cout << "4^2 = 4x4" << endl;
					 cout << "4x4 = 16" << endl;
					 cout << "The answer is 16" << endl;
					 tool.line (); //class function
					 cout << "Now you have a try!" <<endl;
					 cout << "What is 7^2 ?" << endl;
					 ans = 7*7;
					 exp = 0;
					 tool.check (ans, exp); //class function
					 if (exp == 1){
					 	cout << "The answer to the question:" << endl;	 
					 	cout << "7^2 = 7x7" << endl;
					 	cout << "7x7 = 49" << endl;
						}
					 if (exp == 2)
	    	            cout << "Your answer is correct" << endl;
	    	         tool.line (); //class function
					 cout << "You have completed Square of a Number Tutorial!" << endl;
                     tex = "1) Continue to Next Lesson";
					 tool.qloop (tex, mainloop, quit); //class function
		 			 if (quit == 1) {
			 		   choice4 = 2;
                       system("CLS"); //clear screen
					   }
                 }
					 
//------------------------------------------------------------------------------------------------					 
				 if (choice4 == 2){
				 	 cout << "Cube of a Number" << endl;
	                 tool.line (); //class function
	                 cout << "The cube of a number is similar to square of a number" << endl;
	                 cout << "The only difference is that, the cube of a number is any number multiplied by itself 3 times" << endl;
	                 cout << "or the base number is used as a factor for 3 times" << endl;
	                 cout << "Example: 5^3 or 8^3" << endl;
					 tool.line (); //class function
					 cout << "Example: What is 2^3 ?" << endl;
					 cout << "The exponents tells us that 2 is used as a factor for 3 times" << endl;
					 cout << "Therefore multiply 2 by itself three times" << endl;
					 cout << "2^3 = 2x2x2" << endl;
					 cout << "2x2x2 = 8" << endl;
					 cout << "The answer is 8" << endl;
					 tool.line (); //class function
					 cout << "Now you have a try!" <<endl;
					 cout << "What is 9^3 ?" << endl;
					 ans = 9*9*9;
					 exp = 0;
					 tool.check (ans, exp); //class function
					 if (exp == 1){ 
					 	cout << "The answer to the question:" << endl;	 
					 	cout << "9^3 = 9x9x9" << endl;
					 	cout << "9x9x9 = 729" << endl;
						}
					 if (exp == 2)
	    	            cout << "Your answer is correct" << endl;
	    	         tool.line ();
					 cout << "You have completed Cube of a Number Tutorial!" << endl;     
					 tex = "1) Continue to Next Lesson";
					 tool.qloop (tex, mainloop, quit); //class function
		 			 if (quit == 1) {
			 		   choice4 = 3;
                       system("CLS"); //clear screen
					   }
				 }
					 
//------------------------------------------------------------------------------------------------					 
				 if (choice4 == 3){
				 	 cout << "Evaluating Exponents" << endl;
	                 tool.line (); //class function
	                 cout << "Evalutating any exponents is the same way how you would evalute a square or a cube of a number" << endl;
	                 cout << "All you have to do is look at the exponent of the number" << endl;
	                 cout << "This number tells you how many times the base number has been used as a factor by the number of times" << endl;
	                 tool.line (); //class function
	                 cout << "For example: 6^8, the exponent tells you that the base number ( 6 ) has been used as a factor by 8 times" << endl;
	                 cout << "now to get the answer, you will have to multiply the base number ( 6 ) by 8 times like this:" << endl;
	                 cout << "6^8 = 6x6x6x6x6x6x6x6" << endl;
	                 cout << "Then the answer becomes 1679616" << endl;
					 tool.line (); //class function
					 cout << "Example: What is 3^6 ?" << endl;
					 cout << "The exponent tells use that the base number ( 3 ) is used as a factor by 6 times" << endl;
					 cout << "Therefore, multiply 3 by itself six times" << endl;
					 cout << "3^6 = 3x3x3x3x3x3" << endl;
					 cout << "3x3x3x3x3x3 = 729" << endl;
					 cout << "The answer is 729" << endl;
					 tool.line ();
                  	 cout << "Now you have a try!" <<endl;
					 cout << "What is 5^12 ?" << endl;
					 ans = 5*5*5*5*5*5*5*5*5*5*5*5;
					 exp = 0;
					 tool.check (ans, exp); //class function
					 if (exp == 1){
					 	cout << "The answer to the question:" << endl;	 
					 	cout << "5^12 = 5x5x5x5x5x5x5x5x5x5x5x5" << endl;
					 	cout << "5x5x5x5x5x5x5x5x5x5x5x5 = 244140625" << endl;
						}
					 if (exp == 2)
	    	            cout << "Your answer is correct" << endl;
	    	         tool.line (); //class function
					 cout << "You have completed Evaluating Exponents Tutorial!" << endl;     
					 tex = "1) Continue to Learning Fractions";
					 tool.qloop (tex, mainloop, quit); //class function
		 			 if (quit == 1) {
			 		   choice2 = 3;
                       system("CLS"); //clear screen
					   }
				 }
			  }  
				  
//================================================================================================  
             if (choice2 == 3){
                  loop = 1;
                  system("CLS");
                  cout << "Introduction to Fractions" << endl;
                  cout << "Press any key to continue after each instruction!" << endl;
                  tool.line (); //class function
                  cout << "Fractions is a way of writing a decimal number with a denominator and a numerator" << endl;
                  cout << "For example: 0.5 can be written as 1/2" << endl;
                  cout << "or 0.25 and be written as 1/4" << endl;
                  tool.line (); //class function
                  cout << "When your answer is a fraction, always simplify to its lowest" << endl;
                  cout << "For example: 15/20" << endl;
                  cout << "This can be simplified to 3/4 by dividing the numerator and denominator by 5" << endl;
				  tool.enter (); //class function
                  
                  while (loop5 == 0){
                     cout << "Lessons" << endl;
    				 tex = "1) Adding Fractions with Same Denominators ";
                     col = 11; //cyan color
                     tool.color(tex, col); //color function
    				 tex = "2) Adding Fractions with Different Denominators";
    				 col = 10; //green color 
    				 tool.color(tex, col); //color function
    				 tex = "3) Multiplying Fractions";
    				 col = 12; //red color 
    				 tool.color(tex, col); //color function
    				 tex = " "; 
    				 col = 15; //white color 
    				 tool.color(tex, col); //color function
    				 cout << "Your choice is: " << endl;
    				 //cin >> choice5;
    				 if (!(cin >> choice5)) { //if input is not an integer
       					 	cout << "Error, please select again!" << endl;
 						    cin.clear(); // clear the error
    						// clear the input stream
    						cin.ignore(numeric_limits <streamsize>::max(), '\n');
							}  
				      	 else {
		    				 if (choice5 == 1 || choice5 == 2 || choice5 == 3){
		                        loop5 = 1;
		    				    system("CLS"); //clear screen
		                        }
					         else {
		                        cout << "Error, please select again!" << endl;
		                        cin.clear(); // clear the error
    							// clear the input stream
    							cin.ignore(numeric_limits <streamsize>::max(), '\n');
		                        system ("pause"); //pause window
		                        system ("CLS"); //clear screen
		                        }
                  		} 
				  }
//------------------------------------------------------------------------------------------------
                  if (choice5 == 1){
	                 cout << "Adding Fractions with Same Denominators" << endl;
	                 tool.line (); //class function
	                 cout << "If the denominators are the same when you are adding fractions," << endl;
	                 cout << "all you have to do is add the numerator just like adding whole numbers" << endl;
					 tool.line (); //class function
					 cout << "Example: What is 5/10 + 2/10 ?" << endl;
					 cout << "Since the denominator of both fractions are the same (10)," << endl;
					 cout << "You just have to add 5 + 2 and just leave the denominator as 10" << endl;
					 cout << "5/10 + 2 /10 = 7/10" << endl;
					 cout << "The answer is 7/10" << endl;
					 tool.line (); //class function
					 cout << "Now you have a try!" <<endl;
					 cout << "What is 7/15 + 4/15 ?" << endl;
					 nm = 7+4;
					 dm = 15;
					 exp = 0;
					 tool.fcheck (nm, dm, exp); //class function
					 if (exp == 1){
					 	cout << "The answer to the question:" << endl;	 
					 	cout << "7/15 + 4/15 = 11/15" << endl;
						}
					 if (exp == 2)
	    	            cout << "Your answer is correct" << endl;
	    	         tool.line (); //class function
					 cout << "You have completed Adding Fractions with Same Denominators Tutorial!" << endl;
                     tex = "1) Continue to Next Lesson";
					 tool.qloop (tex, mainloop, quit); //class function
		 			 if (quit == 1) {
			 		   choice5 = 2;
                       system("CLS"); //clear screen
					   }
			      }
                  
//------------------------------------------------------------------------------------------------
                  if (choice5 == 2){
	                 cout << "Adding Fractions with Different Denominators" << endl;
	                 tool.line ();
	                 cout << "If the denominators are different when you are adding fractions," << endl;
	                 cout << "you will have to find the common denominators first" << endl;
	                 cout << "to find the common denominator, all you have to do is multiply the two denominators together" << endl;
	                 cout << "this number will be your common denominator" << endl;
	                 tool.line(); //class function
	                 cout << "now rewrite both fractions to the equivalent fractions with the common denominator" << endl; 
					 tool.line (); //class function
					 cout << "Example: What is 3/5 + 2/10 ?" << endl;
					 cout << "The common denominator is 5 x 10" << endl;
					 cout << "5 x 10 = 50" << endl;
					 tool.line (); //class function
					 cout << "now rewrite both fractions to the equivalent fractions with this common denominator" << endl;
					 cout << "3/5 = ?/10" << endl;
					 cout << "to do this, divide the common denominator by your original denominator" << endl;
					 cout << "10/5 = 2" << endl;
					 tool.line (); //class function
					 cout << "now multiply that number with the numerator" << endl;
					 cout << "3 x 2 = 6" << endl;
					 tool.line (); //class function
					 cout << "now you have find the equivalent fraction of the 1st fraction" << endl;
					 cout << "3/5 = 6/10" << endl;
					 tool.line (); //class function
					 cout << "now do the same with the second fraction" << endl;
					 cout << "2/10 = ?/10" << endl;
					 cout << "10/10 = 1" << endl;
					 cout << "2 x 1 = 2" << endl;
					 cout << "2/10 = 2/10" << endl;
					 tool.line (); //class function
					 cout << "now that you have found both equivalent fractions, you can add them" << endl;
					 cout << "6/10 + 2/10" << endl;
					 cout << "add these fractions like how you add fractions with the same denominator in the previous tutorial" << endl;
					 cout << "6/10 + 2/10 = 8/10" << endl;
					 tool.line (); //class function
					 cout << "now simplify your answer to the simplest form" << endl;
					 cout << "8/10 = 4/5" << endl;
					 cout << "therefore the answer is 4/5" << endl;
					 tool.line (); //class function
					 cout << "Now you have a try!" <<endl;
					 cout << "What is 3/4 + 5/7 ?" << endl;
					 nm = 41;
					 dm = 28;
					 exp = 0;
					 tool.fcheck (nm, dm, exp); //class function
					 if (exp == 1){
					 	cout << "The answer to the question:" << endl;	 
					 	cout << "4 x 7 = 28 (common denominator)" << endl;
					 	cout << "3/4 = ?/28" << endl;
					 	cout << "28/4 = 7" << endl;
					 	cout << "7 x 3 = 21" << endl;
					 	cout << "3/4 = 21/28 (equivalent of the 1st fraction)" << endl;
					 	cout << "5/7 = ?/28" << endl;
					 	cout << "28/7 = 4" << endl;
					 	cout << "4 x 5 = 20" << endl;
					 	cout << "5/7 = 20/28 (equivalent of the 2nd fraction)" << endl;
					 	cout << "21/28 + 20/28 = 41/28" << endl;
					 	cout << "Therefore 41/28 is the answer" << endl;
						}
					 if (exp == 2)
	    	            cout << "Your answer is correct" << endl;
	    	         tool.line (); //class function
					 cout << "You have completed Adding Fractions with Different Denominators Tutorial!" << endl;
                     tex = "1) Continue to Next Lesson";
					 tool.qloop (tex, mainloop, quit); //class function
		 			 if (quit == 1) {
			 		   choice5 = 3;
                       system("CLS"); //clear screen
					   }
				 }                  
					 
//------------------------------------------------------------------------------------------------                  
				 if (choice5 == 3){
				 	 cout << "Multiplying Fractions" << endl;
	                 tool.line (); //class function
	                 cout << "Multiplying fracions is very easy" << endl;
	                 cout << "All you have to do is multiply the numerator by the numerator" << endl;
	                 cout << "and multiply the denominator by the denominator" << endl;
					 tool.line (); //class function
					 cout << "Example: What is 9/12 x 4/7 ? " << endl;
					 cout << "Multiply both the numerator together like this:" << endl;
					 cout << "9 x 4 = 36" << endl;
					 cout << "now multiply both the denominator together like this:" << endl;
					 cout << "12 x 7 = 84" << endl;
					 tool.line (); //class function
					 cout << "now put them back into a fraction like this:" << endl;
					 cout << "9/12 x 4/7 = 36/84" << endl;
					 cout << "now simplify the answer to its simplest form" << endl;
					 cout << "36/84 = 3/7" << endl;
					 cout << "therefore the answer is 3/7" << endl;
					 tool.line (); //class function
                  	 cout << "Now you have a try!" <<endl;
					 cout << "What is 8/14 x 3/5 ?" << endl;
					 nm = 12;
					 dm = 35;
					 exp = 0;
					 tool.fcheck (nm, dm, exp); //class function
					 if (exp == 1){
					 	cout << "The answer to the question:" << endl;	 
					 	cout << "8 x 3 = 24 (both numerator multiplied together)" << endl;
					 	cout << "14 x 5 = 70 (both denomator multiplied together)" << endl;
					 	cout << "8/14 x 3/5 = 24/70" << endl;
					 	cout << "24/70 = 12/35 (simplified answer)" << endl;
						}
					 if (exp == 2)
	    	            cout << "Your answer is correct" << endl;
	    	         tool.line (); //class function
					 cout << "You have completed Multiplying Fractions Tutorial!" << endl;
					 while (loop9 == 0){     
						 tex = "1) Go back to Menu";
					     col = 14; //yellow color
				      	 tool.color(tex, col); //color function
				      	 tex = "2) Quit"; 
				      	 col = 12; //red color
				      	 tool.color(tex, col); //color function
				      	 tex = " ";
				      	 col = 15; //white color
				      	 tool.color(tex, col); //color function
				      	 //cin >> quit;
				      	 if (!(cin >> quit)) { //if input is not an integer
       					 	cout << "Error, please select again!" << endl;
 						    cin.clear(); // clear the erro
    						// clear the input stream
    						cin.ignore(numeric_limits <streamsize>::max(), '\n');
							}  
				      	 else {
					      	 if (quit == 1)
							 	loop9 = 1;
						 	 else if (quit == 2){
					 	        loop9 = 1;
					 	        mainloop = 1;
								}
							else {
						        cout << "Error, please select again!" << endl;
						        cin.clear(); // clear the erro
    							// clear the input stream
    							cin.ignore(numeric_limits <streamsize>::max(), '\n');
	 	                        system ("pause"); //pause window
	 	                        system ("CLS"); //clear screen
					            }
							}
					 }
				 }
             }  
				                                    
		} // loop

//================================================================================================   
//Game
if (choice1 == 2){
        int loop9 = 0;
	    while (loop9 == 0){
		//variables & reset
	    int choice6 = 0, col = 0, loop8 = 0, loop10 = 0, quit = 0, score = 0, total = 0, qgame = 0;
	    int startTime, endTime, totalTime, Dscore = 0, Escore = 0, Fscore= 0;
	    float num1 = 0, num2 = 0, answ = 0, num = 0, num3 = 0, num4 = 0, ans = 0, Nans = 0, Dans = 0, uans =0; 
	    string tex;
	    while (loop8 == 0){
	        choice6 = 0;
	        cout << "Select which lesson you want to practice:" << endl;
	        tex = "1) Decimal Numbers";
	        col = 11; //cyan color
	        tool.color(tex, col); //color function
	        tex = "2) Exponents"; 
	        col = 10; //green color 
	        tool.color(tex, col); //color function
	        tex = "3) Fractions";
	        col = 12; //red color 
	        tool.color(tex, col); //color function
	        tex = " ";
	        col = 15; //white color 
	        tool.color(tex, col); //color function
	        if (!(cin >> choice6)){ //not a  number
	            cout << "Error, please select again! here" << endl;
	            cin.clear(); // clear the error
				 // clear the input stream
	            cin.ignore(numeric_limits <streamsize>::max(), '\n');
	            system ("pause"); //pause window
	            system ("CLS"); //clear screen
	            }
	        else {
	             if (choice6 == 1 || choice6 == 2 || choice6 == 3){    
	                loop8 = 1;
	                system ("CLS"); //clear screen
	                cout << "Intructions:" << endl;
	                cout << "You have 1 minute to answer as much questions as possible" << endl;
	                cout << "Everytime you play, you are trying to break your highscore!" << endl;
	                system("Pause"); //pause window
	                system("CLS"); //clear screen
	                }
	              else {
	                   cout << "Error, please select again!" << endl;
	                   cin.clear(); // clear the error
	    			   // clear the input stream
	    			   cin.ignore(numeric_limits <streamsize>::max(), '\n');
	                   system ("pause"); //pause window
	                   system("CLS"); //clear screen
	               }
	       }
	    }
	//--------------------------------------------------------------------------------------------------
	    if (choice6 == 1){
			 cout << "Decimal Numbers" << endl;
			 cout << "In this game, you will be adding and subtracting decimal numbers." << endl;
			 ifstream dhscore ("decimal.bin"); //read from file
   			 int hDscore;
    		 dhscore.read(reinterpret_cast<char*>(&hDscore), sizeof(int)); //read value in file
			 dhscore.close(); //close file
			 cout << "Your highscore is: " << hDscore << endl;
			 cout << "Press any key to start!" << endl;
			 getch(); //pause window
			 decimal deci; //object deci
			 startTime = time(NULL); //start timing
	         while (quit < 10){  
	             deci.rdm(num1, num2, ans); //decimal function
		         cout << "Your answer is: ";
		         cin >> uans;
		         check(uans, ans, score); //check function
		         cout << score << "score" << endl; //check score
				 Dscore = score;
		         total = total+1; //total questions
	             endTime = time(NULL); //get time
		         totalTime = endTime - startTime; //calculate total time
		         quit = totalTime;
		         cout << quit << " Elasped Time" << endl; //quit
				 }
	        }
	        
	//--------------------------------------------------------------------------------------------------        
	    else if (choice6 == 2){
			 cout << "Exponents" << endl;
			 cout << "In this game, you will be evaluating exponents." << endl;
			 ifstream ehscore ("exponent.bin"); //read from file
   			 int hEscore;
    		 ehscore.read(reinterpret_cast<char*>(&hEscore), sizeof(int)); //read value from file
			 ehscore.close(); //close file
			 cout << "Your highscore is: " << hEscore << endl;
			 cout << "Press any key to start!" << endl;
			 getch(); //pause window
			 startTime = time(NULL); //start timing
	         while (quit < 10){
	             expon expo(1,4); //start constructor
	             expo.rdm(num1, num2, num3, num4); //exponent function
				 cout << num1 << num2 << num3 << num4 << endl; //check rand num
		         cout << "What is " << num1 << "^ " << num2 << " ?" << endl;
		         cout << "Your answer is: ";
		         cin >> uans;
		         ans = pow(num1,num2); //num1 to the power of num2
		         cout << ans << "ans1" << endl; //check correct ans
		         check(uans, ans, score); //check function
		         cout << score << "score" << endl; //check score
		         Escore = score;
		         total = total+1; //total questions
	             endTime = time(NULL); //get time
		         totalTime = endTime - startTime; //calculate total time
		         quit = totalTime;
		         cout << quit << " Elasped Time" << endl; //quit
				 }
	         }
	
	//-----------------------------------------------------------------------------------------------------------         
	    else if (choice6 == 3){
			 cout << "Fractions" << endl;
			 cout << "In this game, you will practice multiplying fractions together." << endl;
			 ifstream fhscore ("fraction.bin"); //read from file
   			 int hFscore;
    		 fhscore.read(reinterpret_cast<char*>(&hFscore), sizeof(int)); //read value from file
			 fhscore.close(); //close file
			 cout << "Your highscore is: " << hFscore << endl;
			 cout << "Press any key to start!" << endl;
			 getch(); //pause window
			 startTime = time(NULL); //start timing
	         while (quit < 10){
				 //frac.rdm(num1, num2, num3, num4);
	             fract frac(1,10); //start constructor
	             frac.rdm(num1, num2, num3, num4); //fraction function
				 cout << num1 << num2 << num3 << num4 << endl; //check rand num
		         cout << "What is " << num1 << "/" << num2 << " x " << num3 << "/" << num4 << " ?" << endl;
		         cout << "Numerator: ";
		         cin >> Nans; 
		         cout << "Denominator: ";
		         cin >> Dans;
		         uans = static_cast<float>(static_cast<int>((Nans/Dans) * 100.)) / 100.; //round user input to two decimal places
		         ans = static_cast<float>(static_cast<int>(((num1/num2)*(num3/num4)) * 100.)) / 100.; //round correct answer to two decimal places
		         cout << ans << "ans1" << endl; //check correct ans
		         check(uans, ans, score); //check function
		         cout << score << "score" << endl; //check score
		         Fscore = score; 
		         total = total+1;
	             endTime = time(NULL); //get time 
		         totalTime = endTime - startTime; //calculate total time 
		         quit = totalTime;
		         cout << quit << " Elasped Time" << endl; //check time quit
				 }
	         }
	    else
	        cout <<"error" << endl;
	//===========================================================================================================
	    cout << " " << endl;
	    cout << "TIMES OVER!" << endl;
		cout << "You scored: " << score << " out of " << total << " correct" << endl;
		//High Score in Decimals
		if (choice6 == 1){
			ifstream dhscore ("decimal.bin"); //read from file
		 	int hDscore;
	 		dhscore.read(reinterpret_cast<char*>(&hDscore), sizeof(int)); //read value from file
			dhscore.close(); //close file 
			if (Dscore > hDscore){ //if current score is greater than highscore
		       cout << "You have a New Decimal Highscore!" << endl;
		       ofstream Dfile ("decimal.bin", ios::binary); //write to file
	    	   Dfile.write(reinterpret_cast<const char *>(&Dscore), sizeof(Dscore)); //overwrite the highscore
	    	   Dfile.close (); //close file
			   }
			   //hDscore = Dscore;
	        else
        	   cout << "You did not beat your highscore . . ." << endl;
         }
		else if (choice6 == 2){    
		//High Score in Exponents
			ifstream ehscore ("exponent.bin"); //read from file
	        int hEscore;
	        ehscore.read(reinterpret_cast<char*>(&hEscore), sizeof(int)); //read value from file
	 		ehscore.close(); //close file
			if (Escore > hEscore){ //if current score is greater than highscore
			       cout << "You have a New Exponent Highscore!" << endl; 
			       ofstream Efile ("exponent.bin", ios::binary); //write to file
		    	   Efile.write(reinterpret_cast<const char *>(&Escore), sizeof(Escore)); //overwrite the highscore
		    	   Efile.close (); //close file
				   //hEscore = Escore;
				   }
            else
        	       cout << "You did not beat your highscore . . ." << endl;
		}
		else {
		//High Score in Fractions
			ifstream Fhscore ("fraction.bin"); //read from file
	        int hFscore;
	        Fhscore.read(reinterpret_cast<char*>(&hFscore), sizeof(int)); //read value from file
	        Fhscore.close(); //close file
			if (Fscore > hFscore){ //if current score is greater than highscore
				       cout << "You have a New Fraction Highscore!" << endl;
				       ofstream Ffile ("fraction.bin", ios::binary); //write to file
			    	   Ffile.write(reinterpret_cast<const char *>(&Fscore), sizeof(Fscore)); //overwrite the highscore
			    	   Ffile.close (); //close file
					   //hFscore = Fscore;
					   }
			        else
		        	   cout << "You did not beat your highscore . . ." << endl;
		}
		
		while ( loop10 == 0){
		   cout << "Would you like to play again?" << endl;
		             col = 2; //green color
			      	 tex = "1) Play Again";
			      	 tool.color(tex, col); //color function
			      	 col = 14; //yellow color 
			      	 tex = "2) Back to Main Menu";
			      	 tool.color(tex, col); //color function
		             col = 12; //red color
			      	 tex = "3) Quit"; 
			      	 tool.color(tex, col); //color funcion
			      	 tex = " ";
			      	 col = 15; //white color
			      	 tool.color(tex, col); //color function
		   if (!(cin >> qgame)){ //not a  number
		            cout << "Error, please select again! here" << endl;
		            cin.clear(); // clear the error
					 // clear the input stream
		            cin.ignore(numeric_limits <streamsize>::max(), '\n');
		            system ("pause"); //pause window
		            system ("CLS"); //clear screen
		            }
		        else {	  		   		 
		   			 if (qgame == 1){
		      		 	loop9 = 0;
		      		 	loop10 = 1;
		      			system("pause"); //pause window
		      			system("CLS"); //clear screen
		      			}
			         else if (qgame == 2){
			           loop9 = 1;
					   loop10 = 1; 
					   }
					 else if (qgame == 3){
					 	  loop9 = 1;
			              loop10 = 1;
						   mainloop = 1;
						   }  
			         else { 
					      cout << "Error, please select again!" << endl;
				          cin.clear(); // clear the error
						  // clear the input stream
				          cin.ignore(numeric_limits <streamsize>::max(), '\n');
				          system ("pause"); //pause window
				          system ("CLS"); //clear screen
						  }
		       }
	    }
	} 
}


} //mainloop         
//==============================================================================================	                                  
	cout << "This is to pause the quit window, ***Delete after***" << endl;
   	system ("pause"); //pause window
 	return 0; //ends function
} 
   
