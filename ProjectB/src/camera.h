#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "color.h"
#include "obj.h"
#include <stdbool.h>

#ifndef CAMERA_H
#define CAMERA_H

typedef struct{
    double aspect_ratio;
    int width;
    int height;
    double focal_length;
    int viewport_height; 
    int viewport_width;   
    Vector viewport_u;
    Vector viewport_v;
    Vector pixel_du;
    Vector pixel_dv;
    Point viewport_origin;
    Point pixel_origin;
    Point camera_centre;
    //Point viewport_origin;
    //Point pixel_origin;
} Camera;

Camera init_Camera(double aspect_ratio, int width, double focal_length, int viewport_height, Point centre, int sample_ray_per_pixel, int max_depth);

void render(char *path, Camera cam);
#endif