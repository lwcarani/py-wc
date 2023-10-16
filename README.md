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

You can also mix and match flags:

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

You can also pass in more than one file:

```console
C:\> wc test.txt test2.txt
  7145  58164   342185  test.txt
  26    136     814     test2.txt
  7171  58300   342999  total
  lines words   bytes
```

Or, you can pass in a directory:

```console
C:\> wc test_text
  7145  58164   342185  test_text\test.txt
  26    136     814     test_text\test2.txt
  7171  58300   342999  total
  lines words   bytes
```

Or multiple directories:

```console
C:\> wc test_text test_text2
  44    121     1453    test_text\graph.py
  21    47      568     test_text\node.py
  7145  58164   342185  test_text\test.txt
  26    136     814     test_text\test2.txt
  7145  58164   342185  test_text2\test.txt
  26    136     814     test_text2\test2.txt
  14407 116768  688019  total
  lines words   bytes
```

Finally, you can specify file extensions to ignore:

```console
C:\> wc test_text test_text2 -i .py
  7145  58164   342185  test_text\test.txt
  26    136     814     test_text\test2.txt
  7145  58164   342185  test_text2\test.txt
  26    136     814     test_text2\test2.txt
  14342 116600  685998  total
  lines words   bytes
```

And you can even specify directory names to ignore! First we call `wc` on a python project, ithout ignoring any file extensions or directories:

