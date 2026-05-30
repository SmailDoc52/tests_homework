import pytest 

from winners_check import winners_check


@pytest.mark.parametrize(
    'original_list,result_list,len_list',
    (
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 6, 9], 3),
        ([321, 123], [], 0),
        ([4, 5, 6], [6], 1),
        ([], [], 0),
    )
)
def test_winners_check_returns_checks_and_total_count(original_list, 
                                                result_list, 
                                                len_list):
    assert winners_check(original_list) == (result_list, len_list)