#include <iostream>

using namespace std;

int N, M;
int arr[100010];
int num, a, b;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> M;
  cin >> arr[1];
  for (int i=1; i<N; i++) {
    cin >> num;
    arr[i+1] = num + arr[i];
  }
  for (int j=0; j<M; j++) {
    cin >> a >> b;
    cout << arr[b] - arr[a-1] << '\n';
  }
  return 0;
}