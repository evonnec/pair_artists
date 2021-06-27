from artist_pairs import make_artist_pairs, make_dict
from sys import argv

class TestArtistPairs:
    def test_length_of_values_in_dict(self):
        artist_dict = make_dict(
            input_file="./artist_lists_small.txt",
            pair_num=int(50)
            )
        for k, v in artist_dict.items():
            assert len(v) >= int(50)
            
    def test_pairs_in_tuple(self):
        artist_dict = make_dict(
            input_file="./artist_lists_small.txt", 
            pair_num=int(50)
            )
        make_pairs = make_artist_pairs(
            artist_dict, 
            pair_num=int(50)
            )
        test_pair = "Lady Gaga,Rihanna"
        if test_pair in make_pairs:
            return True
        else:
            return False
