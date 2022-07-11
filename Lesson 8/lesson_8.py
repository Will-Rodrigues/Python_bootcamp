from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def loop():
    end = False
    while not end:
        direction = input("Type 'encode' to encrypt, type 'decode' to descrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(direction, text, shift)

        finish = input("Want restart the program? Type 'yes' or 'no':\n")
        if finish == 'no':
            end = True    


def caesar(direction, text, shift):
    text_list = []

    for letter in text:
        if letter in alphabet:
            alphabet_index = alphabet.index(letter)
            if direction == 'encode':
                new_index = alphabet_index + shift
                while new_index > 26:
                    new_index -= 26
            elif direction == 'decode':
                new_index = alphabet_index - shift
                while new_index < 0:
                    new_index += 26
            text_list.append(alphabet[new_index])
        else:
            text_list.append(letter)

    final_text = ''.join(text_list)
    print(final_text)


loop()
