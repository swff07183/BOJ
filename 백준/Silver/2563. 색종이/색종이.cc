#include <iostream>

using namespace std;

int main()
{
  ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);

  int N, x, y;
  int arr[101][101] = {0, };
  int ans = 0;

  cin >> N;
  for (int c=0; c<N; c++)
  {
    cin >> x >> y;
    for (int i=x; i<x+10; i++)
    {
      for (int j=y; j<y+10; j++)
      {
        arr[i][j] = 1;
      }
    }
  }

  for (int i=1; i<=100; i++)
  {
    for (int j=1; j<=100; j++)
    {
      ans += arr[i][j] ? 1 : 0;
    }
  }

  cout << ans << endl;

  return 0;
}