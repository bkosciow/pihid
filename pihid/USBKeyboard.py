from .USBCapability import Capability

DESCRIPTOR = [
    0x05, 0x01,  # USAGE_PAGE (Generic Desktop)
    0x09, 0x06,  # USAGE (Keyboard)
    0xa1, 0x01,  # COLLECTION (Application)
    None, None,  #  REPORT_ID ()
    0x05, 0x07,  # USAGE_PAGE (Keyboard)
    0x19, 0xe0,  # USAGE_MINIMUM (Keyboard LeftControl)
    0x29, 0xe7,  # USAGE_MAXIMUM (Keyboard Right GUI)
    0x15, 0x00,  # LOGICAL_MINIMUM (0)
    0x25, 0x01,  # LOGICAL_MAXIMUM (1)
    0x75, 0x01,  # REPORT_SIZE (1)
    0x95, 0x08,  # REPORT_COUNT (8)
    0x81, 0x02,  # INPUT (Data,Var,Abs)
    0x95, 0x01,  # REPORT_COUNT (1)
    0x75, 0x08,  # REPORT_SIZE (8)
    0x81, 0x01,  # INPUT (Cnst,Var,Abs) // 0x03
    0x95, 0x05,
    0x75, 0x01,
    0x05, 0x08,
    0x19, 0x01,
    0x29, 0x05,
    0x91, 0x02,
    0x95, 0x01,
    0x75, 0x03,
    0x91, 0x01,  # 0x03
    0x95, 0x06,  # REPORT_COUNT (6)
    0x75, 0x08,  # REPORT_SIZE (8)
    0x15, 0x00,  # LOGICAL_MINIMUM (0)
    0x25, 0x65,  # LOGICAL_MAXIMUM (101)
    0x05, 0x07,  # USAGE_PAGE (Keyboard)
    0x19, 0x00,  # USAGE_MINIMUM (Reserved (no event indicated))
    0x29, 0x65,  # USAGE_MAXIMUM (Keyboard Application)
    0x81, 0x00,  # INPUT (Data,Ary,Abs)
    0xc0,
]

MOD_NONE = 0
MOD_LCTRL = 0x01
MOD_LSHIFT = 0x02
MOD_LALT = 0x04
MOD_LSUPER = 0x08
MOD_RCTRL = 0x10
MOD_RSHIFT = 0x20
MOD_RALT = 0x40
MOD_RSUPER = 0x80

