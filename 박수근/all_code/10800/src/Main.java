import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Node {
    int color,size,order;

    public Node(int color, int size, int order) {
        this.color = color;
        this.size = size;
        this.order = order;
    }
}

public class Main {
    static int n;
    static int total = 0;
    static Map<Integer, Integer> sum = new HashMap<>();
    static Node[] nodeList;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(bf.readLine());
        nodeList = new Node[n];
        arr = new int[n];

        for (int i = 0; i < n; i++) {
            String str = bf.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int c = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            nodeList[i] = new Node(c,s,i);
        }

        Arrays.sort(nodeList,new Comparator<Node>() {
            @Override
            public int compare(Node o1, Node o2) {
                return Integer.compare(o1.size, o2.size);
            }
        });

        for (int i = 0; i < n; i++) {
            Node n = nodeList[i];
            total += n.size;
            if (sum.containsKey(n.color))
                sum.put(n.color, sum.get(n.color) + n.size);
            else
                sum.put(n.color, n.size);
            arr[n.order] = total - sum.get(n.color);
            int idx = i - 1;
            while (idx >= 0 && nodeList[idx].size == n.size) {
                if (nodeList[idx].color != n.color)
                    arr[n.order] -= n.size;
                idx--;
            }
        }

        for (int i = 0; i < n; i++)
            System.out.println(arr[i]);
    }
}
