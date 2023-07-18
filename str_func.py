def capitalize_string(input_string):
    # Приводим строку к верхнему регистру
    return input_string.upper()


def capitalize_words(input_string):
    """приводит первые буквы в заглавные"""
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)