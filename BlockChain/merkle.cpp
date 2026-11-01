#include <iostream>
#include <vector>
#include <string>
#include <functional>

using namespace std;

class MerkleTree {
private:
    vector<string> dataBlocks;
    vector<vector<string>> tree;

    // Replace with SHA-256 for real implementation
    string hashFunction(const string &data) {
        return to_string(hash<string>{}(data));
    }

public:
    MerkleTree(const vector<string> &data) {
        dataBlocks = data;
        buildTree();
    }

    // 1. Construct Merkle Tree
    void buildTree() {
        tree.clear();

        vector<string> currentLevel;

        // Hash all data blocks
        for (string data : dataBlocks)
            currentLevel.push_back(hashFunction(data));

        tree.push_back(currentLevel);

        while (currentLevel.size() > 1) {

            // 2. Duplicate last node if odd
            if (currentLevel.size() % 2 == 1)
                currentLevel.push_back(currentLevel.back());

            vector<string> nextLevel;

            for (int i = 0; i < currentLevel.size(); i += 2) {
                nextLevel.push_back(
                    hashFunction(currentLevel[i] + currentLevel[i + 1])
                );
            }

            tree.push_back(nextLevel);
            currentLevel = nextLevel;
        }
    }

    // 3. Merkle Root
    string getMerkleRoot() {
        return tree.back()[0];
    }

    // Print Tree
    void printTree() {
        cout << "\nMerkle Tree\n\n";

        for (int i = 0; i < tree.size(); i++) {
            cout << "Level " << i << endl;

            for (string h : tree[i])
                cout << h << endl;

            cout << endl;
        }
    }

    // 4. Search Node
    bool searchNode(const string& data) {
        for (string d : dataBlocks)
            if (d == data)
                return true;

        return false;
    }

    // 5. Generate Merkle Proof
    vector<string> generateProof(int index) {

        vector<string> proof;

        for (int level = 0; level < tree.size() - 1; level++) {

            vector<string> nodes = tree[level];

            if (nodes.size() % 2 == 1)
                nodes.push_back(nodes.back());

            if (index % 2 == 0)
                proof.push_back(nodes[index + 1]);
            else
                proof.push_back(nodes[index - 1]);

            index /= 2;
        }

        return proof;
    }

    // 6. Verify Proof (Simplified)
    bool verifyProof(const string& data,
                     const vector<string>& proof,
                     const string& root) {

        string currentHash = hashFunction(data);

        for (string sibling : proof)
            currentHash = hashFunction(currentHash + sibling);

        return currentHash == root;
    }
};

int main() {

    vector<string> transactions = {
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eva"
    };

    MerkleTree mt(transactions);

    mt.printTree();

    cout << "Merkle Root:\n";
    cout << mt.getMerkleRoot() << endl;

    cout << "\nSearching for Charlie...\n";

    if (mt.searchNode("Charlie"))
        cout << "Node Found\n";
    else
        cout << "Node Not Found\n";

    cout << "\nGenerating Proof for Bob...\n";

    vector<string> proof = mt.generateProof(1);

    for (string p : proof)
        cout << p << endl;

    cout << "\nVerifying Proof...\n";

    if (mt.verifyProof("Bob", proof, mt.getMerkleRoot()))
        cout << "Proof Valid\n";
    else
        cout << "Proof Invalid\n";

    return 0;
}