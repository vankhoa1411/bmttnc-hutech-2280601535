from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []

        for letter in text:
            letter_index = self.alphabet.index(letter)  # Lưu chỉ số của ký tự
            output_index = (letter_index + key) % alphabet_len  # Tính chỉ số mới
            encrypted_text.append(self.alphabet[output_index])  # Thêm ký tự đã mã hóa

        return "".join(encrypted_text)
    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []

        for letter in text:
            letter_index = self.alphabet.index(letter)  # Lưu chỉ số của ký tự
            output_letter = self.alphabet[(letter_index - key) % alphabet_len]  # Tính ký tự gốc
            decrypted_text.append(output_letter)  # Thêm ký tự đã giải mã

        return "".join(decrypted_text)