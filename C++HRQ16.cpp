
#include<bits/stdc++.h>

using namespace std;
class Box{
    private:
        int length,breadth,height;
    public:
        void setlength(int l){
            length = l;
        }
        void setbreadth(int b){
            breadth = b;
        }
        void setheight(int h){
            height = h;
        }
        Box(){
            setlength(0);
            setbreadth(0);
            setheight(0);
        }
        Box(int l, int b, int h){
            setlength(l);
            setbreadth(b);
            setheight(h);
        }
        Box(const Box &W){
            setlength(W.length);
            setbreadth(W.breadth);
            setheight(W.height);
        };
        int getLength(){
            return length;
        }
        int getBreadth(){
            return breadth;
        }
        int getHeight(){
            return height;
        }
        long long CalculateVolume(){
            return (long long)length*(long long)breadth*height;
        }
        bool operator<(Box& b){
            if(length<b.length) return true;
            if(breadth<b.breadth && length==b.length) return true;
            if(height<b.height && breadth==b.breadth && length==b.length) return true;
            else return false; 
        }
        friend ostream& operator<<(ostream& out, Box& B);
}; 
ostream& operator<<(ostream& out, Box& B){
    
    out << B.getLength() << " " << B.getBreadth() << " " << B.getHeight();
    return out;
}


void check2()
{
    int n;
    cin>>n;
    Box temp;
    for(int i=0;i<n;i++)
    {
        int type;
        cin>>type;
        if(type ==1)
        {
            cout<<temp<<endl;
        }
        if(type == 2)
        {
            int l,b,h;
            cin>>l>>b>>h;
            Box NewBox(l,b,h);
            temp=NewBox;
            cout<<temp<<endl;
        }
        if(type==3)
        {
            int l,b,h;
            cin>>l>>b>>h;
            Box NewBox(l,b,h);
            if(NewBox<temp)
            {
                cout<<"Lesser\n";
            }
            else
            {
                cout<<"Greater\n";
            }
        }
        if(type==4)
        {
            cout<<temp.CalculateVolume()<<endl;
        }
        if(type==5)
        {
            Box NewBox(temp);
            cout<<NewBox<<endl;
        }

    }
}

int main()
{
    check2();
}

