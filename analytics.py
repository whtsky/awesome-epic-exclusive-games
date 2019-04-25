#!/usr/bin/env python3

import collections
import csv
import json

publisher = collections.defaultdict(list)
developer = collections.defaultdict(list)

with open("games.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        publisher[row["Publisher(s)"]].append(row["Name"])
        developer[row["Developer(s)"]].append(row["Name"])


def make_output(d):
    output = collections.OrderedDict()
    for name, games in d.items():
        output[name] = {"count": len(games), "games": games}
    return output


with open("publishers.json", "w") as f:
    f.write(json.dumps(make_output(publisher), indent=4))

with open("developers.json", "w") as f:
    f.write(json.dumps(make_output(developer), indent=4))
