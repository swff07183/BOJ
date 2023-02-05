#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

vector<int> split(string str, char delimiter);
string getAnswer(vector<int> v, int s, int sz, bool isReverse);

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  
  int T, n, s, sz;
  bool isReverse, isError;
  string p, str_x;
  vector<int> x;
  
  cin >> T;

  for(int tc=1; tc<=T; tc++) {
    // 입력 받고 문자열 => 벡터로 파싱
    cin >> p >> n >> str_x;
    x = split(str_x.substr(1, str_x.size()-2), ',');

    isReverse = false;
    isError = false;
    s = 0;
    sz = x.size();

    for (int i=0; i<p.size(); i++) {
      if (p[i] == 'R') {
        isReverse = !isReverse;
      }
      else {
        if (sz == 0) {
          // error 발생!
          isError = true;
          break;
        }
        else if (isReverse == false) {
          // 앞에서 제거
          s += 1;
        }
        sz -= 1;
      }
    }

    if (isError == true) {
      cout << "error" << endl;
    }
    else {
      cout << getAnswer(x, s, sz, isReverse) << endl;
    }
 
  }

  return 0;
}

vector<int> split(string str, char delimiter) {
    vector<int> ret;
    stringstream ss(str);
    string temp;
 
    while (getline(ss, temp, delimiter)) {
        ret.push_back(stoi(temp));
    }
 
    return ret;
}

string getAnswer(vector<int> v, int s, int sz, bool isReverse) {
  string answer = "";

  answer += '[';
  int e = s + sz - 1;

  if (isReverse == true) {
    for(int i=e; i>=s; i--) {
      answer += to_string(v[i]);
      if (i != s) answer += ',';
    }
  } else {
    for(int i=s; i<=e; i++) {
      answer += to_string(v[i]);
      if (i != e) answer += ',';
    }
  }

  answer += ']';

  return answer;
}