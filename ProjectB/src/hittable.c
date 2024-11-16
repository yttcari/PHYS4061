#include <stdio.h>
#include "obj.h"
#include <math.h>
#include "sphere.h"
#include "math.h"
#include "ray.h"


hit_record init_rec(){
    hit_record rec;

    rec.p = to_point(0, 0, 0);
    rec.n = to_vector(0, 0, 0);
    rec.t = 0;

    return rec;
}