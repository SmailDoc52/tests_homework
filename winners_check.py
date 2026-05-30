def winners_check(receipts: list):
    result = []
    for count, check in enumerate(receipts, start=1):
        if count % 3 == 0:
            result.append(check)
        
    return result, len(result)


if __name__ == '__main__':
    result, count = winners_check([123, 145, 346, 246, 235, 166, 112, 351, 436])
    assert result == [346, 166, 436], f"Список чеков неверный: {result}"
    assert count == 3, f"Количество чеков неверное: {count}"
    print(result)
    print(count)
    result, count = winners_check([123, 145])
    assert result == [], f"Список чеков неверный: {result}"
    assert count == 0, f"Количество чеков неверное: {count}"
    print(result)
    print(count)
