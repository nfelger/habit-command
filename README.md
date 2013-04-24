# Introduction

`habit-command` is a command-line app to help you keep track of habits you're trying to build.

Since this project is about changing human behaviour, it is of utmost importance to include some hand-waving comments about "the brain" and "hunams." So here goes:

Neuroscientists agree<a id='ref1link' href='#ref1'>[1]</a> that the brain is pretty good<a id='ref2link' href='#ref2'>[2]</a> at detecting bullshit<a id='ref3link' href='#ref3'>[3]</a>. So when you tell yourself: "I'm going to work out for half an hour every day from now on!", your brain, being the independent, strong-willed actor that it is, will say "cool, sounds ace!" Until you miss even one single day. Then it'll be like: "Dude, you said you were gonna work out every day! You're clearly fucking with me, so I'll sabotage your efforts."<a id='ref4link' href='#ref4'>[4]</a> It's constantly looking for evidence to support or refute your claim. So if you set out with an ambition that's easily disproved, you set yourself up for failure.

Instead, if you make a statement like: "I'm going to make exercise a priority and will regularly spend time on it.", and then reinforce this belief by providing direct evidence that it's really true and keep reinforcing that evidence, your brain will support you.<a id='ref5link' href='#ref5'>[5]</a>

At least that's what I chose to believe this fine Wednesday.


This app is **designed** (that sounds professional, right?) to help you collect your evidence and do the reinforcing.


<a id='ref1'></a>[[1]](#ref1link) There's lots of 'em, so I'm sure you could round up one or two who agrees on this… [^](#ref1link)<br>
<a id='ref2'></a>[[2]](#ref2link) "pretty good" – see what I did there‽ [^](#ref2link)<br>
<a id='ref3'></a>[[3]](#ref3link) As defined by [pal_sch, Yo Noid et al (2004)](http://www.urbandictionary.com/define.php?term=bullshit). [^](#ref3link)<br>
<a id='ref4'></a>[[4]](#ref4link) Brains can't actually speak, so we haven't _exactly_ found evidence of this yet, but we're pretty sure that's what going on in the brain's head. [^](#ref4link)<br>
<a id='ref5'></a>[[5]](#ref5link) Not in the financial sense, tho. That's still your parents' job. [^](#ref5link)<br>



# Acknowledgements

This is in part inspired by joesgoals.com, which I used in 2006 for about a week or two.



# Usage

Below is a (hopefully) illustrative session that shows how to interact with habit command.

```
$ ./hc
Your top activities for the last 7 days:
1. 7pts: work out
2. 3pts: read
3. 1pts: study neuroscience
(/h for help, /q to quit)

hc> /h
/l          -- list activities
/t          -- track activity
/c          -- create activity
/s<n>       -- show details for activity
/list-all   -- list activities (including archived ones)
/archive<n> -- archive activity number 'n'
/revive<n>  -- un-archive activity number 'n'
/q          -- quit
/h          -- this help screen

hc> /l
(1) study neuroscience
(2) watch game of thrones
(3) work out
(4) read

hc> /t
Which activity would you like to track?
(1) study neuroscience
(2) watch game of thrones
(3) work out
(4) read

?> 2

hc> /c
Name: try to take over the world

hc> /s3
Your 'work out' history for the last 7 days:

   *     *
   *   * *   *
   T F S S M T W

Total points overall: 21pts
Best week:             7pts (this week!)
```


# License

Copyright (c) 2013 Niko Felger

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
