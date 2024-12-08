from func import (
    create_email,
    generate_bulk_emails,
    count_keyword_occurrences,
    extract_excerpt,
    identify_mixed_language,
    is_message_palindrome,
    normalize_message_spacing,
    replace_endings_with_newline,
    summarize_feedback,
    capitalize_headers,
    find_top_long_word,
)

def run_all_functions():
    try:
        # Шаг 1
        email = create_email("Здравствуйте", 5, "иван иванов")
        print(email)
        print("")
        # Шаг 2
        print("Генерация рассылки:")
        generate_bulk_emails("Уважаемый клиент,", "Мы ценим ваш выбор!", 2)
        print("")
        # Шаг 3
        feedback = "Доставка была хорошо, но упаковка плохой. Хорошо, что было быстро."
        keyword_count = count_keyword_occurrences(feedback, "хорошо")
        print(f"Ключевое слово встречается {keyword_count} раз(а).")
        print("")
        # Шаг 4
        excerpt = extract_excerpt(feedback, 9, 25)
        print(f"Извлеченный фрагмент: {excerpt}")
        print("")
        # Шаг 5
        example_strings = [
    "СТРОКTE",
    "Мах MаX",
]

        result, count = identify_mixed_language(*example_strings)
        print("Строки с латинскими символами:", result)
        print("Количество слов с латинскими символами:", count)
        print("")

        # Шаг 6
        palindrome_check = is_message_palindrome("А роза упала на лапу Азора")
        print(f"Сообщение палиндром: {palindrome_check}")
        print("")
        # Шаг 7
        normalized_length = normalize_message_spacing("  Это   сообщение  с  пробелами  ")
        print(f"Длина сообщения после нормализации: {normalized_length}")
        print("")
        # Шаг 8
        formatted_text = replace_endings_with_newline(
            "Привет! Как дела? Все хорошо. Спасибо."
        )
        print(f"Форматированный текст:\n{formatted_text}")
        print("")
        # Шаг 9
        summarized = summarize_feedback(feedback)
        print(f"Ключевые слова в отзывах: {summarized}")

        capitalized = capitalize_headers("заголовок письма к клиенту")
        print(f"Заголовок: {capitalized}")

        longest_word = find_top_long_word(feedback)
        print(f"Самое длинное слово: {longest_word}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    run_all_functions()
