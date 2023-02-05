#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

  int t, n;
  string num, tmp;
  bool isCorrect;
  string answer;
  unordered_set<string> checkSet;
  vector<string> numbers;

  cin >> t;
  for (int tc=0; tc<t; tc++) {
    isCorrect = true;
    checkSet.clear();
    numbers.clear();

    cin >> n;
    for(int i=0; i<n; i++) {
      cin >> num;
      numbers.push_back(num);
    }
    sort(numbers.begin(), numbers.end());
    for (int i=0; i<numbers.size(); i++) {
      if (checkSet.find(numbers[i]) != checkSet.end()) {
        isCorrect = false;
        break;
      }
      checkSet.insert(numbers[i]);

      tmp = "";
      for (int j=0; j<numbers[i].size() - 1; j++) {
        tmp += numbers[i][j];
        if (checkSet.find(tmp) != checkSet.end()) {
          isCorrect = false;
          break;
        }
      }
    }

    answer = isCorrect ? "YES" : "NO";
    cout << answer << endl;
  }
  
}