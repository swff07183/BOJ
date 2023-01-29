#include <iostream>
#include <vector>

using namespace std;

int N, M, cnt, tmp;

vector<int> fact;
vector<vector<int>> party(51, vector<int> (0));

int p[51] = {0, };

void input();
void union_(int x, int y);
int find_(int x);

int main(){
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

  int answer = 0;

  for(int i=0; i<51; i++) {
    p[i] = i;  // parent 초기화
  }

  input();
  for(int i=0; i<M; i++) {
    int factCnt = 0;
    for(int j=0; j<party[i].size(); j++) {
      if (find_(party[i][j]) == 0) {
        factCnt += 1;
      }
    }
    if (factCnt == 0) {
      answer += 1;
    }
  }

  cout << answer << endl;
}

void input(){
  cin >> N >> M;
  cin >> cnt;

  for (int i=0; i<cnt; i++) {
    cin >> tmp;
    fact.push_back(tmp);
    p[tmp] = 0;  // parent가 0 => 거짓말 치면 안댐.
  }
  for (int i=0; i<M; i++) {
    cin >> cnt;
    for (int j=0; j<cnt; j++) {
      cin >> tmp;
      party[i].push_back(tmp);
      union_(party[i][0], tmp);  // 같은 파티 union
    }
  }
}

void union_(int x, int y){
  x = find_(x);
  y = find_(y);
  if (x > y) {
    p[x] = y;
  }
  else if (x < y) {
    p[y] = x;
  }
}

int find_(int x){
  if (x != p[x]) {
    p[x] = find_(p[x]);
  }
  return p[x];
}