KEY_a = [MOD_NONE, 0x04]
KEY_A = [MOD_LSHIFT, 0x04]
KEY_b = [MOD_NONE, 0x05]
KEY_B = [MOD_LSHIFT, 0x05]
KEY_c = [MOD_NONE, 0x06]
KEY_C = [MOD_LSHIFT, 0x06]
KEY_d = [MOD_NONE, 0x07]
KEY_D = [MOD_LSHIFT, 0x07]
KEY_e = [MOD_NONE, 0x08 ]
KEY_E = [MOD_LSHIFT, 0x08 ]
KEY_f = [MOD_NONE, 0x09 ]
KEY_F = [MOD_LSHIFT, 0x09 ]
KEY_g = [MOD_NONE, 0x0a ]
KEY_G = [MOD_LSHIFT, 0x0a ]
KEY_h = [MOD_NONE, 0x0b ]
KEY_H = [MOD_LSHIFT, 0x0b ]
KEY_i = [MOD_NONE, 0x0c ]
KEY_I = [MOD_LSHIFT, 0x0c ]
KEY_j = [MOD_NONE, 0x0d ]
KEY_J = [MOD_LSHIFT, 0x0d ]
KEY_k = [MOD_NONE, 0x0e ]
KEY_K = [MOD_LSHIFT, 0x0e ]
KEY_l = [MOD_NONE, 0x0f ]
KEY_L = [MOD_LSHIFT, 0x0f ]
KEY_m = [MOD_NONE, 0x10 ]
KEY_M = [MOD_LSHIFT, 0x10 ]
KEY_n = [MOD_NONE, 0x11 ]
KEY_N = [MOD_LSHIFT, 0x11 ]
KEY_o = [MOD_NONE, 0x12 ]
KEY_O = [MOD_LSHIFT, 0x12 ]
KEY_p = [MOD_NONE, 0x13 ]
KEY_P = [MOD_LSHIFT, 0x13 ]
KEY_q = [MOD_NONE, 0x14 ]
KEY_Q = [MOD_LSHIFT, 0x14 ]
KEY_r = [MOD_NONE, 0x15 ]
KEY_R = [MOD_LSHIFT, 0x15 ]
KEY_s = [MOD_NONE, 0x16 ]
KEY_S = [MOD_LSHIFT, 0x16 ]
KEY_t = [MOD_NONE, 0x17 ]
KEY_T = [MOD_LSHIFT, 0x17 ]
KEY_u = [MOD_NONE, 0x18 ]
KEY_U = [MOD_LSHIFT, 0x18 ]
KEY_v = [MOD_NONE, 0x19 ]
KEY_V = [MOD_LSHIFT, 0x19 ]
KEY_x = [MOD_NONE, 0x1b ]
KEY_X = [MOD_LSHIFT, 0x1b ]
KEY_y = [MOD_NONE, 0x1c ]
KEY_Y = [MOD_LSHIFT, 0x1c ]
KEY_z = [MOD_NONE, 0x1d ]
KEY_Z = [MOD_LSHIFT, 0x1d ]
KEY_w = [MOD_NONE, 0x1a ]
KEY_W = [MOD_LSHIFT, 0x1a ]

KEY_1 = [MOD_NONE, 0x1e]
KEY_2 = [MOD_NONE, 0x1f]
KEY_3 = [MOD_NONE, 0x20]
KEY_4 = [MOD_NONE, 0x21]
KEY_5 = [MOD_NONE, 0x22]
KEY_6 = [MOD_NONE, 0x23]
KEY_7 = [MOD_NONE, 0x24]
KEY_8 = [MOD_NONE, 0x25]
KEY_9 = [MOD_NONE, 0x26]
KEY_0 = [MOD_NONE, 0x27]
KEY_EXCLAMATION = [MOD_LSHIFT, 0x1e]  # !
KEY_AT = [MOD_LSHIFT, 0x1f]  # @
KEY_HASH = [MOD_LSHIFT, 0x20]  # #
KEY_DOLLAR = [MOD_LSHIFT, 0x21]  # $
KEY_PERCENTAGE = [MOD_LSHIFT, 0x22]  # %
KEY_CARET = [MOD_LSHIFT, 0x23]  # ^
KEY_AMPERSAND = [MOD_LSHIFT, 0x24]  # &
KEY_ASTERISK = [MOD_LSHIFT, 0x25]  # *
KEY_PARENTHESES_OPEN = [MOD_LSHIFT, 0x26]  # (
KEY_PARENTHESES_CLOSE = [MOD_LSHIFT, 0x27]  # )

KEY_ENTER = [MOD_NONE, 0x28]  # ENTER
KEY_ESC = [MOD_NONE, 0x29]  # ESCAPE
KEY_BACKSPACE = [MOD_NONE, 0x2a]  # Backspace
KEY_TAB = [MOD_NONE, 0x2b]  # Tab
KEY_SPACE = [MOD_NONE, 0x2c]  # Spacebar
KEY_MINUS = [MOD_NONE, 0x2d]  # -
KEY_EQUAL = [MOD_NONE, 0x2e]  # =
KEY_BRACKETS_OPEN = [MOD_NONE, 0x2f]  # [
KEY_BRACKETS_CLOSE = [MOD_NONE, 0x30]  # ]
KEY_BACKSLASH = [MOD_NONE, 0x31]  # \
#KEY_HASH = [MOD_NONE, 0x32]  # #

