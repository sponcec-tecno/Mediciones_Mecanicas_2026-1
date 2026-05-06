sol.dat: sol.dat Numerical_solution.cpp
	g++ Numerical_solution.cpp
	./a.out > sol.dat
