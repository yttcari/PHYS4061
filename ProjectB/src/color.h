#include <stdio.h>
#include "ray.h"
#include "obj.h"
#include "mathlib.h"

#ifndef COLOR_H
#define COLOR_H

typedef struct{
    double r;
    double g;
    double b;
} Color;

Color bg_color(Ray r);
void write_color(Color color, FILE *fpt);

Vector color2vec(Color color);
Color vec2color(Vector vec);
Color ray_color(Ray r);
#endif