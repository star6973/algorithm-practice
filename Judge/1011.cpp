/*
    1011. 징검다리 I

    욕심쟁이 마을에 다니는 잘생긴 광성이(02학번, 컴퓨터공학부)는 하나의 골치꺼리를 가지고 있다.
    그 마을에는 강을 건너기 위해서는 징검다리를 지나가야하는데, 징검다리에 씌여있는 숫자만큼의 금액을 징검다리를 건너는데 지불을 해야 한다.
    만약 징검다리에 씌여있는 숫자가 {3, 2, 9, 1, 4, 8, 1, 2, 3, 1} 이고, 점프력이 3이라고 하면 ﻿{3, 2, 9, 1, 4, 8, 1, 2, 3, 1} ﻿ 을 밟아 최솟값 5로 다리를 건널 수 있다.
    강건너 여자친구를 만나러 갈 때마다 너무많은 비용을 지불하고 있는 광성이를 위해, 징검다리를 건너가는데 드는 최소 비용을 구해주자.
    단 광성이의 최대 점프력은 3으로 고정되어 있다고 가정한다.

    # 입력
        첫 줄에 테스트 케이스 T ( 1 <= T <= 100) 이 주어진다.
        각 테스트 케이스는 징검다리의 길이 n ( 0 <= n <= 10,000)과, 그 길이만큼의 징검다리에 씌여있는 숫자 K1 ~ Kn (0 <= ki <= 100) 이 주어진다.

    # 출력
        각 테스트 케이스마다, 건너는데 드는 최소한의 비용을 출력하라.
*/

#include <iostream>
using namespace std;

int min(int x, int y) {
	return x < y ? x : y;
}

int main(void) {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	int T, N;
	cin >> T;
	while (T--) {
		cin >> N;
		int *bridge = new int[N+1];
		for (int n = 1; n <= N; n++) cin >> bridge[n];

		// dp는 해당 idx를 '밟았을 때' 최소값
		long dp[10001];

		for (int n = 1; n <= N; n++) {
			if (n == 1) dp[1] = bridge[1];
			if (n == 2) dp[2] = bridge[2];
			if (n == 3) dp[3] = bridge[3];

			dp[n] = min(dp[n - 1], min(dp[n - 2], dp[n - 3])) + bridge[n];
		}

		int result = min(dp[N], min(dp[N - 1], dp[N - 2]));
		cout << result << "\n";
	}


	return 0;
}