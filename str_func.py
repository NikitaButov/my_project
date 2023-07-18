def capitalize_string(input_string):
    # Приводим строку к верхнему регистру
    return input_string.upper()
"""исправлен баг"""

def capitalize_words(input_string):
    """
    переводит первые буквы в верхний регистр
    """
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
