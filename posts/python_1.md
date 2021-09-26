# 자바스크립트에서 파이썬으로 이주하기

- Written in 09. 26. 2021

## 개요

한 언어로 코딩하다가 다른 언어를 배우고 사용할 필요가 생겼을 때 그 언어의 스타일, 문법을 바로바로 적용하기란 쉽지 않습니다. 이번 포스트에서는 타입스크립트, 자바스크립트에서 파이썬으로 전환하는 개발자들을 위해 자바스크립트와 파이썬을 비교해봅니다.
본 포스트는 파이썬 3.9 공식 문서를 기준으로 작성되었습니다. 갤럭시 - 아이폰 간 새 폰으로 이동 시 사용자 환경 마이그레이션 툴이 있는 것처럼 본 포스트로 그러한 형태의 간단한 가이드라인으로서 작동하기를 희망합니다.

## 표준형

이번 챕터에서는 파이썬 인터프리터에 내장된 표준형에 관해 설명합니다. 자바스크립트에서는 `Object` 데이터 구조에서 파생된 `Array`, `Set`, `Map` 등의 컬렉션이 있는데, 파이썬에서는 이와 유사한 다음과 같은 컬렉션의 객체 형이 있습니다.

1. 숫자
1. 반복자
1. 시퀀스
1. 집합
1. 매핑
1. 클래스
1. 인스턴스
1. 예외

### 0. 표준형의 비교

표준형을 언급하기 이전에, 표준형 간 논리와 비교 연산에 대해 언급하겠습니다.

| 파이썬 논리 연산 | 유사한 자바스크립트 논리 연산 | 설명 |
| --- | --- | --- |
| `x or y` | `x || y` | _x_ 가 거짓이면 _y_, 그렇지 않으면 _x_ |
| `x and y` | `x && y` | _x_ 가 거짓이면 _x_, 그렇지 않으면 _y_ |
| `not x` | `!x` | _x_ 가 거짓이면 `True`, 그렇지 않으면 `False` |

자바스크립트와 동일하게 `or`, `and` 논리 연산자들은 단락-회로 연산자이므로 첫번째 인자에서 참/거짓이 이미 결정되어지는 경우 두번째 값은 구하지 않습니다. `not`의 경우에는 항상 앞에 오게 해야합니다. `not a == b`는 `not (a == b)`로 해석되고, `a == not b`는 문법 오류입니다.

| 파이썬 비교 연산 | 유사한 자바스크립트 비교 연산 | 설명 |
| --- | --- | --- |
| `<` | `<` | 엄격히 작다 |
| `<=` | `<=` | 작거나 같다 |
| `>` | `>` | 엄격히 크다 |
| `>=` | `>=` | 크거나 같다 |
| `==` | `==` | 같다 |
| `!=` | `!=` | 같지 않다 |
| `is` | `===` 또는 `Object.is()` | 객체 아이덴티티 |
| `is not` | `!==` 또는 `!Object.is()` | 부정된 객체 아이덴티티 |

### 1. 숫자

자바스크립트에서는 `Number` 객체를 통해 정수, 실수 관계 없이 동일한 메소드를 지원하게 유지하는 반면, 파이썬에서는 세 가지 다른 숫자 형이 있습니다: 정수 `int`, 실수 `float`, 복소수 `complex`. 특히 자바스크립트에서 복소수는 외부 라이브러리를 쓰지 않는 이상 구현할 수 있는 형태가 없지만, 파이썬은 복소수 형태까지 있다는 점에서 다릅니다.
`x << n` 과 같은 비트 연산을 할 수 있다는 점을 비롯해서 여러 차이점이 있겠지만, 기본적인 연산의 형태와 고급 연산은 `math.floor()` 같은 형태로 구현된다는 점 등이 자바스크립트의 형태와 유사하기 때문에 구체적으로 언급하지는 않겠습니다.

> 자바스크립트에서도 `BigInt`와 같이 조금은 다른 형태의 숫자 객체가 존재하지만, 본래 느슨한 타입의 언어로서 타입을 미리 선언할 필요 없계 설계되어있다는 점에서 `Number`만 언급했습니다.

