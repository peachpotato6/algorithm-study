package array.reversed_primes;

import java.util.Scanner;
import java.util.ArrayList;

public class reversed_primes_easy {

    // 소수 찾기 알고리즘
    public boolean isPrime(int num) {
        // 1은 소수 아님
        if (num == 1) return false;
        // 1과 자기 자신으로만 나누어지는게 소수니까 다른 숫자로도 나눠지면 소수가 아님
        for (int i = 2; i < num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }

    public ArrayList<Integer> solution(int n, int[] arr) {

        ArrayList<Integer> answer = new ArrayList<>();

        // 숫자 앞뒤 바꾸기 알고리즘
        for (int i = 0; i < n; i++) {
            int tmp = arr[i];
            int res = 0;
            while (tmp > 0) {
                int t = tmp % 10;
                res = res * 10 + t;
                tmp = tmp / 10;
            }
            if (isPrime(res)) answer.add(res);
        }

        return answer;
    }

    public static void main(String args[]) {

        reversed_primes_easy T = new reversed_primes_easy();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        for (int x : T.solution(n,arr)) System.out.print(x + " ");
        sc.close();
    }
    
}
