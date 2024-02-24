#!/usr/bin/env python
# coding: utf-8

# In[12]:


INPUT = r"""
#.###########################################################################################################################################
#.........#...###.....#...#...###...#...#.....#.....#...#...###.......#...#...#...###.......###...#...#...#...#.....#####...........#...#...#
#########.#.#.###.###.#.#.#.#.###.#.#.#.#.###.#.###.#.#.#.#.###.#####.#.#.#.#.#.#.###.#####.###.#.#.#.#.#.#.#.#.###.#####.#########.#.#.#.#.#
#.........#.#.....#...#.#.#.#...#.#.#.#.#...#.#.#...#.#.#.#...#.....#.#.#.#.#...#...#.....#.....#.#.#.#.#.#.#.#.#...#.....#.........#.#.#.#.#
#.#########.#######.###.#.#.###.#.#.#.#.###.#.#.#.###.#.#.###.#####.#.#.#.#.#######.#####.#######.#.#.#.#.#.#.#.#.###.#####.#########.#.#.#.#
#.....#...#...#...#.###.#.#.#...#.#...#.....#.#.#...#.#.#.#...#.....#.#.#.#.....#...#...#...#.....#.#.#.#.#.#.#.#...#.....#...........#...#.#
#####.#.#.###.#.#.#.###.#.#.#.###.###########.#.###.#.#.#.#.###.#####.#.#.#####.#.###.#.###.#.#####.#.#.#.#.#.#.###.#####.#################.#
###...#.#...#...#.#.#...#...#...#.........#...#.#...#.#.#.#.###.....#.#.#...#...#...#.#.###.#...#...#.#.#...#...#...#...#.#.................#
###.###.###.#####.#.#.#########.#########.#.###.#.###.#.#.#.#######.#.#.###.#.#####.#.#.###.###.#.###.#.#########.###.#.#.#.#################
#...#...###...#...#...#.........#.......#.#...#.#...#.#.#.#.#...###.#...#...#.....#...#.>.>.#...#.#...#.#.........###.#...#...###...#.......#
#.###.#######.#.#######.#########.#####.#.###.#.###.#.#.#.#.#.#.###.#####.#######.#######v###.###.#.###.#.###########.#######.###.#.#.#####.#
#.....#...#...#.#.......#...#.....#.....#...#.#.#...#.#.#.#...#.#...#...#.#...###.......#...#...#.#.#...#...........#.......#...#.#.#.#.....#
#######.#.#.###.#.#######.#.#.#####.#######.#.#.#.###.#.#.#####.#.###.#.#.#.#.#########.###.###.#.#.#.#############.#######.###.#.#.#.#.#####
#.....#.#.#.....#.......#.#.#.....#.#...###.#...#...#.#.#.#...#.#.#...#.#.#.#...#.......#...###.#.#.#.#.............#...###...#...#...#.....#
#.###.#.#.#############.#.#.#####.#.#.#.###.#######.#.#.#.#.#.#.#.#.###.#.#.###.#.#######.#####.#.#.#.#.#############.#.#####.#############.#
#...#...#...#...#.....#.#.#.#.....#.#.#...#.....#...#.#.#.#.#...#...#...#.#.###.#.###...#.....#.#.#.#.#...#.>.>.###...#.#.....#.......#.....#
###.#######.#.#.#.###.#.#.#.#.#####.#.###.#####.#.###.#.#.#.#########.###.#.###.#.###.#.#####.#.#.#.#.###.#.#v#.###.###.#.#####.#####.#.#####
###.....#...#.#.#...#...#.#.#.....#.#.#...###...#.#...#.#.#...#.>.>...#...#...#.#.#...#.......#.#.#.#...#...#.#...#...#.#.....#.#...#...#...#
#######.#.###.#.###v#####.#.#####.#.#.#.#####.###.#.###.#.###.#.#v#####.#####.#.#.#.###########.#.#.###.#####.###.###.#.#####.#.#.#.#####.#.#
#.......#...#.#.###.>...#.#...#...#...#.>.>.#.#...#.#...#...#...#...###.....#.#...#...........#.#.#.....###...###...#.#...#...#...#.#.....#.#
#.#########.#.#.###v###.#.###.#.#########v#.#.#.###.#.#####.#######.#######.#.###############.#.#.#########.#######.#.###.#.#######.#.#####.#
#.........#...#...#...#.#.#...#.#.....#...#.#.#.#...#...#...###...#.......#...###.......#.....#.#.#.........#...###.#.#...#...#...#...#.....#
#########.#######.###.#.#.#.###.#.###.#.###.#.#.#.#####.#.#####.#.#######.#######.#####.#.#####.#.#.#########.#.###.#.#.#####.#.#.#####.#####
#.........#.....#.....#...#...#.#...#.#...#...#.#.....#.#.#.....#.#...#...###...#.....#.#...###...#...........#...#...#.......#.#.......#...#
#.#########.###.#############.#.###.#.###.#####.#####.#.#.#.#####.#.#.#.#####.#.#####.#.###.#####################.#############.#########.#.#
#.....#.....#...#.......#...#.#.#...#.....#.....#.....#.#.#.#...#...#...#.....#.###...#...#.....#.................#...#...#...#.........#.#.#
#####.#.#####.###.#####.#.#.#.#.#.#########.#####.#####.#.#.#.#.#########.#####.###.#####.#####.#.#################.#.#.#.#.#.#########.#.#.#
#.....#.#.....###...#...#.#.#.#.#.........#.....#...###...#...#.........#.....#.....#...#.......#...............###.#.#.#.#.#.#...#.....#.#.#
#.#####.#v#########.#.###.#.#.#.#########.#####.###.###################.#####.#######.#.#######################.###.#.#.#.#.#.#.#.#v#####.#.#
#.......#.>.#.....#.#...#.#.#...#...#...#.#.....#...#...#...#...........#.....#.....#.#.....#...................#...#...#.#.#.#.#.>.#.....#.#
#########v#.#.###.#.###.#.#.#####.#.#.#.#.#.#####.###.#.#.#.#.###########.#####.###.#.#####.#.###################.#######.#.#.#.###v#.#####.#
#.........#...#...#.#...#.#.###...#.#.#...#.......###.#...#.#.......#...#.....#.###...#...#.#...........#.......#.......#...#...###...#.....#
#.#############.###.#.###.#.###.###.#.###############.#####.#######.#.#.#####.#.#######.#.#.###########.#.#####.#######.###############.#####
#...........#...#...#...#.#.....###...#...###.......#.#...#.........#.#.#...#...###.....#...#...#.....#...#.....#.......#...............#...#
###########.#.###.#####.#.#############.#.###.#####.#.#.#.###########.#.#.#.#######.#########.#.#.###.#####.#####.#######.###############.#.#
#...#####...#.....###...#...#...#.....#.#...#.....#.#...#...#.........#.#.#.........###...###.#.#.#...#...#.....#.....###.......#.........#.#
#.#.#####.###########.#####.#.#.#.###.#.###.#####.#.#######.#.#########.#.#############.#.###.#.#.#.###.#.#####.#####.#########.#.#########.#
#.#.......#...###...#...###...#.#.#...#...#.#...#.#...#...#...#.........#.............#.#...#.#...#.#...#...#...#...#.....###...#.#.........#
#.#########.#.###.#.###.#######v#.#.#####.#.#.#.#.###.#.#.#####.#####################.#.###.#.#####.#.#####.#.###.#.#####.###.###.#.#########
#.#.......#.#.....#...#.#...#.>.>.#.#...#.#.#.#.#...#.#.#.#...#.#.......#...#...#.....#...#.#...#...#.#.....#...#.#...#...#...#...#...#.....#
#.#.#####.#.#########.#.#.#.#.#v###.#.#.#.#.#.#.###.#.#.#.#.#.#v#.#####.#.#.#.#.#.#######.#.###.#.###.#.#######v#.###.#.###.###.#####.#.###.#
#.#.###...#.#.........#...#...#...#.#.#.#.#...#.#...#.#.#.#.#.>.>.#.....#.#.#.#.#...#...#.#.....#.#...#...#...>.>.###...###...#.#.....#.#...#
#.#.###.###.#.###################.#.#.#.#.#####.#.###.#.#.#.###v###.#####.#.#.#.###v#.#.#.#######.#.#####.#.###v#############.#.#.#####.#.###
#.#...#...#.#.#...........#.......#.#.#.#.....#.#...#.#.#...###.###.....#.#...#.#.>.>.#.#...#.....#.....#.#.###.............#...#.#...#.#.###
#.###.###.#.#.#.#########.#.#######.#.#.#####.#.###.#.#.#######.#######.#.#####.#.#v###.###.#.#########.#.#.###############.#####.#.#.#.#.###
#.....###...#...#.........#.#...###.#.#.#...#.#.#...#...###.....#.....#.#...###...#...#.#...#.....#...#.#...#.....#...#...#.....#...#...#...#
#################.#########.#.#.###.#.#.#.#.#.#.#.#########.#####.###.#.###.#########.#.#.#######.#.#.#.#####.###.#.#.#.#.#####.###########.#
###...#.........#.......###...#...#...#.#.#...#...#####...#.....#.#...#...#...#.......#...###.....#.#.#.###...###.#.#.#.#.#...#.#...........#
###.#.#.#######.#######.#########.#####.#.#############.#.#####.#.#.#####.###.#.#############.#####.#.#.###.#####.#.#.#.#.#.#.#.#.###########
###.#.#.......#...#...#.#.........#...#...###...#...#...#.#.....#.#.#...#.....#.#.......#...#...#...#...#...#.....#.#.#.#...#...#.........###
###.#.#######.###.#.#.#.#.#########.#.#######.#.#.#.#.###.#.#####.#.#.#.#######.#.#####.#.#.###.#.#######.###.#####.#.#.#################.###
#...#...#...#...#...#...#...#.......#.###...#.#.#.#.#...#.#.......#.#.#.###...#...#.....#.#.#...#...###...###.......#...###...#...#.....#...#
#.#####.#.#.###.###########.#.#######.###.#.#.#.#.#.###.#.#########v#.#.###.#.#####.#####.#.#.#####.###.###################.#.#.#.#.###.###.#
#.#...#...#.....#...#...###...#.......#...#.#.#.#.#...#.#.......#.>.>.#...#.#.#...#.#...#.#.#.......#...###...#...#...#.....#.#.#.#.#...#...#
#.#.#.###########.#.#.#.#######.#######.###.#.#.#.###.#.#######.#.#v#####.#.#.#.#.#.#.#.#.#.#########.#####.#.#.#.#.#.#.#####.#.#.#.#.###.###
#.#.#.#...#.....#.#...#.....#...#.....#...#.#.#.#...#.#.#.......#.#.#.....#.#.#.#.#.#.#.#.#.#...#...#.......#.#.#...#.#.....#...#.#.#.#...###
#.#.#.#.#.#.###.#.#########.#.###.###.###.#.#.#.###.#.#.#.#######.#.#.#####.#.#.#.#v#.#.#.#.#.#.#.#.#########.#.#####.#####.#####.#.#.#.#####
#...#...#...###.#.#.........#...#...#...#.#...#.#...#.#.#.......#.#.#...#...#.#.#.>.>.#...#.#.#.#.#.#.........#...#...#...#.#.....#.#.#...###
###############.#.#v###########.###.###.#.#####.#.###.#.#######.#.#.###.#.###.#.###v#######.#.#.#.#.#v###########.#.###.#.#.#.#####.#.###.###
###...#...#...#...#.>...#.....#...#...#.#...#...#...#.#.#.....#...#...#.#.###.#.###...#.....#.#.#.#.>.>.#.....#...#.#...#.#.#.#.....#...#...#
###.#.#.#.#.#.#####v###.#.###.###.###.#.###.#.#####.#.#.#.###.#######.#.#.###.#.#####.#.#####.#.#.###v#.#.###.#.###.#.###.#.#.#.#######.###.#
#...#...#...#...###.#...#.#...#...#...#...#.#...#...#.#.#...#.#...#...#.#.#...#.#...#.#.....#.#...#...#...#...#.#...#.#...#.#.#.....#...#...#
#.#############.###.#.###.#.###v###.#####.#.###.#.###.#.###.#.#.#.#.###.#.#.###.#.#.#.#####.#.#####.#######.###.#.###.#.###.#.#####.#.###v###
#...#.........#...#.#.....#...>.>.#.....#.#.#...#.#...#.#...#.#.#.#...#...#.....#.#...#...#...#...#.......#.#...#...#.#.#...#...#...#...>.###
###.#.#######.###.#.###########v#.#####.#.#.#.###.#.###.#.###.#.#.###.###########.#####.#.#####.#.#######.#.#.#####.#.#.#.#####.#.#######v###
###...#.......#...#...#.........#.......#...#.#...#...#.#...#...#.#...###.....###.......#.....#.#.........#.#...#...#.#.#.....#.#.#.......###
#######.#######.#####.#.#####################.#.#####.#.###.#####.#.#####.###.###############.#.###########.###.#.###.#.#####.#.#.#.#########
#.....#.......#...#...#...#.........#.......#...#...#...###.....#.#.....#...#.................#.....#.....#.#...#...#.#.#.....#.#.#.........#
#.###.#######.###.#.#####.#.#######.#.#####.#####.#.###########.#.#####.###.#######################.#.###.#.#.#####.#.#.#.#####.#.#########.#
#...#.#...#...#...#.....#...#.......#.#.....#...#.#.#...#.......#.......###.................#...###.#.#...#...#...#...#.#.....#...###.......#
###.#.#.#.#.###.#######.#####.#######.#.#####.#.#.#.#.#.#.#################################.#.#.###.#.#.#######.#.#####.#####.#######.#######
#...#...#...###.........#...#.........#.#...#.#...#.#.#.#...............###...#.............#.#.###...#.........#.....#.#...#.....#...#.....#
#.#######################.#.###########.#.#.#.#####.#.#.###############.###.#.#.#############.#.#####################.#.#.#.#####.#.###.###.#
#.#...#.......#.......###.#.............#.#...#.....#.#.........#.....#.#...#.#.#...........#.#.....#...#.......#.....#.#.#.......#.....#...#
#.#.#.#.#####.#.#####.###.###############.#####.#####.#########.#.###.#.#.###.#.#.#########.#.#####.#.#.#.#####.#.#####.#.###############.###
#...#...###...#.....#...#.#...#.........#.#...#.....#.........#...###...#...#.#...#.........#.#.....#.#.#...###...#...#...###.....#...#...###
###########v#######.###.#.#.#.#.#######.#.#.#.#####.#########.#############.#.#####.#########.#.#####.#.###v#######.#.#######.###.#.#.#.#####
#.......###.>...###...#.#...#...#...###...#.#.......#.........#...#...#...#.#.#...#...###...#.#.#...#.#.#.>.>.#...#.#.###...#.#...#.#.#.....#
#.#####.###v###.#####.#.#########.#.#######v#########.#########.#.#.#.#.#.#.#.#.#.###v###.#.#.#.#.#.#.#.#.#v#.#.#.#.#.###.#.#.#.###.#.#####.#
#.....#.....###.#...#.#...#.....#.#.#.....>.>.#...###...........#.#.#...#.#.#...#...>.>...#.#.#.#.#.#.#.#.#.#...#.#.#...#.#.#.#...#.#.#.....#
#####.#########.#.#.#.###.#.###.#.#.#.#####v#.#.#.###############.#.#####.#.#########v#####.#.#.#.#.#.#.#.#.#####.#.###.#.#.#.###.#.#.#.#####
#.....#...#...#...#.#...#...###.#.#.#.###...#...#...#...#.......#.#.....#...#...#...#.#.....#.#...#...#.#.#...###...#...#.#.#.#...#.#.#...###
#.#####.#.#.#.#####.###.#######.#.#.#.###.#########.#.#.#.#####.#.#####.#####.#.#.#.#.#.#####.#########.#.###.#######.###.#.#.#.###.#.###v###
#.......#...#.....#...#.......#...#...#...#.........#.#.#.#...#...#...#...#...#.#.#.#.#.....#.........#...###...#.....#...#.#.#...#.#...>.###
#################.###.#######.#########.###.#########.#.#.#.#.#####.#.###.#.###.#.#.#.#####.#########.#########.#.#####.###.#.###.#.#####v###
#.................###...#...#.#...#.....###.....###...#.#.#.#...###.#.#...#...#...#.#...#...#...#.....#.........#.#...#.###.#...#...#.....###
#.#####################.#.#.#.#.#.#.###########.###.###.#.#.###.###.#.#.#####.#####.###.#.###.#.#.#####.#########.#.#.#.###.###.#####.#######
#...#.................#...#...#.#...#.......###...#...#.#...#...#...#.#.#.....#...#.....#...#.#.#.#...#.........#.#.#.#.###.....#...#.......#
###.#.###############.#########.#####.#####.#####.###.#.#####v###.###.#.#.#####.#.#########.#.#.#.#.#.#########.#.#.#.#.#########.#.#######.#
#...#.#...............###...#...#...#.#.....#...#.#...#...#.>.>...###.#.#.......#.......#...#.#...#.#...........#.#.#.#.#.........#.......#.#
#.###.#.#################.#.#.###.#.#.#.#####.#.#.#.#####.#.#v#######.#.###############.#.###.#####.#############.#.#.#.#.###############.#.#
#.#...#.................#.#.#.....#...#.......#.#.#.###...#.#...#...#...#...#...#.....#.#...#.#.....#.....#...###...#.#.#...............#...#
#.#.###################.#.#.###################.#.#.###.###.###.#.#.#####.#.#.#.#.###.#.###.#.#.#####.###.#.#.#######.#.###############.#####
#.#.#...........#.......#.#...#...#.............#.#.#...#...###...#.....#.#...#...###.#...#...#...#...###...#.......#...#...#...###...#.....#
#.#.#.#########.#.#######.###.#.#.#.#############.#.#.###.#############.#.###########.###.#######.#.###############.#####.#.#.#.###.#.#####.#
#...#.....#...#...#.....#.#...#.#.#.....#...#####...#.#...#...#.........#.#.....#...#.....#.....#.#.#...#...........###...#...#.....#.......#
#########.#.#.#####.###.#.#.###.#.#####.#.#.#########.#.###.#.#.#########.#.###.#.#.#######.###.#.#.#.#.#.#############.#####################
###...###...#...###...#...#...#.#.......#.#.........#...#...#...#...#...#...#...#.#...#...#.#...#...#.#...#.......#...#...#...#...#.........#
###.#.#########.#####.#######.#.#########.#########.#####.#######.#.#.#.#####v###.###.#.#.#.#.#######.#####.#####.#.#.###.#.#.#.#.#.#######.#
#...#...........#.....#.......#...........#.........#...#.......#.#...#.#...>.>...#...#.#.#.#.###...#.#.....#.....#.#...#...#.#.#.#.#.....#.#
#.###############.#####.###################.#########.#.#######.#.#####.#.###v#####.###.#.#.#.###.#.#.#.#####.#####.###.#####.#.#.#.#.###.#.#
#...............#.....#.#...#...#...###.....#...#.....#.......#...#.....#...#.#.....###.#.#.#.###.#.#.#.#...#.......#...#...#...#...#...#...#
###############.#####.#.#.#.#.#.#.#.###v#####.#.#.###########.#####.#######.#.#.#######.#.#.#.###.#.#.#.#.#.#########.###.#.###########.#####
###...#.........#.....#.#.#.#.#.#.#...>.>...#.#.#.........#...#.....#...#...#.#.......#.#...#.....#.#...#.#.......#...#...#.#.....#...#.....#
###.#.#.#########.#####.#.#.#.#.#.#####v###.#.#.#########.#.###.#####.#.#.###.#######.#.###########.#####.#######.#.###.###.#.###.#.#.#####.#
#...#.#.......###.....#.#.#...#...###...#...#.#...#...#...#...#.....#.#.#.#...#.......#.......#.....#...#.....###...#...#...#...#...#.....#.#
#.###.#######v#######.#.#.###########.###.###.###.#.#.#.#####.#####.#.#.#.#.###.#############.#.#####.#.#####v#######.###.#####.#########.#.#
#...#.#...###.>.......#.#.#.........#...#...#...#.#.#.#.#.....#...#.#.#...#...#.#...#...#...#.#.#...#.#...#.>.>.#...#...#.#...#.........#...#
###.#.#.#.###v#########.#.#.#######.###.###.###.#.#.#.#.#.#####.#.#v#.#######.#.#.#.#.#.#.#.#.#.#.#.#.###.#.#v#.#.#.###.#.#.#.#########v#####
#...#...#...#.........#...#...#...#.#...###...#.#.#.#.#.#.#...#.#.>.>.#.......#.#.#...#.#.#...#.#.#.#.#...#.#.#...#...#.#.#.#.#.....#.>.#...#
#.#########.#########.#######.#.#.#.#.#######.#.#.#.#.#.#.#.#.#.###v###.#######.#.#####.#.#####.#.#.#.#.###.#.#######.#.#.#.#.#.###.#.#v#.#.#
#.........#...#.......###.....#.#.#...###...#...#.#.#...#.#.#.#.###...#.......#.#.....#.#.....#.#.#...#.....#...#...#...#.#.#.#...#...#...#.#
#########.###.#.#########.#####.#.#######.#.#####.#.#####.#.#.#.#####.#######.#.#####.#.#####.#.#.#############.#.#.#####.#.#.###.#########.#
#.........#...#.........#.......#...#...#.#.......#.#.....#.#.#.#.....###.....#...#...#.....#.#.#.#...........#...#...#...#.#.#...#.........#
#.#########.###########.###########.#.#.#.#########.#.#####.#.#.#.#######.#######.#.#######.#.#.#.#.#########.#######.#.###.#.#.###.#########
#.........#.....#.......#...........#.#.#.......#...#.#...#.#...#.......#...###...#.......#.#.#...#.....#...#.....#...#.....#.#.###.....#...#
#########.#####.#.#######.###########.#.#######.#.###.#.#.#.###########.###.###.#########.#.#.#########.#.#.#####.#.#########.#.#######.#.#.#
###...###.....#...#...###.............#...#.....#...#.#.#.#.#.........#.###...#.#.........#...#.....###...#.....#.#.#.......#.#.#.......#.#.#
###.#.#######.#####.#.###################.#.#######.#.#.#.#.#.#######.#.#####.#.#.#############.###.###########.#.#.#.#####.#.#.#.#######.#.#
#...#.........###...#...#.......#...#.....#.........#...#...#.......#...#.....#...#...#...#...#.#...#...........#.#...#.....#.#.#.#.......#.#
#.###############.#####.#.#####.#.#.#.#############################.#####.#########.#.#.#.#.#.#.#.###.###########.#####.#####.#.#.#.#######.#
#.#...#...###...#.#.....#.#...#...#...#####.........###...#...#.....#...#...###...#.#.#.#.#.#.#.#...#...........#.......#####...#...#.......#
#.#.#.#.#.###.#.#.#.#####.#.#.#############.#######.###.#.#.#.#.#####.#.###.###.#.#.#.#.#.#.#.#.###.###########.#####################.#######
#...#...#.....#...#.....#...#.............#.......#...#.#.#.#.#.......#...#...#.#.#.#.#.#.#.#.#.#...#...#...###.###...#...#...#.....#.......#
#######################.#################.#######.###.#.#.#.#.###########.###.#.#.#.#.#.#.#.#.#.#.###.#.#.#.###v###.#.#.#.#.#.#.###.#######.#
#.............#...#.....###...............#...#...#...#.#...#.....#.....#.#...#.#.#.#.#.#.#.#.#.#...#.#.#.#.#.>.>.#.#.#.#.#.#.#...#.#...#...#
#.###########.#.#.#.#######.###############.#.#.###.###.#########.#.###.#.#.###.#.#.#.#.#.#.#.#.###.#.#.#.#.#.###.#.#.#.#.#.#.###.#.#.#.#v###
#...........#...#...#.....#...............#.#.#...#...#.........#.#...#...#.#...#.#.#.#.#.#.#.#.#...#.#...#.#.#...#.#.#.#.#.#...#.#...#.>.###
###########.#########.###.###############.#.#.###.###.#########.#.###.#####v#.###.#.#.#.#.#.#.#.#.###.#####.#.#.###.#.#.#.#.###.#.#######v###
#...........#...#...#.#...#...###.........#.#...#...#.#.....#...#.#...#...>.>.#...#.#.#.#.#.#...#...#...#...#.#.....#...#.#...#.#.#.......###
#.###########.#.#.#.#.#.###.#.###.#########.###.###.#.#.###.#.###.#.###.#######.###.#.#.#.#.#######.###.#.###.###########.###.#.#.#.#########
#...#.....#...#...#.#.#...#.#.#...#...#...#...#.###.#.#...#.#...#.#.###.......#...#.#...#.#.#.....#.#...#...#.....#####...#...#.#.#.........#
###.#.###.#.#######.#.###.#.#.#.###.#.#.#.###.#.###.#.###.#.###.#.#v#########.###.#.#####.#.#.###.#.#.#####.#####.#####.###.###.#.#########.#
#...#.#...#.#.......#.#...#.#.#...#.#.#.#.#...#...#.#...#.#.#...#.>.>.#.....#...#.#.#...#...#...#...#.###...#.....#.....#...###.#.#.....###.#
#.###.#.###.#.#######.#.###.#.###v#.#.#.#.#.#####.#.###.#.#.#.#######.#.###.###.#.#.#.#.#######.#####.###.###.#####.#####.#####.#.#.###.###.#
#...#.#...#.#.......#.#.#...#.#.>.>.#.#.#.#...#...#...#.#.#.#.......#.#...#...#.#.#...#.......#.#...#...#...#...#...#...#.#...#...#...#.....#
###.#.###.#.#######.#.#.#.###.#.#####.#.#.###.#.#####.#.#.#.#######.#.###.###.#.#.###########.#.#.#.###.###.###.#.###.#.#.#.#.#######.#######
###.#.#...#.#.......#.#.#.###.#.....#.#.#.#...#...#...#.#.#.#...#...#...#...#.#.#.#...#...#...#.#.#.#...#...#...#...#.#.#...#.#.......#.....#
###.#.#.###.#.#######.#.#.###.#####.#.#.#.#.#####.#.###.#.#.#.#.#.#####.###.#.#.#.#.#.#.#.#.###.#.#.#.###.###.#####.#.#.#####.#.#######.###.#
###...#.....#.........#...###.......#...#...#####...###...#...#...#####.....#...#...#...#...###...#...###.....#####...#.......#.........###.#
###########################################################################################################################################.#

"""


