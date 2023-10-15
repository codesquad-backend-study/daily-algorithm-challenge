import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> closet = new HashMap<>();

        for (String[] cloth: clothes) {
            closet.put(cloth[1], closet.getOrDefault(cloth[1], 0) + 1);
        }

        if (closet.keySet().size() == 1) {
            return clothes.length;
        }

        int result = 1;
        for (Integer value : closet.values()) {
            result *= value + 1;
        }

        return result - 1;
    }
}
