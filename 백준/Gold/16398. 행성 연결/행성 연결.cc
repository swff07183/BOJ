#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void union_(int x, int y);
int find_(int x);

int p[1010] = {0, };

struct Edge {
  int x, y, v;
  Edge(int a, int b, int c) {
    x = a;
    y = b;
    v = c;
  }

  bool operator< (const Edge &e) const {
    return v < e.v;
  }
};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

  int N, tmp, x, y;
  int cnt = 0;
  long answer = 0;

  cin >> N;
  for (int i=0; i<N; i++) {
    p[i] = i;
  }

  vector<Edge> v;
  for(int i=0; i<N; i++) {
    for(int j=0; j<N; j++) {
      cin >> tmp;
      if (i < j) {
        v.push_back(Edge(i, j, tmp));
      }
    }
  }
  sort(v.begin(), v.end());

  for(int i=0; i<v.size(); i++) {
    x = find_(v[i].x);
    y = find_(v[i].y);
    if (x != y) {
      union_(x, y);
      answer += v[i].v;
      cnt += 1;
    }
    if (cnt >= N-1) break;
  }

  cout << answer << endl;

  return 0;
}

void union_(int x, int y) {
  x = find_(x);
  y = find_(y);

  if (x > y) p[x] = y;
  else if (x < y) p[y] = x;
}

int find_(int x) {
  if (x != p[x]) {
    p[x] = find_(p[x]);
  }

  return p[x];
}