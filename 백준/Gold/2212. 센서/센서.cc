#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, K;
vector<int> v;
vector<int> dist;

int main() {
  int tmp;
  cin >> N >> K;
  int answer = 0;
  int cnt = N;
  for(int i=0; i<N; i++) {
    cin >> tmp;
    v.push_back(tmp);
  }
  sort(v.begin(), v.end());

  for(int i=0; i<N-1; i++) {
    tmp = v[i+1] - v[i];
    if (tmp != 0) dist.push_back(tmp);
    else cnt -= 1;
  }

  sort(dist.begin(), dist.end());

  for(int i=0; i<cnt-K; i++) answer += dist[i];
  cout << answer << endl;
  

  return 0;
}