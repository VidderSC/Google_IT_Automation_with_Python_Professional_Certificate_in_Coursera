echo I/O Streams and Bash
echo
echo Redirection is the process of sending a stream to a different destination
echo
echo if we run the stdout_example.py file, it will simply print some text on the terminal but,
echo if instead we write the following:
echo \"stdout_example.py \> new_file.txt\" 
echo it will create a new file with the output from the python file or if the file already exist,
echo WARNING - it will be overwritten!
echo 
echo on the other hand, we can append to the file if it already exist or create a new file, by using \>\> instead.
echo \"stdout_example.py \>\> new_file.txt\"
echo
echo we can use \< to input data to a file, for example:
echo \"python 02_streams_err.py \< 02_new_file.txt\"
echo will override the input in the code and pass the info inside the txt file.
echo
echo \2\> can redirect errors to a different file, using the previous example it will work like this:
echo \"python 02_streams_err.py \< 02_new_file.txt \2\> error_file.txt\"
echo in this case it didnt show the error in the terminal because it was redirected to error_file.txt
echo we use \2 because it represent the file descriptor of the STDERR stream
echo \0 is the file descriptor of STDIN, \1 is for STDOUT and \2 is for STDERR
echo
echo We can also redirect and echo to a file, for example:
echo "These are the contents of the file" \> 02_new_file_from_echo.txt
echo