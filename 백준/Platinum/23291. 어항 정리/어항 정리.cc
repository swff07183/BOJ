#include <iostream>
using namespace std;

int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, -1, 0, 1};

class FishBowl {
private:
	int* fishes;
	int tmp[101][101];
	int size;
public:
	FishBowl(int* fishes, int size) {
		this->fishes = new int [size];
		this->size = size;
		for(int i=0; i<size; i++) {
			this->fishes[i] = fishes[i];
		}
	}
	~FishBowl() {
		delete [] fishes;
	}
	
	void printTmp() {
		cout << "======================================" << endl;
		for (int i=size-1; i>=0; i--) {
			for (int j=0; j<size; j++) {
				cout << tmp[i][j] << ' ';
			}
			cout << endl;
		}
		cout << "======================================" << endl;
	}
	void printFishes() {
		cout << "======================================" << endl;
		for (int i=0; i<size; i++) {
				cout << fishes[i] << ' ';
			
			cout << endl;
		}
		cout << "======================================" << endl;
	}
	void resetTmp() {
		for (int i=0; i<size; i++) {
			for (int j=0; j<size; j++) {
				tmp[i][j] = 0;
			}
		}
		for (int i=0; i<size; i++) {
			tmp[0][i] = fishes[i];
		}
	}
	void stackFish() {
		resetTmp();
		
		tmp[1][1] = tmp[0][0];
		tmp[0][0] = 0;

		int height = 2;
		int width = 1;
		int possibleSize = size - 2;

		while (possibleSize >= height) {
			int offset = size-possibleSize-width;
			
			for (int i=0; i<height; i++) {
				for (int j=0; j<width; j++) {
					tmp[width-j][i+offset+width] = tmp[i][j+offset];
					tmp[i][j+offset] = 0;
				}
			}
			int tmpWidth = width;
			width = height;
			height = tmpWidth + 1;
			possibleSize -= width;
		}
	}
	void addMinFish() {
		int tmp = 10000000;
		for (int i=0; i<size; i++) {
			if (tmp > fishes[i]) tmp = fishes[i];
		}
		for (int i=0; i<size; i++) {
			if (tmp == fishes[i]) fishes[i]++;
		}
	}
	void setBalance() {
		int ni, nj, d;
		int addTmp[101][101] = {0, };
		for (int i=0; i<size; i++) {
			for (int j=0; j<size; j++) {
				for (int k=0; k<4; k++) {
					ni = i + di[k];
					nj = j + dj[k];
					if (!(0<=ni && ni<size && 0<=nj && nj<size) || tmp[i][j]==0 || tmp[ni][nj]==0) continue;
					d = (tmp[i][j] - tmp[ni][nj]) / 5;
					if (d > 0) {
						addTmp[i][j] -= d;
						addTmp[ni][nj] += d;
					}
				}
			}
		}
		for (int i=0; i<size; i++) {
			for (int j=0; j<size; j++) {
				tmp[i][j] += addTmp[i][j];
			}
		}
	}

	void flatBowl() {
		int cnt = 0;
		for (int j=0; j<size; j++) {
			for (int i=0; i<size; i++) {
				if (tmp[i][j] != 0) {
					fishes[cnt++] = tmp[i][j];
				}
			}
		}
	}
	
	void halfStackFish() {
		resetTmp();
		int offset = 0;
		int h = 1;
		int w = size / 2;
		for (int cnt=0; cnt<2; cnt++) {
			for (int i=0; i<h; i++) {
				for (int j=0; j<w; j++) {
					tmp[h-i-1+h][w-1-j+offset+w] = tmp[i][j+offset];
					tmp[i][j+offset] = 0;
				}
			}
			offset += size/2;
			w /= 2;
			h *= 2;
		}
	}
	int checkFish() {
		int maxN = -1;
		int minN = 10000000;
		for (int i=0; i<size; i++) {
			if (fishes[i] > maxN) maxN = fishes[i];
			if (fishes[i] < minN) minN = fishes[i];
		}
		return maxN - minN;
	}
};

int main() {
	int N, K;
	cin >> N >> K;
	int* arr = new int[N];
	
	for (int i=0; i<N; i++) {
		cin >> arr[i];
	}
	FishBowl fishBowl(arr, N);

	int fishGap = fishBowl.checkFish();
	int ans = 0;
	while (fishGap > K) {
		fishBowl.addMinFish();
		fishBowl.stackFish();
		fishBowl.setBalance();
		fishBowl.flatBowl();
		fishBowl.halfStackFish();
		fishBowl.setBalance();
		fishBowl.flatBowl();
		fishGap = fishBowl.checkFish();
		ans++;
	}

	cout << ans << endl;

	delete [] arr;

	return 0;
}

/*
1. 물고기의 수가 가장 적은 어항(여러개면 전부 다)에 물고기 한마리 넣음.

2. 어항 쌓기

3. 어항 물고기수 조절
	d(물고기수 차 // 5) > 0 일때, 물고기 보내기

4. 어항 일렬로 다시 놓기(왼쪽, 아래 순서)

5. 공중 부양 작업. N/2씩 두번 반복
*/