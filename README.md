# Word List Aggregator

Designed to take several password list files in a directory and combine all the unique passwords into one wordlist file.
Very useful if you have many wordlists and credential dumps, but want to get rid of any duplicate passwords.

## Usage
```
python3 wordlistagg.py <inputdir> <outputfile>
```
inputdir = the directory full of wordlists (wordlists must be in the root of this directory)
outputfile = the file path to write the new super wordlist to.

## Disclaimer
Do not use for illegal purposes. I do not accept any responsibility for any harm caused by using these scripts.

## Licence

MIT License

Copyright (c) 2021 Thomas W Whittam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
