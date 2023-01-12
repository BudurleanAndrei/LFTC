start

variable
n1: integer;
n2: integer;
n3: integer;
greatest: integer;

start

sk(n1)
sk(n2)
sk(n3)

maybe (n1 >= n2 also n1 >= n3) {
	greatest is n1
}
otherwise maybe (n2 >= n1 also n2 >= n3) {
		greatest is n2
	} otherwise {
			greatest is n3
		}

ps(greatest)

end