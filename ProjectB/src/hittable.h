#ifndef HITTABLE_H
#define HITTABLE_H

#include <stdio.h>
#include "obj.h"
#include <math.h>
#include "math.h"


typedef struct{
    // The point where the ray hit the object
    Point p;
    // Normal vector of that point
    Vector n;
    // For ray = P + t * direction
    double t;

} hit_record;

hit_record init_rec();
#endif