# In[16]:

from collections import defaultdict, deque


def day23_puzzle1():
    # Part 1
    edges = defaultdict(set)
    data = INPUT.strip().splitlines()
    rows = len(data)
    cols = len(data[0])
    for r, row in enumerate(data):
        for c, v in enumerate(row):
            if v == ".":
                for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    if not (0 <= r + dr < len(data) and 0 <= c + dc < len(row)):
                        continue
                    if data[r + dr][c + dc] == ".":
                        edges[(r, c)].add((r + dr, c + dc))
                        edges[(r + dr, c + dc)].add((r, c))
            if v == ">":
                edges[(r, c)].add((r, c + 1))
                edges[(r, c - 1)].add((r, c))
            if v == "v":
                edges[(r, c)].add((r + 1, c))
                edges[(r - 1, c)].add((r, c))

    queue = deque([(0, 1, 0)])
    visited = set()

    best = 0
    while queue:
        r, c, d = queue.pop()
        if d == -1:
            visited.remove((r, c))
            continue
        if (r, c) == (rows - 1, cols - 2):
            best = max(best, d)
            continue
        if (r, c) in visited:
            continue
        visited.add((r, c))
        queue.append((r, c, -1))
        for er, ec in edges[(r, c)]:
            queue.append((er, ec, d + 1))

    print(f"Part 1: {best}")