### 2. 반복자 (Iterator)

이터레이터 형 (또는 반복자 형)에 대한 내용은 아래 내장 함수 설명 시 같이 다루겠습니다.

### 3. 시퀀스

세 가지 기본 시퀀스 형이 있습니다:

   1. 리스트 `list`
      - `[]`, `[a, b, c]`, `[x for x in iterable]`, `list(iterable)`
   1. 튜플 `tuple`
      - `()`, `a,`, `(a,)`, `a, b, c`, `(a, b, c)`, `tuple(iterable)`
   1. 범위 객체 `range`
      - `range(start, stop[, step])`

이 기본 시퀀스 뿐만 아니라 가변, 불변인지의 여부, 순서를 기억하는 지의 여부 등에 따라서 `collections.abc.Sequence` 표준 라이브러리 등을 통해 세부적인 데이터 시퀀스 형으로 나뉠 수 있습니다. 파이썬의 이 세 가지 기본 시퀀스는 자바스크립트와 상당히 다른 부분입니다. 또한 기본적으로 내재하고 있는 시퀀스 연산이 파이썬에서 자주 사용되고 있는데, 자바스크립트에서는 보지 못한 연산들이 많아 주의깊게 살펴봐야 합니다.

| 파이썬 시퀀스 연산 | 설명 |
| --- | --- |
| `x in sequence` | _sequence_ 의 항목 중 하나가 _x_ 와 같으면 `True`, 그렇지 않으면 `False` |
| `x not in sequence` | _sequence_ 의 항목 중 하나가 _x_ 와 같으면 `False`, 그렇지 않으면 `True` |
| `sequence1 + sequence2` | _sequence1_ 와 _sequence2_ 의 이어 붙이기 |
| `sequence * n` 또는 `n * sequence` | _sequence_ 를 그 자신에 `n` 번 더하는 것과 같습니다
| `sequence[i]` | _sequence_ 의 _i_ 번째 항목, 0에서 시작합니다 |
| `sequence[i:j]` | _sequence_ 의 _i_ 에서 _j_ 까지의 슬라이스 |
| `sequence[i:j:k]` | _sequence_ 의 _i_ 에서 _j_ 까지 스텝 k 의 슬라이스 |

| 파이썬 시퀀스 내장 함수 | 설명 |
| --- | --- |
| `sequence.index(x)` | _sequence_ 의 첫 번째 _x_ 의 인덱스 |
| `sequence.count(x)` | _sequence_ 등장하는 _x_ 의 총 개수 |

또한 `Object.freeze()` 또는 `Immutable.js` 등을 통해 구현되던 불변 객체를 자바스크립트에서 써왔던 경험이 있다면, 다음에서 설명하고 있는 불변 시퀀스, 가변 시퀀스 형에 대해 어렵지 않게 이해할 수 있습니다.

#### 불변 시퀀스만 가지고 있는 것

시퀀스 내 어떠한 변화라도 있다면, 새로운 아이덴티티와 해쉬 값을 갖는 시퀀스입니다. 때문에 불변 시퀀스에서만 `hash()` 내장 함수를 지원하고 있으며 이를 통해 같은 불변 시퀀스인지 비교해볼 수 있습니다. 또한 위에서 언급된 연산 중 `sequence1 + sequence2`를 이용했는데, 이 시퀀스들이 불변 시퀀스였다면, 항상 새로운 객체가 생성됩니다. 때문에 이 불변 시퀀스에 무언가를 이어붙여야 한다면 `str.join()`, `bytes.join()`, `list.extend()` 등을 이용해야 실행 시간을 최적화할 수 있습니다.

#### 가변 시퀀스만 가지고 있는 것

`collections.abc.MutableSequence`에도 정의되어있는 가변 시퀀스 형은, 보다 폭넓은 연산을 제공합니다. 가변 시퀀스에서만 가지고 있는 연산은 다음과 같습니다.

