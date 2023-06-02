#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#define MAX_COUNT 200
int count = 0; // Contador de movimentos
int quantidade = 6; // Nº de discos
int n = 19;
int fat, auxiliar;
int a = 0, b = 1;

void TorreHanoi(int origem, int destino, int auxiliar, int quantidade){
  if( quantidade == 1 ){
    printf("Move de %d para %d\n", origem, destino);
    count+=1;
  }else{
    TorreHanoi(origem, auxiliar, destino, quantidade-1);
    TorreHanoi(origem, destino, auxiliar, 1);
    TorreHanoi(auxiliar, destino, origem, quantidade-1);
  }
}

void main(){
  // Chama a função Torre de Hanoi passando como parâmetro a origem, o destino, o pino auxiliar e a quantidade de discos
  pid_t pid;
  pid = fork();
  
  if(pid == 0){
    //Fatorial
      for(fat = 1; n > 1; n = n - 1){
      fat = fat * n;
      printf("\nFatorial calculado: %d", fat);
    }
  }else{
    //Fibonati    
    pid = fork();
    
    if(pid == 0){
      for(int i = 0; i < n; i++) {
        auxiliar = a + b;
        a = b;
        b = auxiliar;
        printf("%d\nFibonati: ", auxiliar);
      }
    }else{
      //Torre de Hanoi
      TorreHanoi(0, 2, 1, quantidade);
      printf("\nQuantidade de Discos: %d\n", quantidade);
      printf("Nº minimo de movimentos: %d\n\n", count);
    }
  }

  exit(0);
}
