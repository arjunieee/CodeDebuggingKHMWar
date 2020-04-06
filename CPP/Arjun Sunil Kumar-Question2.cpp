#include<iostream>
#include<math.h>				//Math header file has been added
using namespace std;
int main ()
{
  int num, d = 0, n, r, p = 0, a = 1;
  char choice;
  cin >> num;					//<< has been changed to >>
  cin >> choice;				//<< has been changed to >>
  switch (choice)				//Switch added
  {
    case 'a':					//Colon and '' has been added 
        n = num;
        while (n != 0)
          {
        	n = n / 10;
        	d++;
          }
        n = num;
        while (n != 0)
          {
        	r = n % 10;
        	a = a * sqrt(r)*d;		//== has been replaced by = and sqrt has been added
        	n = n / 10;
           }
        cout << ++a+r+d << "\n";
        break;					//Break has been added
    case 'p':
        n = num;
        while (n != 0)
          {
        	r = n % 10;
        	p = p * 10 + r;			//== has been replaced by = and sqrt has been added
        	n = n / 10;
          }
        cout << p << "\n";
        break;					//Break has been added
    }
  return(0);
}
