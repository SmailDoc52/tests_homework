import pytest 

from get_race_winner import get_race_winner


@pytest.mark.parametrize(
    'hare_distances,turtle_distances,result',
    (
        ([8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3], 'черепаха'),
        ([3, 3, 3, 3, 3, 3, 3], [8, 5, 3, 2, 0, 1, 1], 'заяц'),
        ([0, 6, 1, 2, 8, 0, 3], [8, 5, 3, 2, 0, 1, 1], 'одинаково'),
        ([], [], 'одинаково'),
        ([1], [], 'заяц'),
        ([], [1], 'черепаха'),
    )
)
def test_get_race_winner_returns_winner_race_by_distance(hare_distances, 
                                                         turtle_distances, 
                                                         result):
    assert get_race_winner(hare_distances, turtle_distances) == result