#include <iostream>
#include <set>

using namespace std;

int N;
int num[] = {1, 5, 10, 50};

set<int> s;

void recur(int cnt, int check, int total = 0) {
  if (cnt == 3) {
    s.insert(total + (num[3] * (N - check)));
    return;
  }

  for(int i=0; i<=N-check; i++) {
    recur(cnt+1, check + i, total + (num[cnt] * i));
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);

  cin >> N;

  recur(0, 0);

  cout << s.size() << endl;

  return 0;
}
