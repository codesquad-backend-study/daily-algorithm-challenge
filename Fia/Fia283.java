package Fia;

public class Fia283 {
    public void moveZeroes(int[] nums) {
        int zero = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == 0) {
                int next = nums[i + 1];
                if (next == 0) {
                    zero++;
                    continue;
                }
                nums[i - zero] = next;
                nums[i + 1] = 0;
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = {0, 1, 0, 3, 12};
        Fia283 fia283 = new Fia283();
        fia283.moveZeroes(nums);
    }
}
