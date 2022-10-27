
variable
nr: integer;
i: integer;

start

sk(nr)

maybe (nr % 2 == 0) {
	finish(isnot)
}

i is 3

until (i * i >= nr) {
	maybe (nr % i == 0) {
		finish(isnot)
	}
	
	i is i + 2
}

finish(is)