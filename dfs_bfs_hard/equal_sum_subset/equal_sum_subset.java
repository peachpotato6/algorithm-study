import java.util.*;
public class equal_sum_subset {

    static String answer = "NO";
    static int n, total = 0;
    static int[] arr;
    boolean flag = false;

    public void DFS(int L, int sum) {

        if (flag) return;
        if (sum > total/2) return;
        if (L == n) {
            if (sum == (total-sum)) {
                answer = "YES";
                // 답 찾았으면 스택에 남아있는 DFS들 다 return
                flag = true;
            }
        }
        else {
            // 두 갈래로 뻗기
            DFS(L+1, sum+arr[L]);
            DFS(L+1, sum);
        }
    }

    public static void main(String args[]) {

        equal_sum_subset T = new equal_sum_subset();
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            total += arr[i];
        }
        T.DFS(0,0);
        System.out.println(answer);
        sc.close();
    }

    
}
