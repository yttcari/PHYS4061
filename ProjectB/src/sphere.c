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

Sphere create_sphere(Point centre, double radius){
    Sphere s;
    s.centre = centre;
    s.radius = radius;

    return s;
}

bool hit_sphere(Sphere sphere, Ray ray, double tmin, double tmax, hit_record *rec){
    Vector ray_displacement = subtract_vec(point2vec(sphere.centre), point2vec(ray.origin));

    double a = dot(ray.direction, ray.direction);
    double b = dot(ray.direction, ray_displacement);
    double c = dot(ray_displacement, ray_displacement) - sphere.radius * sphere.radius;

    double discriminant = b * b - a * c;
    
    if (discriminant < 0){
        return false;
    } else {
        discriminant = sqrt(discriminant);
        double root = (b - discriminant) / a;

        if ((root < tmin) ||  (root > tmax)){
            root = (b + discriminant) / a;
            if ((root < tmin) ||  (root > tmax)){
                return false;
            }
        }

        rec->t = root;  
        rec->p = vec2point(ray_at(ray, root));
        rec->n = scale_vec(subtract_vec(point2vec(rec->p), point2vec(sphere.centre)), 1/sphere.radius);

        return true;
    }
}

// Organize all Sphere object
typedef struct{
    Sphere s[MAXOBJECT];
    // Return the last index
    int n;
} sphere_list;

void add_sphere(Sphere s, sphere_list *s_list){
    s_list->s[s_list->n] = s;
    s_list->n = s_list->n + 1;
}

bool check_hit_sphere_list(sphere_list s_list, Ray r, double tmin, double tmax, hit_record *rec){
    hit_record temp_rec;
    bool hit_anything = false;
    double closest_t = tmax;

    for(int i=0;i<s_list.n;i++){
        if (hit_sphere(s_list.s[i], r, tmin, closest_t, &temp_rec)){
            hit_anything = true;
            closest_t = temp_rec.t;
            rec->n = temp_rec.n;
            rec->p = temp_rec.p;
            rec->t = temp_rec.t;
        }
    }

    return hit_anything;
}

sphere_list init_sphere_list(){
    sphere_list s_list;
    Sphere sphere = create_sphere(to_point(0, 0, 0), 0);
    for(int i=0;i<MAXOBJECT;i++){
        s_list.s[i] = sphere;
    }
    s_list.n = 0;

    return s_list;
}