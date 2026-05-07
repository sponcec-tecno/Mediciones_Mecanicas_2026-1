#include <iostream>
#include <cmath>
#include <functional>

using funptr = std::function<double(double)>;
long long fct(int n);
double cost(double x);
double aux(double x, int n);
double f(double th);
//double simpson(double a, double b, int nintervals, funptr fun);

//double const g = 9.7754427;
//double const l = 0.15;
double const a = M_PI/2;
double const th_0 = (3*M_PI/4);

int main(int argc, char **argv){

//	for(double t = 0.0; t < M_PI; t+=0.031415){
//		std::cout << t << " " << cost(t) << "\n";
//	}

	int n = 200;
	//double aux = std::sqrt(l/g);
	double b = th_0;
	double ax = (b-a)/n;
	//std::cout << aux << "\n";
	for(double x = a+ax; x+ax < b; x += ax){
        std::cout << x << " " << f(x) << "\n";
	}
	// std::cout << simpson(-1.0, 2, 1000, f) << "\n";

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
	for(int i = 0; i <= 5; ++i){
		s *= -1.0;
		res += s*aux(x, i*2);
	}
	return res;
}

double aux(double x, int n){
	return std::pow(x,n)/fct(n);
}

double f(double th){
	
	if(std::fabs(th) == th_0){
		return 0;
	}
	else{
		double th_02 = std::pow(cost(th_0), 2);
		double th2 = std::pow(cost(th), 2);
		return 1.0/(std::sqrt(th_02-th2));
	}
}

// double simpson(double a, double b, int nintervals, funptr fun)
// {
//     double deltax = (b-a)/(nintervals);
//     double suma = 0.0; 
//     double sum = 0.0; 
//     for (int k=1; k<= nintervals/2; k++){
//         double xk = a+((2*k-1)*deltax);
//         suma = suma + fun(xk);
//     }
//         for (int k=0.0; k<= nintervals/2 -1 ; k++){
//         double xk = a+(2*k*deltax);
//         sum = sum + fun(xk);
//     }
//     suma = (4*suma + 2*sum + fun(a) + fun(b))*(deltax/3);

//     return suma;
// }

//Implementar función factorial
//Implementar taylor
//Implementar la función a integrar
//Realizar la integral(Simpson)
