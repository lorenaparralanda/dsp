# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > See table below:

| Command | Description |
| --------| ------------- |
pwd | print working directory
touch | create file
rm -r | remove directory and all of its children
> | redirect to a file (gets rid of text)
>> | appends (keeps original text)
cat | outputs contents of file 
\| | pipes a command
grep | global regular expression print (looks for a pattern)
sed | stream editor
man | helps you out!
env | returns a list of the environment variables


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > See table below:

| Command | Description |
| --------| ------------- |
ls | lists files in directory
ls -a | lists all hidden and un-hidden files in directory 
ls -l | lists files in long formal listing
ls -lh | list files in human readable format
ls -lah | lists all hidden and un-hidden files in human readable format
ls -t | lists files and sorts them by modification time (newest first)
ls -Glp | in long listing, list does not include long list names, but indicates directories


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > See table below:

| Command | Description |
| --------| ------------- |
ls -d | displays only directories
ls -F | flags filenames
ls -r | displays files in reverse order
ls -R | displays subdirectories as well
ls -u | displays files by the file access time

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` builds and executes command lines from standard input. For example, below, multiline output is converted into a single line.

```
devuser@system:/etc find . -name "*bash*" | xargs
./bash.bashrc ./bash.bash_logout ./defaults/etc/bash.bashrc ./defaults/etc/bash.bash_logout ./defaults/etc/skel/.bashrc ./defaults/etc/skel/.bash_profile ./postinstall/bash.sh.done ./setup/bash.lst.gz ./skel/.bashrc ./skel/.bash_profile
```

 

