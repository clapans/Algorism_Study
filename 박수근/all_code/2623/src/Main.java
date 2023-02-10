import java.util.*;

public class Main {
    static int n,m;
    static int[] degree;
    static List<Integer>[] orderList;
    static boolean[] visit;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        degree = new int[n+1];
        orderList = new List[n+1];
        for (int i = 0; i < n + 1; i++) orderList[i] = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int tmp = sc.nextInt();
            int[] sArr = new int[tmp];
            for (int j = 0; j < tmp; j++) sArr[j] = sc.nextInt();
            for (int j = 0; j < tmp; j++) {
                if (j == tmp - 1) continue;
                orderList[sArr[j]].add(sArr[j + 1]);
                degree[sArr[j+1]]++;
            }
        }
        List<Integer> integerList = findStart();
        List<Integer> res = new ArrayList<>();
        if (integerList.size() == 0) System.out.println(0);
        else {
            Queue<Integer> queue = new LinkedList<>(integerList);
            visit = new boolean[n+1];
            for (int x : integerList) {
                visit[x] = true;
                res.add(x);
            }
            while (queue.size() > 0) {
                int x = queue.poll();

                for (int i : orderList[x]) {
                    degree[i]--;
                    if (degree[i] == 0 && !visit[i]) {
                        visit[i] = true;
                        queue.add(i);
                        res.add(i);
                    }
                }
            }
            if (isCycle())
                for (int i : res) System.out.println(i);
            else
                System.out.println(0);
        }
    }

    static List<Integer> findStart() {
        List<Integer> integerList = new ArrayList<>();
        for (int i = 1; i < n + 1; i++)
            if (degree[i] == 0) integerList.add(i);
        return integerList;
    }

    static boolean isCycle() {
        for (int i = 1; i < n + 1; i++)
            if (!visit[i]) return false;
        return true;
    }
}
