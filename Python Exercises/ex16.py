#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    dict = {}
    result = []
    fp = open(filename, 'r')
    for line in fp:
        if line.find('Popularity in') != -1:
            ind = line.find('Popularity in')
            year = line[ind + 14:ind + 18]
            result.append(year)
        elif line.find('"right"') != -1:
            s1 = line.replace('</td>', ' ')
            s2 = s1.replace('<td>', ' ')
            s3 = s2.replace(s2[0:18], '')
            s4 = s3.strip()
            s = s4.split('  ')
            # next is handling for names that appear more than once
            # only keep entry with highest rank
            if s[1] in dict:
                value1 = int(s[0]) if int(s[0]) < dict[s[1]] else dict[s[1]]
                value2 = int(s[0])
            elif s[2] in dict:
                value2 = int(s[0]) if int(s[0]) < dict[s[2]] else dict[s[2]]
                value1 = int(s[0])
            else:
                value1 = int(s[0])
                value2 = int(s[0])
            dict[s[1]] = value1
            dict[s[2]] = value2
    fp.close()
    names = dict.keys()
    snames = sorted(names)
    for num in snames:
        namenum = num + ' ' + str(dict[num])
        result.append(namenum)
    return result


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    for filename in args:
        res = extract_names(filename)
    outname = 'summary_' + res[0] + '.txt'
    if summary:
        out = open(outname, 'w')
        for val in res:
            out.write(val + '\n')
        out.close
    else:
        for val in res:
            print
            val


if __name__ == '__main__':
    main()
