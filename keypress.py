import time
import ctypes

# Import the SendInput object
SendInput = ctypes.windll.user32.SendInput

#code obtained from https://github.com/Paradoxis/Windows-Sound-Manager/blob/master/keyboard.py

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBoardInput(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class HardwareInput(ctypes.Structure):
    _fields_ = [
        ("uMsg", ctypes.c_ulong),
        ("wParamL", ctypes.c_short),
        ("wParamH", ctypes.c_ushort)
    ]

class MouseInput(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time",ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class Input_I(ctypes.Union):
    _fields_ = [
        ("ki", KeyBoardInput),
        ("mi", MouseInput),
        ("hi", HardwareInput)
    ]

class Input(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("ii", Input_I)
    ]

VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1
VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MEDIA_STOP = 0xB2

def key_down(keyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBoardInput(keyCode, 0x48, 0, 0, ctypes.pointer(extra))
    x = Input( ctypes.c_ulong(1), ii_ )
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def key_up(keyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBoardInput(keyCode, 0x48, 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def key(key_code, length = 0):    
    key_down(key_code)
    time.sleep(length)
    key_up(key_code)


def volume_up():
    key(VK_VOLUME_UP)

def volume_down():
    key(VK_VOLUME_DOWN)

def next_track():
    key(VK_MEDIA_NEXT_TRACK)

def prev_track():
    key(VK_MEDIA_PREV_TRACK)

def play_pause():
    key(VK_MEDIA_PLAY_PAUSE)

# it is only for testing use only 
def main():
    done = False
    while (not done):
        inp = input("volume up: w   volume down: s  next: d    prev: a     play/pause: p     quit: q\n")

        if inp == 'w':
            volume_up()
            print("volume up")
        if inp == 's':
            volume_down()
            print("volume down")
        if inp == 'd':
            next_track()
            print("next")
        if inp == 'a':
            prev_track()
            print("previous")
        if inp == 'p':
            play_pause()
            print("play/pause")
        if inp == 'q':
            done = True

    print(" -----  quit -----")            


if __name__ == "__main__":
    main()


 

