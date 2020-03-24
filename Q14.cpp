#include <iostream>
#include <sstream>
using namespace std;

class Student{
    private:
        int Age;
        int Standard;
        string First_Name;
        string Last_Name;
    public:
        void set_age(int umar){
            Age = umar;
        }
        void set_standard(int kaksha){
            Standard = kaksha;
        }
        void set_first_name(string pehla_naam){
            First_Name = pehla_naam;
        }
        void set_last_name(string doosra_naam){
            Last_Name = doosra_naam;
        }
        int get_age(){
            return Age;
        }
        int get_standard(){
            return Standard;
        }
        string get_first_name(){
            return First_Name;
        }
        string get_last_name(){
            return Last_Name;
        }
        string to_string(){
            string sAge, sStandard;
            stringstream str1;
            str1 << Age;
            sAge = str1.str(); 
            stringstream str2;
            str2 << Standard;
            sStandard = str2.str();
            return sAge + "," + First_Name + "," + Last_Name + "," + sStandard;
        }
};
int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}
