#include <stdlib.h>
#include <stdio.h>

#define SIZE 3

int find_min(int x[SIZE], int s);

int main(){
  int v[SIZE] = {4,2,7};
  int m = find_min(v,SIZE);
  printf("Minimum is : %d\n", m);
}

int find_min(int x[SIZE], int s){
  int i,tmp;
  tmp=x[0];
  for(i=0;i<s;i++){
    if(x[i]<tmp){
      tmp=x[i];
    }
  }
  return tmp;
}
