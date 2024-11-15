#include <stdio.h>
#include "mathlib.h"
#include "obj.h"

// Define ray
typedef struct{
    Point origin;
    Vector direction;
} Ray;


// Function for ray operation

Vector ray_at(Ray ray, double t){
    Vector origin_position_vector = point2vec(ray.origin);
    return add_vec(origin_position_vector, scale_vec(ray.direction, t));
}