echo Basic Linux commands using Bash
echo echo, cat, ls, chmod, mkdir, cd, pwd, cp, touch, mv, rmdir
echo
echo - echo is used to print messages to the screen,
echo - cat showing contents of files,
echo - ls lists contents of a directory,
echo - chmod changes permissions of a file.
echo - mkdir creates a new directory
echo ~\$ mkdir new_folder
echo
echo - cd changes to a directory
echo ~\$ cd new_folder --\> \~/new_folder\$
echo cd.. will change the actual directory to the previous directory
echo
echo - pwd prints the current working directory
echo
echo - cp copy files from to a folder or creating a copy of the file in the same directory
echo \~/new_folder\$ \"cp ../spider.txt .\" will copy the txt file that its in the parent directory \"..\" to the actual directory \".\"
echo \"cp spider.txt anotherfile.txt\" will create a copy of the spider file but with a different name.
echo
echo - touch will create a new empty file
echo touch myfile.txt
echo
echo ls \-l will show details of the listed files
echo ls \-la will show hidden files plus the extra details from before
echo
echo - mv will be used to move or rename.
echo \"mv myfile.txt emptyfile.txt\" here we have renamed the file from myfile to emptyfile.
echo
echo - rmdir is used to delete empty directories
echo rmdir new_folder
echo