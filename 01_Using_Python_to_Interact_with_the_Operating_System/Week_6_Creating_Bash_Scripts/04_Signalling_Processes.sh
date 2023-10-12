echo Signalling Processes
echo
echo Signals are Tokens delivered to running processes to indicate a desired action
echo
echo for example Ctrl-C is a signal that will break the process of the
echo command Ping but will not exit with an error.
echo
echo The signal that Ctrl-C sends is called SIGINT \"Signal Interrupt\"
echo another signal could be Ctrl-Z which is called SIGSTOP \"Signal Stop\"
echo but this one we can resume the process by entering fg. 
echo Note that this last one does not work on windows terminal using bash, only in Linux.
echo 
echo \"kill\" will send a SIGTERM \"Signal Terminate\"
echo Kill being another program we need to run it from a different terminal and 
echo we need to know the PID of the process that we want to terminate.
echo
echo to find out the PID of the process that we want to terminate, we can run the
echo \"ps\" command that lists all the running processes. 
echo depending on the modifiers that we pass it when we run it, will display 
echo different subsets of processes, in this case we will run it as:
echo \"ps ax\" will list all the running processes in the current computer and
echo then we will use the \"grep\" command to filter the list and show us only
echo the line of the process that we are looking for.
echo
echo \"ps ax \| grep ping\"
echo with this line we learn that the process ID for PING is \4\6\1\9 and now we
echo can use it with the kill command as follow:
echo \"kill \4\6\1\9\"
echo
echo There are more signals that we can send and they might cause programs to react differently.
echo Many long running programs, for example, will reload their configuration 
echo from disk if we send them a signal.
echo This way we can let the program know that there is an important change in the configuration
echo and it can get applied without the program having to stop to reread it.
echo 
echo Programs that provide web services may also receive a signal to tell them that they should
echo finish dealing with any currently open connections and then terminate cleanly once it is done.
echo
echo Understanding what these signals are and how to send them will let you interact with the processes
echo on your system that you are in charge of and make them behave as you want.
echo 