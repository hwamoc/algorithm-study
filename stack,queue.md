#Stack과 Queue

## Stack

![image](https://user-images.githubusercontent.com/43736669/84123996-91aab200-aa75-11ea-968f-6dfd582cf0fd.png)

데이터의 접근(삽입, 삭제)은 오직 top에서만 일어난다. top에 데이터를 삽입하는 연산을 push, 삭제(리턴)하는 연산을 pop 이라고 함.
undo 기능, 후위표기 계산, 수식 괄호 검사, DFS 등에 사용



## Queue

![image](https://user-images.githubusercontent.com/43736669/84124035-9ff8ce00-aa75-11ea-9d13-97be54de28bd.png)

한쪽 끝(rear)에서 삽입 작업, 다른쪽 끝(front)에서 삭제 작업이 이루어짐.
rear에서 일어나는 삽입을 enQueue, front에서 이루어지는 삭제연산을 deQueue

시간 순서대로 처리되는 작업 예약, 각종 시뮬레이션, 프로세스 스케쥴링, BFS 등에 사용

### Queue의 종류

* Linear Queue : 기본적인 큐

![image](https://user-images.githubusercontent.com/43736669/84124882-c0755800-aa76-11ea-99dc-1144957dc682.png)
![image](https://user-images.githubusercontent.com/43736669/84125105-0a5e3e00-aa77-11ea-9b61-ce48d7519d90.png)

위와 같이 빈 공간이 생겼을 때 공간을 효율적으로 쓰기 위해서는 자료를 한칸씩 옮겨야 하는 불편함이 있다.

* Circular Queue : 원형 모양의 큐
 
![image](https://user-images.githubusercontent.com/43736669/84125237-3aa5dc80-aa77-11ea-8bd9-5c2ffe1dd88d.png)

위와 같이 큐를 원형으로 만들어서 위에 나온 Linear Queue의 단점을 보완한 형태.

* Priority Queue : 데이터들이 우선순위를 가진 큐

먼저 들어간 데이터가 먼저 오는 큐와 달리 들어간 순서에 상관없이 우선순위가 높은 데이터가 먼저 나옴.