| 파이썬 가변 시퀀스 연산 | 설명 |
| --- | --- |
| `sequence[i] = x` | _sequence_ 의 항목 _i_ 를 _x_ 로 대체합니다 |
| `sequence[i:j] = t` | _i_ 에서 _j_ 까지의 _sequence_ 슬라이스가 이터러블 _t_ 의 내용으로 대체됩니다 |
| `del sequence[i:j]` | `sequence[i:j] = []` 와 같습니다 |
| `sequence[i:j:k] = t` | `sequence[i:j:k]` 의 항목들이 _t_ 의 항목들로 대체됩니다 |
| `del sequence[i:j:k]` | 리스트에서 `sequence[i:j:k]` 의 항목들을 제거합니다 |
| `sequence.append(x)` | 시퀀스의 끝에 _x_ 를 추가합니다 (`sequence[len(sequence):len(sequence)] = [x]` 와 같습니다) |
| `sequence.clear()` | _sequence_ 에서 모든 항목을 제거합니다 (`del sequence[:]` 와 같습니다) |
| `sequence.copy()` | _sequence_ 의 얕은 복사본을 만듭니다 (`sequence[:]` 와 같습니다) |
| `sequence.extend(t)` 또는 `sequence += t` | _t_ 의 내용으로 _sequence_ 를 확장합니다 (대부분 `sequence[len(sequence):len(sequence)] = _t_` 와 같습니다) |
| `sequence *= n` | 내용이 _n_ 번 반복되도록 _sequence_ 를 갱신합니다 |
| `sequence.insert(i, x)` | _x_ 를 _sequence_ 의 _i_ 로 주어진 인덱스에 삽입합니다 (`sequence[i:i] = [x]` 와 같습니다) |
| `sequence.pop()` 또는 `sequence.pop(i)` | _i_ 에 있는 항목을 꺼냄과 동시에 _sequence_ 에서 제거합니다 |
| `sequence.remove(x)` | `sequence[i]` 가 _x_ 와 같은 첫 번째 항목을 _sequence_ 에서 제거합니다 |
| `sequence.reverse()` | 제자리에서 _sequence_ 의 항목들의 순서를 뒤집습니다 |

#### 또다른 시퀀스 형

사실 세 가지 시퀀스 이외에도 바이너리 데이터, 텍스트 문자열의 처리를 위해 추가된 시퀀스도 존재합니다. 이는 다른 포스트를 통해 설명하겠습니다.

### 4. 집합

집합 객체는 순서 없는 컬렉션, 순서 없는 시퀀스입니다. `set`, `frozenset` 등의 내장형이 있으며, `x in set`, `for x in set` 등을 지원합니다. 순서가 없는 컬렉션이므로, 집합은 원소의 위치나 삽입 순서를 기록하지 않습니다. 따라서 시퀀스에는 있는 인덱싱, 슬라이싱 등을 지원하지 않습니다.

### 5. 매핑

매핑 객체는 가변 객체로, 딕셔너리 `dict`라는 오직 하나의 표준 매핑 형이 있습니다. `dict()` 생성자를 이용해 만들 수도 있지만, `{'jack': 4098, 'sjoerd': 4127}` 과 같이 `key:value` 쌍을 나열해서 만들 수도 있습니다. 다음 예제는 모두 `{"one": 1, "two": 2, "three": 3}`와 같은 딕셔너리를 돌려줍니다.

```python
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> f = dict({'one': 1, 'three': 3}, two=2)
>>> a == b == c == d == e == f
True
```

## 내장 함수

우선 파이썬 인터프리터에 포함된 내장 함수 중 주요 함수를 다뤄봅니다.

### 숫자 놀이

다음은 정수, 실수 형태의 숫자들을 변환해주기 위한 내장 함수 목록입니다. 내장 함수의 인수가 반드시 정수, 실수인 경우가 아닌 함수들도 있고, 인수를 여러 형태로 받는 경우도 있으나 자바스크립트에서 주로 사용하는 내장 함수의 대체 함수 사용을 목적으로 작성한 것이기에 모든 인수의 형태를 언급하진 않을 것입니다. 자세한 내용은 공식 문서를 참고하기 바랍니다.

