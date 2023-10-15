import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        int max = nums.length / 2;

        HashSet<Integer> dictionary = new HashSet<>();

        for (int num : nums) {
            dictionary.add(num);

            if (dictionary.size() > max) {
                return max;
            }
        }

        return dictionary.size();
    }
}
