#include <bits/stdc++.h>

using namespace std;

class merkle
{
private:
    vector<string> datablock;
    vector<vector<string>> tree;
    string hashf(const string &data)
    {
        return to_string(hash<string>{}(data));
    }

public:
    merkle(vector<string> &data)
    {
        datablock = data;
        buildtree();
    }
    void buildtree()
    {
        tree.clear();
        vector<string> currentlevel;
        for (string data : datablock)
        {
            currentlevel.push_back(hashf(data));
        }
        tree.push_back(currentlevel);
        while (currentlevel.size() > 1)
        {
            vector<string> nextlevel;
            if (currentlevel.size() % 2 == 1)
            {
                currentlevel.push_back(currentlevel.back());
            }
            for (int i = 0; i < currentlevel.size(); i = i + 2)
            {
                nextlevel.push_back(hashf(currentlevel[i] + currentlevel[i + 1]));
            }
            tree.push_back(nextlevel);
            currentlevel = nextlevel;
        }
    }
    vector<string> proftree(int index)
    {
        vector<string> prof;
        for (int i = 0; i < datablock.size() - 1; i++)
        {
            vector<string> level = tree[i];

            if (level.size() % 2 == 1)
            {
                level.push_back(level.back());
            }

            if (index % 2 == 0)
            {
                prof.push_back(level[i + 1]);
            }
            else
            {
                prof.push_back(level[i - 1]);
            }
            index /= 2;
        }
        return prof;
    }

    void print_tree()
    {
        for (int i = 0; i < tree.size(); i++)
        {
            cout << "this is level:" << i << endl;
            for (auto level : tree[i])
            {
                cout << level << " ,";
            }
            cout << endl;
        }
    }
    string root()
    {
        return tree.back()[0];
    }

    bool check_proff(string data, int index, vector<string> &ptr, string root)
    {

        string tem = hashf(data);
        string tem1;
        for (string level : ptr)
        {
            if (index % 2 == 0)
            {
                tem = hashf(tem + level);
            }
            else
            {
                tem = hashf(level + tem);
            }
            index /= 2;
        }
        return root == tem;
    }
};
int main()
{
    vector<string> transaction = {"shadat", "murad", "iyasin", "plabon"};

    merkle st(transaction);
    st.buildtree();
    st.print_tree();
    vector<string> prof = st.proftree(1);
        string root = st.root();
    if (st.check_proff("murad", 1, prof, root))
    {
        cout << "valid";
    }
    else
    {
        cout << "not valid";
    }
    return 0;
}