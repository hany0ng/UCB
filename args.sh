#!/bin/bash

#echo "hello, world"

#echo $0
#-what does this contain?
#--contains name of the script.

#echo $1
#-what happens when you run the script with arguments?
#--returns argument as variable 1.
#-what happens when you run the script without arguments?
#--returns blank line as nothing has been assigned to variable 1.

if [ $# = 3 ]; then
        echo "The name of the script is $0."
	echo "The value of the first argument is $1."
	echo "The value of the second argument is $2."
	echo "The value of the third argument is $3."

else
        echo "Your command line needs 3 arguments."
fi
