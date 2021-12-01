"""
This fulfills the spec, but also allows
for an arbitrary number of teams.

Adil Hanney 8/11/2021
"""

from os import listdir, path
from argparse import ArgumentParser, Namespace

from typing import Dict, List

SCORES: Dict[str, int] = {
    "t": 5,  # Try
    "c": 2,  # Goal kick
    "p": 3,  # Penalty
    "d": 3,  # Drop goal
}


def getArgs() -> (str, str):
    argParser: ArgumentParser = ArgumentParser()
    argParser.add_argument("input_folder")
    argParser.add_argument("output_folder")
    args: Namespace = argParser.parse_args()
    return args.input_folder, args.output_folder


# This restricts the number of teams (solely to match the expected output)
# Set to minus one to disable the limit
TEAMS_LIMIT: int = 2
# TEAMS_LIMIT: int = -1


if __name__ == "__main__":
    input_folder, output_folder = getArgs()

    for filename in listdir(input_folder):
        scores: List[int] = [0 for i in range(TEAMS_LIMIT)]

        scoreFeed: str
        with open(path.join(input_folder, filename)) as input_file:
            scoreFeed = input_file.read().strip()

        while len(scoreFeed):
            # scoreFeed begins with "T{N}{a}" where {N} is the team number and {a} is the score type
            team: int = int(scoreFeed[1])
            score: int = SCORES[scoreFeed[2]]
            scoreFeed = scoreFeed[3:]  # cut out the current triplet

            while len(scores) < team and TEAMS_LIMIT < 0:
                scores.append(0)

            scores[team - 1] += score

        filename = filename.rsplit(".", 1)[0] + "_n58949ah.txt"  # username needs to be in output filename
        with open(path.join(output_folder, filename), "w") as output_file:
            output_file.write(":".join(str(n) for n in scores))
