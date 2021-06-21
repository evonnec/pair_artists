#!/usr/bin/env python

from csv import reader, writer
from typing import List
from collections import defaultdict
from sys import argv

    ## open the csv file, 
    ## for each line, add the line number to a defaultdict(set) in which the artist is the key
    ## the lists on which the artist appears are numbered in a set (which is the value of the defaultdict)
    ## setify the intersection between the first artist and every other artist in which the length >= 50 
    ## since the artists both have to intersect on 50 lists, reduce the dict if the len(values) < 50
    ## before even making pairs. This is to speed up run time for the next function.
    ## make the artist pairs such that we only add the to the list of tuples if
    ## there are fifty intersection values between artists.
    ## deconstruct that list of tuples and place in a csv
    ## each function does one thing except the first which opens the input file and 
    ## loads them into a data structure we can use


def _make_dict(input_file: str) -> None:
    with open(input_file, mode='r', newline='') as input_data:
        csvreader = reader(input_data, delimiter='\n')
        output_dict = defaultdict(set)
        line_count = 1
        for line in csvreader:
            artist_str = "('%s')" % "','".join(line)
            for artist in artist_str.split(','):
                output_dict[artist].add(line_count)
            line_count += 1
        reduced_output_dict = defaultdict(set, {k: v for k, v in output_dict.items() if len(v) >= 50})
        return reduced_output_dict

def _make_artist_pairs(potential_pairs: defaultdict(set)) -> List[tuple]:
    pair_tuple = []
    for k, v in potential_pairs.items():
        for key, value in potential_pairs.items():
            if key != k and len(v.intersection(value)) >= 50:
                pair_tuple.append((k, key))
    return pair_tuple

def _write_tuple(output_file: str, pairs: List[tuple]) -> None:
    with open(output_file, mode='w', newline='') as output_data_file:
        _ = writer(output_data_file, delimiter='\n')
        for pair in pairs:
            line = ",".join(pair) + "\n"
            output_data_file.write(line)

def pair_artists(artists_input_file: str, artists_output_file: str) -> None:
    artist_dict = _make_dict(artists_input_file)
    artist_pairs = _make_artist_pairs(artist_dict)
    _write_tuple(artists_output_file, artist_pairs)

if __name__ == "__main__":
    pair_artists(artists_input_file="./" + argv[1] + ".txt", artists_output_file="./" + argv[2] + ".csv")