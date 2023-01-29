#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
  int s, e, v;
  Edge(int x, int y, int z) {
    s = x;
    e = y;
    v = z;
  }
  bool operator< (const Edge &e) const {
    return v < e.v;
  }
};

int m, n;
vector<Edge> v;
int answer = 0;

int p[200001] = {0, };

bool input();
void union_(int x, int y);
int find_(int x);
bool tc;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

  while (1) {
    int cnt = 0;
    int x, y;

    tc = input();
    if (tc == false) {
      break;
    }

    for (int i=1; i<=m; i++) {
      p[i] = i;  // parent 초기화
    }
    sort(v.begin(), v.end());
    
    for (int i=0; cnt < m-1; i++) {
      int x = find_(v[i].s);
      int y = find_(v[i].e);
      if (x != y) {
        union_(x, y);
        answer -= v[i].v;
        cnt += 1;
      }
    }

    cout << answer << endl;
  }

  return 0;
}

bool input() {
  int x, y, z;

  cin >> m >> n;
  if (m == 0 && n == 0) {
    return false;
  }

  // 초기화
  answer = 0;
  for (int i=0; i<m; i++) {
    p[i] = i;
  }

  v.clear();

  for(int i=0; i<n; i++) {
    cin >> x >> y >> z;
    v.push_back(Edge(x, y, z));
    answer += z;
  }
  return true;
}

void union_(int x, int y) {
  if (x < y) p[y] = x;
  else if (x > y) p[x] = y;

  return ;
}

int find_(int x) {
  if (x != p[x]) p[x] = find_(p[x]);

  return p[x];
}