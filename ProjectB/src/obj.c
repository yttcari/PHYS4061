#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

// Useful objects

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


// Useful functions

Vector to_vector(double x, double y, double z){
    Vector vec;

    vec.x = x;
    vec.y = y;
    vec.z = z;

    return vec;
}

Point to_point(double x, double y, double z){
    Point vec;

    vec.x = x;
    vec.y = y;
    vec.z = z;

    return vec;
}


Vector point2vec(Point point){
    Vector vec;

    vec.x = point.x;
    vec.y = point.y;
    vec.z = point.z;

    return vec;
}

Point vec2point(Vector vec){
    Point point;

    point.x = vec.x;
    point.y = vec.y;
    point.z = vec.z;

    return point;
}

// For the sake of debug
void print_vec(Vector vec){
    printf("%lf %lf %lf\n", vec.x, vec.y, vec.z);
}