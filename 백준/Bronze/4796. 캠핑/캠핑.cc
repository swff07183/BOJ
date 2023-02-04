#include <iostream>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  
  int L, P, V, answer;

  for (int tc=1; ; tc++){
    answer = 0;

    cin >> L >> P >> V;
    if (L==0 && P==0 && V==0) break;

    answer += (V / P) * L + min(V%P, L);

    cout << "Case " << tc << ": " << answer << endl;
  }

  return 0;
}