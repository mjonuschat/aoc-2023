#!/usr/bin/env python
# coding: utf-8

# In[1]:


INPUT = """
.##.#....####..
###....###...##
.....###..#####
.....###..#####
###....###...##
.##.#....####..
#.#..#.#...#.##
##..#.##.#.##..
.#.#.#.#..#.###
.#.###.#..#..##
.#..#.....#.###
..###.###..##..
...#.#..#..####
#.####.##..#.##
..##.##.###.###
#.#.##.#..#.###
#..###...###.#.

....##..##...
..#..####..#.
.############
.############
..#..####..#.
....##..##...
###......#.##

.##..#..#.###
.##.#...#..##
..#.######.#.
.......#.....
.......#.....
..#.######.#.
.##.#...#..##
.##..#..#.###
####.#####.#.
####.#####.#.
.##.....#.###

#..##.##.
#...###..
##..###.#
##.##..##
##.##..##
##..###.#
#...###..
#..##.##.
##.##.###
..##.....
..#...###
..##..#..
..#...#..
..#...###
..##.....

..##.##.##...
##.#......###
..########...
#####..######
..#......#...
.####..####..
#....##....##
....#..#.....
#...####...##
##.#....#.###
#...#..#...##
#####..######
##..#..#..###
.#...##...#..
..#.#..#.#...

.####..
.####..
##..###
..##...
.####..
##..###
#.##.#.
.####..
#####.#

#.#..##..#.#..###
#.##.##.##.#.####
#.#......#.#.#...
#..........#.####
.##########..#.##
#..######..####..
##...###..##.####
#..........######
#.########.#..#..
.#..#..#..#.###..
.##..##..##..#...
#.########.#..#..
...#....#...#..##

#......
.#.#.#.
.##..##
.##...#
.#.#.#.
#......
#.###..
#.###..
#......
.#.#.#.
.##...#

.##.##.
#.##..#
....##.
#..####
##.#..#
####..#
.#.....
##.#...
..#.##.
###.##.
###.##.

....#.##.
#.#....#.
#.#....#.
....#.###
.#....###
.####.##.
...##....
##.######
.##.#....
#..#.##.#
.####.###
#...####.
#...####.

..##...###..#..#.
..##...###..#..#.
####.#.#.#..#.#.#
..###.#....#.####
##.###.#####...##
...#.#...##..#...
...#..###....#..#
###.....#......#.
#.###...#####.##.
..###.#.##..#..#.
..#####.#.#......
###....#.#.#..##.
..#.####.##.#....

.###..#.#
.###..#.#
..##.##.#
#.#####.#
#.#.#####
.###.....
##.#.##.#
.#.###.#.
#.####.##
#.####.##
.#.###.#.
##.#.##.#
.###.#...

########.
...#.#.##
#..#####.
#..#.....
..##.#...
..##...#.
..##...#.
..##.#...
#.##.....
#..#####.
...#.#.##
########.
##.##.###
....#####
..#.....#
..#.....#
....#####

....##....#
.##.#.####.
#..#.######
#..###.##.#
....#.#..#.
#.#########
....##....#
#..##......
#####..##..
#..#..####.
.##...#..#.

........#......
.........#.####
##....##....#..
.##..##...##..#
.##..##.##...#.
########.####.#
########.####.#
.##..##.##...#.
.##..##...##..#
##....##....#..
.........#.####
........#......
.#...##.#.#...#
#.#..#.#....##.
###..####.####.
#......#...##.#
##########...##

##.#.#..#####
##.###.#.#...
.....##..#...
####.######..
.##..###.#.##
#.####.####..
.#...#..#.#..
.###.##..#.##
##.##...#####
#..####.#####
...##.....###
#.#...###..##
#.#...###..##
...##...#.###
#..####.#####

....#..##.#..####
#.##.######.###.#
#####.#.#.#.#....
#####.#.#.#.#....
#.##.######.###.#
....#..####..####
..##.#####.....##
#.#.#....###.#..#
..#...#.##.####..
.##...###.#.###..
.##...###.#.###..

.###.#..#.###..
#.#.#.##.#.#.##
..#.######.#...
..#...##...#...
#.##.####..#.##
##.########.###
..#..####..#...
#.##......##.##
##.#..##..#.###

##.#........#.###
###..##..##..####
#..#..#.....#..##
...#.##..##.#....
#..#..#..#..#..##
...###.##.###....
#.#####..#####.##
....########.....
..#.#..##..#.#...
.#.###.##.###.#..
..##..####..##...
#.#..#....#..#.##
.#..##.##.##..#..
####..####..#####
##.#.##..##.#.###

#.#.##.#.###..#
##......###.##.
....##...##....
####..######..#
.##....##.#####
#........#.....
##......####..#

..###.#..####
..###.###..##
..###.###.###
..#.#..#....#
..#.#..##...#
..###.###.###
..###.###..##
..###.#..####
###..#...#.##
###....#.#.#.
...#.###..##.
######.###..#
##......#..#.

.#######.##.#####
.#...#........#..
##...###....###..
##...###....###..
.#...#........#..
.#######.##.#####
#.####..####.####
#.##..########..#
.#.#...#....#...#
..###..#....#..##
...#.#..#..#..#.#

##.#...##...#
...#.#....#.#
###.#.####.#.
..###.####.##
##.#.#....#.#
##..#..##..#.
......####...
##.#.#....#.#
..#.##....##.
......#..#...
...##.####.##
..#....##....
##...######.#

............#.#
##.#....#.###..
.##.#..#.##...#
###########..##
....####....##.
#..##..##..##..
####....####.#.
...#.##.#......
#..#....#..###.
.#........#.###
.#.#....#.#...#
.##......##.###
....####....#..
##.#....#.##.##
#..######..###.
#...#..#...###.
#...#..#...###.

.#..#.#.#
.#..#.#.#
....##..#
#.#######
##..#..#.
.#.#.#..#
...#....#
.###..#.#
...#..###
.#.##.##.
#####...#
#####...#
.#.##.##.
...#..###
.####.#.#
...#....#
.#.#.#..#

##.#.#.
###..##
##.#.##
.###...
.###...
##.#.##
###..##
##.#.#.
...###.
.#.###.
##.#.#.
###..##
##.#.##

.####..##
.#.##..##
##.######
.....##..
###..##..
....#..#.
##.######
....####.
.#.#....#

#.#..#.#.##..##
........#.#####
...##....#..##.
.#.##.####.###.
########.#.#.##
##.##.##..##..#
..#..#..##..#.#
..#..#..##..#.#
##.##.##..##..#

..#...#.#######
#.##....#..##..
..###..########
#....#.##..##..
#....####..##..
..###..########
#.##....#..##..
..#...#.#######
..####.###....#
#####.###.####.
.##..####......
...##...##.##.#
#...###..######

#..#...#..#
#......#..#
.##......#.
####..#.###
..##..##...
#.##.#.#..#
#...##.###.
##.#...##..
##..###...#
##..###...#
##.#...##..
#...##.###.
#.##.#.#..#

.########....##..
###.##.###.##..##
..#.##.#..##.##.#
.##....##..######
##.#.##.##..####.
##.#..#.##.#....#
..######.........

.##..##.#.#..#.
#......########
#########......
#########.####.
###..###.#.##.#
##.######.####.
##.##.##.......
.######..#....#
..####...##..##
########..#..#.
..#..#..##.##.#
#.#..#.###....#
...##....#....#
...##....#.##.#
#......##..##..
#########.#..#.
...........##..

#....#..#.#.##.
...##.#...#####
...##.#....####
#....#..#.#.##.
..###.###...##.
#..##..##.##..#
##...#......##.
.####.#..#.....
.##.##.#....##.
.#..#..#.##.##.
##.##.###......
#..#.....##....
#.#..#..#..####
.###.#.#...####
...#....#######
..#.#.#...#.##.
...#........##.

.......##.......#
#..###....###..#.
####.######.#####
....###..###.....
.##..#....#..##..
.##..#....#..##..
#####.####.######
.##.###..###.##.#
.##.#..##..#.##..
#..#........#..##
####.##..##.#####
###.##.##.##.###.
....###..###.....

.....#........#
.....#........#
..###...#.#.#..
##.#.##....#..#
###..#.#.####.#
.###....#..#..#
...#.#.#.#..##.
...#.#.#.#..##.
.###....#.....#

#####.#
.....##
#####..
#####..
#..####
####.##
....#..
....#..
####.##
#..####
######.

##.##.#######
.###.#...##..
###.##...##..
..#.#....##..
#..###.######
.#.#.#.#....#
...#...##..##
..##.##......
..##.####..##
.##.##.##..##
.#####.######

....##...
..#....#.
....##...
####..###
####..###
##.#..#.#
..#....#.
###.....#
..#....#.
..##..##.
...####..

#########....
##.##.####...
.#....#..#...
#.#..#.##.#..
.##..##..#...
.########....
#.####.#.....
#..##..#.##..
########.....
.######.#####
.######...#..
..####..##...
#.####.#.####
#.####.#.....
...##......##

...##.##.....#.
..###.##.....#.
....##.#..###.#
..####.#.###.#.
##...##..###.#.
##.####...##..#
###.##.####.#.#
...#....#.#....
##.#####..##.##
....##.#.###...
##.#.####.#.###
......##..##.##
####.#..####..#

.##..#.##
#..##.##.
#..##.###
.##..#.##
####..##.
....#.###
.##...#..

...#..##..#..#..#
.#.#..##..#..#..#
#......#.#.##.#.#
#...####.#.##.#.#
...###.###....###
...#.#...######..
#..####..........
..##..##.#.##.#.#
##.#.#..#..##..#.

####.#..#.####.
.##..####..##..
##.##.##.##.###
..###.#..###...
##.#..##..#.##.
##..######..##.
...###..###...#
...###..###...#
##..######..##.
##.#..##..#.##.
..###.#..###...

..##..##..#.##..#
.####.###########
.#..#.##........#
.####.##..#..#..#
##..##.#.#.##.#.#
#....#..###..###.
......#..........

#.#..##.###..##
####.#.#..#..#.
..##.#..###..##
.#..##..##.##.#
.#..#...#######
##.#.#####.##.#
#.#.......#..#.
#.#...#........
#...#...#######
#.#...#.#.#..#.
.#...#..#.#..#.
##.#..##..#..#.
####..##..#..#.

####..#...###..#.
.##.#.#.##.######
..#.##...######.#
##.##..##.#####.#
#.##....#........
#.##....#........
##.##...#.#####.#
..#.##...###...##
..#.##...###...##
##.##...#.#####.#
#.##....#........
#.##....#........
##.##..##.#####.#

####..###.######.
#....##.####..###
#....##.####..###
####..###.######.
#..#.####.#.##.#.
#####....#..##..#
.#.#...#...#.##..
...##.#.#..#..#..
#.#.#..#.#......#
#.####.##........
#.###...#..#..#..
.#####.#.########
....#..#...####..
.#..#.#.##.####.#
..##..#.#.#....#.
.##.#..###.####.#
.#....#..########

#..##...#..#....#
####.#.#....#..#.
.#.....###.######
..####.##.##.##.#
..####.##.##.##.#
.#.....##########
####.#.#....#..#.
#..##...#..#....#
#...######.######
##..#.#...##....#
#....###.####..##
#...##..###.####.
.###..#....#.##.#

..##.#..#.##...
..#.#....#.#...
..#.#....#.#...
..##.#..#.##...
.####.##.####.#
#.#.######.#.##
#.#.#.##.#.#.##
..###.##.###.##
#..##.##.##..##
##.##.##.##.##.
##..##..##..##.

#.###.##.#.#.##.#
#..####....######
##...##..###....#
####..#.###.#..#.
##.##...#.#..#...
...#...##.#..##..
###.#.#.#.#..##..
..#..##.##.#.##.#
.##.####.#.......
.##.####.#.......
..#..##.##.#.##.#
###.#.#.#.#..##..
...#...##.#..##..

....##...
....##...
####.#..#
.##.#.#..
..#.###.#
.##.#.###
#####.###
.##.###..
#####.##.

.#.#......#######
###.###....#.####
#...#.#.##...####
.###.#..##...####
#####....####....
#.##..##.#...####
#.#.###.#.....##.
.##.###.#..#.....
###..#..##.#.####
..#.#.#..#.#.....
.###....#........
####.#..##..#....
#.##....#..#.####
.###.###.#..#####
.##..#.#..#######

...#.####
....###.#
#.#.#...#
#.#.#...#
....#.#.#
...#.####
##.#..#.#
##..#....
.#....###
##...#.##
##...#.##
.#....###
##..#....
##.#..#.#
...#.####
....#.#.#
#.#.#...#

##..##..#######
..######.......
....##....####.
....##....####.
#..#..#..######
#.#....#.##..##
###....########
###....###....#
.#......#..##..
...####...#..#.
#.#....#.######
#.#####..##..##
..#....#..#..#.
####..#########
...#..#...#..#.

####...####
####...####
##...#....#
.####..####
...##..#...
.##.#.#..#.
##..#..#..#
#.#..##.#.#
.#..##..#.#
##.#####...
####.####..
####.####..
##.#####...
.#..##..#.#
..#..##.#.#

#.#.#.#.###
#...#.#.###
.######.#.#
####......#
..#.##.###.
.##...###..
.##...###..
..#.##.###.
####......#
.######.#.#
#...#.#.###

##..#.#
...#.##
...#.##
.#..#.#
####..#
.#####.
.#####.

#.##.#.##....
#######..####
....#.#.##..#
..##..##..##.
......###....
.#..#.###....
#######.##..#
########.....
.#..#.##.####
#.##.#...####
#....#.#.#..#
##..##...####
##..##.######

#..##.#..##
##.##.#.###
####....#..
####....#..
##.##.#.###
#..##.#..##
#...#....#.
...##.####.
##..##...##
.#...#.#...
.###.#.##.#
#..###..##.
#..###...#.
.###.#.##.#
.#...#.#...

..#.####.#..##.
.....##.....###
..#.#..#.#...#.
##.#....#.####.
.#........#.#.#
...##..##...##.
###.####.###..#
###......######
####.##.####.##

...##....####....
########..##..###
########......###
#......#..##..#..
#.#..#.#..##..#.#
#.#..#.########.#
...##...######...
.#....#.######.#.
#..##..##.##.###.
#########....####
##....###....###.

..#.##..######..#
..#.##..######..#
##.##..#..##..#..
#...#.#..####..#.
.....#..######..#
.#.##.####..####.
#...#.#.#....###.
##...#####..#####
..#..#.#..##..#.#

.......####
##..##.#.#.
##..###.#..
#.##.##..##
#....##..##
.####.##...
#######....
##..###....
.#..#.##...
.#..#.#..##
......###..
..##....#..
##..####.##

.##....#.
####....#
.##..##..
...##..##
...##..##
.##..##..
####....#

#.#.#.#.###
...##.....#
.######.##.
......#.##.
.#####.#...
.#...##...#
.#...##...#
.#####.#...
.#....#.##.
.######.##.
...##.....#
#.#.#.#.###
##.#.##.#.#
.#.##..#.#.
.#....###..
.#....###..
.#.##..#.#.

#....#.####..
#.####.###..#
.#..#.#..#.#.
#.#..#....##.
#######..####
.#.#####.###.
.#.#####.###.
#######..####
#.#..#....##.
.#..#.#..#.#.
#.########..#
#....#.####..
#....#.####..

.#...###.##.#
.......######
.##.##..#..##
....#.#...#..
.##.###..#.##
.##.####..#.#
####.###.#..#
#..#.#....###
....##.....#.
....##.....#.
#..#.#....###

.##.##..#......
.#.#.....##.###
.#.#.....##.###
.##.##..#......
...#..##..#.#.#
#####.#....#.##
#####.###.#.###
..#.#.#.#..##..
..#.#.###..#...

#.#...##.##..
####.##.#####
#...#....#.##
##..####.##..
##.#.#..#....
.##..##.#..##
.#..#.##.####
.#..#.....#..
#######.#####
##.##..#.....
##.##........
#######.#####
.#..#.....#..
.#..#.##.####
.##..##.#..##
##.#.#..#....
##..####.##..

..#.###..###.#..#
..#.###..###.#..#
......#..#.......
.#..##....##..#..
.#.#...##...#.#.#
..#.#......#.#...
##............##.
#.##........##.##
..###.#..#.###...
.#....#..#....#..
#...#.#..#.#...##
######.##.######.
.#.##########.#.#
##.#.#.##.#.#.##.
.#.#.##..##.#.#..
#.############.##
#####......###.#.

#..#...
..#####
.#....#
.#..###
#...###
.#.####
.#.#...
...####
.#.##..
..###..
...##..
...##..
..###..
.#.##..
...####

#.#######....#.#.
#..#.##.##......#
...#.##.##......#
#.#######....#.#.
#.#######....#.#.
...#.##.##......#
#..#.##.##......#
#.#######....#.#.
##.#.#######....#
###.###...##.#...
#..#....#####....
..#.#..##.......#
###.######.#.#.#.
.#.#####.........
...##.#..######..
.###.#.##..#####.
#...#.#..#.###.##

#...#.#
####...
####...
#...#.#
.....##
..##.##
.##...#
..##...
#.##.##
..###..
..###..
#.##.##
..##...
..#...#
..##.##

.#..#..##.#...##.
.#..#..##.#...##.
#.#.#####..####.#
....#.##....#.##.
.##.##.#.####....
###..###.....####
#.##.#..##.......

.#.#.###.#.##
#.###..#.#.##
#####.#.###..
#####.#.###..
#.###..#.#.##
.#.#.###.#.##
#....##..#...
#...####..###
##.#.###..#.#
##..#...#.###
##..#...#.###
##.#.###..#.#
#...####..###
#....##..#...
.#.#.###.####

.##.##.
#..#.#.
######.
#..#...
#..#..#
#..#..#
#..##..
######.
#..#.#.

.##.#.##.#..#.##.
.##.#.##.#..#.##.
###.#.##.#.##....
#.#.##.....#.####
##..#.##.#######.
....#.##.#.###..#
..#......#.##....
.#......###.#.##.
#..#.###.#...#..#

...##...#..##
#.####.###...
...##.....#..
.#.##.#..##..
##....###....
........#..##
#......####..
#..##..#.....
###..###..###
.######..#...
#.####.....##

##....##..##..##.
...#####.#..#.###
####.##.######.##
..##...#..##..#..
##.#...########..
..##....##..##...
..#.#############
..####....##....#
###....##....##.#
..##.###.#..#.###
##...#.#......#.#
##..##.###..###.#
...#.#...####...#
...#...##.##.##..
###..##.##..##.##
..#.#..##....##..
..###.###....###.

........#.###
..##...#####.
.####.#.##..#
.####.#..#.#.
##..####..#.#
##..##..#...#
##..##..#...#
##..####..#.#
.####.#..#.#.
.####.#.##..#
..##...#####.
........#.###
######.#.#..#
##..####..###
#....#..#....
#.##.#.#....#
##.####.###.#

#.#..#.#.#.#.####
###..#####....##.
#..##..##..###..#
#.######.###.#..#
########..#..####
.#.##.#.##...####
#.####.#.#..##..#
##....##..#..#..#
..####...##..#..#
#.####.#.#.......
...##...###..#..#
.#....#.###..#..#
..#..#..#.#..####

...#...###.#.#...
.......#....#..##
.##.....##.####..
.#..######.#.##..
.#####.....###...
.#...###..###..##
###.#..#....##...
.#.####.#.#..#.##
#.####..##.#.####
#.#.##..##.#.####
.#.####.#.#..#.##

.##.#....#..#..#.
#....####....#...
#.#...##...#.####
.#...####...#.###
#.##.####.##.#.##
.#.##.##.##.#.#.#
#..###..###..##.#
#..###..###..##.#
.#.##.##.##.#.#.#
#.##.####.##.#.##
.#...####...#.###

.#..#.##...
.##..###...
####..##.##
.......#.##
.##.#.#....
....####...
.##.#...#..
####.#.##..
.##..##..##

.#.####..
#..######
##.##....
.##.##...
.##.##...
##.##....
#..######
.#.####..
#..#..###
.#...####
##.......
##....#..
#..#...##
.###..###
#...#...#
.#..#....
#.###....

.##.###.###.###
.#####.##.#..##
.#####.##.#..##
.##.###.#######
.#.##....##.###
##.###..#...###
.#...#.#####.##
##.###...######
.#.#.##....##..
##.#.#.##..#...
###.##..##.#...
#####....###...
#....#......###

.###...#.###.
#...#.#.....#
#...#.#.....#
.###...#.###.
.#..#....#..#
#..###.##.#..
#.##..#..#...
#.######...#.
#.######...#.
#.##..#..#...
##.###.##.#..
.#..#....#..#
.###...#.###.

......####.#...#.
......##.##..#.#.
.#..#..#.####...#
.#..#..##.##.####
#.##.###..##..###
#######.##..###..
#.##.#....##..#..
..##...###.######
......##..##...##
......#.#...#.###
......#.#...#.###
......##..##.#.##
..##...###.######

#..#..#..
.....####
.##.#...#
.##.#...#
.....####
#..#..#..
##.##.#..
#..#..#..
......#.#
.##...#..
####...#.
#####.#.#
#..#..#..
.##..#...
#####....
#..#.####
.......#.

.....#.#.
###...#..
..#..#.##
..###.##.
##.##....
##.##....
..###.##.
..#..#.##
###...#..
....##.#.
...######

...##.##.#..####.
...##.##.#..####.
#.####..#..#.....
#..........#....#
..#.##...#..#..#.
.#...##..#.#.##.#
.#.#..##...##..##
#...#...#########
.#.##.#..###....#

..#.##.
....###
.....##
##...##
...#...
##..##.
###....
...##.#
##..#..
..##..#
..##..#
##..#.#
...##.#

#..#..#......#..#
#..#..#......#..#
###.######.#..#.#
.#.####.#.#####..
##..####..###.#..
.##...###.#.#.##.
...#....#.#.#####
##.#..####..#....
##.#..###..#..##.
##.#..###..#..##.
##.#..####..#....
...#....#.#.#####
.##...###.#.#.##.
##...###..###.#..
.#.####.#.#####..
###.######.#..#.#
#..#..#......#..#

..#...#.#.##.
.###.#....##.
.##.#..######
#.##.##.#....
#######..####
#.#.##..#....
##.#..#.##..#
..#....######
......#######
......#######
..#....######
#..#..#.##..#
#.#.##..#....
#######..####
#.##.##.#....
.##.#..######
.###.#....##.

##..#..#..#
...#...##..
###..##..##
..#..##..#.
###.####.##
###..##..##
##.#.##.#.#
##.######.#
..########.

##..###
####.##
.#.#...
.....##
..#.###
..#.###
###....
##.....
##...##
..#....
##.#...
###.#..
..#.###

..##....#
...####.#
...##..##
#####..##
...######
####....#
.....##..
...#.##.#
##.#....#

####...#.#.......
#.#.####.####...#
..#.##.#...##....
..#.##.#...##....
#.#.####.####...#
####...#.#.......
#..#.#..#.#.#.##.
.#....#....#..###
..#.##.#...#.#.#.
..#.##.#...#.#.#.
.##...#....#..###
#..#.#..#.#.#.##.
####...#.#.......

#.######.
#.#....##
.#..#.###
.#..#.###
#.#....##
#.######.
......#.#
.#....#.#
#.######.
#.#....##
.#..#.###

.##...#..#...##..
##..#.####.#..###
#......#.......##
##..#..##..#..###
..###..##..###...
#..#..####..#..##
#.##.#....#.##.##
#.##.#....#.##.##
.###.#....#.###..
"""


