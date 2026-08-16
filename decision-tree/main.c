#include <stdio.h>
#include "tree.h"

int main () {

    double X[][2] = {
        {100, 1200}, 
        {110, 1250},
        {150, 1400},
        {160, 1500},
        {300, 1800},
        {350, 1900}

    }; //TODO: Add data
    int y[] = {0, 0, 1, 1, 2, 2};
    int n_samples = 6;
    int n_features = 2;
    int num_classes = 3;

    double gini_value = gini(y, n_samples, num_classes);
    printf("Initial Gini: %4f\n", gini_value);
    Split best = find_best_split(X, y, n_samples, n_features, num_classes);
    printf("\n\n");
    printf("Best split: \n");
    printf("Feature: %d\n", best.feature);
    printf("Threshold: %.2f\n", best.threshold);
    printf("Gini: %4.f\n", best.gini);

    return 0;
}