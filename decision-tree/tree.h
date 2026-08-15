
#ifndef TREE_H
#define TREE_H

typedef struct {
    int feature;
    double gini;
    double threshold;
} Split;

double gini (const int *y, int n, int num_classes);

Split find_best_split (const double X[][2], const int *y, int n_samples, int n_features, int num_classes);

#endif