#include <stdio.h>
#include "camera.h"

int main(){
    Camera cam = init_Camera(1, 400, 1, 2, to_point(0, 0, 0), 1, 1);
    sphere_list s_list = init_sphere_list();

    add_sphere(create_sphere(to_point(0, -100, 0), 95), &s_list);
    add_sphere(create_sphere(to_point(0, 0, -1), 0.5), &s_list);

    render("image.ppm", cam, s_list);
 
    printf("Finish rendering\n");
}