#include<iostream>
#include<vector>
#include<string>
#include<functional>
using namespace std;
class merkle_p
{
private:
vector<string> blockdata;
    vector<vector<string>> tree;
    string hashf(const string &data){return  to_string(hash<string>{}(data));}
public:
   merkle_p(const vector<string> &data)
   {
        blockdata=data;
        buildtree();
   }
   void buildtree()
   {
    tree.clear();
    vector<string> currentlayer;
    for(string node: blockdata){
        currentlayer.push_back(hashf(node));
    }
    tree.push_back(currentlayer);
    while (currentlayer.size()>1)
    {
        if(currentlayer.size()%2==1){
            currentlayer.push_back(currentlayer.back());
        }
        vector<string> nextlevel;
        for (int i = 0; i < currentlayer.size(); i+=2)
        {
            nextlevel.push_back(hashf(currentlayer[i] + currentlayer[i+1]));
        }
        tree.push_back(nextlevel);
        currentlayer=nextlevel;
        
    }
    
   }
   string root()
   {
    return tree.back()[0];
   }
   void ptree(){
    for (int i = 0; i < tree.size(); i++)
    {
        cout<<"this is level "<<i<<endl;
        for (string ptt :tree[i])
        {
            cout<<"   "<<ptt;
        }cout<<endl;
        
    }
    
   }

   vector<string> prof(int index){
            vector<string>proof ;
            for (int i = 0; i <tree.size()-1; i++)
            {
                vector<string>node=tree[i];
                if(node.size()%2==1)
                {
                    node.push_back(node.back());
                }
                if(index%2==0){
                    proof.push_back(node[index+1]);
                }else{
                    proof.push_back(node[index-1]);
                }
                index/=2;
            }
            return proof;
            
   }
   bool vprof(const string &data, int index, const vector<string> &pr, const string &root)
   {
   string current = hashf(data);

   for(string s : pr)
   {
       if(index % 2 == 0){
           current = hashf(current + s);
       } else {
           current = hashf(s + current);
       }
       index /= 2;
   }
   return current == root;
   }
};
int main()
{
    vector<string> transaction={
        "shadat",
        "murad",
        "iyasin"
    };
    merkle_p t(transaction);
    t.buildtree();
    t.ptree();


    vector<string> pt=t.prof(2);
    for(string proof_node :pt)
    {
        cout<<"  "<<proof_node;
    }
    cout<<endl;
    if(t.vprof("iyasin",2,pt,t.root()))
    {
        cout<<"Proof Valid - iyasin verified"<<endl;
    }else{
        cout<<"Proof Invalid - iyasin not verified"<<endl;
    }
    if(t.vprof("sha",2,pt,t.root()))
    {
        cout<<"Proof Valid - sha verified"<<endl;
    }else{
        cout<<"Proof Invalid - sha not verified"<<endl;
    }
    return 0;
}

