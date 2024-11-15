#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

#ifndef OBJ_H
#define OBJ_H

typedef struct{
    double x;
    double y;
    double z;
} Vector;

typedef struct{
    double x;
    double y;
    double z;
} Point;

Vector to_vector(double x, double y, double z);
Point to_point(double x, double y, double z);

Vector point2vec(Point point);
Point vec2point(Vector vec);

void print_vec(Vector vec);
#endif