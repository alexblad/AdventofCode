#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <chrono>

using namespace std;

// --- HELPER: Integer Power Function ---
long long ipow(long long base, int exp) {
    long long res = 1;
    for (int i = 0; i < exp; i++) res *= base;
    return res;
}

// --- MATH APPROACH ---
map<int, vector<long long>> mask_cache;

vector<long long> get_masks(int d) {
    if (mask_cache.count(d)) {
        return mask_cache[d];
    }

    vector <long long> masks;
    
for (int l = 1; l <= d / 2; l++) {
        if (d % l == 0) {
            long long numerator = ipow(10, d) -1;
            long long denominator = ipow(10, l) -1;
            masks.push_back(numerator / denominator);
        }
    }

    mask_cache[d] = masks;
    return masks;
}

long long solve_math(const vector<pair<long long, long long>> & ranges){
    long long count = 0;
    for (const auto& r : ranges) {
        for (long long id = r.first; id <= r.second; id++) {
            int d = (int)log10(id) + 1;
            
            const vector<long long>& masks = get_masks(d);

            for (long long mask: masks) {
                if (id % mask == 0){
                    count ++;
                    break;
                }
            }
        }
    }
    return count;
}

// --- STRING APPROACH ---
long long solve_string(const vector<pair<long long, long long>> & ranges) {
    long long count = 0;
    for (const auto& r : ranges) {
        for (long long id = r.first; id <= r.second; id++) {
            string s = to_string(id);

            string doubled = s + s;

            string searchArea = doubled.substr(1, doubled.length() -2);

            if (searchArea.find(s) != string::npos) {
                count ++;
            }
        }
    }
    return count;
}

int main() {
    // Dummy Data
    vector<pair<long long, long long>> ranges = { {100000, 200000},
     {500000000, 1000000000} 
    };

    cout << "Starting C++ Benchmark..." << endl;

    // --- BENCHMARK MATH ---
    auto start = chrono::high_resolution_clock::now();
    long long math_count = solve_math(ranges);
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> diff = end - start;
    cout << "Math Method: " << diff.count() << "s ( Found:" << math_count << " )" << endl;

    // --- Benchmark String ---
    start = chrono::high_resolution_clock::now();
    long long string_count = solve_string(ranges);
    end = chrono::high_resolution_clock::now();
    diff = end - start;
    cout << "String Method: " << diff.count() << " s (Found: " << string_count << ")" << endl;

    return 0;
}