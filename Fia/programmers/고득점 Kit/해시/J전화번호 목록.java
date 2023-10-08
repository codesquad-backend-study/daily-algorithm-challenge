import java.util.HashMap;
import java.util.Set;

class Solution {
    public boolean solution(String[] phone_book) {
        HashMap<Character, HashMap> trie = new HashMap<>();

        for (String phoneNumber : phone_book) {
            HashMap<Character, HashMap> current = trie;

            for (int i = 0; i < phoneNumber.length(); i++) {
                Set<Character> numbers = current.keySet();

                char alphabet = phoneNumber.charAt(i);

                if (!numbers.contains(alphabet)) {
                    current.put(alphabet, new HashMap<>());
                }

                if (current.get(alphabet) != null &&
                    current.get(alphabet).keySet().contains('*')) {
                    return false;
                }

                current = current.get(alphabet);
            }

            Set<Character> numbers = current.keySet();

            if (numbers.size() > 1) {
                return false;
            }

            if (!numbers.isEmpty() && !numbers.contains('*')) {
                return false;
            }

            current.put('*', null);
        }

        return true;
    }
}
