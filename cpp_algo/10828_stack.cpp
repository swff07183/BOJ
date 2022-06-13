#include <iostream>
#include <string>

using namespace std;

int stack[10010];
int top = -1;

void push(int num) {
	top++;
	stack[top] = num;
}

int top_() {
	if (top == -1) return -1;
	else return stack[top];
}

int pop() {
	if (top == -1) return -1;
	else {
		int ret = stack[top];
		stack[top] = 0;
		top--;
		return ret;
	}
}

int main() {
	int N, num;
	cin >> N;
	string oper;
	for (int i=0; i<N; i++)
	{
		cin >> oper;
		if (oper=="push") {
			cin >> num;
			push(num);
		}
		else if (oper=="top") cout << top_() << endl;
		else if (oper=="pop") cout << pop() << endl;
		else if (oper=="size") cout << top+1 << endl;
		else if (oper=="empty") cout << (top==-1 ? 1 : 0) << endl;
	}
}