# In[5]:


import numpy as np


def parse_block(block):
    return np.array([[c == "#" for c in line] for line in block.splitlines()])


def mirrored(block):
    for i in range(1, block.shape[0]):
        side2 = block[i : i + i, :]
        side1 = block[i - side2.shape[0] : i, :]
        if np.array_equal(side1, np.flip(side2, axis=0)):
            return i
    return 0


def smudged(block, index):
    p1 = []
    p2 = []
    for i in range(1, block.shape[0]):
        side2 = block[i : i + i, :]
        side1 = block[i - side2.shape[0] : i, :]
        if np.array_equal(side1, np.flip(side2, axis=0)):
            p1.append(i)
        if np.sum(side1 != np.flip(side2, axis=0)) == 1:
            p2.append(i)

    if not p2:
        return 0

    if p1 == p2:
        print("EQ", index)
        
    if len(p2) > 1:
        print("MULTI", index)
        
    return p2[0]


def day13_puzzle1(blocks):
    r = sum(mirrored(block) for block in blocks)
    c = sum(mirrored(np.transpose(block)) for block in blocks)
    total = 100 * r + c
    print(f"Part 1: {total}")


def day13_puzzle2(blocks):
    r = sum(smudged(block, i) for i, block in enumerate(blocks))
    c = sum(smudged(np.transpose(block),i) for i, block in enumerate(blocks))
    total = 100 * r + c
    print(f"Part 2: {total}")


blocks = list(map(parse_block, INPUT.strip().split("\n\n")))
day13_puzzle1(blocks)
day13_puzzle2(blocks)


# In[ ]:



