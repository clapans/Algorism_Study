import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Floyd {
    static boolean[][] floydArr;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] s = bf.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int k = Integer.parseInt(s[1]);

        floydArr = new boolean[n+1][n+1];

        for (int i = 0; i < k; i++) {
            String[] tmp = bf.readLine().split(" ");
            int a = Integer.parseInt(tmp[0]);
            int b = Integer.parseInt(tmp[1]);

            floydArr[a][b] = true;
        }

        for (int t = 1; t < n+1; t++)
            for (int i = 1; i < n+1; i++)
                for (int j = 1; j < n+1; j++) {
                    if (floydArr[i][j]) continue;
                    floydArr[i][j] = floydArr[i][t] && floydArr[t][j];
                }

        int t = Integer.parseInt(bf.readLine().split(" ")[0]);
        for (int i = 0; i < t; i++) {
            String[] tmp = bf.readLine().split(" ");
            int a = Integer.parseInt(tmp[0]);
            int b = Integer.parseInt(tmp[1]);

            System.out.println(compare(a,b));
        }
    }

    static int compare(int a, int b) {
        if (floydArr[a][b]) return -1;
        if (floydArr[b][a]) return 1;
        return 0;
    }
}
