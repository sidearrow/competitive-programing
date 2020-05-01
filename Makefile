build-cpp:
	g++ -O2 -o a.out $1

exec-cpp:
	./a.out < in
