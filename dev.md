# 개발 참고

# 개발 환경

- pyenv
  - local version : 3.8.10
  - [GitHub - pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)
- poetry
  - https://python-poetry.org/docs/m

# 환경 설정
기본적으로 pyenv와 poetry를 설치 해 줍니다.

## peotry 설정
커맨드에서 아래와 같이 설정을 합니다.
```
poetry config virtualenvs.in-project true
poetry config virtualenvs.path "./.venv"
```

## poetry 가상 환경 만들기
```
peotry install
.venv/Scripts/activate
```
## 언어 작업하기
소스에 다국어 처리가 필요한 부분에 `self.tr("예제")`와 같이 넣어 줍니다.

```
ui.ps1
```
위와 같이 커맨드를 실행해서 다국어 자료를 추가해 줍니다.

```
pyside6-linguist.ex
```
를 실행하고 해당 언어 파일을 열고 번역을 해 줍니다.
그리고 `파일 > 배포`를 눌러서 .qm 파일을 만들어 줍니다.

