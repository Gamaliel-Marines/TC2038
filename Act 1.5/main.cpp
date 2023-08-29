#include <iostream>
#include <string>

using namespace std;


void calculateChange(int change, int bills[], int n)
{
    
    

}

int returnChange(int p, int q, int bills[], int n)
{
    if(p > q)
    {
        cout<<"The bill is not enough"<<endl;
        return -1;
    }

    else
    {
        int Change = q -p;
        cout<<"The change is: "<<Change<<endl;
        return Change;
        calculateChange(Change, bills, n);
    }

}



int main()
{
    int P;
    int Q;
    int N;
    int BILLS[N];

    for(int i = 0; i < N; i++)
    {
        cout<<"Enter the value of the bill: "<<endl;
        cin>>BILLS[i];
    }

    cout<<"Enter the price: "<<endl;
    cin>>P;
    cout<<"Enter the bill: "<<endl;
    cin>>Q;


    returnChange(P,Q,BILLS,N);

}

