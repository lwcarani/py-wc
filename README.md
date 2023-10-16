# pywc

## About
wc stands for word count. pywc is my version of the Linux style command line tool named wc. As the name implies, its only use is for counting the number of lines, words, bytes, or characters in the files or directories specified in the input arguments. 

This version is written in python. 

## Instructions
For Windows, create a folder named `Aliases` in your C drive: `C:/Aliases`. Add this folder to PATH. Next, create a batch file that will execute when you call the specified alias. For example, on my machine, I have a batch file named `wc.bat` located at `C:/Aliases`, that contains the following script:

```bat
@echo off
echo.
python C:\...\GitHub\pywc\main.py %*
```

So now, when I type `wc` in the command prompt, this batch file will execute, which in turn, runs the `pywc` Python script. 

## Examples

`pywc` allows you to execute typical Linux-style `wc` commands. Line count for a single file:

```console
C:\> wc test.txt -l
  7145  test.txt
  7145  total
  lines
```

Byte count:

```console
C:\> wc test.txt -c
  342185        test.txt
  342185        total
  bytes
```

Character count:

```console
C:\> wc test.txt -m
  339289        test.txt
  339289        total
  chars
```

And word count:

```console
C:\> wc test.txt -w
  58164 test.txt
  58164 total
  words
```

You can mix and match flags:

```console
C:\> wc test.txt -w -l
  7145  58164   test.txt
  7145  58164   total
  lines words
  
C:\> wc test.txt -w -l -c -m
  7145  58164   339289  342185  test.txt
  7145  58164   339289  342185  total
  lines words   chars   bytes
```

And if you don't pass any flags, you get lines, words, and bytes by default:

```console
C:\> wc test.txt
  7145  58164   342185  test.txt
  7145  58164   342185  total
  lines words   bytes
```

Can pass in any number of files or directories. Can also pass file extensions or directories to ignore. 

## Acknowledgements
Thanks to [John Crickett](https://github.com/JohnCrickett) for the idea from his site, [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-wc)! 