#define KEY_SEMICOLON 0x33 // Keyboard ; and :
#define KEY_APOSTROPHE 0x34 // Keyboard ' and "
#define KEY_GRAVE 0x35 // Keyboard ` and ~
#define KEY_COMMA 0x36 // Keyboard , and <
#define KEY_DOT 0x37 // Keyboard . and >
#define KEY_SLASH 0x38 // Keyboard / and ?
#define KEY_CAPSLOCK 0x39 // Keyboard Caps Lock

KEY_UNDERSCORE = [MOD_LSHIFT, 0x2d]  # _
KEY_PLUS = [MOD_LSHIFT, 0x2e]  # +
KEY_BRACES_OPEN = [MOD_LSHIFT, 0x2f]  # {
KEY_BRACES_CLOSE = [MOD_LSHIFT, 0x30]  # }
KEY_PIPE = [MOD_LSHIFT, 0x31]  # |
KEY_TILDE = [MOD_LSHIFT, 0x32]  # ~



KEYS = {
    'a': KEY_a,
    'A': KEY_A,
    'b': KEY_b,
    'B': KEY_B,
    'c': KEY_c,
    'C': KEY_C,
    'd': KEY_d,
    'D': KEY_D,
    'e': KEY_e,
    'E': KEY_E,
    'f': KEY_f,
    'F': KEY_F,
    'g': KEY_g,
    'G': KEY_G,
    'h': KEY_h,
    'H': KEY_H,
    'i': KEY_i,
    'I': KEY_I,
    'j': KEY_j,
    'J': KEY_J,
    'k': KEY_k,
    'K': KEY_K,
    'l': KEY_l,
    'L': KEY_L,
    'm': KEY_m,
    'M': KEY_M,
    'n': KEY_n,
    'N': KEY_N,
    'o': KEY_o,
    'O': KEY_O,
    'p': KEY_p,
    'P': KEY_P,
    'q': KEY_q,
    'Q': KEY_Q,
    'r': KEY_r,
    'R': KEY_R,
    's': KEY_s,
    'S': KEY_S,
    't': KEY_t,
    'T': KEY_T,
    'u': KEY_u,
    'U': KEY_U,
    'v': KEY_v,
    'V': KEY_V,
    'x': KEY_x,
    'X': KEY_X,
    'y': KEY_y,
    'Y': KEY_Y,
    'z': KEY_z,
    'Z': KEY_Z,
    'w': KEY_w,
    'W': KEY_W,

    '1': KEY_1,
    '2': KEY_2,
    '3': KEY_3,
    '4': KEY_4,
    '5': KEY_5,
    '6': KEY_6,
    '7': KEY_7,
    '8': KEY_8,
    '9': KEY_9,
    '0': KEY_0,
    '!': KEY_EXCLAMATION,
    '@': KEY_AT,
    '#': KEY_HASH,
    '$': KEY_DOLLAR,
    '%': KEY_PERCENTAGE,
    '^': KEY_CARET,
    '&': KEY_AMPERSAND,
    '*': KEY_ASTERISK,
    '(': KEY_PARENTHESES_OPEN,
    ')': KEY_PARENTHESES_CLOSE,

    '\n': KEY_ENTER,
    '\t': KEY_TAB,
    ' ': KEY_SPACE,
    '-': KEY_MINUS,
    '_': KEY_UNDERSCORE,
    '=': KEY_EQUAL,
    '+': KEY_PLUS,
    '[': KEY_BRACKETS_OPEN,
    '{': KEY_BRACES_OPEN,
    ']': KEY_BRACKETS_CLOSE,
    '}': KEY_BRACES_CLOSE,
    '\\': KEY_BACKSLASH,
    '|': KEY_PIPE,
    '~': KEY_TILDE,



}


class Keyboard(Capability):

    def get_descriptor(self):
        return DESCRIPTOR

    def press(self, key):
        pass
