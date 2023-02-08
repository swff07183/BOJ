#include <iostream>
#include <unordered_set>
#include <string>

using namespace std;

int main() {
  ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);

  int N, cnt;
  int k = 1;
  cin >> N;

  string students[N+1];
  unordered_set<string> set;

  for (int i=0; i<N; i++) {
    cin >> students[i];
  }

  while(true) {
    set.clear();
    for (int i=0; i<N; i++) {
      set.insert(students[i].substr(students[i].size() - k, k));
    }
    if (set.size() == N) break;
    k++;
  }

  cout << k << endl;

  return 0;
}