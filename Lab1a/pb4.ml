
variable
2nr: integer;

start

sk(nr)

maybe (nr % 2 == 0) {
	finish#(isnot)
}

number i
i is 3

until (i * i >= nr) {
	maybe (nr % i == 0) {
		finish(isnot)
	}
	
	i += 2
}


finish(is)

end