#include <iostream>
using namespace std;

int N, M, K;
int** A;
int** B;
int** ans;

void matrix_mul() {
    int tmp;

    for (int i=0; i<N; i++) {
        for (int j=0; j<K; j++) {
            tmp = 0;
            for (int r=0; r<M; r++) {
                tmp += (A[i][r] * B[r][j]);
            }
            ans[i][j] = tmp;
        }
    }
}


int main() {
    
    cin >> N >> M;
    A = new int*[N];
    for(int i=0; i<N; i++) A[i] = new int[M];

    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cin >> A[i][j];
        }
    }

    cin >> M >> K;
    B = new int*[M];
    for (int i=0; i<M; i++) B[i] = new int[K];
    
    for (int i=0; i<M; i++) {
        for (int j=0; j<K; j++) {
            cin >> B[i][j];
        }
    }
    ans = new int*[N];
    for (int i=0; i<N; i++) ans[i] = new int[K];
    
    matrix_mul();

    for (int i=0; i<N; i++) {
        for (int j=0; j<K; j++) {
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}