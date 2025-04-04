# 코드

## 알고리즘 설명

이 프로젝트는 이렇게 작동해요:

1. 마술봉을 흔들면 (흔들기 감지)
2. 웃음소리가 나와요
3. 랜덤한 색상이 만들어져요 (빨강, 초록, 파랑을 섞어서)
4. 모든 네오픽셀 LED에 그 색상이 나타나요
5. 2초 동안 빛을 내요
6. LED가 꺼져요
7. 다시 흔들 때까지 기다려요

## 블록코딩

이 그림처럼 블록을 연결하면 돼요:

![code](/img/block.png)

## 텍스트코딩 (Python)

```python
def on_gesture_shake():
    global random_color
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.IN_BACKGROUND)
    # 랜덤 색상 생성 (빨강, 초록, 파랑 값을 랜덤으로 지정)
    random_color = neopixel.rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    # 모든 네오픽셀에 랜덤 색상 적용
    strip.show_color(random_color)
    basic.pause(2000)
    strip.clear()
    strip.show()
    basic.pause(200)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

random_color = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P1, 8, NeoPixelMode.RGB)
```

## 코드 업로드하는 방법

1. 컴퓨터에서 [MakeCode 편집기](https://makecode.microbit.org/)를 열어요.
2. "새 프로젝트" 버튼을 눌러요.
3. 왼쪽 메뉴에서 "고급"을 클릭한 다음 "확장기능"을 선택해요.
4. "neopixel"을 검색하고 선택해요.
5. 블록을 그림처럼 연결해요.
6. 프로젝트 이름을 넣고 저장해요.
7. "다운로드" 버튼을 눌러서 파일을 컴퓨터에 저장해요.
8. USB 케이블로 마이크로비트를 컴퓨터에 연결해요.
9. 다운로드한 파일을 마이크로비트 드라이브에 복사해요.
10. 코드가 마이크로비트에 올라가면 자동으로 실행돼요.

## 코드 바꿔보기

1. **다른 소리 넣기**:
   - 웃음소리 대신 다른 소리를 선택해보세요.
   
2. **LED 색상 패턴 바꾸기**:
   - 모든 LED가 같은 색이 아니라 무지개처럼 여러 색으로 만들어보세요.

3. **빛이 나는 시간 바꾸기**:
   - 2000 (2초) 대신 다른 숫자를 넣어 빛이 나는 시간을 바꿔보세요.

4. **A 버튼과 B 버튼 기능 추가하기**:
   - A 버튼을 누르면 다른 효과가 나오게 만들어보세요.

## 문제 해결하기

- **LED가 전혀 안 켜져요**: 
  - 네오픽셀 확장기능이 추가되었는지 확인하세요.
  - 전선이 P1 핀에 제대로 연결되었는지 확인하세요.
  
- **흔들어도 반응이 없어요**:
  - 마이크로비트가 잘 작동하는지 확인하세요.
  - 코드가 제대로 업로드 되었는지 확인하세요.
  
- **LED가 이상한 색으로 나와요**:
  - 네오픽셀 전선이 제대로 연결되었는지 확인하세요.
  - 특히 데이터 선이 P1 핀에 제대로 연결되었는지 확인하세요.
