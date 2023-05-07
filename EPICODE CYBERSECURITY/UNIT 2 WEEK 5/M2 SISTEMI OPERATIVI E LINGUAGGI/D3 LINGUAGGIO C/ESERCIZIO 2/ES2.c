#include <stdio.h>
#include <stdlib.h>

int main() {
    int punteggio = 0;
    char scelta;
    char risposta;
    char ultima_scelta;
    char nickname[20];
    
    printf("Benvenuto! Questo e' un quiz a punti. Rispondi correttamente a piu' domande possibili per incrementare il tuo punteggio!\n\nInserisci 1 per iniziare una nuova partita\nInserisci 0 per uscire\n");
    scanf("%c", &scelta);
    while(scelta != '0' && scelta != '1') {
        printf("Scelta errata, inserisci il valore corretto\n\nInserisci 1 per una nuova partita\nInserisci 0 per uscire\n");
        rewind(stdin);
        scanf("%c",&scelta);  
    }
    	
    do {
    	

    if(scelta == '0') {
    	printf ("Ok, sara' per un'altra volta!");
		exit(0);
	}
	
    if(scelta == '1') {
    	
	
	printf ("Inserisci il tuo nickname: ");
	rewind(stdin);
	fgets (nickname, 20, stdin);
	printf ("\nOk, %s\n", nickname);
	

        printf("/ / / LET'S GET IT ON! / / /\n"
        "\nInserisci il numero corrispondente alla risposta che ritieni corretta!\n");


        printf("\nDomanda 1: Di che colore era il cavallo bianco di Napoleone?\n\n 1) Blu\n 2) Bianco\n 3) Era un unicorno\n");
        
		do {
			
			rewind(stdin);
			scanf("%c", &risposta);

        if (risposta == '2') {
                printf ("Corretto!\n");
                punteggio = punteggio +1;
        }

        else if (risposta == '1' || risposta == '3') {
				printf ("Risposta errata\n");
        }
        
        else {
        	printf ("Inserisci un valore tra 1 e 3\n");
		} 
        
    	} while (risposta != '1' && risposta != '2' && risposta != '3'); 
    	
    	
    	
         
        printf("\nDomanda 2: Quanti MB ci sono in un GB?\n\n 1) 1024\n 2) 124\n 3) 100\n");
        
        do {
        
		rewind(stdin);	
        scanf("%c", &risposta);

        if (risposta == '1') {
                printf ("Corretto!\n");
                punteggio = punteggio +1;
        }

        else if (risposta == '2' || risposta == '3') {
                printf ("Risposta errata\n");
       }
       
       else {
       	printf ("Inserisci un valore tra 1 e 3\n");
	   }
       
       } while (risposta != '1' && risposta != '2' && risposta != '3'); 
        
        
        
        
        printf("\nDomanda 3: Quale di questi 3 pianeti e' il più lontano dal sole?\n\n 1) Marte\n 2) Nettuno\n 3) Giove\n");
        
        do {
		
        rewind(stdin);
        scanf("%c", &risposta);

        if (risposta == '2') {
                printf ("Corretto!\n");
                punteggio = punteggio +1;
        }

        else if (risposta == '1' || risposta == '3') {
                printf ("Risposta errata\n");
        }

		else {
			printf ("Inserisci un valore tra 1 e 3\n");
		}

		} while (risposta != '1' && risposta != '2' && risposta != '3');
		
		printf("\nIl quiz e' terminato! Hai totalizzato %d punti", punteggio);
		printf("\n\nVuoi giocare ancora?\n\nDigita 1 per iniziare una nuova partita\nDigita 0 per uscire\n");
        
    	}
    	
        
        do {
        
        rewind(stdin);
        scanf("%c",&ultima_scelta);

        if (ultima_scelta == '0') {
        	printf ("Have a nice day!");
        }
        	
        else if (ultima_scelta == '1') {
        	printf ("Ok! Ricominciamo\n\n");
		}
		
		else {
			printf ("Inserisci una risposta valida\n\n");
		}
		

		} while (ultima_scelta != '0' && ultima_scelta != '1');
		
		

        } while (ultima_scelta == '1');
    

}