#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class CntNum {
public:
    int value, cnt;
    CntNum(int value=0, int cnt=0) {
        this->value = value;
        this->cnt = cnt;
    }
    const bool operator<(CntNum &cntNum2) {
        if (this->cnt == cntNum2.cnt)
            return this->value < cntNum2.value;
        else 
            return this->cnt < cntNum2.cnt;
    }
};

int r, c, k;
int arr[101][101] = {0, };

int max(int n1, int n2) {
    return n1 > n2 ? n1 : n2;
}

vector<int> getSortResult(int* tmp) {
    // tmp : 1~100 카운팅 배열
    vector<int> res;
    vector<CntNum> sortVector;

    for (int i=1; i<101; i++) {
        if (tmp[i] != 0) {
            sortVector.push_back(CntNum(i, tmp[i]));
        }
    }
    
    sort(sortVector.begin(), sortVector.end());

    for (int i=0; i!=sortVector.size(); i++) {
        res.push_back(sortVector[i].value);
        res.push_back(sortVector[i].cnt);
    }

    return res;
}

int rowSort() {
    vector<int> tmp;
    int sz;
    int ret = 0;

    for (int i=0; i<100; i++) {
        int cntArr[101] = {0, };
        for (int j=0; j<100; j++) {
            cntArr[arr[i][j]] += 1;
        }
        
        tmp = getSortResult(cntArr);
        sz = tmp.size();
        for (int j=0; j<sz; j++) {
            arr[i][j] = tmp[j];
        }
        for (int j=sz; j<100; j++) {
            arr[i][j] = 0;
        }

        ret = max(ret, sz);
    }

    return ret;
}

int colSort() {
    vector<int> tmp;
    int sz;
    int ret = 0;

    for (int j=0; j<100; j++) {
        int cntArr[101] = {0, };
        for (int i=0; i<100; i++) {
            cntArr[arr[i][j]] += 1;
        }
        
        tmp = getSortResult(cntArr);
        sz = tmp.size();
        for (int i=0; i<sz; i++) {
            arr[i][j] = tmp[i];
        }
        for (int i=sz; i<100; i++) {
            arr[i][j] = 0;
        }

        ret = max(ret, sz);
    }

    return ret;
}



int main() {
    int rCnt = 3;
    int cCnt = 3;
    int ans = 0;

    cin >> r >> c >> k;
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            cin >> arr[i][j];
        }
    }
    
    while (ans <= 100) {
        if (arr[r-1][c-1] == k) {
            cout << ans << endl;
            return 0;
        }

        // 행의개수 >= 열의 개수 -> R연산
        if (rCnt >= cCnt) {
            cCnt = rowSort();
        }

        // 행의개수 <  열의 개수 -> C연산
        else {
            rCnt = colSort();
        }


        ans += 1;   // 연산 시간 증가

    }
    cout << -1 << endl;

    return 0;
}