#include <iostream>
using namespace std;

int arr[101][101];
int N, L;

int checkRow(int i) {
    int visited[N] = {0, };
    int cnt;

    for (int j=0; j<N-1; j++) {
        // 오르막길
        if (arr[i][j+1] - arr[i][j] == 1) {
            cnt = 0;
            for (int k=j; k>=0 && arr[i][k]==arr[i][j] && cnt < L; k--) {
                if (visited[k] == 1) {
                    // cout << i << " " << j << endl;
                    // for (int x=0; x<N; x++) {
                    //     cout << visited[x] << " ";
                    // }
                    // cout << endl;
                    return 0;
                }
                cnt++;
            }
            if (cnt < L) {
                // 갈수 없는 경우
                return 0;
            }
        }
        // 내리막길
        else if (arr[i][j+1] - arr[i][j] == -1) {
            cnt = 0;
            for (int k=j+1; k<N && arr[i][k]==arr[i][j+1] && cnt < L; k++) {
                cnt++;
                visited[k] = 1;
            }
            if (cnt < L) {
                // 갈수 없는 경우
                return 0;
            }
            
        }
        else if (arr[i][j] == arr[i][j+1]) {
            // 평평한 경우
        }
        else {
            // 차이가 2 이상 나는경우
            return 0;
        }
    }
    return 1;
}

int checkCol(int j) {
    int visited[N] = {0, };
    int cnt;

    for (int i=0; i<N-1; i++) {
        // 오르막길
        if (arr[i+1][j] - arr[i][j] == 1) {
            cnt = 0;
            for (int k=i; k>=0 && arr[k][j]==arr[i][j] && cnt < L; k--) {
                if (visited[k] == 1) {
                    return 0;
                }
                cnt++;
            }
            if (cnt < L) {
                // 갈수 없는 경우
                return 0;
            }
        }
        // 내리막길
        else if (arr[i+1][j] - arr[i][j] == -1) {
            cnt = 0;
            for (int k=i+1; k<N && arr[k][j]==arr[i+1][j] && cnt < L; k++) {
                cnt++;
                visited[k] = 1;
            }
            if (cnt < L) {
                // 갈수 없는 경우
                return 0;
            }
            
        }
        else if (arr[i+1][j] == arr[i][j]) {
            // 평평한 경우
        }
        else {
            // 차이가 2 이상 나는경우
            return 0;
        }
    }

    return 1;
}

int main() {
    int ans = 0;
    cin >> N >> L;

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> arr[i][j];
        }
    }

    // 행 탐색
    for (int i=0; i<N; i++) {
        ans += checkRow(i);
    }

    // 열 탐색
    for (int j=0; j<N; j++) {
        ans += checkCol(j);
    }

    cout << ans << endl;

    return 0;
}

/*
길을 지나갈 수 있는 경우

1. 모든 칸의 높이가 같은 경우
2. 인접한 칸의 높이 차이가 1이면서 낮은 칸이 연속으로 L개 있을 때
*/