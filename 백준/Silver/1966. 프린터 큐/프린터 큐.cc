#include <iostream>

using namespace std;

int max();

int T, N, M;
  int queue[100];
  bool visited[100];

int main() {
  ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);

  cin >> T;
  int idx, target, cnt;

  for(int tc=1; tc<=T; tc++) {
    cin >> N >> M;
    for(int i=0; i<N; i++) {
      cin >> queue[i];
      visited[i] = false;
    }

    idx = 0, cnt = 1;
    target = max();
    while(true) {
      if (queue[idx] == target) {
        if (idx == M) {
          cout << cnt << endl;
          break;
        } 
        else {
          visited[idx] = true;
          target = max();
          cnt += 1;
        }
      }
      idx = (idx + 1) % N;
    }
  }

  return 0;
}

int max() {
  int ans = -1;
  for(int i=0; i<N; i++) {
    if (queue[i] > ans && visited[i] == false) {
      ans = queue[i];
    }
  }

  return ans;
}