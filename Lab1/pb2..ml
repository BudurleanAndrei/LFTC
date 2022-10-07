Number is prime

sk - scan from keyboard
ps - print to screen
finish - return
until - reverse while (does action until statement is true)

is - true
isnot - false



number nr

sk(nr)

maybe (nr % 2 == 0) {
	finish(isnot)
}

number i
i is 3

until (i * i >= nr) {
	maybe (nr % i == 0) {
		finish(isnot)
	}
	
	i is i + 2
}


finish(is)