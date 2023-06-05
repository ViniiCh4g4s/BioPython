entrada = open("humano.fasta").read().replace("\n", "")
saida = open("humano.html", "w")

cont = {}

# Inicializar contadores para pares de bases
for valor1 in 'ATCG':
    for valor2 in 'ATCG':
        cont[valor1 + valor2] = 0

# Contar ocorrências de pares de bases
for posicao in range(len(entrada) - 1):
    par_bases = entrada[posicao:posicao + 2]
    cont[par_bases] += 1

# Escrever resultados no arquivo de saída HTML
i = 1
for k in cont:
	transparencia = cont[k]/max(cont.values())
	saida.write("<div style='width:100px;height:100px;border:1px solid #111;float:left;color:white;background-color:rgba(0,0,0,"+str(transparencia)+")'>"+k+"</div>")

	if i%4 == 0:
		saida.write("<div style='clear:both'></div>")

	i+=1

saida.close()
