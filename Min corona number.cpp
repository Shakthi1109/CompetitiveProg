#include <iostream>
using namespace std;

int main()
{
    int T,n,sum,i,j,ans=0,flag=0;
    cin>>T;
    while(T>0)
    {
        
        cin>>n;
        if (n==1)
        {
            cout<<n<<endl;
        }
        else
        {
            sum=0;
            flag=0;
            for(i=1;i<=n;i++)
            {
                for(j=1;j<=i;++j)
                {
                    if(i%j==0)
                    {
                        if(sum<n)
                        {
                            sum++;
                        }
                        
                    }
                    if(sum>=n)
                    {
                        flag=1;
                        ans=i;
                        break;
                    }
                }
                if(flag==1)
                    break;
            }
         cout<<ans<<endl;   
        }
        
        T--;
    }

    return 0;
}