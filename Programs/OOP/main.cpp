#include <stdio.h>
#include <iostream>
#include <string.h>
#include <iomanip>
using namespace std;

class counter_top
{
    protected:
        char* material;
        int size;
        double cost;
        double price;
    public:
        counter_top(char* mtrl, int sz = 24, double cst = 25.00);  //{ cst = 25.00; sz = 24; };
        virtual void set_price(void)
        {
            price = cost*size*1.07;
        }
        double get_price(void)
        {
            return price;
        }
        int get_size(void)
        {
            return size;
        }
        char* get_mtrl(void)
        {
            return material;
        }
        ~counter_top(void)
        {
            delete [] material;
            cout << "goodbye" << endl;
        }
};

counter_top::counter_top(char* mtrl, int sz, double cst): size(sz)
{
    material = new char[ strlen(mtrl)+1 ];
    strcpy(material, mtrl);
    cost = cst;
    cout << "hello1" << endl;
}

ostream& operator<<(ostream& os, counter_top& ct)
{
    os.setf(ios::fixed);
    os << setprecision(2);
    os << "Basic " << ct.get_mtrl() << " counter top, " << ct.get_size() << " sq ft, is priced at $" << ct.get_price() << endl;
    return os;
}

class special_counter_top: public counter_top
{
    private:
        double special_install_cost;
    public:
        special_counter_top(char* mtrl, double cst = 28.00, double spc_instl_cst = 7.00, int sz = 34): counter_top(mtrl, sz, cst)
        {
            special_install_cost = spc_instl_cst;
            cout << "hello2" << endl;
        }
        virtual void set_price(void)
        {
            price = 1.08*cost*size + special_install_cost*size;
        }
        friend ostream& operator<<(ostream& os, const special_counter_top& spt)
        {
            os.setf(ios::fixed);
            os << setprecision(2);
            os << "Special " << spt.material << " counter top, " << spt.size << " sq ft, is priced at $" << spt.price << endl;
        }
};

main()
{
    cout << "OOP Program" << endl;
    counter_top ct1("granite", 22);
    counter_top ct2("marble", 24, 27.00);
    special_counter_top s_ct1("composite_quartz", 30.00, 7.50);
    //ct1("granite", 22);
    //ct2(27.00, "marble", 24);
    //s_ct1(30.00, 7.50, "composite_quartz");

    counter_top *p;

    p = &ct1;
    p->set_price();
    cout << ct1;

    p = &ct2;
    p->set_price();
    cout << ct2;

    p = &s_ct1;
    p->set_price();
    cout << s_ct1;
}
