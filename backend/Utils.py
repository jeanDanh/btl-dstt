import numpy as np

class SVD:
    @staticmethod
    def svd_decompose(matrix):
        U, S, Vt = np.linalg.svd(matrix, full_matrices=False)
        return U, S, Vt
    
    @staticmethod
    def svd_reconstruct(U, S, Vt):
        S_matrix = np.diag(S)
        return np.dot(U, np.dot(S_matrix, Vt))
    
    @staticmethod
    def svd_reduce(U, S, Vt, energy_ratio=0.95):
        total_energy = np.sum(S**2)
        if total_energy == 0:
            return U, S, Vt

        energy = 0
        k = 0
        for i in range(len(S)):
            energy += S[i]**2
            if energy / total_energy >= energy_ratio:
                k = i + 1
                break

        U_k = U[:, :k]
        S_k = S[:k]
        Vt_k = Vt[:k, :]
        return U_k, S_k, Vt_k

    
    @staticmethod
    def calc(matrix):
        U, S, Vt = SVD.svd_decompose(matrix)
        U_k, S_k, Vt_k = SVD.svd_reduce(U, S, Vt)
        return SVD.svd_reconstruct(U_k, S_k, Vt_k)

class ShoppingMatrix:
    def __init__ (self, cus_id, prod_id, purchase):
        self.threshold = 0
        self.num = 10
        self.cus_map = {cus: idx for idx, cus in enumerate(cus_id)}
        self.prod_map = {prod: idx for idx, prod in enumerate(prod_id)}
        self.prods = prod_id

        self.matrix = np.zeros((len(cus_id), len(prod_id)))

        for cus, prod, value in purchase:
            if cus in self.cus_map and prod in self.prod_map:
                self.matrix[self.cus_map[cus]][self.prod_map[prod]] += value

    def getRow(self, id):
        n_matrix = SVD.calc(self.matrix)

        products = n_matrix[self.cus_map[id]]

        prodrec = [(score, idx) 
                    for idx, score in enumerate(products) 
                    if self.matrix[self.cus_map[id]][idx] == 0 and score > self.threshold
                    ]

        return [self.prods[idx] 
                for score, idx in sorted(prodrec, key=lambda x: x[0], reverse=True)[:self.num]
                ]