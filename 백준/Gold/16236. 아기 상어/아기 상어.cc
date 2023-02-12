#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <queue>

using namespace std;

int N;
int arr[21][21];

class Point
{
  public:
    int i, j;
    Point() {}
    Point(int x, int y)
    {
      i = x;
      j = y;
    }
};

class Fish
{
  public:
    int i, j, size;
    Fish(int x, int y, int sz)
    {
      i = x;
      j = y;
      size = sz;
    }
    const bool operator <(const Fish& otherFish) const
    {
      if (i != otherFish.i) return i < otherFish.i;
      else return j < otherFish.j;
    }
};

class Shark
{
  public:
    int i, j, size, cnt;
    Shark() {}
    Shark(int x, int y)
    {
      i = x;
      j = y;
      size = 2;
      cnt = 0;
    }
    void eat(Fish& fish)
    {
      i = fish.i;
      j = fish.j;
      cnt++;
      if (cnt == size)
      {
        cnt = 0;
        size++;
      }
    }
    int getDist(Fish& fish, int n)
    {
      // 자기보다 큰 물고기는 못지나감 => bfs로 거리 재야할듯?
      queue<Point> q;
      Point p;
      int ni, nj;
      int visited[21][21] = {0, };
      int ans = 0;
      int di[4] = {-1, 0, 1, 0};
      int dj[4] = {0, -1, 0, 1};

      q.push(Point(i, j));
      visited[i][j] = 1;
      while (q.size() > 0)
      {
        int qSize = q.size();
        for (int k=0; k<qSize; k++)
        {
          p = q.front();
          q.pop();
          if (p.i == fish.i && p.j == fish.j) return ans;
          for (int d=0; d<4; d++)
          {
            ni = p.i + di[d];
            nj = p.j + dj[d];
            if (!(0<=ni && ni<n && 0<=nj && nj<n) || visited[ni][nj] == 1 || arr[ni][nj] > size) continue;
            visited[ni][nj] = 1;
            q.push(Point(ni, nj));
          }
        }
        ans++;
      }

      return -1;
    }
};

int main()
{
  ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
  cin >> N;
  int ans = 0;  // 생존 시간
  vector<Fish> fishes;  // 물고기들
  Shark shark;  // 상어
  int target; // 먹었는지 체크

  // 기본 입력
  for (int i=0; i<N; i++)
  {
    for (int j=0; j<N; j++)
    {
      cin >> arr[i][j];
      if (arr[i][j] == 9)
      {
        // shark
        shark = Shark(i, j);
        arr[i][j] = 0;
      }
      else if (arr[i][j] > 0)
      {
        // Fish
        fishes.push_back(Fish(i, j, arr[i][j]));
      }
    }
  }
  while (true)
  {
    target = -1;  // target 초기화
    sort(fishes.begin(), fishes.end());  // fishes 정렬
    // fishes 순회하면서 먹을 수 있는 물고기 찾기
    for(int i=0; i<fishes.size(); i++)
    {
      if (shark.getDist(fishes[i], N) != -1 && (fishes[i].size < shark.size && (target == -1 || shark.getDist(fishes[i], N) < shark.getDist(fishes[target], N))))
      {
        target = i;
      }
    }
    if (target != -1)
    {
      ans += shark.getDist(fishes[target], N);
      shark.eat(fishes[target]);
      arr[fishes[target].i][fishes[target].j] = 0;
      fishes.erase(fishes.begin() + target);
    }
    else break;
  }

  cout << ans << endl;

  return 0;
}
