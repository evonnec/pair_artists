#!/usr/bin/env python

from csv import reader, writer
from typing import List, Tuple, DefaultDict, Set
from collections import defaultdict
from sys import argv

    ## open the csv file, 
    ## for each line, add the line number to a defaultdict(set) in which the artist is the key
    ## the lists on which the artist appears are numbered in a set (which is the value of the defaultdict)
    ## setify the intersection between the first artist and every other artist in which the length >= 50/
    ## since the artists both have to intersect on 50 lists, reduce the dict if the len(values) < 50
    ## before even making pairs, i.e. we throw out pairs. This is to speed up run time for the next function, 
    ## We make the artist pairs such that we only add them to the list of tuples if
    ## there are 50 intersection values between artists. The number 50 is configurable at the command line
    ## for extensibility of the codebase.
    ## The next functions deconstruct that list of tuples and place in a csv with a comma delimiter and newline.
    ## Each function does one thing except the first which opens the input file and 
    ## loads them into a data structure we can use. This allows for clean code.
    ## I use mypy --strict to enforce types as input and output here, but in test_artist_pairs.py just mypy


def make_dict(
    input_file: str, 
    pair_num: int
    ) -> DefaultDict[str, Set[int]]:
    with open(input_file, mode='r', newline='') as input_data:
        csvreader = reader(input_data, delimiter='\n')
        output_dict = defaultdict(set)
        line_count = 1
        for line in csvreader:
            artist_str = "('%s')" % "','".join(line)
            for artist in artist_str.split(','):
                output_dict[artist].add(line_count)
            line_count += 1
        reduced_output_dict = defaultdict(set, {k: v for k, v in output_dict.items() if len(v) >= pair_num})
        return reduced_output_dict

def make_artist_pairs(
    potential_pairs: DefaultDict[str, Set[int]], 
    pair_num: int
    ) -> List[Tuple[str, str]]:
    pair_tuple = []
    for k, v in potential_pairs.items():
        for key, value in potential_pairs.items():
            if key != k and len(v.intersection(value)) >= pair_num:
                pair_tuple.append((k, key))
    return pair_tuple

def write_tuple(
    output_file: str, 
    pairs: List[Tuple[str, str]]
    ) -> None:
    with open(output_file, mode='w', newline='') as output_data_file:
        _ = writer(output_data_file, delimiter='\n')
        for pair in pairs:
            line = ",".join(pair) + "\n"
            output_data_file.write(line)

def pair_artists(
    artists_input_file: str, 
    artists_output_file: str, 
    pair_num: int
    ) -> None:
    artist_dict = make_dict(artists_input_file, pair_num)
    artist_pairs = make_artist_pairs(artist_dict, pair_num)
    write_tuple(artists_output_file, artist_pairs)

if __name__ == "__main__":
    pair_artists(
        artists_input_file="./" + argv[1] + ".txt", 
        artists_output_file="./" + argv[2] + ".csv", 
        pair_num = int(argv[3])   
    )