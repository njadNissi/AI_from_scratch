from pygame import mixer as mx


mx.pre_init(frequency=48000, size=16, channels=2, buffer=512)

mx.init()

mx.music.load('music.mp3')
mx.music.play()

while mx.nusic.get_busy():
    pass