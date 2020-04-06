#include<iostream>	
#include<string.h>			//Spelling error string
using namespace std;
int getLIndex(char[],char);		//Prototype has been added
int getFIndex(char[],char);		//Prototype has been added
int main()
{
	char str[100];
	char ch; 
	int Lindex,Findex; 
	cin>>str;			//Semi colon missing
	cin>>ch;
	Lindex = getLIndex(str,ch);
	Findex = getFIndex(str,ch);
	if(Lindex!=-1)
		cout<<Findex<<endl<<Lindex;
	else
		cout<<"NOT FOUND"<<endl;
	return 0;	
}
int getFIndex(char string[],char c)	//Type changed
{
	int size = strlen(string);	//Function name corrected to strlen
	int i=0;
	while(i<size)
	{
		
		if(string[i]==c){
		    return i;
		   break;
		}	
		i++; 
	}
	
}
int getLIndex(char string[], char c)	//Data Types corrected
{
	int size = strlen(string);	//Function name corrected to strlen
	int i=size; 
	while( i>=0)			//Semicolon has been removed
{		
		if(string[i]==c)
		{
		    return i;
            break;
		}
	i--;
}
		
}