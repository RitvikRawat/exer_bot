#!/bin/bash

a=25
for i in *.png; do
  new=$(printf "%02d.png" "$a") #04 pad to length of 4
  mv -- "$i" "$new"
  let a=a+1
done