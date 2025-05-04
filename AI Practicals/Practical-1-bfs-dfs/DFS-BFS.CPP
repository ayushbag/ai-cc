#include <bits/stdc++.h>
using namespace std;

void dfs(int adj_mat[10][10], int n, int node, int visited[10]) {
	cout << "DFS" << endl;

	stack<int> stk;
	stk.push(node);

	while (!stk.empty()) {
		int i = stk.top();
		stk.pop();

		if (!visited[i]) {
			visited[i] = 1;
			cout << i << "-->";
			for (int j = 0; j < n; j++) {
				if (adj_mat[i][j] == 1 && !visited[j]) {
					stk.push(j);
				}
			}
		}
	}
	cout << "NULL" << endl;
}


void bfs(int adj_mat[10][10],int n,int node,int visited[10])
{
	cout<<"BFS"<<endl;

	queue<int> q;
	q.push(node);
	visited[node] = 1;

	while(!q.empty()){
		int i = q.front();
		q.pop();

		cout<<i<<"-->";
		for(int j=0;j<n;j++){
			if(adj_mat[i][j]==1 && visited[j]!=1){
				q.push(j);
				visited[j] = 1;
			}
		}
	}
	cout<<"NULL"<<endl;

}

int main() {

	int n;
	int adj_mat[10][10] = {0},visited[10] = {0};

	cout<<"Enter the total number of nodes in the graph --> ";
	cin>>n;

	for(int i=0;i<n;i++){
		for(int j=i+1;j<n;j++){
			cout<<"Do you want edge between "<<i<<" and "<<j<<"?. (Y or N) ";
			char s;	cin>>s;
			if(s=='y' || s=='Y'){
				adj_mat[i][j] = adj_mat[j][i] = 1;
			}
		}
	}

	cout << "\nAdjacent Matrix is : \n";
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << adj_mat[i][j] << " ";
		}
		cout << endl;
	}

	int ch;
	do{

		cout<<"\n\n";
		cout<<"1. DFS"<<endl;
		cout<<"2. BFS"<<endl;
		cout<<"0. Exit"<<endl;
		cout<<"Enter Choice:- ";
		cin>>ch;
		switch(ch){
			case 1:
				for(int i=0;i<n;i++)	visited[i] = 0;
				cout<<"DFS on the given graph is :- ";
				dfs(adj_mat,n,0,visited);
				break;
			case 2:
				for(int i=0;i<n;i++)	visited[i] = 0;
				cout<<"BFS on the given graph is :- ";
					bfs(adj_mat,n,0,visited);
				break;
			case 0:
				break;
			default:
				cout<<"Invalid Choice \n\n";
			break;
		}
	}while(ch!=0);

	cout<<"Program Finished ";
	return 0;
}


/* demonstration DFS

Enter the total number of nodes in the graph --> 3
Do you want edge between 0 and 1? Y
Do you want edge between 0 and 2? N
Do you want edge between 1 and 2? Y

Adjacency Matrix
0 1 0
1 0 1
0 1 0

output:
0 --> 1 --> 2 --> NULL */
