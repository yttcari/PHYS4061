#include <stdio.h>
#include "math.h"
#include "obj.h"
#ifndef RAY_H
#define RAY_H

typedef struct{
    Point origin;
    Vector direction;
} Ray;

Vector ray_at(Ray ray, double t);

#endif