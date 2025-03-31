# Análise da prática aula 01

## Máquina usada
* Processador: AMD Ryzen 5 6600H with Radeon Graphics 3.30 GHz
* RAM instalada: 16,0 GB (utilizável: 15,2 GB)
* Tipo de sistema: Sistema operacional de 64 bits, processador baseado em x64

## Função Recursiva
* Ambos os algoritmos apresentados possuem complexidade de tempo O(√n), pois verificam a divisibilidade de n apenas até sua raiz quadrada. A versão recursiva (is_prime_recursive) chama a si mesma sucessivamente com um divisor crescente, o que resulta em aproximadamente √n chamadas no pior caso. No entanto, foi observado problemas com a recursão excessiva em alguns casos gerando o erro "RecursionError" para números grandes.

* Tempo (recursivo): 0.748692 segundos


## Função Iterativa
* Já a versão iterativa (is_prime_number) percorre apenas os números ímpares a partir de 3 até √n, reduzindo o número de iterações pela metade em comparação a uma abordagem ingênua. Sem a sobrecarga de chamadas recursivas, essa versão foi significativamente mais eficiente na prática.


---

João Pedro Norberto da Silva, 31/03/2025