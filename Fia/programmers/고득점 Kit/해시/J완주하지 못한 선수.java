import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {

        HashMap<String, Integer> dictionary = new HashMap<>();

        for (String p : participant) {
            dictionary.put(p, dictionary.getOrDefault(p, 0) + 1);
        }

        for (String c : completion) {
            dictionary.put(c, dictionary.get(c) - 1);

            if (dictionary.get(c) == 0) {
                dictionary.remove(c);
            }
        }

        return dictionary.keySet().iterator().next();
    }
}
