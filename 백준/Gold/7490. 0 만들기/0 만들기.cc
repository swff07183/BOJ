#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

void backtracking(int cnt, string s);
int calc(string s);
int to_int(char n);

int T, N;
char oper[] = {' ', '+', '-'};
vector<string> v;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

  cin >> T;
  for(int tc=1; tc<=T; tc++) {
    cin >> N;
    backtracking(1, "1");
    v.push_back("");
  }

  for(int i=0; i<v.size()-1; i++) {
    cout << v[i] << endl;
  }
}

void backtracking(int cnt, string s) {
  // 가능한 모든 식 구하기
  if (cnt == N) {
    // 계산해주고 0이되면 vector에 추가
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
    if (s[i] == '+' || s[i] == '-') {
      total += sign * tmp;
      tmp = 0;
      sign = s[i] == '+' ? 1 : -1;
    }
    else if (s[i] == ' ') {
      tmp *= 10;
    }
    else {
      tmp += to_int(s[i]);
    }
  }
  // 마지막 남은 숫자 더해주기
  total += sign * tmp;

  return total;
}

int to_int(char n) {
  return n - '0';
}