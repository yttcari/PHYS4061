#ifndef SPHERE_H
#define SPHERE_H

#include <stdio.h>
#include <math.h>
#include "obj.h"
#include "ray.h"
#include "mathlib.h"
#include "hittable.h"

#define MAXOBJECT 10

typedef struct{
    Point centre;
    double radius;
} Sphere;

typedef struct{
    Sphere s[MAXOBJECT];
    // Return the last index
    int n;
} sphere_list;

bool hit_sphere(Sphere sphere, Ray ray, double tmin, double tmax, hit_record *rec);
Sphere create_sphere(Point centre, double radius);

#define MAXOBJECT 10

sphere_list add_sphere(Sphere s, sphere_list *s_list);
bool check_hit_sphere_list(sphere_list s_list, Ray r, double tmin, double tmax, hit_record *rec);

sphere_list init_sphere_list();

#endif