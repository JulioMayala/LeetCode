class Solution(object):
    def maxProfit(self, prices):
        # 1. Null-Safety: Salvaguarda contra secuencias vacías
        if not prices:
            return 0
            
        # 2. Inicializamos el umbral más bajo con infinito
        compra_minima = float('inf')
        # 3. Inicializamos la cota superior matemática en cero
        ganancia_maxima = 0
        
        # 4. Iteración lineal sobre valores directos (Evitando el Memory Fetching)
        for precio in prices:
            # Desglose Lógico Dinámico (Ejemplo: [7, 1, 5])
            # Paso A (precio=7): 7 < inf -> compra_minima = 7. ganancia = 0
            # Paso B (precio=1): 1 < 7 -> compra_minima = 1. ganancia = 0
            # Paso C (precio=5): 5 < 1 (False). 5 - 1 = 4. 4 > 0 -> ganancia = 4
            
            if precio < compra_minima:
                compra_minima = precio
            elif precio - compra_minima > ganancia_maxima:
                ganancia_maxima = precio - compra_minima
                
        return ganancia_maxima