import pytest 

from acquaintance import acquaintance


@pytest.mark.parametrize(
    'boys_list,girls_list,result',
    (
        (['Peter', 'Alex', 'John', 'Arthur', 'Richard'], 
         ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'], 
         "Alex и Emma, Arthur и Kate, " 
         "John и Kira, Peter и Liza, "
         "Richard и Trisha"),
        (['Peter', 'Alex', 'John', 'Arthur'], 
         ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'], 
         "Кто-то может остаться без пары!"),
        (['Peter', 'Alex', 'John', 'Arthur', 'Richard'], 
         ['Kate', 'Liza', 'Kira', 'Emma'], 
         "Кто-то может остаться без пары!"),
        ([], 
         [], 
         ""),
    )
)
def test_acquaintance_returns_sorted_pairs_or_warning_message(boys_list, 
                                                              girls_list, 
                                                              result):
    assert acquaintance(boys_list, girls_list) == result
        