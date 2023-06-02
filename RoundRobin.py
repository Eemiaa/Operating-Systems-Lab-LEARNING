fila_processos = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}
timeSlice = int(input("forneça o time slice:\n"))

print(fila_processos)
while True:

    txt = input("forneça os dados do processo:\n").split(", ")

    if(txt[0]==''):
        break

    
    
    

    if(len(txt)==3):
        prioridade = int(txt[0])
        nome = txt[1]
        tempo = int(txt[2])
        fila_processos[prioridade].append([nome, tempo])
        print(fila_processos)
        #fila_processos[prioridade][0][1] -= 1
        #print(fila_processos)
    else:
        nome = txt[0]
        tempo = int(txt[1])
        fila_processos[10].append([nome, tempo])
        print(fila_processos)


cont_prioridade=0


while True:
    if fila_processos[cont_prioridade]!=[]:
        cont_processo=0
        
        while True:
            tempo_uso=0

            if(len(fila_processos[cont_prioridade])>cont_processo):
                for i in range(timeSlice):

                    if(fila_processos[cont_prioridade][cont_processo][1] > 0):
                        fila_processos[cont_prioridade][cont_processo][1] -= 1
                        tempo_uso+=1

                    else:
                        break
                if(fila_processos[cont_prioridade][cont_processo][1]==0):
                    print(fila_processos[cont_prioridade][cont_processo][0],"*, ", tempo_uso)
                else:
                    print(fila_processos[cont_prioridade][cont_processo][0],", ", tempo_uso)

                if(fila_processos[cont_prioridade][cont_processo][1] == 0):
                    fila_processos[cont_prioridade].pop(cont_processo)
                    cont_processo -= 1


                cont_processo += 1
            elif fila_processos[cont_prioridade] != []:
                cont_processo = 0
            else: break
           

    cont_prioridade +=1
    if(cont_prioridade == 11):
        break
    
#executar cada processo e ir reduzindo o tempo e printando


