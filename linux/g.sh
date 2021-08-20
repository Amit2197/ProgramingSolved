#!/bin/sh
user_function() {
    echo "welcome"
    printf "World of Linux\n"
}

unset -f user_function
user_function
exit 0