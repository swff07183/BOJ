#include <iostream>
using namespace std;

int N, M;
int arr[51][51];
int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, 1, 0, -1};
bool inRange (int i, int j);
bool isClean (int i, int j);

class Point {
public:
    int i, j;
    Point() {}
    Point(int i, int j) {
        this->i = i;
        this->j = j;
    }
};

class Robot {
private:
    int i, j;   // 현재 좌표
    int d;      // 현재 방향
    int cnt;    // 청소한 칸 개수
public:
    Robot(int i=0, int j=0, int d=0) {
        // 생성자
        this->i = i;
        this->j = j;
        this->d = d;
        this->cnt = 0;
    }
    void setPos(int i, int j) {
        // 위치 설정
        this->i = i;
        this->j = j;
    }
    Point getPos() { return Point(this->i, this->j); }
    int getDir() { return d; }
    void setDir(int d) {
        // 방향 설정
        this->d = d;
    }
    void clean() {
        arr[i][j] = 2;
        this->cnt++;
    }
    int getCnt() { return cnt; }
};



int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    int r, c;    // r, c : 좌표
    int d;      //d :방향
    int ni, nj, nd;
    Point p;

    cin >> N >> M;
    cin >> r >> c >> d;

    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cin >> arr[i][j];
        }
    }

    // 구현
    Robot robot = Robot(r, c, d);
    for (int c=1;;c++) {
        Point p = robot.getPos();
        // 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if (arr[p.i][p.j] == 0) {
            robot.clean();
        }
        // 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        if (isClean(p.i, p.j) == true) {
            nd = (robot.getDir() + 2) % 4;
            ni = p.i + di[nd];
            nj = p.j + dj[nd];
            // 1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            if (inRange(ni, nj) && arr[ni][nj] != 1) {
                robot.setPos(ni, nj);
            }
            // 2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else {
                break;
            }
        }
        // 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        else {
            nd = (robot.getDir() + 3) % 4;
            robot.setDir(nd);
            ni = p.i + di[nd];
            nj = p.j + dj[nd];
            if (inRange(ni, nj) && arr[ni][nj] == 0) {
                robot.setPos(ni, nj);
            }
        }
    }

    cout << robot.getCnt() << endl;

    return 0;
}

bool inRange (int i, int j) {
    return (0<=i && i<N && 0<=j && j<M);
}

bool isClean(int i, int j) {
    int ni, nj;
    for (int d=0; d<4; d++) {
        ni = i + di[d];
        nj = j + dj[d];
        if (inRange(ni, nj) && arr[ni][nj]==0) {
            return false;
        }
    }
    return true;
}
