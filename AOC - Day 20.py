#!/usr/bin/env python
# coding: utf-8

# In[1]:


INPUT = r"""
%dj -> fj, jn
%xz -> cm
%fn -> rj
%fv -> nt, zp
%ls -> ph, cf
%rk -> zp, tp
&jn -> km, cr, vz
%nh -> ph, ls
%tx -> gb
%xg -> dv, zp
%tp -> gx
&zp -> kj, kz, gx, fv, lv, tp
&gq -> rx
%fj -> sl, jn
%cr -> vz, jn
%rt -> fn, mf
%kj -> tt
%tk -> mg, ph
%xt -> jn, gh
%qx -> bx
%lv -> sx
%nz -> dp, ph
%sx -> kj, zp
%dd -> bf
%gb -> jp
%bj -> ph, nn
%sk -> mf
%bx -> tx, mf
%mt -> xg, zp
%vz -> hf
%vx -> mf, sk
%tt -> mt, zp
%br -> jn, fk
&xj -> gq
%mg -> ph, ps
%nt -> zp, rk
&qs -> gq
%rj -> qx, mf
%bf -> vx, mf
&kz -> gq
%fk -> jn, gk
%dv -> zp
%dp -> ph
&mf -> gb, tx, xj, dd, qx, rt, fn
&ph -> nn, xz, tk, ps, qs
%ps -> xz
&km -> gq
broadcaster -> fv, cr, rt, tk
%gk -> jn, xt
%cf -> ph, nz
%tl -> jn, br
%cm -> bj, ph
%nn -> nh
%jp -> mf, dd
%gh -> jn, dj
%hf -> tl, jn
%sl -> jn
%gx -> lv
"""


# In[13]:


from collections import defaultdict, deque
import math

def parse_input():
    rx = ""
    counts = {}
    modules = {}
    flipflops = defaultdict(int)
    conjunctions = defaultdict(dict)

    for line in INPUT.strip().splitlines():
        src, _, *dests = line.replace(",", "").split()

        match src[0]:
            case "%" | "&":
                kind = src[0]
                src = src[1:]
            case _:
                kind = ""
        
        modules[src] = (kind, dests)

        for dest in dests:
            conjunctions[dest][src] = 0
            if dest == "rx":
                rx = src

    # Count the inputs for the final `rx` module
    counts = {x: 0 for x in conjunctions[rx]}

    return modules, flipflops, conjunctions, counts

def day20_puzzle1():
    modules, flipflops, conjunctions, _ = parse_input()
    counts = [0, 0]
    for _ in range(1000):
        queue = deque([(None, 'broadcaster', 0)])
        while queue:
            src, mod, input = queue.popleft()
            counts[input] += 1
    
            if mod not in modules: 
                continue
            kind, dests = modules[mod]
    
            match kind, input:
                case '', _:
                    output = input
                case '%', 0:
                    output = flipflops[mod] = not flipflops[mod]
                case '&', _:
                    conjunctions[mod][src] = input
                    output = not all(conjunctions[mod].values())
                case _,_: 
                    continue
    
            for d in dests:
                queue.append((mod, d, output))

    print(f"Part 1: {math.prod(counts)}")

def day20_puzzle2():
    modules, flipflops, conjunctions, counts = parse_input()
    for press in range(1, 1_000_000_000):
        if all(counts.values()):
            break

        queue = deque([(None, 'broadcaster', 0)])
        while queue:
            src, mod, input = queue.popleft()
    
            if mod not in modules: 
                continue
            kind, dests = modules[mod]
    
            match kind, input:
                case '', _:
                    output = input
                case '%', 0:
                    output = flipflops[mod] = not flipflops[mod]
                case '&', _:
                    conjunctions[mod][src] = input
                    output = not all(conjunctions[mod].values())
    
                    if 'rx' in dests:
                        for k, v in conjunctions[mod].items():
                            if v: counts[k] = press
                case _,_: 
                    continue
    
            for d in dests:
                queue.append((mod, d, output))

    print(f"Part 2: {math.prod(counts.values())}")

day20_puzzle1()
day20_puzzle2()


# In[ ]:




