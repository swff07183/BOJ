#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

void backtracking(int cnt, string s);
int calc(string s);
int to_int(char n);

int T, N;
int visited[10] = {0, };
char oper[] = {' ', '+', '-'};
vector<string> v;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

  cin >> T;
  for(int tc=1; tc<=T; tc++) {
    // visited 초기화
    for(int i=0; i<10; i++) visited[i] = 0;
    // 
    cin >> N;
    backtracking(1, "1");
    v.push_back("");
  }

  for(int i=0; i<v.size()-1; i++) {
    cout << v[i] << endl;
  }
}

void backtracking(int cnt, string s) {
  if (cnt == N) {
    if(calc(s) == 0) {
      v.push_back(s);
    }
    return ;
  }

  for(int i=0; i<3; i++) {
    backtracking(cnt+1, s+oper[i]+to_string(cnt+1));
  }
}

int calc(string s) {
  int total = 0;
  int tmp = 0;
  int sign = 1;
  for (int i=0; i<s.size(); i++) {
    if (s[i] == '+') {
      total += sign * tmp;
      tmp = 0;
      sign = 1;
    }
    else if (s[i] == '-') {
      total += sign * tmp;
      tmp = 0;
      sign = -1;
    }
    else if (s[i] == ' ') {
      tmp *= 10;
    }
    else {
      tmp += to_int(s[i]);
    }
  }

  total += sign * tmp;

  return total;
}

int to_int(char n) {
  return n - '0';
}