#!/usr/bin/env bash

. gen.sh

use_solution sl.cpp

compile gen_random.py

samplegroup
limits n=100 m=100
sample 1
sample 2
sample 3

group group1 50
limits n=100 m=100
include_group sample
tc small0 gen_random n=100 m=100
tc small1 gen_random n=10 m=10
tc small2 gen_random n=10 m=100
tc small3 gen_random n=3 m=100
tc small4 gen_random n=100 m=3
tc small5 gen_random n=2 m=1
tc small6 gen_random n=10 m=3
tc small7 gen_random n=100 m=16
tc small8 gen_random n=100 m=15
tc small9 gen_random n=100 m=15
tc small10 gen_random n=100 m=15
tc small11 gen_random n=100 m=15
tc small12 gen_random n=100 m=15

group group2 150
limits n=100000 m=2000000000
include_group group1
tc rich gen_random n=2 m=20000000
tc large0 gen_random n=100000 m=2000000000
tc large1 gen_random n=100000 m=400000
tc large2 gen_random n=100000 m=300000
tc large3 gen_random n=100000 m=300000
tc large4 gen_random n=100000 m=300001
tc large5 gen_random n=100000 m=10000
tc large6 gen_random n=100000 m=1
tc large7 gen_random n=100000 m=14
tc large8 gen_random n=100000 m=7
tc large9 gen_random n=100000 m=18
