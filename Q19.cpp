#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person{
    public:
        string name;
        int age;
        void set_name(string s){
            name = s;
        }
        void set_age(int y){
            age = y;
        }
        virtual void getdata() = 0;
        virtual void putdata() = 0;
};

class Professor : public Person{
    public:
        static int curr_idp;
        int publications,v;
        Professor(){curr_idp++;}
        virtual void getdata(){
            string n; int a;
            cin>>n>>a>>publications;
            name = n; age = a;
            v = curr_idp;
        }
        virtual void putdata(){
            cout<<name<<" "<<age<<" "<<publications<<" "<<v<<endl;
        }
        
};
class Student : public Person{
    public:
        int marks[6],l;
        static int curr_ids;
        Student(){curr_ids++;}
        virtual void getdata(){
            string h; int y;
            cin>>h>>y>>marks[0]>>marks[1]>>marks[2]>>marks[3]>>marks[4]>>marks[5];
            name = h; age = y;
            l = curr_ids;
        }
        virtual void putdata(){
            cout<<name<<" "<<age<<" "<<marks[0]+marks[1]+marks[2]+marks[3]+marks[4]+marks[5]<<" " << l <<endl;
        }
    
};
int Professor::curr_idp = 0;
int Student::curr_ids = 0;
int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
