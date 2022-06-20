#include <iostream>

using namespace std;

int oper[4];
int min_result = 1000000001;
int max_result = -1000000001;
int numbers[12];

int calc(int n1, int n2, int oper) {
  if (oper==0) return n1 + n2;
  else if (oper==1) return n1 - n2;
  else if (oper==2) return n1 * n2;
  else if (oper==3) return n1 / n2;
  else return 100000;
}

void recur(int cur, int total, int N) {
  // cout << cur << " " << total << " " << N << endl;
  if (cur == N) {
    if (min_result > total) min_result = total;
    if (max_result < total) max_result = total;
    return;
  }
  for (int i=0; i<4; i++) {
    if (oper[i] > 0){
      oper[i] -= 1;
      recur(cur+1, calc(total, numbers[cur], i), N);
      oper[i] += 1;
    }
  }
}



int main() {
  int N;
  int i;

  cin >> N;
  for (i=0; i<N; i++) {
    cin >> numbers[i];
  }
  for (i=0; i<4; i++) {
    cin >> oper[i];
  }
  recur(1, numbers[0], N);
  cout << max_result << "\n" << min_result;
  return 0;
}