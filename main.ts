input.onGesture(Gesture.Shake, function () {
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.InBackground)
    // 랜덤 색상 생성 (빨강, 초록, 파랑 값을 랜덤으로 지정)
    random_color = neopixel.rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    // 모든 네오픽셀에 랜덤 색상 적용
    strip.showColor(random_color)
    basic.pause(2000)
    strip.clear()
    strip.show()
    basic.pause(200)
})
let random_color = 0
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P1, 8, NeoPixelMode.RGB)
