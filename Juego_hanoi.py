class Hanoi:
    def __init__(self, n=3):
        self.t, self.m = {'A': list(range(n,0,-1)), 'B': [], 'C': []}, 0
        print(f"TORRES DE HANOI - {n} DISCOS\nInicio: A={self.t['A']}, B={self.t['B']}, C={self.t['C']}\n")
    
    def resolver(self, n, o, d, a):
        if n > 0:
            self.resolver(n-1, o, a, d)
            disco = self.t[o].pop()
            self.t[d].append(disco)
            self.m += 1
            print(f"Paso {self.m}: Mover disco {disco} de {o} a {d}")
            print(f"Estado: A={self.t['A']}, B={self.t['B']}, C={self.t['C']}")
            self.resolver(n-1, a, d, o)
            
if __name__ == "__main__":
    h = Hanoi(3)
    h.resolver(3, 'A', 'C', 'B')
    print(f"\n¡Completado en {h.m} movimientos! (Óptimo: {2**3-1})")
