#include <stdio.h>
#include "obj.h"

#ifndef MATHLIB_H
#define MATHLIB_H
double dot(Vector vec1, Vector vec2);
Vector add_vec(Vector vec1, Vector vec2);
Vector scale_vec(Vector vec, double scalar);
Vector subtract_vec(Vector vec1, Vector vec2);
double get_magnitude(Vector vec);
#endif