#!/bin/bash
x=3;
y=5;
z=10;
if ["("$x-eq 3")" -a "("$y-eq5-0 $z-eq10")"]
then
echo $x
else
echo $y
fi

# Ans: 5