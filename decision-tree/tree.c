#include <stdio.h>
#include <float.h>
#include "tree.h"

/***
 * 
 * Gini = 1 - sum (p_i ^ 2)
 * 
 */

double gini (const int *y, int n, int num_classes) {

    int counts[num_classes];
    // init
    for (int i = 0; i <= num_classes; i++ ) {
        counts[i] = 0;
    }

    for (int i = 0; i < n; i++ ) {
        counts[y[i]]++;
    }

    
}