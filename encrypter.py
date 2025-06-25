import os
import sys
import random
import string
from pathlib import Path

class EncryptionSystem:
    def __init__(self):
        self.chars_to_encrypt = (
            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' +
            'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' +
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
            'abcdefghijklmnopqrstuvwxyz' +
            '0123456789' +
            ' .,!?;:-_+=*/\\@#$%^&()[]{}<>"\'' +
            '№~`|'
        )

        self.encrypt_dict, self.decrypt_dict = self.generate_dictionaries()  
    
    def generate_dictionaries(self):
        encrypt_dict = {}
        decrypt_dict = {}
        used_codes = set()

        code_chars = string.ascii_letters + string.digits + '!@#$%^&*()_+-=[]{};:,./<>?'


        for char in self.chars_to_encrypt:
            while True:
                code = ''.join(random.choices(code_chars, k=5))   
                if code not in used_codes:
                    encrypt_dict[char] = code
                    decrypt_dict[code] = char
                    used_codes.add(code)
                    break

        return encrypt_dict, decrypt_dict
    
    def encrypt_file(self, input_path, output_path):
        try:
            with open(input_path, 'r', encoding='utf-8') as f:   
                content = f.read()
            
            encrypted = []
            
            for char in content:
                encrypted.append(self.encrypt_dict.get(char, char))
            
            with open(output_path, 'w', encoding='utf-8') as f: 
                f.write(''.join(encrypted))
            
            print(f"Файл успешно зашифрован и сохранен как {output_path}")
            return True

        except Exception as e:
            print(f"Ошибка при шифровании: {e}")
            return False
    
    def decrypt_file(self, input_path, output_path):
        try:
            with open(input_path, 'r', encoding='utf-8') as f: 
                content = f.read()

            decrypted = []
            i = 0

            while i < len(content):
                if i + 5 <= len(content):
                    code = content[i:i+5]
                    
                    if code in self.decrypt_dict:
                        decrypted.append(self.decrypt_dict[code])
                        
                        i += 5
                        continue
                decrypted.append(content[i])
                i += 1

            with open(output_path, 'w', encoding='utf-8') as f: 
                f.write(''.join(decrypted))

            print(f"Файл успешно расшифрован и сохранен как {output_path}")
            return True
        except Exception as e:
            print(f"Ошибка при дешифровании: {e}")
            return False

def main():
    print("=== Система шифрования ===") 
    print("1. Зашифровать файл")
    print("2. Расшифровать файл")
    choice = input("Выберите действие (1/2): ")

    if choice not in ('1', '2'):
        print("Неверный выбор")  
        return

    input_file = input("Введите путь к исходному файлу: ")
    if not os.path.exists(input_file):
        print("Файл не найден")
        return

    input_path = Path(input_file)

    if choice == '1':
        output_file = input_path.stem + "_encrypted" + input_path.suffix
    
    else:
        output_file = input_path.stem + "_decrypted" + input_path.suffix

    cipher = EncryptionSystem()

    if choice == '1':
        cipher.encrypt_file(input_file, output_file)

    else:
        cipher.decrypt_file(input_file, output_file)

if __name__ == "__main__":
    main()