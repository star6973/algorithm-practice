/*
    1086. Hashcash

    비트코인에서 화폐를 발행하는 방식을 마이닝(mining)이라 부른다.
    비트코인의 화폐는 10분에 한 번씩 일정량이 생성되며 마이닝에 참여한 사용자 중 한 명에게 지급된다.
    참여자들은 hashcash라는 문제를 풀어야 한다. hashcash는 특정한 조건을 가지는 해시값을 찾는 것이다.


    예를 들어 가장 많이 사용하는 해시 알고리즘인 SHA-256으로 임의의 데이터를 해시한 값을 구하면 256비트(32바이트)의 값을 얻는다.
    해시 함수는 단방향 함수라 데이터로부터 해시값을 구할 수는 있지만 해시값으로부터 데이터를 역산하는 것은 이론적으로 불가능하고,
    해시값이 같은 임의의 데이터를 만들어 내는 것 역시 매우 어렵다. 특정한 해시값이 나오는 데이터를 찾으려면 2256개
    (256비트로 나올 수 있는 모든 경우의 수)의 데이터를 일일이 확인해야 한다. 현대의 컴퓨터로는 불가능한 작업이다.

    hashcash 문제는 이 불가능한 역산 작업과 유사하다. 특정한 해시값이 나오는 데이터를 찾는 것은 너무 어려우니
    특정한 범위의 해시값이 나오는 데이터를 찾도록 난이도를 낮춘 것이다.

    "hello world"라는 문자열에 임의의 nonce 숫자(암호 시스템에서 사용하는 일회용 일련번호)를 덧붙여서 SHA-256으로 해시값을 구한 것이다.
    해시값은 "SHA-256 hash calculator"와 같은 사이트에서도 쉽게 확인할 수있다. 위의 값 가운데 'hello world 1'과 'hello world 4'의 해시값의
    시작 부분에는 숫자 0이 각각 1개와 3개가 있다. 0이 4개 이상인 해시값을 찾으려면 nonce 숫자를 조금 더 바꾸어 가면서 시도하면 될 것이다.
    0의 개수가 하나씩 늘어날 때마다 확률적으로 16배씩 더 많은 nonce 숫자를 대입해 보아야 한다. 0의 개수가 5개인 해시값을 찾으려면
    약 백만 개의 nonce 숫자를 대입해야 할 것이라 컴퓨터를 사용해도 쉽게 찾기 어렵다.

    입력 문자열에 대해서 다음과 같은 커스텀 해시값이 00000 으로 끝나도록 Nonce 값을 찾아 출력하시오.
*/

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int CustomHash(const char *str) {

	unsigned long hash = 5381;

	int c;
	while (c = *str++) {
		hash = ((hash << 5) + hash) + c;
	}
	return hash & 0x7FFFFFFF;

}

int main(void) {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	int T;
	cin >> T;
	cin.ignore(256, '\n');

	while (T--) {

		string str;
		string origin;
		getline(cin, str);

		origin = str;

		int num = 1;

		while (true) {

			str = str.append(" ");
			str = str.append(to_string(num));

			vector<char> writable(str.begin(), str.end());
			writable.push_back('\0');
			char* s = &writable[0];

			int Hash = CustomHash(s);

			if (Hash % 10000 == 0) break;
			else {
				num += 1;
				str = origin;
			}
		}

		cout << num << "\n";
	}

	return 0;
}