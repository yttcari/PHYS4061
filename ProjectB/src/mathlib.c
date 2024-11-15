#include <stdio.h>
#include <math.h>
#include "obj.h"

double dot(Vector vec1, Vector vec2){
    return vec1.x * vec2.x + vec1.y * vec2.y + vec1.z * vec2.z;
}

Vector add_vec(Vector vec1, Vector vec2){
    Vector result;

    result.x = vec1.x + vec2.x;
    result.y = vec1.y + vec2.y;
    result.z = vec1.z + vec2.z;

    return result;
}

Vector scale_vec(Vector vec, double scalar){
    Vector result;

    result.x = vec.x * scalar;
    result.y = vec.y * scalar;
    result.z = vec.z * scalar;

    return result;
}

Vector subtract_vec(Vector vec1, Vector vec2){
     Vector result;

    result.x = vec1.x - vec2.x;
    result.y = vec1.y - vec2.y;
    result.z = vec1.z - vec2.z;

    return result;
}

// Return magnitude of a vector object
double get_magnitude(Vector vec){
    double mag = 0;
    mag += vec.x * vec.x + vec.y * vec.y + vec.z * vec.z;
    return sqrt(mag);
}