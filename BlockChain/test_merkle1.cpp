#include <bits/stdc++.h>

using namespace std;

class Merkle1
{
private:
    vector<string> datablock;
    vector<vector<string>> tree;
    string hashf(const string &data)
    {
        return to_string(hash<string>{}(data));
    }

public:
    Merkle1(vector<string> &data)
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
        for (int i = 0; i < tree.size() - 1; i++)
        {
            vector<string> level = tree[i];

            if (level.size() % 2 == 1)
            {
                level.push_back(level.back());
            }

            if (index % 2 == 0)
            {
                prof.push_back(level[index + 1]);
            }
            else
            {
                prof.push_back(level[index - 1]);
            }
            index /= 2;
        }
        return prof;
    }


void print_tree()
{
    if (tree.empty())
        return;

    int n = tree.size();
    int leafCount = tree[0].size();

    const int nodeWidth = 8;
    const int nodeGap = 4;
    int width = leafCount * (nodeWidth + nodeGap);

    for (int i = n - 1; i >= 0; i--)
    {
        int count = tree[i].size();
        int step = width / count;

        string line(width + nodeWidth, ' ');

        for (int j = 0; j < count; j++)
        {
            string h = tree[i][j].substr(0, 6);

            int center = step * j + step / 2;
            int start = center - h.size() / 2;

            line.replace(start, h.size(), h);
        }

        cout << line << "\n\n";
    }

    cout << "Transactions:\n";

    for (string data : datablock)
        cout << data << "  ";

    cout << endl;
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
    vector<string> transaction = {"shadat", "murad", "iyasin"};

    Merkle1 st(transaction);
    st.print_tree();
    vector<string> prof = st.proftree(1);
    for(auto p :prof){
        cout<<p<<" ";
    }
    cout<<endl;
        string root = st.root();

    if (st.check_proff("murad1", 1, prof, root))
    {
        cout << "valid";
    }
    else
    {
        cout << "not valid";
    }
    return 0;
}