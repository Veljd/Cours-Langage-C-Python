#include <stdio.h>
#include <stdlib.h>
#include "le_juste_prix.h"

void jouer_juste_prix() {
    printf("Bienvenue au Juste Prix !\n");
    printf("Je pense à un nombre entre 1 et 100. Devinez quel est ce nombre !\n");

    int nombre_a_deviner = rand() % 100 + 1;
    int nombre_devine = 0;

    while (!nombre_devine) {
        int proposition;
        printf("Entrez votre proposition : ");
        if (scanf("%d", &proposition) != 1) {
            printf("Veuillez entrer un nombre valide.\n");
            continue;
        }

        if (proposition < nombre_a_deviner) {
            printf("C'est plus !\n");
        } else if (proposition > nombre_a_deviner) {
            printf("C'est moins !\n");
        } else {
            printf("Félicitations ! Vous avez trouvé le juste prix !\n");
            nombre_devine = 1;
        }
    }

    printf("Merci d'avoir joué !\n");
}
