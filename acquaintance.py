def acquaintance(boys: list, girls: list):
    result = ""
    boys.sort()
    girls.sort()
    
    if len(boys) == len(girls):
        for boy, girl in zip(boys, girls):
           result += f'{boy} и {girl}, '
        result = result[:-2]
    else:
        result = "Кто-то может остаться без пары!"
    return result


if __name__ == '__main__':
    # Этот код менять не нужно
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    result = acquaintance(boys, girls)
    assert result == (
        "Alex и Emma, Arthur и Kate, "
        "John и Kira, Peter и Liza, "
        "Richard и Trisha"
        ), f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")

    boys = ['Peter', 'Alex', 'John', 'Arthur']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
    result = acquaintance(boys, girls)
    assert result == (
        "Кто-то может остаться без пары!"
        ), f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")

    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma']
    result = acquaintance(boys, girls)
    assert result == (
        "Кто-то может остаться без пары!"
        ), f"Знакомство не удалось: {result}"
    print(f"Результат знакомства: {result}")
