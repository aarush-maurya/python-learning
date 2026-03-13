def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    characters = 'abcdefghijklmnopqrstuvwxyz1234567890'

    if not encrypt:
        shift = - shift
    
    shifted_characters = characters[shift:] + characters[:shift]
    translation_table = str.maketrans(characters + characters.upper(), shifted_characters + shifted_characters.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)