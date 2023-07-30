
import java.util.*;

public class remove_parentheses {

    public String solution(String s) {
        Stack<Character> stack = new Stack<>();
        for (char x : s.toCharArray()) {
            if (x == ')') {
                // '(' 전까지 제거
                while (stack.peek() != '(') {
                    if (!stack.isEmpty()) stack.pop();
                }
                // '(' 제거
                if (!stack.isEmpty()) stack.pop();
            }
            else stack.push(x);
        }

        return stack.stream().collect(StringBuilder::new, StringBuilder::append, StringBuilder::append).toString();
    }

    public static void main(String args[]){
        remove_parentheses T = new remove_parentheses();
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(T.solution(s));
        sc.close();
    }

}