mors = {
    "a": "•–",
    "b": "–•••",
    "c": "–•–•",
    "d": "–••",
    "e": "•",
    "f": "••–•",
    "g": "––•",
    "Ğ": "––•",
    "h": "••••",
    "ı": "••",
    "i": "••",
    "j": "•–––",
    "k": "–•–",
    "l": "•–••",
    "m": "––",
    "n": "–•",
    "o": "–––",
    "p": "•––•",
    "q": "––•–",
    "r": "•–•",
    "s": "•••",
    "t": "–",
    "u": "••–",
    "v": "•••–",
    "w": "•––",
    "x": "–••–",
    "y": "–•––",
    "z": "––••",
    "ö": "–––•",
    "ü": "••––",
    "ç": "––––",
    "0": "–––––",
    "1": "•––––",
    "2": "••–––",
    "3": "•••––",
    "4": "••••–",
    "5": "•••••",
    "6": "–••••",
    "7": "––•••",
    "8": "–––••",
    "9": "––––•",
    ".": "•–•–•–",
    ",": "––••––",
    "?": "••––••",
    "-": "––––•",
    "/": "–••–•",
    " ": " ",
}

text = input("Enter text:").lower()

mors_code = ""

for letters in text:
    mors_code = mors_code + mors[lower_letter] + " "

print(mors_code)