def day23_puzzle2():
    edges = defaultdict(set)
    data = INPUT.strip().splitlines()
    rows = len(data)
    cols = len(data[0])

    for r, row in enumerate(data):
        for c, v in enumerate(row):
            if v in ".>v":
                for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    if not (0 <= r + dr < rows and 0 <= c + dc < cols):
                        continue
                    if data[r + dr][c + dc] in ".>v":
                        edges[(r, c)].add((r + dr, c + dc, 1))
                        edges[(r + dr, c + dc)].add((r, c, 1))

    # Prune second degree nodes
    while True:
        for n, e in edges.items():
            if len(e) == 2:
                a, b = e
                edges[a[:2]].remove(n + (a[2],))
                edges[b[:2]].remove(n + (b[2],))
                edges[a[:2]].add((b[0], b[1], a[2] + b[2]))
                edges[b[:2]].add((a[0], a[1], a[2] + b[2]))
                del edges[n]
                break
        else:
            break

    queue = deque([(0, 1, 0)])
    visited = set()
    best = 0
    while queue:
        r, c, d = queue.pop()
        if d == -1:
            visited.remove((r, c))
            continue
        if (r, c) == (rows - 1, cols - 2):
            best = max(best, d)
            continue
        if (r, c) in visited:
            continue
        visited.add((r, c))
        queue.append((r, c, -1))
        for er, ec, l in edges[(r, c)]:
            queue.append((er, ec, d + l))

    print(f"Part 2: {best}")


day23_puzzle1()
day23_puzzle2()


# In[ ]: