#include <stdio.h>

void print_menu();
int play_game();

int main() {

    char scelta = '\0'; 
    print_menu();

    scanf(" %c", &scelta);

    if (scelta == 'B') {
        printf("Gioco terminato, arrivederci \n");
        return 0;
    }

    while (scelta == 'A') {
        play_game();
        print_menu();
        scanf(" %c", &scelta); 
    }

    return 0;
}

void print_menu() {
    printf("menù di avvio:\n");
    printf("Premi A per iniziare un nuovo gioco \n Premi B per uscire dal gioco\n");
    printf("inserisci la lettera della tua scelta:\n");
}

int play_game() {
    int punteggio = 0;
    char nome[20] = {'\0'};
    char risposta1, risposta2, risposta3;
    printf("inserisci il nome del giocatore: \n");
    scanf("%s", nome); 

    printf("Domanda numero 1:\n");
    printf("Qual'è la capitale dell'italia? \n");
    printf("A Milano \n B Roma \n C Torino \n");
    printf("inserire la risposta:");
    scanf(" %c", &risposta1);


if (risposta1 == 'B') 
	{
      punteggio++;
	}

    printf("Domanda numero 2:\n");
    printf("Qual'è la capitale della germania? \n");
    printf("A Berlino \n B Monaco \n C Francoforte \n");
    printf("inserire la risposta:");
    scanf(" %c", &risposta2);


if (risposta2 == 'A') 
	{
	punteggio++;
	}


printf("Domanda numero 3:\n");
printf("Qual'è la capitale della francia? \n");
printf("A Lione \n B Marsiglia \n C Parigi \n");
printf("inserire la risposta:");
scanf(" %c", &risposta3);

if (risposta3 == 'C')
	{
	punteggio++;
	}

    printf("Partita conclusa, punteggio totalizzato da %s:%d\n", nome, punteggio);

    return 0;
}