def caesar_cipher_ru(text, shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = ''

    for char in text:
        lower_char = char.lower()
        if lower_char in alphabet:
            index = alphabet.find(lower_char)
            new_index = (index + shift) % len(alphabet)
            new_char = alphabet[new_index]

            if char.isupper():
                new_char = new_char.upper()

            result += new_char
        else:
            result += char 

    return result

text = 'Ц пят фт этяым ыт абэь эьыиай, щлощл атом'
shift = 47

decrypted = caesar_cipher_ru(text, -shift)

print('Оригинал:', text)
print('Расшифровано:', decrypted)