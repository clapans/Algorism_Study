import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static Map<Integer,Map<Integer,Boolean>> isIncludeMap;
    static List<Integer>[] orderArr;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] s = bf.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int k = Integer.parseInt(s[1]);

        orderArr = new List[n+1];
        for (int i = 1; i < n+1; i++)
            orderArr[i] = new ArrayList<>();

        for (int i = 0; i < k; i++) {
            String[] tmp = bf.readLine().split(" ");
            int a = Integer.parseInt(tmp[0]);
            int b = Integer.parseInt(tmp[1]);

            orderArr[a].add(b);
        }

        isIncludeMapping();

        int t = Integer.parseInt(bf.readLine().split(" ")[0]);
        for (int i = 0; i < t; i++) {
            String[] tmp = bf.readLine().split(" ");
            int a = Integer.parseInt(tmp[0]);
            int b = Integer.parseInt(tmp[1]);

            System.out.println(compare(a,b));
        }

    }

    static void isIncludeMapping() {
        isIncludeMap = new HashMap<>();
        for (int i = 1; i < orderArr.length; i++)
            isIncludeMap.put(i,bfs(i));
    }

    static Map<Integer,Boolean> bfs(int start) {
        Queue<Integer> queue = new LinkedList<>();
        Map<Integer,Boolean> res = new HashMap<>();
        boolean[] visit = new boolean[orderArr.length];

        queue.add(start);

        while (queue.size() > 0) {
            int node = queue.poll();
            for (int num : orderArr[node])
                if (!visit[num]) {
                    visit[num] = true;
                    res.put(num,true);
                    queue.add(num);
                }
        }
        return res;
    }

    static int compare(int a, int b) {
        if (isIncludeMap.get(a).containsKey(b)) return -1;
        if (isIncludeMap.get(b).containsKey(a)) return 1;
        return 0;
    }
}
