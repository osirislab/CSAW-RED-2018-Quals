#include <string>
#include <iostream>
#include <experimental/filesystem>
#include <vector>
using namespace std;

namespace fs = std::experimental::filesystem;

vector<string> ScanEverything(const string& rootDir)
{
    vector<string> results;

    for (auto& p : fs::directory_iterator(rootDir))
    {
        try
        {
            if (fs::is_directory(p.symlink_status()))
            {
                auto t = ScanEverything(p.path().c_str());
                results.insert(results.end(), t.begin(), t.end());
            }
            else
            {
                string filename = p.path().c_str();

                vector<string> filetypes = {".csv", ".docx"};

                for (const auto& t : filetypes)
                {
                    // if (filename.find(t, filename.length()-t.length()))
                    if (filename.find(t) != std::string::npos)
                    {
                        results.push_back(filename);
                    }
                }
            }
        }
        catch(...)
        {
            continue;
        }
    }

    return results;
}

int main()
{
    string path = "/home/kyle/";
    auto results = ScanEverything(path);
    for (const auto& s : results)
        cout << s << endl;

    // Send to server....
}