#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "color.h"
#include "mathlib.h"
#include "obj.h"
#include <stdbool.h>

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
    //int sample_ray_per_pixel;
    //int max_depth;
} Camera;

Camera init_Camera(double aspect_ratio, int width, double focal_length, int viewport_height, Point centre, int sample_ray_per_pixel, int max_depth){
    Camera cam;

    cam.aspect_ratio = aspect_ratio;
    cam.width = width;
    cam.height = round(width / aspect_ratio);

    cam.focal_length = focal_length;
    cam.viewport_height = viewport_height;
    cam.viewport_width = viewport_height * width / round(width / aspect_ratio);

    cam.viewport_u = to_vector(cam.viewport_width, 0, 0);
    cam.viewport_v = to_vector(0, -viewport_height, 0);

    cam.pixel_du = scale_vec(cam.viewport_u, 1./width);
    cam.pixel_dv = scale_vec(cam.viewport_v, 1./cam.height);

    cam.camera_centre = centre;

    Vector viewport_origin;
    viewport_origin = subtract_vec(point2vec(centre), to_vector(0, 0, focal_length));
    cam.viewport_origin = vec2point(subtract_vec(viewport_origin, add_vec(scale_vec(cam.viewport_u, 0.5), scale_vec(cam.viewport_v, 0.5))));

    cam.pixel_origin = vec2point(add_vec(point2vec(cam.viewport_origin), scale_vec(add_vec(cam.pixel_du, cam.pixel_dv), 0.5)));
    
    printf("Resolution: %d * %d\n", cam.width, cam.height);
    return cam;
}

void render(char *path, Camera cam){
    FILE *fpt;

    fpt = fopen(path, "w");

    fprintf(fpt, "P3\n");
    fprintf(fpt, "%d %d\n", cam.width, cam.height);
    fprintf(fpt, "255\n");


    for(int j=0;j<cam.height;j++){
        for(int i=0; i<cam.height;i++){
            Vector pixel_centre = add_vec(point2vec(cam.pixel_origin), add_vec(scale_vec(cam.pixel_du, i), scale_vec(cam.pixel_dv, j)));
            Vector ray_direction = subtract_vec(pixel_centre, point2vec(cam.camera_centre));
            Ray r;
            r.origin = cam.camera_centre;
            r.direction = ray_direction;

            Color pixel_color = bg_color(r);
            write_color(pixel_color, fpt);
        }
    }

    fclose(fpt);
}
