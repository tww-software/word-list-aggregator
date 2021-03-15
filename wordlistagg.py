"""
password list aggregator

take several password list files in a directory
and combine all the unique passwords into one
"""


import argparse
import os


def open_wordlist(path):
    with open(path, 'r', errors='ignore') as wordf:
        passwordlist = []
        for line in wordf:
            passwordlist.append(line)
    return passwordlist


def create_wordlist(wordlist, outpath):
    with open(outpath, 'w') as wordout:
        for line in wordlist:
            wordout.write(line)


def parse_cli_args():
    parser = argparse.ArgumentParser(
        'combine all the unique passwords of several password lists into one')
    parser.add_argument('inputdir', help='directory containing wordlists')
    parser.add_argument('outputfile', help='file to output passwords')
    args = parser.parse_args()
    return args


def main():
    totalpasswords = 0
    bigset = set()
    args = parse_cli_args()
    for textfile in os.listdir(args.inputdir):
        fullpath = os.path.join(args.inputdir, textfile)
        if os.path.isfile(fullpath) and textfile.endswith('.txt'):
            currentlist = open_wordlist(fullpath)
            currentlistlen = len(currentlist)
            totalpasswords += currentlistlen
            print('{} passwords in {}'.format(currentlistlen, textfile))
            bigset.update(currentlist)
    create_wordlist(bigset, args.outputfile)
    print('processed a total of {} passwords'.format(totalpasswords))
    print('{} unique passwords in {}'.format(len(bigset), args.outputfile))


if __name__ == '__main__':
    main()
