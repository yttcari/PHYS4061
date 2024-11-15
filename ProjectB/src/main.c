#include <stdio.h>
#include "camera.h"

int main(){
    Camera cam = init_Camera(1, 100, 1, 2, to_point(0, 0, 0), 1, 1);
    print_vec(point2vec(cam.viewport_origin));
    render("image.ppm", cam);
    printf("Finish rendering\n");
}