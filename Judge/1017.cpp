/*
    1017. 돈을 줍자

    동수가 길을 걷고 있는데, 천사가 나타나서 가는 길에 돈을 뿌려 놓았다. 그리고는 하는 말이
    "마음껏 돈을 가져가세요, 하지만 연속해서 3개의 돈을 주우면 지옥에 가게 됩니다"
    불쌍한 동수를 위해 가장 많은 돈을 주울 수 있는 프로그램을 작성해서 건내주도록 합시다.

    돈이 [5, 7, 10, 1, 2, 10, 11, 6] 으로 놓여져 있다면 ﻿ [5, 7, 10, 1, 2, 10, 11, 6]﻿  이렇게 7, 10, 10, 11을 주어 38원(.....) 을 주울 수 있습니다.

    # 입력
        첫 번째 줄에는 테스트 케이스의 수 T (1 <= T <= 100) 가 주어집니다.
        두번째 줄에는, 떨어진 돈의 갯수 N (1 <= N <= 1,000) 과, N개의 금액이 주어집니다. 금액은 합해서 30,000 을 초과하지 않습니다.

    # 출력
        각 테스트 케이스 마다 가장 많이 주울 수 있는 돈의 액수를 출력 해 주세요.
*/

#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	int T, N;
	cin >> T;

	while (T--) {
		cin >> N;

		int result = 0;
		int dp[30001];
		int coin[1001];

		for (int n = 1; n <= N; n++) cin >> coin[n];

		dp[0] = 0;
		dp[1] = coin[1];
		dp[2] = coin[1] + coin[2];

		if (N > 2) {
			for (int i = 3; i <= N; i++) {
			    // dp의 의미: 현재 i번째 위치에서 가질 수 있는 최대 동전의 합
				dp[i] = max(dp[i - 3] + coin[i - 1] + coin[i], max(dp[i - 2] + coin[i], dp[i - 1]));
			}
			cout << dp[N] << "\n";
		}
		else {
			cout << dp[N] << "\n";
		}
	}

	return 0;
}