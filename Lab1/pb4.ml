Number is prime with lexical errors

sk - scan from keyboard
ps - print to screen
finish - return
until - reverse while (does action until statement is true)

is - true
isnot - false


// Variable name cannot begin with number
number 2nr

sk(nr)

maybe (nr % 2 == 0) {
	// Cannot match finish#
	finish#(isnot)
}

number i
i is 3

until (i * i >= nr) {
	maybe (nr % i == 0) {
		finish(isnot)
	}
	
	// Cannot match +=
	i += 2
}


finish(is)