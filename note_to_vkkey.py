# Jan 16, 2021

# Adam Vert

# VK Codes https://docs.microsoft.com/en-gb/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
win_keys= {
    'Empty':None,
    'ESC' : 0x01,
    '!' : 0x02,
    '1' : 0x02,
    '@' : 0x03,
    '2' : 0x03,
    '#' : 0x04,
    '3' : 0x04,
    '$' : 0x05,
    '4' : 0x05,
    '%' : 0x06,
    '5' : 0x06,
    '^' : 0x07,
    '6' : 0x07,
    '&' : 0x08,
    '7' : 0x08,
    '*' : 0x09,
    '8' : 0x09,
    '(' : 0x0A,
    '9' : 0x0A,
    ')' : 0x0B,
    '0' : 0x0B,
    '_' : 0x0C,
    '-' : 0x0C,
    '+' : 0x0D,
    '=' : 0x0D,
    'BKSP' : 0x0E,
    'TAB' : 0x0F,
    'Q' : 0x10,
    'W' : 0x11,
    'E' : 0x12,
    'R' : 0x13,
    'T' : 0x14,
    'Y' : 0x15,
    'U' : 0x16,
    'I' : 0x17,
    'O' : 0x18,
    'P' : 0x19,
    '{' : 0x1A,
    '[' : 0x1A,
    '}' : 0x1B,
    ']' : 0x1B,
    'ENTER' : 0x1C,
    'CTRL' : 0x1D,
    'A' : 0x1E,
    'S' : 0x1F,
    'D' : 0x20,
    'F' : 0x21,
    'G' : 0x22,
    'H' : 0x23,
    'J' : 0x24,
    'K' : 0x25,
    'L' : 0x26,
    ':' : 0x27,
    ';' : 0x27,
    '"' : 0x28,
    "'" : 0x28,
    " '" : 0x28,
    'TILDE' : 0x29,
    'BACKTICK' : 0x29,
    'LSHIFT' : 0x2A,
    '|' : 0x2B,
    'BSLASH' : 0x2B,
    'Z' : 0x2C,
    'X' : 0x2D,
    'C' : 0x2E,
    'V' : 0x2F,
    'B' : 0x30,
    'N' : 0x31,
    'M' : 0x32,
    '<' : 0x33,
    ',' : 0x33,
    '>' : 0x34,
    '.' : 0x34,
    '?' : 0x35,
    '/' : 0x35,
    'RSHIFT' : 0x36,
    'PRTSC' : 0x37,
    '*' : 0x37,
    'ALT' : 0x38,
    'SPACEBAR' : 0x39,
    'CAPSLOCK' : 0x3A,
    'F1' : 0x3B,
    'F2' : 0x3C,
    'F3' : 0x3D,
    'F4' : 0x3E,
    'F5' : 0x3F,
    'F6' : 0x40,
    'F7' : 0x41,
    'F8' : 0x42,
    'F9' : 0x43,
    'F10' : 0x44,
    'NUMLOCK' : 0x45,
    'SCROLL_LOCK' : 0x46,
    'HOME' : 0x47,
    'NUM7' : 0x47,
    'UP' : 0x48,
    'NUM8' : 0x48,
    'PGUP' : 0x49,
    'NUM9' : 0x49,
    'NUM-' : 0x4A,
    'LEFT' : 0x4B,
    'NUM4' : 0x4B,
    'NUM5' : 0x4C,
    'RIGHT' : 0x4D,
    'NUM6' : 0x4D,
    'NUM+' : 0x4E,
    'END' : 0x4F,
    'NUM1' : 0x4F,
    'DOWN' : 0x50,
    'NUM2' : 0x50,
    'PGDN' : 0x51,
    'NUM3' : 0x51,
    'INS' : 0x52,
    'NUM0' : 0x52,
    'DEL' : 0x53,
    'NUM.' : 0x53,
    'F11' : 0x85,
    'F12' : 0x86,
    'q' : 0x10,
    'w' : 0x11,
    'e' : 0x12,
    'r' : 0x13,
    't' : 0x14,
    'y' : 0x15,
    'u' : 0x16,
    'i' : 0x17,
    'o' : 0x18,
    'p' : 0x19,
    'a' : 0x1E,
    's' : 0x1F,
    'd' : 0x20,
    'f' : 0x21,
    'g' : 0x22,
    'h' : 0x23,
    'j' : 0x24,
    'k' : 0x25,
    'l' : 0x26,
    'z' : 0x2C,
    'x' : 0x2D,
    'c' : 0x2E,
    'v' : 0x2F,
    'b' : 0x30,
    'n' : 0x31,
    'm' : 0x32,
    }

def binding_of_isaac_dict():
    # dict = {36: "RETURN",
    #         37: "ESCAPE",
    #         53:"A",
    #         54: "Q",
    #         55: "S",
    #         56: "W",
    #         57: "D",
    #         58: "E",
    #         77:"LEFT",
    #         79: "DOWN",
    #         80: "UP",
    #         81: "RIGHT"}
    dict = {36: "Return",
            37: "ESC",
            53:"A",
            54: "Q",
            55: "S",
            56: "W",
            57: "D",
            58: "E",
            77:"LEFT",
            79: "DOWN",
            80: "UP",
            81: "RIGHT"}
    return dict

def league_of_legends_dict():
    dict = {63: "1",
            64: "LSHIFT",
            65: "Q",
            66: "A",
            67: "W",
            68: "D",
            69: "E",
            70: "F",
            71: "R",
            72: "2",
            }
    return dict