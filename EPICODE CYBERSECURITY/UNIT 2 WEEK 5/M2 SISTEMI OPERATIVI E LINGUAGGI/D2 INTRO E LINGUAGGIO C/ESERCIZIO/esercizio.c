#include <stdio.h>
#include <math.h>

int main () {
  
    float D;

    printf ("Inserisci un numero reale D\n");
    scanf ("%f", &D);

    // Calcola e stampa l'area del quadrato di lato D
    float area_quadrato = D * D;
    printf ("L'area del quadrato di lato %f è %f\n", D, area_quadrato);

    // Calcola e stampa l'area del cerchio di diametro D
    float r = D / 2;
    float area_cerchio = M_PI * r * r;
    printf ("L'area del cerchio di diametro %f è %f\n", D, area_cerchio);

    // Calcola e stampa l' area del triangolo equilatero di lato D
    float altezza = sqrt (3) / 2 * D;
    float area_triangolo = D * altezza / 2;
    printf ("L'area del triangolo equilatero di lato %f è %f\n", D, area_triangolo);

    return 0;
}
