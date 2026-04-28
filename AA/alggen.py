import numpy as np

class GeneticAlgorithm:
    def __init__(self, n, a, b, coef, precision, p_cross, p_mut, steps):
        self.n = n  
        self.a = a  
        self.b = b  
        self.coef = coef  
        self.precision = precision  
        self.p_cross = p_cross  
        self.p_mut = p_mut  
        self.steps = steps  
        
        self.m = int(np.ceil(np.log2((b - a) * (10 ** precision))))
        self.d = (b - a) / (2**self.m - 1)
        
        self.population = self.generate_initial_population()

    def f(self, x):
        return self.coef[0]*(x**2) + self.coef[1]*x + self.coef[2]

    def decode(self, binary_str):
        val_int = int(binary_str, 2)
        return self.a + val_int * self.d

    def generate_initial_population(self):
        pop = []
        for _ in range(self.n):
            bits = ''.join(np.random.choice(['0', '1'], size=self.m))
            x = self.decode(bits)
            pop.append({'bits': bits, 'x': x, 'f': self.f(x)})
        return pop

    def binary_search_selection(self, q, x):
        st = 0
        dr = len(q) - 1
        idx = 0
        while st <= dr:
            m = (st + dr) // 2
            if q[m] >= x:
                idx = m
                dr = m - 1
            else:
                st = m + 1
        return idx

    def run(self, output_file):
        with open(output_file, "w") as f_out:
            f_out.write("Populatia initiala:\n")
            for i, ind in enumerate(self.population):
                f_out.write(f"{i+1}: {ind['bits']} x= {ind['x']:.6f} f= {ind['f']:.6f}\n")

            best_ind_ever = max(self.population, key=lambda x: x['f']).copy()

            total_f = sum(ind['f'] for ind in self.population)
            p_sel = [ind['f'] / total_f for ind in self.population]
            f_out.write("\nProbabilitati selectie:\n")
            for i, p in enumerate(p_sel):
                f_out.write(f"cromozom {i+1} probabilitate {p}\n")

            q = np.cumsum([0] + p_sel)
            f_out.write("\nIntervale probabilitati selectie:\n")
            f_out.write(" ".join([f"{val:.6f}" for val in q]) + "\n\n")

            selected_pop = []
            for _ in range(self.n):
                u = np.random.random()
                idx = self.binary_search_selection(q[1:], u)
                selected_pop.append(self.population[idx].copy())
                f_out.write(f"u={u:.6f} selectam cromozomul {idx+1}\n")

            f_out.write("\nDupa selectie:\n")
            for i, ind in enumerate(selected_pop):
                f_out.write(f"{i+1}: {ind['bits']} x= {ind['x']:.6f} f= {ind['f']:.6f}\n")

            f_out.write(f"\nProbabilitatea de incrucisare {self.p_cross}\n")
            to_cross_idx = []
            for i in range(self.n):
                u = np.random.random()
                if u < self.p_cross:
                    f_out.write(f"{i+1}: {selected_pop[i]['bits']} u={u:.6f} < {self.p_cross} participa\n")
                    to_cross_idx.append(i)
                else:
                    f_out.write(f"{i+1}: {selected_pop[i]['bits']} u={u:.6f}\n")

            np.random.shuffle(to_cross_idx)
            for i in range(0, len(to_cross_idx) - 1, 2):
                idx1, idx2 = to_cross_idx[i], to_cross_idx[i+1]
                p_cut = np.random.randint(1, self.m)
                
                b1, b2 = selected_pop[idx1]['bits'], selected_pop[idx2]['bits']
                new_b1 = b1[:p_cut] + b2[p_cut:]
                new_b2 = b2[:p_cut] + b1[p_cut:]
                
                f_out.write(f"Recombinare dintre cromozomul {idx1+1} cu {idx2+1}:\n")
                f_out.write(f"{b1} {b2} punct {p_cut}\nRezultat: {new_b1} {new_b2}\n")
                
                selected_pop[idx1]['bits'], selected_pop[idx2]['bits'] = new_b1, new_b2

            f_out.write(f"\nProbabilitate de mutatie pentru fiecare gena {self.p_mut}\nAu fost modificati cromozomii:\n")
            for i in range(self.n):
                mutated = False
                bits_list = list(selected_pop[i]['bits'])
                for j in range(self.m):
                    if np.random.random() < self.p_mut:
                        bits_list[j] = '1' if bits_list[j] == '0' else '0'
                        mutated = True
                if mutated:
                    selected_pop[i]['bits'] = "".join(bits_list)
                    f_out.write(f"{i+1}\n")

            for ind in selected_pop:
                ind['x'] = self.decode(ind['bits'])
                ind['f'] = self.f(ind['x'])
            
            selected_pop.sort(key=lambda x: x['f'])
            if best_ind_ever['f'] > selected_pop[0]['f']:
                selected_pop[0] = best_ind_ever.copy()

            self.population = selected_pop
            
            f_out.write("\nEvolutia maximului:\n")
            for step in range(1, self.steps + 1):
                current_max = max(ind['f'] for ind in self.population)
                current_avg = sum(ind['f'] for ind in self.population) / self.n
                f_out.write(f"Generatia {step}: Max={current_max:.10f}, Media={current_avg:.10f}\n")

                best_ind = max(self.population, key=lambda x: x['f']).copy()

                total_f = sum(ind['f'] for ind in self.population)
                p_sel = [ind['f'] / total_f for ind in self.population]
                q = np.cumsum([0] + p_sel)
                new_pop = [self.population[self.binary_search_selection(q[1:], np.random.random())].copy() for _ in range(self.n)]
                
                to_cross = [i for i in range(self.n) if np.random.random() < self.p_cross]
                np.random.shuffle(to_cross)
                for i in range(0, len(to_cross)-1, 2):
                    p_cut = np.random.randint(1, self.m)
                    i1, i2 = to_cross[i], to_cross[i+1]
                    b1, b2 = new_pop[i1]['bits'], new_pop[i2]['bits']
                    new_pop[i1]['bits'] = b1[:p_cut] + b2[p_cut:]
                    new_pop[i2]['bits'] = b2[:p_cut] + b1[p_cut:]

                for ind in new_pop:
                    bits_list = list(ind['bits'])
                    for j in range(self.m):
                        if np.random.random() < self.p_mut:
                            bits_list[j] = '1' if bits_list[j] == '0' else '0'
                    ind['bits'] = "".join(bits_list)
                    ind['x'] = self.decode(ind['bits'])
                    ind['f'] = self.f(ind['x'])

                new_pop.sort(key=lambda x: x['f'])
                if best_ind['f'] > new_pop[0]['f']:
                    new_pop[0] = best_ind
                
                self.population = new_pop

if __name__ == "__main__":
    with open("input.txt", "r") as f_in:
        n = int(f_in.readline().strip())
        line2 = f_in.readline().split()
        a, b = float(line2[0]), float(line2[1])
        coef = list(map(float, f_in.readline().split()))
        precision = int(f_in.readline().strip())
        p_cross = float(f_in.readline().strip())
        p_mut = float(f_in.readline().strip())
        steps = int(f_in.readline().strip())

    ga = GeneticAlgorithm(n, a, b, coef, precision, p_cross, p_mut, steps)
    ga.run("Evolutie.txt")