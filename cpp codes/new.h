#include<iostream>
using namespace std;
void f(int a)
{
	return 5+a;
}
void f(int *a)
{
	return 5+ *a;
}
int main()
{	int a=9
	cout<<f(a);
	cout<<f(&a);
}