def on_gesture_shake():
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

strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P1, 8, NeoPixelMode.RGB)