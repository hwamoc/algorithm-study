# Hash 

## Hash란
암호학에서 많이 사용하는 개념으로 파일의 무결성(원본 데이터의 변함없음)을 확인하고자 데이터를 다른 데이터로 변환 시킨 것.

![image](https://user-images.githubusercontent.com/43736669/84117250-2dcfbb80-aa6c-11ea-8fee-fb247b9cfbc0.png)

위 그림은 인풋 데이터에 653을 곱하는 단순한 해싱 과정을 보여주고 있음(단 이 경우 해시의 크기는 일정하지 않음..)

## Hashing Algorithm
임의의 크기의 데이터를 고정된 크기의 hash로 변환하는 수학적 알고리즘. 이 변환 알고리즘은 단방향 함수로 디자인되어있음(뒤집기가 불가능).
ex) Division Method

![image](https://user-images.githubusercontent.com/43736669/84118833-7daf8200-aa6e-11ea-9d84-4b0dfb7dc356.png)

![image](https://user-images.githubusercontent.com/43736669/84118660-3f19c780-aa6e-11ea-8de1-5c35807446b2.png)

원소를 해시 테이블의 크기로 나누어 나머지의 값을 테이블의 주소로 사용하는 Hashing Algorithm. 25,13,16,5,7 의 input을 각각 mod 연산자를 이용해 0부터 12까지의 인덱스에 저장.
이 외에 다양한 해시 함수들이 존재


## 탐색 측면에서의 Hashing

위 mod를 이용한 해시알고리즘을 보면 (충돌이 없다는 가정 하에)데이터 저장 위치를 찾는 과정이나, 데이터를 탐색 할 때 모두 mod 연산 한번으로 O(1) 시간 안에 저장과 탐색을 수행할 수 있다.
따라서 충분한 테이블 크기와 해시값의 충돌이 없는 알고리즘을 사용한다면 모든 데이터의 탐색을 O(1) 시간에 수행할 수 있을 것이다. 

## Table 생성 방식
### 1. Direct Addressing Table

![image](https://user-images.githubusercontent.com/43736669/84119900-01b63980-aa70-11ea-9dd4-4e60f8abe616.png)

key 값을 직접적으로 저장할 배열의 인덱스로 이용하는 방법.
key 값을 다른 변환이나 연산 없이 바로 주소로 활용하므로 탐색, 저장, 삭제, 변경 등이 모두 매우 빠른 시간안에 수행.
하지만 테이블의 크기가 매우 커져야 하고 저장 데이터가 적으면 공간 낭비가 심함.

### 2. Hash Table

![image](https://user-images.githubusercontent.com/43736669/84120214-75584680-aa70-11ea-8885-6b0f279fa959.png)

위에 소개한 mod 연산자를 이용하는 해싱과 유사하게 Key 값을 다양한 함수를 이용해 계산한 후 계산된 결과를 배열의 인덱스로 사용하는 방식. Direct Addressing Table에 비해 공간 낭비가 적지만 다른 데이터가 동일한 해시 값을 가지는 충돌 위험이 있으므로 이것을 피하는 효율적인 알고리즘을 생각해 내는 것이 관건

## 충돌
데이터의 값은 다르나 해시값은 동일하게 생성되는 경우를 충돌이라고 함. 충돌 방지 및 최소화 방법에 대해 알아보자.
### Chaining

![image](https://user-images.githubusercontent.com/43736669/84120740-370f5700-aa71-11ea-8a3e-996d0e1b8736.png)

해시값이 동일한 데이터들을 연결 리스트 형태로 저장하는 방식. 버킷 정렬과 비슷한 개념인듯.
삽입,삭제 시에 바로 해시값을 이용해 주소를 찾으면 되니 O(1)이 걸리고, 탐색 시에 충돌이 있다면 중복되는 값의 수(연결리스트의 크기)만큼 탐색을 해야 한다.
여기서 모든 해시값이 중복되는 Worst Case의 경우 탐색이 O(N) 시간에 탐색을 수행한다.

### Linear probing

![image](https://user-images.githubusercontent.com/43736669/84122648-b867e900-aa73-11ea-9600-c7bd867f4f5d.png)

충돌이 일어나면 충돌이 일어난 바로 다음 인덱스에 데이터를 저장하는 것. 탐색은 해당 해시값을 기준으로 탐색
primary clustering : 특정 해시값 주변 버킷이 채워져 있는 형태. 이 방식은 이러한 문제에 취약.
따라서 이런 문제를 해결하기 위해 quad ratic probing(다음 저장하는 인덱스를 1^2, 2^2 등 제곱 폭으로 탐색) 방식 사용.
여기서 또 secondary clustering이 일어나서 이중 해싱을 사용.

### Simple uniform hash

좋은 해시 함수의 조건은 다음과 같다(Simple uniform hash function)
* 모든 해시값들이 나타날 확률이 동일할 것.
* 각각의 해시값들은 서로 연관성을 가지지 않고 독립적으로 생성될 것(패턴이나 순서가 없도록).

### division method에서의 테이블 크기 선택

앞서 소개한 division method에서는 k mod m 연산을 수행하는 m 값(테이블의 크기)을 선택할 때
* m의 크기는 보통 키의 수의 3배가 적당하다(적재율 30%쯤까지 충돌이 거의 일어나지 않음)
* m으로 2^n 값을 사용하면, 이진수 데이터로 보았을 때 일정 비트 이하만 해쉬값에 영향을 끼친다. 예를들어 8을 사용한다면 00001000 이므로 4번째 비트 이하만 해시값에 영향을 끼쳐 충돌 일어날 확률이 높다. 따라서 보통 2^n에 근접한 소수 선택.
* 따라서 최적의 m은 키의 갯수의 3배쯤 되는 2의 지수승에 근접한 소수


## Python 에서의 Hash
Python에서는 dictionary 자료형을 해시를 이용해 사용(Java, C++의 Hashmap과 유사).
그리고 자세히는 못 뜯어봤지만 이러한 해시 수식을 사용한다고 함..

![image](https://user-images.githubusercontent.com/43736669/84123579-fb768c00-aa74-11ea-9cf7-c87774745420.png)

