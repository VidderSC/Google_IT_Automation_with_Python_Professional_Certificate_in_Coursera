echo Pipes and Pipelines
echo
echo Pipes connect the output of one program to the input of another in order to pass data between programs.
echo Pipes are represented by the \"\|\" character
echo
echo \"ls -l \| less\" will create a list and divide it by pages that we can change using the arrows or the page up or page down and Q to exit.
echo
echo \"cat spider.txt \| tr \' \' \'\\n \| sort \| uniq \-c \| sort \-nr \| head \"
echo
echo That is a complex command line. Let us go through it step by step. 
echo We are first using cat to get the contents of our spider.txt file.
echo Those contents are then sent to a command called tr, which gets its name from the word translate.
echo It takes the characters in the first parameter, in this case, it is a space and then transform them
echo into a character in the second parameter. In this case, it is a newline character.
echo So basically, what we are doing is putting each word in its own separate line.
echo
echo Next, we pass results to the sort command through a pipe. This command sorts results alphabetically.
echo The sorted results are then passed to the unique command, which displays each match once,
echo and by using a \-c flag, it prefixes each unique line with a number of times it occurred.
echo This output is passed via pipe to the sort command once more, this time, with the \-nr flag,
echo which sorts results numerically and in reverse order, from most to least hits.
echo 
echo The output is finally passed to the head command, which prints the first \1\0 lines to STDOUT.
echo
echo \"cat haiku.txt\" returns:
echo advance your career,
echo automating with Python,
echo it\'s so fun to learn.
echo
echo \"cat haiku.txt \| python capitalize.py\" returns:
echo Advance your career,
echo Automating with Python,
echo It\'s so fun to learn.
echo
echo Please note that the following will work the same but cannot be connected to other pipes.
echo \"python3 capitalize.py \< haiku.txt\"
echo Advance your career,
echo Automating with Python,
echo It\'s so fun to learn.
echo