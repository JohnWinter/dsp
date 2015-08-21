# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > pushd <destination folder> : saves current folder and moves me to destination, 
popd takes me to folder saved after i executed pushd.

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > list directory.
ls -a : lists all files including hidden files
ls -l: returns one file per line and includes meta data such as the created date, and file size 
ls -lh: same as ls-l accept it uses giga/mega/et prefixes to decrease the file size string. 
ls -ah is not meaningful. h is only useful when used with -l


---


---

What does `xargs` do? Give an example of how to use it.

> Xargs takes a newline separated list and maps the list to a command.

 find ./ -name '*.log' | xargs rm
  Finds all log files and map them to 'rm' commands. That is, if it finds system.log and rails.log it will run the command `rm system.log rails.log`.

---

