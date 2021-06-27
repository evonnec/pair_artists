from artist_pairs import make_artist_pairs, make_dict

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
        test_pair = "Lady Gaga", "Rihanna"
        assert test_pair in make_pairs
    def test_pairs_in_tuple_smaller(self):
        artist_dict = make_dict(
            input_file="./test_artist_lists_small.txt", 
            pair_num=int(3)
            )
        make_pairs = make_artist_pairs(
            artist_dict, 
            pair_num=int(3)
            )
        test_pair = "Coldplay", "Muse"
        test_pair2 = "Green Day", "Muse"
        test_pair3 = "Coldplay", "Green Day"
        test_pair4 = "Muse", "Coldplay"
        test_pair5 = "Muse", "Green Day"
        test_pair6 = "Green Day", "Coldplay"
        assert (test_pair in make_pairs) and (test_pair2 in make_pairs) and (test_pair3 in make_pairs) \
            and (test_pair4 in make_pairs) and (test_pair5 in make_pairs) and (test_pair6 in make_pairs)