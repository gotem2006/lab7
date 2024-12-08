# Шаг 1
def create_email(greeting, item_count, user_name):
    
    def format_name(name):
        return name.title()

    email_text = (
        f"{greeting}, {format_name(user_name)}!\n"
        f"Спасибо за ваш заказ. Вы заказали {item_count + 1} товаров.\n"
        "Мы свяжемся с вами в ближайшее время."
    )
    return email_text

# Шаг 2
def generate_bulk_emails(base_text, personalization_text, count):
    """
    Генерирует текст рассылки для нескольких получателей.
    """
    combined_text = f"{base_text}\n{personalization_text}\n"
    emails = (combined_text for _ in range(count))
    for email in emails:
        print(email)

# Шаг 3
def count_keyword_occurrences(feedback, keyword):
    """
    Считает количество упоминаний ключевого слова в отзывах.
    """
    return feedback.lower().count(keyword.lower())

# Шаг 4
def extract_excerpt(message, start, end):
    """Извлекает часть сообщения по индексам (в одну строку)."""
    return message[start:end] if 0 < start < len(message) - 1 and 0 < end < len(message) - 1 and start < end else None


# Шаг 5
def identify_mixed_language(*strings):
    """
    Ищет строки, содержащие слова с латинскими буквами, визуально схожими с кириллическими.
    
    :param strings: Произвольное количество строк.
    :return: Список строк с латинскими символами и количество таких слов.
    """
    # Набор латинских букв, схожих с кириллическими
    visually_identical_latin = set("aеoсpxymtrhnk")
    flagged_texts = []
    flagged_word_count = 0

    for text in strings:
        words = text.split()
        for word in words:
            if any(char.lower() in visually_identical_latin for char in word):
                flagged_texts.append(word)
                flagged_word_count += 1
                break  # Переходим к следующей строке, если нашли в текущей

    return flagged_texts, flagged_word_count

 
 
# Шаг 6
def is_message_palindrome(message):
    """
    Проверяет, является ли текст сообщения палиндромом.
    """
    normalized_message = ''.join(filter(str.isalnum, message)).lower()
    return normalized_message == normalized_message[::-1]

# Шаг 7
def normalize_message_spacing(message):
    """
    Удаляет лишние пробелы из текста сообщения и возвращает его длину.
    """
    return len(' '.join(message.split()))

# Шаг 8
def replace_endings_with_newline(text):
    """
    Преобразует текст с заменой окончаний предложений на символы переноса строки.
    """
    import re
    return re.sub(r'[.!?]', '\n', text)

# Шаг 9.1
def summarize_feedback(feedback):
    """
    Суммирует отзывы, оставляя только ключевые слова.
    """
    keywords = ["хорошо", "быстро", "плохо", "доставка", "товар"]
    return ', '.join([word for word in feedback.split() if word.lower() in keywords])

# Шаг 9.2
def capitalize_headers(text):
    """
    Делает каждое слово заглавным в заголовках отзывов или темах писем.
    """
    return text.title()

# Шаг 9.3
def find_top_long_word(review):
    """
    Находит самое длинное слово в отзыве.
    """
    words = review.split()
    return max(words, key=len) if words else ''