```console
C:\> wc matching-algorithms -l
  6     matching-algorithms\.gitignore
  22    matching-algorithms\README.md
  2     matching-algorithms\.git\COMMIT_EDITMSG
  16    matching-algorithms\.git\config
  1     matching-algorithms\.git\description
  2     matching-algorithms\.git\FETCH_HEAD
  2     matching-algorithms\.git\HEAD
  7     matching-algorithms\.git\index
  2     matching-algorithms\.git\ORIG_HEAD
  16    matching-algorithms\.git\hooks\applypatch-msg.sample
  25    matching-algorithms\.git\hooks\commit-msg.sample
  175   matching-algorithms\.git\hooks\fsmonitor-watchman.sample
  9     matching-algorithms\.git\hooks\post-update.sample
  15    matching-algorithms\.git\hooks\pre-applypatch.sample
  50    matching-algorithms\.git\hooks\pre-commit.sample
  14    matching-algorithms\.git\hooks\pre-merge-commit.sample
  54    matching-algorithms\.git\hooks\pre-push.sample
  170   matching-algorithms\.git\hooks\pre-rebase.sample
  25    matching-algorithms\.git\hooks\pre-receive.sample
  43    matching-algorithms\.git\hooks\prepare-commit-msg.sample
  79    matching-algorithms\.git\hooks\push-to-checkout.sample
  129   matching-algorithms\.git\hooks\update.sample
  7     matching-algorithms\.git\info\exclude
  11    matching-algorithms\.git\logs\HEAD
  11    matching-algorithms\.git\logs\refs\heads\main
  33    matching-algorithms\.git\logs\refs\remotes\origin\HEAD
  11    matching-algorithms\.git\logs\refs\remotes\origin\main
  12    matching-algorithms\.git\objects\00\0d21fcd4cb2ca6e59ef2b2002cb1048d541f27
  4     matching-algorithms\.git\objects\01\6ca9c5ca0ff63978f9922ad01a1825c485a6bd
  1     matching-algorithms\.git\objects\03\337b5c7dbec27bf6f6e6924006a0c119807769
  6     matching-algorithms\.git\objects\03\efc0b7f527818bb540c6c5584ba612ecc1f594
  2     matching-algorithms\.git\objects\04\caa8e53017b4ab5a660ca8fdb2583eb5362ac2
  5     matching-algorithms\.git\objects\05\a357455eee5604cf4df366252cfe9c8f2f135e
  1     matching-algorithms\.git\objects\09\2bf3e7900f85f5f61af91578883c0a27fbd979
  8     matching-algorithms\.git\objects\09\34ea9b62bd31b4bfd8c4299f0c99ba8eb7d074
  4     matching-algorithms\.git\objects\0a\66ffa21b808f14e472b8923cc06ee17b6b0e30
  3     matching-algorithms\.git\objects\0b\96665845a9fc038ece44f13d56851fdb3e9913
  3     matching-algorithms\.git\objects\0c\c5762af493d1dc5d0e7cc6afba4c9a8cd59e1a
  4     matching-algorithms\.git\objects\0f\772273d50d95af0e8228ac1e3991802ca133af
  2     matching-algorithms\.git\objects\10\5cb69c8126a9821a9b60eefa545493bea7af69
  8     matching-algorithms\.git\objects\14\09ea0477d18d1265ba2198dec5aba43311f919
  6     matching-algorithms\.git\objects\14\9e179ddcef5f250a0d457cbbc8a8598a7ea56d
  2     matching-algorithms\.git\objects\16\4dee95843a1040ed4e5786ce0bdb0404fce3c7
  1     matching-algorithms\.git\objects\17\9beaa4916f3066fd5a1d118fea0c3981ec0377
  2     matching-algorithms\.git\objects\18\9f66776d49cd6466fa0ecc9ac242f298498c0e
  1     matching-algorithms\.git\objects\1a\81cd8eb500d40599b5a6af6c3771c1c209b7e8
  9     matching-algorithms\.git\objects\24\69195205a89376a0e264940fcd4cbf92e776d3
  2     matching-algorithms\.git\objects\2a\c8234a99788f02864a4e52865561f6a5c0cf66
  4     matching-algorithms\.git\objects\2c\095aa199c98877d853e6c7418e251f021d2858
  6     matching-algorithms\.git\objects\2f\977032ce0b7c592dd6dfc1578daf90465712f6
  2     matching-algorithms\.git\objects\30\311bdd6eefa848215aeb374a1e81f0422ba4dc
  1     matching-algorithms\.git\objects\35\3f3fbb423644c20310875a4a9b0f320b8472c8
  2     matching-algorithms\.git\objects\35\5cfe627e10c353a0622033ec854480aa45a6a5
  8     matching-algorithms\.git\objects\36\aa7c1a8250066e1f72602624784c381c7cfe47
  12    matching-algorithms\.git\objects\38\7f1ecdc33689b9832facbc79d5a7b350781e9c
  4     matching-algorithms\.git\objects\45\289f3fb33ed737ba32477315d2d5dfec5916f5
  2     matching-algorithms\.git\objects\46\670337f355e2ce85e2b86b55929a2c0003fce4
  4     matching-algorithms\.git\objects\46\b61ec0bbdca71363c33e9a2984ae81aea49d65
  9     matching-algorithms\.git\objects\48\2adbc27ccbd61a72a42437f051a7c554697c0e
  2     matching-algorithms\.git\objects\49\6f2da837dfc087e1780e769d45a049f9526a39
  3     matching-algorithms\.git\objects\49\c1a8aca332004b01ba3b5311dc5df76bbc4412
  9     matching-algorithms\.git\objects\4d\a730235cf72ec132fbc58211db69aeef361ddd
  10    matching-algorithms\.git\objects\4f\a4ecf0807c318bed1a5b187a094f61d56a8997
  9     matching-algorithms\.git\objects\55\893097ffaae27e8966686c0eba5f978fc30f69
  2     matching-algorithms\.git\objects\55\e4fafb340aedb627ae6a83f3a47f38d8fd17f7
  3     matching-algorithms\.git\objects\57\020d7a093ad291bbb127936d7ba333ca0f417d
  1     matching-algorithms\.git\objects\57\ba1a9eb61aabf8a9f355736bf37e4fc35e8a38
  1     matching-algorithms\.git\objects\5b\6f10feb2f6dccf6b6646de20786e5984f76ae5
  2     matching-algorithms\.git\objects\5c\9f6a1231a64a60cda335aab6b56655817eeea2
  2     matching-algorithms\.git\objects\5d\0a4763935dad000434d62731b6aa01ebb130d1
  2     matching-algorithms\.git\objects\60\3b2d4ea63da2a1abc5ad988d0778b41ab4ee01
  4     matching-algorithms\.git\objects\62\d256746da9d28392b4ba52a7165feb2f8dbeeb
  11    matching-algorithms\.git\objects\65\11e9b9a71e21bd93ebd7b6c56f204cad5bf151
  2     matching-algorithms\.git\objects\66\9366557b06d1c037613a6e846931ebbba4fd63
  1     matching-algorithms\.git\objects\6f\9509c88bed7080d496fc5e1d87a9315e30549d
  2     matching-algorithms\.git\objects\75\7c54dc0b4bf7edb1f1cdd89b0f441482274998
  4     matching-algorithms\.git\objects\76\cb89c01d795dd41ccbaa0d1080a5c16807f67c
  2     matching-algorithms\.git\objects\7b\004c01d76cc06d5d8248ab31cc049cc19f5383
  2     matching-algorithms\.git\objects\7d\24640b77c38b84b12d081f519e08238784d52a
  2     matching-algorithms\.git\objects\7d\83f4a503dc10bae5d19a6711a5e05398bff429
  2     matching-algorithms\.git\objects\7e\76c1ad1732110f153d3828af39dbc6e0352aed
  1     matching-algorithms\.git\objects\7f\de9be408eaf61e6479123dd648631e587a69e1
  2     matching-algorithms\.git\objects\83\18423da9a4f73461bcddc93203ef361722acd3
  12    matching-algorithms\.git\objects\83\f6d95476afa6fb88f8dbe5dc94ec5534897384
  3     matching-algorithms\.git\objects\85\29717a14738aa61b0d1fbb5392e9a32a95c838
  2     matching-algorithms\.git\objects\89\3fe505d9af10f04abc4a4a7c8111a3eeffbd58
  1     matching-algorithms\.git\objects\8d\a5ebfafbf3ef7a44680d3aa40833fbfc1336c3
  3     matching-algorithms\.git\objects\8e\5dff36b31240309255cda561b41384c1532753
  2     matching-algorithms\.git\objects\8f\87bb0cd9eb91644f865c9b34e739cfd2e52e89
  2     matching-algorithms\.git\objects\91\b5f4e717c244518bebe7dc700ed0ea8bb53057
  4     matching-algorithms\.git\objects\91\cd93c59e08145be520068c1b2149168859f86c
  14    matching-algorithms\.git\objects\92\220a0b842ef847474a5577920aae801b5a9bb8
  2     matching-algorithms\.git\objects\9d\fb9af432fd7ada9c839d2f1f648457d620e609
  2     matching-algorithms\.git\objects\9e\32406d8f0b61943382fc09028b23a7eac6ce24
  2     matching-algorithms\.git\objects\a4\7b497c678a3c9e080567170c22e917b856d154
  1     matching-algorithms\.git\objects\a7\9d0521b0ead0b83df67faacc89d86709b43ad6
  1     matching-algorithms\.git\objects\a7\b4cdd90a69728f1b5d0f44048ea17fe784b65b
  17    matching-algorithms\.git\objects\a9\f0bf8781c8154d7c2b64c1bcfe450388bc48b5
  1     matching-algorithms\.git\objects\ab\2d599d0ab5cc83aeca856b9a878c19176b6475
  5     matching-algorithms\.git\objects\ae\7ece480dd34cefe0be8fc1468b5b9b40b53b5d
  1     matching-algorithms\.git\objects\b2\faac4308bdb86ee184d638fac8ebd933af4bf2
  4     matching-algorithms\.git\objects\b6\45f27b781af23c4cb6ee610e8fa0396bea123a
  1     matching-algorithms\.git\objects\b8\0c246e7886ac724e9501b5eea46502d70931e1
  1     matching-algorithms\.git\objects\bd\037fcb6bffac4ce63c5804fefe38c9a9783e3d
  5     matching-algorithms\.git\objects\be\52369b3a6d051d87dd31762b2eac876a0da74e
  1     matching-algorithms\.git\objects\bf\4bf806a309ad94e07c5d5aeb79e3213691de99
  1     matching-algorithms\.git\objects\c7\a8e9372af0bfd72531a1a51d109c4fcf6bb67f
  3     matching-algorithms\.git\objects\c8\6e2e430e1a990dc06cf4064f40f843d8ee19f8
  13    matching-algorithms\.git\objects\c8\e7f121be82ca1b2d82a0b3c9c78cc9538d39e2
  2     matching-algorithms\.git\objects\cc\33fad8fe23fe6a6358ec67800697a7edf04691
  2     matching-algorithms\.git\objects\cd\620f8d2a5e25bdf63571ec62c6343f8d8a9db3
  7     matching-algorithms\.git\objects\d1\ea52f806e033a972ba604ea3d84894c5743104
  2     matching-algorithms\.git\objects\d7\6b6bef3a7b9e11fe3ef54b363b500d1f7dacaf
  2     matching-algorithms\.git\objects\dd\9107788044beeac219f388ec407b7ee7963ef4
  1     matching-algorithms\.git\objects\dd\d90a8241e81b1c2680932fd13ff66456aab8c8
  2     matching-algorithms\.git\objects\de\35ae3f7705048f79c5c311c8909deecb910a6f
  1     matching-algorithms\.git\objects\df\e0770424b2a19faf507a501ebfc23be8f54e7b
  12    matching-algorithms\.git\objects\df\f061105e5f4c646404e74c10005642fe66f230
  3     matching-algorithms\.git\objects\e0\eef57f311949b04717e887a623319ef7140d59
  1     matching-algorithms\.git\objects\e1\2b850fa2dff1081315b74ac30580d3e7c7bf9f
  3     matching-algorithms\.git\objects\e2\6698cbd1eba7a04d6843344464358d67d39c13
  1     matching-algorithms\.git\objects\e6\9de29bb2d1d6434b8b29ae775ad8c2e48c5391
  2     matching-algorithms\.git\objects\e7\8c23e4f705f854e23b966f277620ddead47267
  1     matching-algorithms\.git\objects\ec\554de06cb005d3482d5db863227be29ced8202
  2     matching-algorithms\.git\objects\ec\f68c4d00d8ec5a65bdb18d8a48bcad1259ac8e
  2     matching-algorithms\.git\objects\ed\4eca9f0ef03b54f99c8263800709addc1acbad
  1     matching-algorithms\.git\objects\f0\068bae1b50f7b8ce62374819becac2c1ac395c
  3     matching-algorithms\.git\objects\f4\5f4249e989b919e37e83252eb477b772e4dee0
  2     matching-algorithms\.git\objects\f9\4a132a71a830d406fdd437614f12759bb3e825
  5     matching-algorithms\.git\objects\fa\19b2bb66dde866581c81e85c2cf1f590252c26
  1     matching-algorithms\.git\objects\fb\75d698e6ebc711e2e7e16123ec47c3198b7dd4
  2     matching-algorithms\.git\objects\fd\6690d1380958c5f22a25bed4f5ca34bd20f68f
  3     matching-algorithms\.git\objects\ff\75481a8bd2251e860820af9fe718d8ed198958
  2     matching-algorithms\.git\refs\heads\main
  2     matching-algorithms\.git\refs\remotes\origin\HEAD
  2     matching-algorithms\.git\refs\remotes\origin\main
  21    matching-algorithms\python\data_generator.py
  44    matching-algorithms\python\graph.py
  21    matching-algorithms\python\node.py
  95    matching-algorithms\python\test_da.py
  394   matching-algorithms\python\test_ttc.py
  39    matching-algorithms\python\algos\da_utils.py
  92    matching-algorithms\python\algos\deferred_acceptance.py
  61    matching-algorithms\python\algos\top_trading_cycle.py
  80    matching-algorithms\python\algos\ttc_utils.py
  1     matching-algorithms\python\algos\__init__.py
  15    matching-algorithms\python\algos\__pycache__\da_utils.cpython-311.pyc
  30    matching-algorithms\python\algos\__pycache__\deferred_acceptance.cpython-311.pyc
  34    matching-algorithms\python\algos\__pycache__\top_trading_cycle.cpython-311.pyc
  13    matching-algorithms\python\algos\__pycache__\ttc_utils.cpython-311.pyc
  2     matching-algorithms\python\algos\__pycache__\__init__.cpython-311.pyc
  6     matching-algorithms\python\__pycache__\data_generator.cpython-311.pyc
  31    matching-algorithms\python\__pycache__\graph.cpython-311.pyc
  6     matching-algorithms\python\__pycache__\node.cpython-311.pyc
  2316  total
  lines
```

Yikes. Now, let's call `wc` on the same directory, but ignore any compiled python bytecode files (.pyc) and any .git directories:

```console
C:\> wc matching-algorithms -l -i .pyc .git
  6     matching-algorithms\.gitignore
  22    matching-algorithms\README.md
  21    matching-algorithms\python\data_generator.py
  44    matching-algorithms\python\graph.py
  21    matching-algorithms\python\node.py
  95    matching-algorithms\python\test_da.py
  394   matching-algorithms\python\test_ttc.py
  39    matching-algorithms\python\algos\da_utils.py
  92    matching-algorithms\python\algos\deferred_acceptance.py
  61    matching-algorithms\python\algos\top_trading_cycle.py
  80    matching-algorithms\python\algos\ttc_utils.py
  1     matching-algorithms\python\algos\__init__.py
  876   total
  lines
```

Much better!

## Acknowledgements
Thanks to [John Crickett](https://github.com/JohnCrickett) for the idea from his site, [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-wc)!

Feedback, bug reports, issues, and pull requests welcome!