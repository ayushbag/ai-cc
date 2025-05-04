import java.util.*;

class PrimMST {
    static class Edge {
        int dest, weight;
        Edge(int dest, int weight) {
            this.dest = dest;
            this.weight = weight;
        }
    }

    int V;
    List<List<Edge>> adj;

    PrimMST(int v) {
        V = v;
        adj = new ArrayList<>();
        for (int i = 0; i < V; i++)
            adj.add(new ArrayList<>());
    }

    void addEdge(int u, int v, int weight) {
        adj.get(u).add(new Edge(v, weight));
        adj.get(v).add(new Edge(u, weight)); // undirected graph
    }

    void primMST() {
        boolean[] visited = new boolean[V];
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[]{0, 0}); // {vertex, weight}
        int totalWeight = 0;

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int u = curr[0];
            int w = curr[1];

            if (visited[u]) continue;
            visited[u] = true;
            totalWeight += w;

            System.out.println("Include vertex: " + u + " with edge weight: " + w);

            for (Edge edge : adj.get(u)) {
                if (!visited[edge.dest])
                    pq.offer(new int[]{edge.dest, edge.weight});
            }
        }

        System.out.println("Total weight of Prim's MST: " + totalWeight);
    }

    public static void main(String[] args) {
        PrimMST graph = new PrimMST(5);
        graph.addEdge(0, 1, 2);
        graph.addEdge(0, 3, 6);
        graph.addEdge(1, 2, 3);
        graph.addEdge(1, 3, 8);
        graph.addEdge(1, 4, 5);
        graph.addEdge(2, 4, 7);
        graph.addEdge(3, 4, 9);

        graph.primMST();
    }
}
