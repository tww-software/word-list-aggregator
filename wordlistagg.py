"""
password list aggregator

take several password list files in a directory
and combine all the unique passwords into one
"""


import argparse
import os


def open_wordlist(path):
    """
    open a wordlist

    Note:
        a wordlist should be a text document with one word per line

    Args:
        path(str): full path to the wordlist

    Returns:
        passwordlist(list): list of all the words (as strings) in the wordlist
    """
    with open(path, 'r', errors='ignore') as wordf:
        passwordlist = []
        for line in wordf:
            passwordlist.append(line)
    return passwordlist


def create_wordlist(wordlist, outpath):
    """
    create our own wordlist
    write each word on a new line in a text file

    Args:
        wordlist(list): list of strings (words) to write to file
        outpath(str): full path to write wordlist to
    """
    with open(outpath, 'w') as wordout:
        for line in wordlist:
            wordout.write(line)


def parse_cli_args():
    """
    parse arguments off the command line

    Returns:
        args(argparse.Namespace): the CLI arguments
    """
    parser = argparse.ArgumentParser(
        'combine all the unique passwords of several password lists into one')
    parser.add_argument('inputdir', help='directory containing wordlists')
    parser.add_argument('outputfile', help='file to output passwords')
    args = parser.parse_args()
    return args


def main():
    """
    main program code
    """
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
