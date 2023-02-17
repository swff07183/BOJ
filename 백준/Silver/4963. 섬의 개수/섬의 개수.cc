#include <iostream>
#include <queue>
using namespace std;

class Point;
void init();
void bfs(int si, int sj);

int w, h;
int arr[51][51] = {0, };
bool visited[51][51] = {false, };
int di[8] = {-1, 0, 1, 0, 1, 1, -1, -1};
int dj[8] = {0, -1, 0, 1, -1, 1, -1, 1};

int main() {
  int ans;

  for (int tc=1;;tc++) {
    cin >> w >> h;
    if (w == 0 && h == 0) break;
    // 초기화 및 입력
    init();
    ans = 0;
    for (int i=0; i<h; i++) {
      for (int j=0; j<w; j++) {
        cin >> arr[i][j];
      }
    }

    // bfs
    for (int i=0; i<h; i++) {
      for (int j=0; j<w; j++) {
        if (arr[i][j] == 1 && visited[i][j] == false) {
          bfs(i, j);
          ans++;
        }
      }
    }

    cout << ans << endl;
  }

  return 0;
}

class Point
{
public:
  int i, j;
  Point() {}
  Point(int i, int j) { this->i = i; this->j = j; }
};

void init() {
  for (int i=0; i<51; i++) {
    for (int j=0; j<51; j++) {
      arr[i][j] = 0;
      visited[i][j] = false;
    }
  }
}

void bfs(int si, int sj) {
  queue<Point> q;
  Point pos;
  int ni, nj;
  visited[si][sj] = true;
  q.push(Point(si, sj));
  while (q.size()) {
    pos = q.front();
    q.pop();
    for (int d = 0; d < 8; d++) {
      ni = pos.i + di[d];
      nj = pos.j + dj[d];
      if (!(0<=ni && ni<h && 0<=nj && nj<w) || visited[ni][nj] || arr[ni][nj] == 0)
        continue;
      visited[ni][nj] = true;
      q.push(Point(ni, nj));
    }
  }
}