#!/usr/bin/env python
# coding: utf-8

# ##### 1. Euristica admisibila
# 
# O stare este evaluata in functie de numarul de gauri dintre doua clatite consecutive. O gaura este definita ca fiind o pereche de clatite adiacente care nu se afla in ordinea corecta fata de configuratia finala.
# 
# Scopul este obtinerea unei stive sortate, adica o configuratie in care nu mai exista nicio gaura.
# 
# O mutare in aceasta problema consta intr-o singura operatie de tip `flip(k)`, care inverseaza ordinea clatitelor aflate pe pozitiile de la `0` la `k`.
# 
# Propun urmatoarea euristica:
# 
# $$
# h(n)=\lceil \text{nr. gauri} / 2 \rceil
# $$
# 
# Aceasta euristica este admisibila deoarece o singura operatie `flip(k)` poate corecta cel mult doua gauri. Prin urmare, daca intr-o stare exista un anumit numar de gauri, sunt necesare cel putin `ceil(nr. gauri / 2)` mutari pentru eliminarea lor.
# 
# In starea finala, numarul de gauri este 0, deci si valoarea euristicii este 0. Rezulta astfel ca euristica nu supraestimeaza niciodata costul real minim pana la solutie, deci este admisibila.
# 

# ##### 2. Algoritmul A*

# In[7]:


import heapq
import math

def flip(k, stack):
    v = list(stack)
    i = 0
    j = k
    while i < j:
        v[i], v[j] = v[j], v[i]
        i += 1
        j -= 1
    return tuple(v)

def h(stack):
    gauri = 0
    for i in range(len(stack) - 1):
        if stack[i + 1] != stack[i] + 1:
            gauri += 1
    return math.ceil(gauri / 2)

def gata(stack):
    return list(stack) == sorted(stack)

def astar_pancake(starta):
    start = tuple(starta)
    q = []
    heapq.heappush(q, (h(start), 0, start, []))
    best = {start: 0}
    while q:
        f, g, stack, drum = heapq.heappop(q)
        if gata(stack):
            return drum, list(stack)
        n = len(stack)
        for k in range(1, n):
            nxt = flip(k, stack)
            g_nou = g + 1
            if nxt not in best or g_nou < best[nxt]:
                best[nxt] = g_nou
                f_nou = g_nou + h(nxt)
                heapq.heappush(q, (f_nou, g_nou, nxt, drum + [k]))
    return None, None

stack = [7, 2, 5, 1, 6, 3, 4]

drum, sortata = astar_pancake(stack)

print("Stiva initiala:", stack)
print("Flipuri:", drum)
print("Stiva sortata:", sortata)


# ##### 3. Algoritmul IDA*
# 

# In[ ]:


import math

def flip(k, stack):
    v = list(stack)
    i = 0
    j = k
    while i < j:
        v[i], v[j] = v[j], v[i]
        i += 1
        j -= 1
    return tuple(v)

def h(stack):
    gauri = 0
    for i in range(len(stack) - 1):
        if stack[i + 1] != stack[i] + 1:
            gauri += 1
    return math.ceil(gauri / 2)

def gata(stack):
    return list(stack) == sorted(stack)

def cauta(stack, g, limita, drum, viz):
    f = g + h(stack)

    if f > limita:
        return f, None

    if gata(stack):
        return True, drum

    minim = float("inf")
    n = len(stack)

    for k in range(1, n):
        nxt = flip(k, stack)

        if nxt not in viz:
            viz.add(nxt)
            rez, sol = cauta(nxt, g + 1, limita, drum + [k], viz)

            if rez is True:
                return True, sol

            if rez < minim:
                minim = rez

            viz.remove(nxt)

    return minim, None

def ida_pancake(starta):
    start = tuple(starta)
    limita = h(start)

    while True:
        viz = {start}
        rez, drum = cauta(start, 0, limita, [], viz)

        if rez is True:
            stack = list(start)
            for k in drum:
                stack = list(flip(k, stack))
            return drum, stack

        if rez == float("inf"):
            return None, None

        limita = rez

stack = [7, 2, 5, 1, 6, 3, 4]

drum, sortata = ida_pancake(stack)

print("Stiva initiala:", stack)
print("Flipuri:", drum)
print("Stiva sortata:", sortata)

