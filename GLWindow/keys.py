'''
    Virtual Key Codes
'''

LBUTTON = 0x01
RBUTTON = 0x02
CANCEL = 0x03
MBUTTON = 0x04
XBUTTON1 = 0x05
XBUTTON2 = 0x06
BACK = 0x08
TAB = 0x09
CLEAR = 0x0C
RETURN = 0x0D
SHIFT = 0x10
CONTROL = 0x11
MENU = 0x12
PAUSE = 0x13
CAPITAL = 0x14
KANA = 0x15
HANGUEL = 0x15
HANGUL = 0x15
JUNJA = 0x17
FINAL = 0x18
HANJA = 0x19
KANJI = 0x19
ESCAPE = 0x1B
CONVERT = 0x1C
NONCONVERT = 0x1D
ACCEPT = 0x1E
MODECHANGE = 0x1F
SPACE = 0x20
PRIOR = 0x21
NEXT = 0x22
END = 0x23
HOME = 0x24
LEFT = 0x25
UP = 0x26
RIGHT = 0x27
DOWN = 0x28
SELECT = 0x29
PRINT = 0x2A
EXECUTE = 0x2B
SNAPSHOT = 0x2C
INSERT = 0x2D
DELETE = 0x2E
HELP = 0x2F
LWIN = 0x5B
RWIN = 0x5C
APPS = 0x5D
SLEEP = 0x5F
NUMPAD0 = 0x60
NUMPAD1 = 0x61
NUMPAD2 = 0x62
NUMPAD3 = 0x63
NUMPAD4 = 0x64
NUMPAD5 = 0x65
NUMPAD6 = 0x66
NUMPAD7 = 0x67
NUMPAD8 = 0x68
NUMPAD9 = 0x69
MULTIPLY = 0x6A
ADD = 0x6B
SEPARATOR = 0x6C
SUBTRACT = 0x6D
DECIMAL = 0x6E
DIVIDE = 0x6F
F1 = 0x70
F2 = 0x71
F3 = 0x72
F4 = 0x73
F5 = 0x74
F6 = 0x75
F7 = 0x76
F8 = 0x77
F9 = 0x78
F10 = 0x79
F11 = 0x7A
F12 = 0x7B
F13 = 0x7C
F14 = 0x7D
F15 = 0x7E
F16 = 0x7F
F17 = 0x80
F18 = 0x81
F19 = 0x82
F20 = 0x83
F21 = 0x84
F22 = 0x85
F23 = 0x86
F24 = 0x87
NUMLOCK = 0x90
SCROLL = 0x91
LSHIFT = 0xA0
RSHIFT = 0xA1
LCONTROL = 0xA2
RCONTROL = 0xA3
LMENU = 0xA4
RMENU = 0xA5
BROWSER_BACK = 0xA6
BROWSER_FORWARD = 0xA7
BROWSER_REFRESH = 0xA8
BROWSER_STOP = 0xA9
BROWSER_SEARCH = 0xAA
BROWSER_FAVORITES = 0xAB
BROWSER_HOME = 0xAC
VOLUME_MUTE = 0xAD
VOLUME_DOWN = 0xAE
VOLUME_UP = 0xAF
MEDIA_NEXT_TRACK = 0xB0
MEDIA_PREV_TRACK = 0xB1
MEDIA_STOP = 0xB2
MEDIA_PLAY_PAUSE = 0xB3
LAUNCH_MAIL = 0xB4
LAUNCH_MEDIA_SELECT = 0xB5
LAUNCH_APP1 = 0xB6
LAUNCH_APP2 = 0xB7
OEM_1 = 0xBA
OEM_PLUS = 0xBB
OEM_COMMA = 0xBC
OEM_MINUS = 0xBD
OEM_PERIOD = 0xBE
OEM_2 = 0xBF
OEM_3 = 0xC0
OEM_4 = 0xDB
OEM_5 = 0xDC
OEM_6 = 0xDD
OEM_7 = 0xDE
OEM_8 = 0xDF
OEM_102 = 0xE2
PROCESSKEY = 0xE5
PACKET = 0xE7
ATTN = 0xF6
CRSEL = 0xF7
EXSEL = 0xF8
EREOF = 0xF9
PLAY = 0xFA
ZOOM = 0xFB
NONAME = 0xFC
PA1 = 0xFD
OEM_CLEAR = 0xFE

KEY_NAME = {
    0x01: 'LBUTTON',
    0x02: 'RBUTTON',
    0x03: 'CANCEL',
    0x04: 'MBUTTON',
    0x05: 'XBUTTON1',
    0x06: 'XBUTTON2',
    0x08: 'BACK',
    0x09: 'TAB',
    0x0C: 'CLEAR',
    0x0D: 'RETURN',
    0x10: 'SHIFT',
    0x11: 'CONTROL',
    0x12: 'MENU',
    0x13: 'PAUSE',
    0x14: 'CAPITAL',
    0x15: 'KANA/HANGUEL/HANGUL',
    0x17: 'JUNJA',
    0x18: 'FINAL',
    0x19: 'HANJA/KANJI',
    0x1B: 'ESCAPE',
    0x1C: 'CONVERT',
    0x1D: 'NONCONVERT',
    0x1E: 'ACCEPT',
    0x1F: 'MODECHANGE',
    0x20: 'SPACE',
    0x21: 'PRIOR',
    0x22: 'NEXT',
    0x23: 'END',
    0x24: 'HOME',
    0x25: 'LEFT',
    0x26: 'UP',
    0x27: 'RIGHT',
    0x28: 'DOWN',
    0x29: 'SELECT',
    0x2A: 'PRINT',
    0x2B: 'EXECUTE',
    0x2C: 'SNAPSHOT',
    0x2D: 'INSERT',
    0x2E: 'DELETE',
    0x2F: 'HELP',
    0x5B: 'LWIN',
    0x5C: 'RWIN',
    0x5D: 'APPS',
    0x5F: 'SLEEP',
    0x60: 'NUMPAD0',
    0x61: 'NUMPAD1',
    0x62: 'NUMPAD2',
    0x63: 'NUMPAD3',
    0x64: 'NUMPAD4',
    0x65: 'NUMPAD5',
    0x66: 'NUMPAD6',
    0x67: 'NUMPAD7',
    0x68: 'NUMPAD8',
    0x69: 'NUMPAD9',
    0x6A: 'MULTIPLY',
    0x6B: 'ADD',
    0x6C: 'SEPARATOR',
    0x6D: 'SUBTRACT',
    0x6E: 'DECIMAL',
    0x6F: 'DIVIDE',
    0x70: 'F1',
    0x71: 'F2',
    0x72: 'F3',
    0x73: 'F4',
    0x74: 'F5',
    0x75: 'F6',
    0x76: 'F7',
    0x77: 'F8',
    0x78: 'F9',
    0x79: 'F10',
    0x7A: 'F11',
    0x7B: 'F12',
    0x7C: 'F13',
    0x7D: 'F14',
    0x7E: 'F15',
    0x7F: 'F16',
    0x80: 'F17',
    0x81: 'F18',
    0x82: 'F19',
    0x83: 'F20',
    0x84: 'F21',
    0x85: 'F22',
    0x86: 'F23',
    0x87: 'F24',
    0x90: 'NUMLOCK',
    0x91: 'SCROLL',
    0xA0: 'LSHIFT',
    0xA1: 'RSHIFT',
    0xA2: 'LCONTROL',
    0xA3: 'RCONTROL',
    0xA4: 'LMENU',
    0xA5: 'RMENU',
    0xA6: 'BROWSER_BACK',
    0xA7: 'BROWSER_FORWARD',
    0xA8: 'BROWSER_REFRESH',
    0xA9: 'BROWSER_STOP',
    0xAA: 'BROWSER_SEARCH',
    0xAB: 'BROWSER_FAVORITES',
    0xAC: 'BROWSER_HOME',
    0xAD: 'VOLUME_MUTE',
    0xAE: 'VOLUME_DOWN',
    0xAF: 'VOLUME_UP',
    0xB0: 'MEDIA_NEXT_TRACK',
    0xB1: 'MEDIA_PREV_TRACK',
    0xB2: 'MEDIA_STOP',
    0xB3: 'MEDIA_PLAY_PAUSE',
    0xB4: 'LAUNCH_MAIL',
    0xB5: 'LAUNCH_MEDIA_SELECT',
    0xB6: 'LAUNCH_APP1',
    0xB7: 'LAUNCH_APP2',
    0xBA: 'OEM_1',
    0xBB: 'OEM_PLUS',
    0xBC: 'OEM_COMMA',
    0xBD: 'OEM_MINUS',
    0xBE: 'OEM_PERIOD',
    0xBF: 'OEM_2',
    0xC0: 'OEM_3',
    0xDB: 'OEM_4',
    0xDC: 'OEM_5',
    0xDD: 'OEM_6',
    0xDE: 'OEM_7',
    0xDF: 'OEM_8',
    0xE2: 'OEM_102',
    0xE5: 'PROCESSKEY',
    0xE7: 'PACKET',
    0xF6: 'ATTN',
    0xF7: 'CRSEL',
    0xF8: 'EXSEL',
    0xF9: 'EREOF',
    0xFA: 'PLAY',
    0xFB: 'ZOOM',
    0xFC: 'NONAME',
    0xFD: 'PA1',
    0xFE: 'OEM_CLEAR',
}
