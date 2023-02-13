#include <iostream>
#include <queue>

using namespace std;

class Point
{
  public:
    int i, j;

    Point() {}
    Point(int x, int y) {
      i = x;
      j = y;
    }
};

int cnt;
int visited[101][101] = {0, };
int arr[101][101];
int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, -1, 0, 1};
int N;

void reset_visited();
void bfs(int si, int sj, int height);
int max(int n1, int n2);


int main()
{
  ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
  
  int ans = -1;

  cin >> N;

  for (int i=0; i<N; i++) {
    for (int j=0; j<N; j++) {
      cin >> arr[i][j];
    }
  }

  for (int h=0; h<=100; h++) {
    // initialize
    cnt = 0;
    reset_visited();
    // bfs
    for (int i=0; i<N; i++) {
      for (int j=0; j<N; j++) {
        if (arr[i][j] > h && visited[i][j] != 1) {
          visited[i][j] = 1;
          bfs(i, j, h);
          cnt += 1;
        }
      }
    }
    ans = max(ans, cnt);
  }

  cout << ans << endl;

  return 0;
}

void reset_visited()
{
  for (int i=0; i<101; i++) {
    for (int j=0; j<101; j++) {
      visited[i][j] = 0;
    }
  }
}

void bfs(int si, int sj, int height)
{
  queue<Point> q;
  Point pos;
  int ni, nj;
  q.push(Point(si, sj));

  while (q.size() > 0) {
    pos = q.front();
    q.pop();

    for (int d=0; d<4; d++) {
      ni = pos.i + di[d];
      nj = pos.j + dj[d];

      if (!(0<=ni && ni<N && 0<=nj && nj<N) || visited[ni][nj] == 1 || arr[ni][nj] <= height) {
        continue;
      }
      visited[ni][nj] = 1;
      q.push(Point(ni, nj));
    }
  }
}

int max(int n1, int n2)
{
  return n1 > n2 ? n1 : n2;
}