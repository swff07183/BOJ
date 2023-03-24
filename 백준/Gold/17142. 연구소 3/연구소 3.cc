#include <iostream>
#include <vector>
#include <queue>
#define INF 1000000
using namespace std;

class Point {
public:
    int i, j;
    Point(int i=0, int j=0) {
        this->i = i;
        this->j = j;
    }
};

int N, M;
int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, -1, 0, 1};
int virusCnt = 0;
int zeroCnt = 0;
int ans = INF;
int arr[51][51];
vector<Point> viruses;
vector<Point> activatedVirus;

int min(int n1, int n2) {
    return n1 < n2 ? n1 : n2;
}

int bfs() {
    int visited[51][51] = {0, };
    queue<Point> q;
    Point p;

    int t = 0;
    int ni, nj;
    int cnt = 0;
    for (int i=0; i<M; i++) {
        q.push(activatedVirus[i]);
        visited[activatedVirus[i].i][activatedVirus[i].j] = 1;
    }

    while (q.size() > 0) {
        int sz = q.size();
        
        for (int i=0; i<sz; i++) {
            p = q.front();
            q.pop();
            
            for (int d=0; d<4; d++) {
                ni = p.i + di[d];
                nj = p.j + dj[d];
                if (!(0<=ni && ni<N && 0<=nj && nj<N) || arr[ni][nj]==1 || visited[ni][nj] != 0) 
                    continue;
                visited[ni][nj] = 1;
                if (arr[ni][nj] == 0) cnt++;
                q.push(Point(ni, nj));
            }
        }
        t++;
        if (cnt == zeroCnt) return t;
    }

    return INF;

}

void activate(int cnt=0, int start=0) {
    if (cnt==M) {
        // 바이러스 체크
        ans = min(ans, bfs());
        return;
    }
    
    for (int i=start; i<virusCnt; i++) {
        activatedVirus.push_back(viruses[i]);
        activate(cnt+1, i+1);
        activatedVirus.pop_back();
    }
}

int main() {
    cin >> N >> M;    

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 2) {
                virusCnt++;
                viruses.push_back(Point(i, j));
            }
            else if (arr[i][j] == 0) {
                zeroCnt++;
            }
        }
    }
    if (zeroCnt == 0) {
        cout << 0 << endl;
        return 0;
    }
    activate();
    if (ans == INF)
        ans = -1;
    cout << ans << endl;

    return 0;
}