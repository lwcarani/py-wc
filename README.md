# pywc

## About
wc stands for word count. pywc is my version of the Linux style command line tool named wc. As the name implies, its only use is for counting the number of lines, words, bytes, or characters in the files or directories specified in the input arguments. 

This version is written in python. 

## Instructions
For Windows, Set up C:/Aliases folder, create batch file, add to PATH...

```console
C:\> wc test.txt

  7145  58164   342185  test.txt
  7145  58164   342185  total
  lines words   bytes
```

Can pass in any number of files or directories. Can also pass file extensions or directories to ignore. 

## Acknowledgements
Thanks to [John Crickett](https://github.com/JohnCrickett) for the idea from his site, [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-wc)! 