#include <stdio.h>
#include <stdlib.h>
#define _CRT_SECURE_NO_WARNINGS

#define MAX_VERTEX 1001
int graph[MAX_VERTEX][MAX_VERTEX] ={0,};

int DFS[MAX_VERTEX] = {0,};
int BFS[MAX_VERTEX] = {0,};
void do_dfs(int start, int n);
void do_bfs(int start, int n);

int queue[MAX_VERTEX];
int main()
{
    int n,edge,start, a,b; 
    // n은 정점 개수, m은 간선 갯수, v는 시작점, a와b는 각각 그래프의 인덱스
    scanf("%d %d %d", &n, &edge, &start);

    for(int i = 0; i < edge; i++){
        scanf("%d %d", &a, &b);
        graph[a][b]= 1;
        graph[b][a] = 1;
    }

    do_dfs(start,n);

    // for(int i = 0 ; i< edge; i++){
    //     for(int j = 0 ; j<edge;j++){
    //         printf("%d",graph[i][j]);
    //     }
    //     printf("\n");
    // }


    printf("\n");
    do_bfs(start,n);



    return 0;
}


void do_dfs(int start, int n)
{
    int k;
    DFS[start] = 1;
    printf("%d ", start);
    for(k = 1 ; k <= n; k++){
        if (graph[start][k] == 1 && DFS[k] == 0){
            do_dfs(k,n);
        } 
    } 
}

void do_bfs(int start, int n)
{
    int front = 0 , rear = 1, pop;

    BFS[start] = 1;
    printf("%d",start);

    queue[0] = start;
    rear++;

    while(front<rear){
        pop = queue[front];
        front++;

        for(int i = 0; i <=n;i++){
            if(graph[pop][i] == 1 && BFS[i] == 0){
                printf(" %d",i);
                queue[rear] = i;
                rear++;
                BFS[i] = 1;
            }
        }
    }
}