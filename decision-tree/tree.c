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

    double result = 1.0;

    for (int i = 0; i < num_classes; i++ ) {
        double probability = (double)counts[i] / n;
        result -= probability * probability;
    }

    return result;
}


Split find_best_split (const double X[][2], const int *y, int n_samples, int n_features, int num_classes) {

    Split best;
    best.feature = -1;
    best.threshold = 0.0;
    best.gini = DBL_MAX;

    for (int feature = 0; feature < n_features; feature++ ) {
        for (int sample = 0; sample < n_samples; sample++ ) {
            double threshold = X[sample][feature];
            int left_count = 0;
            int right_count = 0;

            for (int i = 0; i < n_samples; i++ ) {
                if (X[i][feature] <= threshold) {
                    left_count++;
                } else {
                    right_count++;
                }
            }

            if (left_count == 0 || right_count == 0) {continue;}

            int left_y[left_count];
            int right_y[right_count];


            int left_index = 0;
            int right_index = 0;

            for (int i = 0; i < n_samples; i++ ) {
                  if (X[i][feature] <= threshold)
                {
                    left_y[left_index++] = y[i];
                }
                else
                {
                    right_y[right_index++] = y[i];
                }
            }

            double left_gini = gini(left_y, left_count, num_classes);
            double right_gini = gini(right_y, right_count, num_classes);

            double weighted_gini = ((double) left_count / n_samples) * left_gini + ((double)right_count/n_samples) * right_gini;

            if (weighted_gini < best.gini) {
                best.gini = weighted_gini;
                best.feature = feature;
                best.threshold = threshold;
            }
        }
    }

    return best;
}