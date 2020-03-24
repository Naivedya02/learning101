#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n,q;
    scanf("%d %d", &n,&q);
    int len[n];
    int **p = (int **)malloc(n*sizeof(int *));
    for(int i=0; i<n;i++){
        scanf("%d", &len[i]);
        p[i] = (int *)malloc(len[i]*sizeof(int));
        for(int j=0;j<len[i];j++){
            scanf("%d", &p[i][j]);
        }
    }
    int x,y;
    for(int k=0;k<q;k++){
        scanf("%d %d", &x, &y);
        printf("%d\n", p[x][y]);
    }   
    return 0;
}
