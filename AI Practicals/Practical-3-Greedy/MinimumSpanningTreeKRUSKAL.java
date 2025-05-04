import java.util.*;

class Edge implements Comparable<Edge> {
    int source;
    int destination;
    int weight;

    public Edge(int source, int destination, int weight) {
        this.source = source;
        this.destination = destination;
        this.weight = weight;
    }

    @Override
    public int compareTo(Edge other) {
        return Integer.compare(this.weight, other.weight);
    }
}

public class MinimumSpanningTreeKRUSKAL {
    static class DisjointSet {
        int[] parent;
        int[] rank;

        public DisjointSet(int vertices) {
            parent = new int[vertices];
            rank = new int[vertices];

            for (int i = 0; i < vertices; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
        }

        int find(int vertex) {
            if (parent[vertex] != vertex) {
                parent[vertex] = find(parent[vertex]);
            }
            return parent[vertex];
        }

        void union(int vertex1, int vertex2) {
            int root1 = find(vertex1);
            int root2 = find(vertex2);

            if (root1 != root2) {
                if (rank[root1] < rank[root2]) {
                    parent[root1] = root2;
                } else if (rank[root1] > rank[root2]) {
                    parent[root2] = root1;
                } else {
                    parent[root2] = root1;
                    rank[root1]++;
                }
            }
        }
    }

    public static void kruskalAlgorithm(List<Edge> edges, int vertices) {
        DisjointSet disjointSet = new DisjointSet(vertices);
        List<Edge> mstEdges = new ArrayList<>();

        Collections.sort(edges);

        for (Edge edge : edges) {
            int sourceRoot = disjointSet.find(edge.source);
            int destinationRoot = disjointSet.find(edge.destination);

            if (sourceRoot != destinationRoot) {
                mstEdges.add(edge);
                disjointSet.union(edge.source, edge.destination);
            }
        }

        int mstWeight = 0;
        System.out.println("Edges in the Minimum Spanning Tree:");
        for (Edge edge : mstEdges) {
            System.out.println(edge.source + " - " + edge.destination + " : " + edge.weight);
            mstWeight += edge.weight;
        }

        System.out.println("Weight of the Minimum Spanning Tree: " + mstWeight);
    }

    public static void main(String[] args) {
        int vertices = 4;
        List<Edge> edges = new ArrayList<>();

        edges.add(new Edge(0, 1, 10));
        edges.add(new Edge(0, 2, 6));
        edges.add(new Edge(0, 3, 5));
        edges.add(new Edge(1, 3, 15));
        edges.add(new Edge(2, 3, 4));

        kruskalAlgorithm(edges, vertices);
    }
} 