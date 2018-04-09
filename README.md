# 프로젝트 소개
이 프로젝트는 ko-po-check 프로젝트를 개인적인 용도(리브레오피스)로 수정한 프로젝트입니다.

원래 프로젝트는 https://github.com/changwoo/ko-po-check 를 참고하십시오.


--------------------------------------------------------
## 원래 프로젝트 기본 설명

ko-po-check - 한국어 PO 파일 검사툴

이 프로그램은 한국어 메시지 번역 파일(PO 파일)에서 흔히 범하는
실수들을 찾아내는 프로그램입니다.

이 프로그램은 파이썬 3.0 이상에서 동작합니다. 일반적인 파이썬 모듈과
마찬가지 방법으로 설치할 수 있습니다.

    $ python3 setup.py install

또는 pip나 easy_install을 이용해 PyPI에서 ko-po-check를 설치하셔도
됩니다.

    $ pip install ko-po-check

이 프로그램은 GNU General Public License version 3 혹은 그 이후
버전으로 배포합니다. 정확한 라이선스는 COPYING 파일에서 볼 수
있습니다.

도와 주신 분들은 소스 코드의 THANKS 파일에 들어 있습니다. 이 프로그램
개발에 관한 정보는 github의 프로젝트 페이지에 있습니다. 제안 사항이나
문제점은 다음 프로젝트 페이지로 알려 주십시오.

프로젝트 페이지: https://github.com/changwoo/ko-po-check

문제점: https://github.com/changwoo/ko-po-check/issues

Package Index (PyPI)
   https://pypi.python.org/pypi/ko-po-check


--------------------------------------------------------

## 이 프로젝트에서 변경된 사항

### 특정 keyid 의 경우 검사 무시
: 리브레오피스는 UI/HELP 의 각 문자열에 고유 식별번호(KeyID)가 존재하며, 이는 .po 파일 내에 '#.' 으로 시작하는 줄에서 찾을 수 있다.
이를 이용하여 ko-po-check 에서 검사하지 않는 문자열 목록을 만들고 관리한다.

##### 기본 개념
* 무시할 key id 목록 관리
	- 파일로 관리한다.
	- 각 keyid 는 한 줄에 하나씩 넣는다.
	- '#' 문자 뒤의 내용은 주석으로 무시한다. 예) HqCxG #임프레스에서는 'show'를 '재생'으로 번역한다.
* ignore file
	- 원하는 위치에 원하는 이름으로 생성이 가능하다.
	- 기본 파일은 현재 작업 디렉터리에 .ko-po-check-ignore 라는 파일명으로 생성된다.

##### 사용법
* 기본 무시 목록 파일 사용

```$ ko-po-check --ignore=default ./sd/messages.po```

* 무시 목록 파일 지정

```$ ko-po-check --ignore=file:./_ko-po-check/sd/messages ./sd/messages.po```

* 무시 목록에 keyid 추가 (기본 파일에만 추가됨)

```$ ko-po-check --ignore=add:ZXQSM,mAJ52```

* 무시 목록 파일 초기화 (기본 파일에만 초기화 가능)

```$ ko-po-check --ignore=clear```

##### 팁
* 기본 파일에 무시할 keyid 리스트를 만들고 나중에 다른 이름으로 바꾼다.
* 가능하면 원래 디렉토리 구조를 따른다

```./_ko-po-check/sd/messages : sd/messages.po 파일용 무시 목록```

 * .po 파일 정보 관련 내용도 무시하고 싶으면 파일에 빈줄을 추가한다. 또는 --ignore=add:

##### TODO / Known issues
* ignore 클래스의 코드 정리 필요 : 현재는 클래스라기보다 그냥 코드 분리 수준
* 하나의 파일로 관리할 수 있으면 좋을텐데..
* 파일을 지정해서 추가할 수 있으면 좋을텐데..
* 이러다 디비 쓰지 싶다......
* 원래 프로젝트로 pull request 는... 코드 정리 좀 하고, 범용으로 쓸 수 있게 만들 수 있게 되면???
