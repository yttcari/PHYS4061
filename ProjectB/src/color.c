#include <stdio.h>
#include "ray.h"
#include "obj.h"
#include "mathlib.h"

typedef struct{
    double r;
    double g;
    double b;
} Color;

Color to_color(double r, double g, double b){
    Color color;
    color.r = r;
    color.g = g;
    color.b = b;

    return color;
}

// Change to vector object for computation
Vector color2vec(Color color){
    Vector vec;

    vec.x = color.r;
    vec.y = color.g;
    vec.z = color.b;

    return vec;
}

Color vec2color(Vector vec){
    Color color;

    color.r = vec.x;
    color.g = vec.y;
    color.b = vec.z;

    return color;
}

Color ray_color(Ray r){
    return to_color(0, 0, 0);
}

void write_color(Color color, FILE *fpt){
    fprintf(fpt, "%d %d %d\n", (int) round(color.r * 255.999), (int) round(color.g * 255.999), (int) round(color.b * 255.999));
}

Color bg_color(Ray r){
    Vector unit_direction = scale_vec(r.direction, 1./get_magnitude(r.direction));
    double a = 0.5 * (unit_direction.y + 1);

    Vector start_color_vector = scale_vec(to_vector(1, 1, 1), 1. - a);
    Vector end_color_vector = scale_vec(to_vector(0.5, 0.7, 1), a);

    return vec2color(add_vec(start_color_vector, end_color_vector));
}