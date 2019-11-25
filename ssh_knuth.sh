#!/usr/bin/expect -f

spawn ssh jgardi@knuth.cs.hmc.edu
expect "Password:"
send -- "Spider-man-1\r\r"
interact
