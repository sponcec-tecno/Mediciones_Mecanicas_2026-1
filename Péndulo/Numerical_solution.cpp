#include <iostream>
#include <cmath>
#include <functional>

using funptr = std::function<double(double)>;
long long fct(int n);
double cost(double x);
double aux(double x, int n);
double f(double th);
double gauss5(double a, double b, funptr fun);

double const g = 9.7754427;
double const l = 0.15;
double const th_0 = (3*M_PI/4);

int main(int argc, char **argv){

//	for(double t = 0.0; t < M_PI; t+=0.031415){
//		std::cout << t << " " << cost(t) << "\n";
//	}

	double n = 200;

	double aux = std::sqrt(l/g);
	for(double x = -th_0; x < th_0; x+=(th_0/n)){
              std::cout << x << " " << gauss5(x, x+(th_0/n), f) << "\n";
	}



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

double f(double th){
	return 1/(cost(th_0)-cost(th));
}

double gauss5(double a, double b, funptr fun)
{
    // puntos de gauss
    std::vector<double> x = {0.0000000000000000, -0.5384693101056831, 
                            0.5384693101056831, -0.9061798459386640, 
                            0.9061798459386640};
    // pesos 
    std::vector<double> w = {0.5688888888888889, 0.4786286704993665,
                             0.4786286704993665, 0.2369268850561891,
                             0.2369268850561891};

    // aux
    double aux1 = (b-a)/2;
    double aux2 = (b+a)/2;

    // suma
    double suma = 0.0;
    for (int ii = 0; ii < 5; ii++) {
        suma = suma + w[ii]*fun(aux1*x[ii] + aux2);
    }

    return aux1*suma;
}

//Implementar función factorial
//Implementar taylor
//Implementar la función a integrar
//Realizar la integral(Simpson)