| 파이썬 내장 함수 | 유사한 자바스크립트 함수 | 설명 |
| --- | --- | --- |
| `abs(x)` | `Math.abs(x)` | 절댓값 반환 |
| `bin(x)` | `x.toString(2)` | 이진 문자열 반환 |
| `bool([x])` | `Boolean(x)` 또는 `!!x` | 부울 값 반환 |
| `bytearray([x])` | `ArrayBuffer(x)` | 0 <= x < 256 범위 정수의 가변 배열 |
| `bytes([x])` | `Object.freeze(ArrayBuffer(x))` | 0 <= x < 256 범위 정수의 bytearray 불변 버전 |
| `chr(i)` | `String.fromCharCode(i)` | 아스키코드에 해당하는 문자열 반환 |
| `complex(x)` | - | 복소수 값 반환 |
| `divmod(a, b)` | - | (몫, 나머지) 반환 |
| `float([x])` | `parseFloat(x)` | 실수 형태로 변환 |
| `hex(x)` | `x.toString(16)` | 16진수 문자열로 변환 |
| `int(x)` | `parseInt(x)` | 정수 형태로 변환 |
| `max(a, b)` | `Math.max(a, b)` | 최댓값 반환 |
| `min(a, b)` | `Math.min(a, b)` | 최솟값 반환 |
| `oct(x)` | `x.toString(8)` | 8진수 문자열로 변환 |
| `pow(a, b)` 또는 `a ** b` | `Math.pow(a, b)` 또는 `a ** b` | a의 b 거듭제곱 |
| `round(a)` | `Math.round(a)` | 소수점 반올림 |

### 반복자 (Iterator)

ECMAScript 2015 (ES6)부터 iterable protocol이 적용되어 컬렉션 내 반복 작업을 해야할 때 `Symbol.iterator` 메소드를 이용해 보다 간결한 코드를 구사할 수 있었습니다. 파이썬에도 동일한 역할을 하는 반복자가 존재하는데 이번 챕터에서는 반복자를 이용하는 내장 함수를 정리해보았습니다. 말이 어렵지만, 아래 항목들을 보면 쉽게 이해할 수 있을 것입니다.

| 파이썬 내장 함수 | 유사한 자바스크립트 함수 | 설명 |
| --- | --- | --- |
| `all(iterable)` | `iterable.every((a) => !!a)` | _iterable_ 의 모든 요소가 참이거나 비어있으면 `True` 반환 |
| `any(iterable)` | `iterable.some((a) => !!a)` | _iterable_ 의 요소 중 어느 하나라도 참이면 `True` 반환 |
| `enumerate(iterable)` | `Object.entries(iterable)` | [...(index, value)] 형태의 열거 객체 반환 |
| `filter(function, iterable)` | `iterable.filter((value, index) => Boolean)` | function에서 참이 되는 iterable 요소만 반환 |
| `frozenset([iterable])` | `Object.freeze(iterable)` | 불변 객체 반환 |
| `list([iterable])` | `new Array([iterable])` | _iterable_ 를 list 객체 형으로 변환 |
| `set([iterable])` | `new Set([iterable])` | _iterable_ 를 set 객체 형으로 변환 |
| `sum(iterable)` | `iterable.reduce((a, b) => a + b, 0)` | 합계 반환 |

이터레이터에 대한 자세한 내용은 다음 문서를 참고하세요.

> [파이썬 공식 문서 - 이터레이터 형](https://docs.python.org/ko/3.9/library/stdtypes.html#typeiter)
> [MDN Web Docs - 반복기 및 생성기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Iterators_and_Generators)

## 참고

- [파이썬 공식 문서 - 표준형](https://docs.python.org/ko/3.9/library/stdtypes.html)
- [파이썬 공식 문서 - 내장 함수](https://docs.python.org/ko/3.9/library/functions.html)
- [파이썬 공식 문서 - 파이썬 표준 라이브러리](https://docs.python.org/ko/3.9/library/functions.html)
