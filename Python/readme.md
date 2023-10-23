파이썬 학습 Repo

**튜플**  
몇 가지 점을 제외하곤 리스트와 비슷한 자료구조  
리스트는[], 튜플은()으로 둘러싼다.  
(리스트의 요소값은 생성,삭제,수정 가능하지만 튜플은 못바꿈)
```
t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = ('a', 'b', ('c','d'))

del t1[0] // 오류
```
</br>

**딕셔너리**  
"이름" : "홍길동", "생일" = "몇월며칠" 이런 대응 관계를 나타낼 수 있는 딕셔너리라는 자료형이 있다. 연관 배열이라고도 하는데 키 벨류를 한 쌍으로 가지는 자료형이다. 

딕셔너리는 리스트나 튜플처럼 순차적으로 요소값을 구하는게 아니라 키를 통해 벨류를 얻는다. key(baseball) value(야구)라면 baseball의 단어 뜻을 찾기 위해 사전 내용을 순차적으로 검색이 아니라 해쉬맵느낌이다.
</br>

**함수 def 자바의 메소드**  
</br>

**클래스는 왜 필요한가**  
C언어도 클래스가 없는데 파이썬도 클래스 없이 프로그램 잘 만든게 있다. 함수나 자료형처럼 꼭 필요한 요소는 아니다. 적재 적소에 잘 쓰면 매우 유용한데 

계산기에 숫자 3을 입력하고 +를 입력한 후 4를 입력하면 결괏값으로 7을 보여 준다. 다시 한번 +를 입력한 후 3을 입력하면 기존 결괏값 7에 3을 더해 10을 보여 준다. 즉, 계산기는 이전에 계산한 결괏값을 항상 메모리 어딘가에 저장하고 있어야 한다.

계산기 n 대로 def add를 돌리면 global 변수가 수십개라면 불가능해진다.  
```
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
```
</br>

**__init__.py의 용도**  
__init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려 주는 역할, 패키지와 관련된 설정이나 초기화 코드를 포함할 수 있다. 

__init__()은 반드시 첫 번째 인수로 self를 지정해야한다. self에는 인스턴스 자체가 전달되어 있다. 이로 인해, 메소드 내에 인스턴스 변수를 작성하거나, 참고하는 것이 가능해진다. 클래스를 생성할 때에 지정한 인수는 초기화 메소드의 2 번째부터 작성해 나가면 된다.

ex)
```
class MyStatus:
    def __init__(self,age,name,height,weight):
        self.age = age
        self.name = name
        self.height = height
        self.weight = weight

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)

    def print_height(self):
        print(self.height)

    def print_weight(self):
        print(self.weight)
```
</br>

**self의 역할**  
클래스의 구성을 취득할 때에 정형의 구문? 클래스 내에 정의된 함수를 메서드라고 하는데 메서드의 첫번째인자는 self로 지정한다. 필수 규칙은 아닌거같다.

```
        def func1():
                print("function 1")
        def func2(self):
                print("function 2")
```
이렇게 해도 첫번째 인자가 self가 아닌데 func1은 오류가 없음, self는 객체의 인스턴스 그 자체를 말한다. 즉, 객체 자기 자신을 참조하는 매개변수인 셈이다. 

객체지향 언어는 모두 이걸 메소드에 안보이게 전달하지만, 파이썬은 클래스의 메소드를 정의할 때 self를 명시한다. 메소드를 불러올 때 self는 자동으로 전달된다. self를 사용함으로 클래스내에 정의한 멤버에 접근할 수 있게된다.
