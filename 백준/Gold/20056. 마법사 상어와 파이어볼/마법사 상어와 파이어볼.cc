#include <iostream>
#include <vector>
using namespace std;

int di[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dj[8] = {0, 1, 1, 1, 0, -1, -1, -1};

class FireBall {
public:
    int m, s, d;
    FireBall(int m=0, int s=0, int d=0) {
        this->m = m;
        this->s = s;
        this->d = d;
    }
};

int N, M, K;

int main() {
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    cin >> N >> M >> K;
    vector<FireBall> v[N][N];
    vector<FireBall> tmp[N][N];
    int ni, nj;


    for(int i=0; i<M; i++) {
        int r, c, m, s, d;
        cin >> r >> c >> m >> s >> d;
        v[r-1][c-1].push_back(FireBall(m, s, d));
    }

    // 총 K번 수행
    for(int cnt=0; cnt<K; cnt++) {
        // 파이어볼 이동
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                for (int k=0; k<v[i][j].size(); k++) {
                    FireBall fb = v[i][j][k];
                    ni = (i + di[fb.d] * fb.s + N*1001) % N;
                    nj = (j + dj[fb.d] * fb.s + N*1001) % N;
                    tmp[ni][nj].push_back(fb);
                }
                v[i][j].clear();
            }
        }
        // 이동이 끝난 후 두개이상인 경우 체크
        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                if (tmp[i][j].size() > 0) {
                    if (tmp[i][j].size() >= 2) {
                        int m=0, s=0;
                        int d = tmp[i][j][0].d % 2;
                        bool check = true;
                        for (int k=0; k<tmp[i][j].size(); k++) {
                            FireBall fb = tmp[i][j][k];
                            m += fb.m;
                            s += fb.s;
                            if (fb.d%2 != d) check = false;
                        }
                        m /= 5;
                        s /= tmp[i][j].size();
                        if (m > 0) {
                            for (int d=check?0:1; d<8; d+=2){
                                v[i][j].push_back(FireBall(m, s, d));
                            }
                        }
                    }
                    else {
                        v[i][j].push_back(tmp[i][j][0]);
                    }
                }
                tmp[i][j].clear();
            }
        }
        
    }
    // 출력
    int ans = 0;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (v[i][j].size() > 0) {
                for (int k=0; k<v[i][j].size(); k++) {
                    ans += v[i][j][k].m;
                }
            }
        }
    }
    cout << ans << endl;

    return 0;
}