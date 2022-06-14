#include <iostream>

using namespace std;

int result = 1000000;
int N, half, tmp;
bool v[20];
int arr[21][21];

void recur(int cur, int s) {
  if (cur == half) {
    tmp = 0;
    for (int i=0; i<N; i++) {
      for (int j=0; j<N; j++) {
        if (v[i]&&v[j]) tmp += arr[i][j];
        else if (!(v[i] || v[j])) tmp -= arr[i][j];
      }
    }
    if (tmp < 0) tmp = -tmp;
    if (result > tmp) result = tmp;
    return;
  }
  for (int i=s; i<N; i++){
    if (!v[i]) {
      v[i] = true;
      recur(cur+1, i+1);
      v[i] = false;
    }
  }

}


int main() {
  cin >> N;

  half = N/2;


  for (int i=0; i<N; i++) {
    for (int j=0; j<N; j++) {
      cin >> arr[i][j];
    }
  }
  recur(0, 0);
  cout << result;
  return 0;
}