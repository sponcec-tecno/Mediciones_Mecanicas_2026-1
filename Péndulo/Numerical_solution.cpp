#include <iostream>
#include <cmath>

long long fct(int n);
double cost(double x);
double aux(double x, int n);
double f(double th_0, double th);

double const g = 9.7754427;
double const l = 0.15;

int main(int argc, char **argv){

//	for(double t = 0.0; t < M_PI; t+=0.031415){
//		std::cout << t << " " << cost(t) << "\n";
//	}
	double aux = std::sqrt(l/g);

	return 0;
}

long long fct(int n){
	if (n == 0){return 1;}
	if (n == 1){return 1;}
	return n*fct(n-1);
}

double cost(double x){
	double s = -1.0;
	double res = 0.0;
	for(int i = 0; i <= 10; ++i){
		s *= -1.0;
		res += s*aux(x, i*2);
	}
	return res;
}

double aux(double x, int n){
	return std::pow(x,n)/fct(n);
}

double f(double th_0, double th){
	if (th_0==th) {return 0.0;}
	return 1/(cost(th_0)-cost(th));
}

//Implementar función factorial
//Implementar taylor
//Implementar la función a integrar
//Realizar la integral(Simpson)
