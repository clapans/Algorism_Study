import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

class State {
    private int[] horses;
    private int next,score;
    private static final int[] redD = new int[32];
    private static final int[] blueD = {
            0,0,0,0,0,21,0,0,0,0,
            25,0,0,0,0,27,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0
    };

    private static final int[] scoreBoard = {
            0,2,4,6,8,10,12,14,16,18,20,22,24,
            26,28,30,32,34,36,38,40,13,16,19,25,
            22,24,28,27,26,30,35
    };

    public State(int[] horses, int next, int score) {
        this.horses = horses;
        this.next = next;
        this.score = score;
    }

    public int getScore() {
        return score;
    }

    public int[] getHorses() {
        return horses;
    }

    public int getNext() {
        return next;
    }

    public boolean move(int idx, int cnt, boolean start) {
        if (cnt > 5) return false;
        if (horses[idx] == -1) return true;
        if (cnt < 1) {
            if (isDuplicate(idx)) return false;
            score += scoreBoard[horses[idx]];
            return true;
        }
        if ((horses[idx] == 5 || horses[idx] == 10 || horses[idx] == 15) && start)
            horses[idx] = blueD[horses[idx]];
        else
            horses[idx] = redD[horses[idx]];
        return move(idx,cnt - 1,false);
    }

    public boolean isDuplicate(int idx) {
        for (int i = 0; i < 4; i++) {
            if (i == idx) continue;
            if (horses[i] == horses[idx])
                return true;
        }
        return false;
    }

    public static void settings() {
        for (int i = 0; i < 32; i++)
            redD[i] = i + 1;

        redD[24] = 30;
        redD[26] = 24;
        redD[29] = 24;
        redD[31] = 20;
        redD[20] = -1;
    }
}

public class Main {

    static boolean isSetting;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        if (!isSetting) {
            State.settings();
            isSetting = true;
        }

        String[] inputs = bf.readLine().split(" ");
        int[] dices = new int[10];
        for (int i = 0; i < 10; i++)
            dices[i] = Integer.parseInt(inputs[i]);
        System.out.println(maxResult(dices));
    }

    static int maxResult(int[] dices) {
        int res = 0;
        Queue<State> queue = new LinkedList<>();
        queue.add(new State(new int[] {0,0,0,0},0,0));

        while (queue.size() > 0) {
            State state = queue.poll();
            if (state.getNext() == dices.length) {
                if (state.getScore() > res)
                    res = state.getScore();
                continue;
            }
            int cnt = dices[state.getNext()];
            int[] horses = state.getHorses();

            for (int i = 0; i < 4; i++) {
                if (horses[i] == -1) continue;
                State newState = new State(new int[] {
                        horses[0],horses[1],
                        horses[2],horses[3]
                },state.getNext() + 1,state.getScore());
                if (newState.move(i,cnt,true))
                    queue.add(newState);
            }
        }
        return res;
    }
}
