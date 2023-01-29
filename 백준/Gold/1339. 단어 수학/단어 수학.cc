#include <iostream>
#include <vector>
#include <string>
using namespace std;

int N;
int answer = -1;

vector<string> words;
vector<char> alphas;
string word;

int check[26] = {0, };
int visited[26] = {0, };
int number[26] = {0, };

int getIdx(char alpha) {
  return alpha - 'A';
}

int max(int n1, int n2) {
  return n1 > n2 ? n1 : n2;
}

int getSum() {
  int total = 0;
  int tmp;
  for (int i=0; i<words.size(); i++) {
    tmp = 1;
    for (int j=words[i].size() - 1; j>=0; j--) {
      total += number[getIdx(words[i][j])] * tmp;
      tmp *= 10;
    }
  }

  return total;
}

void dfs(int cnt) {
  if (cnt == alphas.size()) {
    // 값 구하고
    answer = max(answer, getSum());
    return;
  }

  int nxt = 9 - cnt;
  for (int i=0; i<alphas.size(); i++) {
    if (visited[getIdx(alphas[i])] == 0) {
      visited[getIdx(alphas[i])] = 1;
      number[getIdx(alphas[i])] = nxt;
      dfs(cnt + 1);
      visited[getIdx(alphas[i])] = 0;
      number[getIdx(alphas[i])] = 0;
    }
  }

}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N;
  for (int i=0; i<N; i++) {
    cin >> word;
    words.push_back(word);
    for (int j=0; j<word.length(); j++) {
      if (check[getIdx(word[j])] == 0) {
        check[getIdx(word[j])] = 1;
        alphas.push_back(word[j]);
      }
    }
  }

  dfs(0);

  cout << answer;

  return 0;
}