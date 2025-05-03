import java.util.*;

class Node implements Comparable<Node> {
    int id;
    int distance;

    public Node(int id, int distance) {
        this.id = id;
        this.distance = distance;
    }

    @Override
    public int compareTo(Node other) {
        return Integer.compare(this.distance, other.distance);
    }
}

public class DijkstraAlgorithm {
    public static void dijkstra(int[][] graph, int source) {
        int numVertices = graph.length;
        int[] distances = new int[numVertices];
        boolean[] visited = new boolean[numVertices];

        Arrays.fill(distances, Integer.MAX_VALUE);
        distances[source] = 0;

        PriorityQueue<Node> priorityQueue = new PriorityQueue<>();
        priorityQueue.add(new Node(source, 0));

        while (!priorityQueue.isEmpty()) {
            Node currentNode = priorityQueue.poll();
            int currentDistance = currentNode.distance;
            int currentId = currentNode.id;

            if (visited[currentId]) {
                continue;
            }

            visited[currentId] = true;

            for (int neighbor = 0; neighbor < numVertices; neighbor++) {
                int weight = graph[currentId][neighbor];

                if (weight > 0 && !visited[neighbor]) {
                    int distance = currentDistance + weight;

                    if (distance < distances[neighbor]) {
                        distances[neighbor] = distance;
                        priorityQueue.add(new Node(neighbor, distance));
                    }
                }
            }
        }

        System.out.println("Vertex\tDistance");
        for (int i = 0; i < numVertices; i++) {
            System.out.println(i + "\t" + distances[i]);
        }
    }

    public static void main(String[] args) {
        int[][] graph = {
                {0, 4, 0, 0, 0, 0, 0, 8, 0},
                {4, 0, 8, 0, 0, 0, 0, 11, 0},
                {0, 8, 0, 7, 0, 4, 0, 0, 2},
                {0, 0, 7, 0, 9, 14, 0, 0, 0},
                {0, 0, 0, 9, 0, 10, 0, 0, 0},
                {0, 0, 4, 14, 10, 0, 2, 0, 0},
                {0, 0, 0, 0, 0, 2, 0, 1, 6},
                {8, 11, 0, 0, 0, 0, 1, 0, 7},
                {0, 0, 2, 0, 0, 0, 6, 7, 0}
        };

        int sourceVertex = 0;
        dijkstra(graph, sourceVertex);
    }
}