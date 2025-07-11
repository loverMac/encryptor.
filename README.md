# 🔐 Система шифрования текста

Проект представляет собой программу для шифрования и дешифрования текстовых файлов с использованием уникальных 5-символьных кодов для каждого символа.

## 🌟 Особенности

- **Поддержка языков**: Русский и английский алфавиты (регистро-зависимые)
- **Широкий охват символов**:
  - Все буквы (верхний/нижний регистр)
  - Цифры (0-9)
  - Специальные символы (пробелы, знаки препинания и др.)
- **Стойкое шифрование**: Каждый символ заменяется уникальным 5-символьным кодом
- **Автогенерация ключей**: Коды генерируются случайным образом при каждом запуске
- **Простота использования**: Интуитивно понятный консольный интерфейс

## 🛠 Технологии

- Python 3.7+
- Стандартные библиотеки:
  - `random` для генерации кодов
  - `pathlib` для кросс-платформенной работы с путями
  - `string` для работы с символами

## 🚀 Установка и запуск

1. Убедитесь, что у вас установлен Python 3.7 или новее:
   ```bash
   python --version
