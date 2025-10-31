# Константа розміру таблиці 
M = 13

# Список вхідних слів  
WORDS = ["НЕ", "КЛАДИ", "ВСІ", "ЯЙЦЯ", "В", "ОДИН", "КОШИК", "ЩОБ", "НЕ", "ВТРАТИТИ", "ВСЕ", "ОДРАЗУ"]

# Словник позицій українських букв
LETTER_POSITIONS = {
    'А':1, 'Б':2, 'В':3, 'Г':4, 'Ґ':5, 'Д':6, 'Е':7, 'Є':8,
    'Ж':9, 'З':10, 'И':11, 'І':12, 'Ї':13, 'Й':14, 'К':15, 'Л':16,
    'М':17, 'Н':18, 'О':19, 'П':20, 'Р':21, 'С':22, 'Т':23, 'У':24,
    'Ф':25, 'Х':26, 'Ц':27, 'Ч':28, 'Ш':29, 'Щ':30, 'Ь':31, 'Ю':32, 'Я':33
}

def hash_division(word: str) -> int:
    """Хеш-функція: h(k) = (сума позицій букв) mod 13."""
    total = 0
    for ch in word:
        total += LETTER_POSITIONS.get(ch, 0)
    return total % M

def build_open_hash_table(words: list, m: int) -> list:
    """Будує хеш-таблицю з ланцюжками."""
    table = [[] for _ in range(m)]
    for w in words:
        h = hash_division(w)
        table[h].append(w)
    return table

def display_hash_table(table: list):
    """Виводить хеш-таблицю у зручному форматі."""
    print("\n--- Результат хешування (Таблиця M=13) ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")

# Виконання:
hash_table = build_open_hash_table(WORDS, M)
display_hash_table(hash_table)
