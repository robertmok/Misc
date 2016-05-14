#include <iostream>
#include <string>
#include <conio.h>
#include <windows.h>
using namespace std;

//header file
//functions for tutorial

#ifndef TUTOOL_H
#define TUTOOL_H

class tutool {
public:
             
    void check (float ans, int& exp){  //practice answer checking function
         string tex2;
         int col2 = 0;
         int loop6 = 0;
    	 float uans = 0;
    	 while (exp == 0){
    	 	   cout << "What is your answer? " << endl;
    	 	   cin >> uans;
    	 	   if (ans == uans) //if answer is correct
    	 	      exp = 2; 
    		   else {
  	  	          cout << "\n";
    		   	  cout << "Your answer is not correct" << endl;
    		   	  loop6 = 0;
    		   	  while (loop6 == 0){
				 	  tex2 = "0) Try Again";
	    		   	  col2 = 2; //green color
	    		   	  HANDLE handle = GetStdHandle(STD_OUTPUT_HANDLE); 
		              SetConsoleTextAttribute( handle, col2 ); //set the color
		              cout << tex2 << endl; //output text
		              tex2 = "1) Answer"; 
		              col2 = 14; //yellow color
	    	          SetConsoleTextAttribute( handle, col2 ); //set the color
	    	          cout << tex2 << endl; //output text
	    			  tex2 = " "; 
	    			  col2 = 15; //white color
	    	          SetConsoleTextAttribute( handle, col2 ); //set the color back to white
	    	          cout << tex2 << endl; //output text to change color back to white
	    			  cin >> exp;
					  if (exp == 0 || exp == 1) 
					  	 loop6 = 1;
					  else{
					  	   cout << "Error, please select again!" << endl;
					  	   system ("pause");
						   }	  
	    			  }
				  }
       }
   }
    
    void fcheck (int nm, int dm, int& exp){ //fraction answer checking function
         string tex3;
         int col3 = 0;
    	 int unm = 0, udm = 0;
    	 int loop7 = 0;
    	 while (exp == 0){
    	 	   cout << "What is your numerator? " << endl;
    	 	   cin >> unm;
    	 	   cout << "What is your denominator? " << endl;
    	 	   cin >> udm;
    	 	   if (unm == nm && udm == dm) //if numerator and denominator is correct
    	 	      exp = 2;
    		   else {
    		   	  cout << "Your answer is not correct" << endl;
    		   	  cout << "Did you simplify your answer?" << endl;
    		   	  cout << "\n";
    		   	  loop7 = 0;
    		   	  while (loop7 == 0){
	    		   	  tex3 = "0) Try Again";
	    		   	  col3 = 2; //green color
	    		   	  HANDLE handle = GetStdHandle(STD_OUTPUT_HANDLE); 
		              SetConsoleTextAttribute( handle, col3 ); //set the color
		              cout << tex3 << endl; //output text
		              tex3 = "1) Answer";
		              col3 = 14; //yellow color
	    	          SetConsoleTextAttribute( handle, col3 ); //set the color
	    	          cout << tex3 << endl; //output text
	    			  tex3 = " ";
	    			  col3 = 15; //white color
	    	          SetConsoleTextAttribute( handle, col3 ); //set the color back to white
	    	          cout << tex3 << endl; //output text to change back to white
	    			  cin >> exp;
					  if (exp == 0 || exp == 1) 
					  	 loop7 = 1;
					  else {
					  	   cout << "Error, please select again!" << endl;
						   system ("pause");
					       }	  
    			  }
  			  }
         }
   }
   
   void qloop (string tex, int& mainloop, int& quit){  //quit loop function
   		int loop8 = 0, col = 0;	
  		 while (loop8 == 0){
		     col = 2; //green color
	      	 HANDLE handle = GetStdHandle(STD_OUTPUT_HANDLE);
             SetConsoleTextAttribute( handle, col); //set the color
             cout << tex << endl; //output text
	      	 tex = "2) Back to Menu"; 
	      	 col = 14; //yellow color
	      	 SetConsoleTextAttribute( handle, col); //set the color
             cout << tex << endl; //output text
	      	 tex = "3) Quit";
	      	 col = 12; //red color
	      	 SetConsoleTextAttribute( handle, col); //set the color
             cout << tex << endl; //output text
	      	 tex = " "; 
	      	 col = 15; //white color
	      	 SetConsoleTextAttribute( handle, col); //set the color
             cout << tex << endl; //change back to white
	      	 if (!(cin >> quit)) { //if input is not a integer
				 	cout << "Error, please select again!" << endl;
			   		cin.clear(); // clear the error
					// clear the input stream
				    cin.ignore(numeric_limits <streamsize>::max(), '\n');
					}  
	         else {
		      	 if (quit == 3){
	 		        loop8 = 1;
		      	    mainloop = 1;
					}
		      	 else if (quit == 1){ 
	                 loop8 = 1;
	                 }
	             else if (quit == 2)
				 	  loop8 = 1;
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

    void line (){ //pause with new line function
         getch(); //pause window
    	 cout << "\n"; //new line
    }

    void enter (){ //pause with clear screen function
         getch(); //pause
         system("CLS");//clear screen
         }
            
    void color(string tex, int col){ //change color function
    	HANDLE handle = GetStdHandle(STD_OUTPUT_HANDLE);
    	SetConsoleTextAttribute( handle, col ); //set the color
    	cout<< tex << endl; //output text
     }    
};

#endif
