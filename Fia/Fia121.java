package Fia;

public class Fia121 {
    public int maxProfit(int[] prices) { // 주의 : [2, ..., 11, 1, ..., 9]
        int minPrice = prices[0];
        int maxProfit = 0;
        for (int i = 1; i < prices.length; i++) {
            minPrice = Math.min(minPrice, prices[i]);
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }
        return maxProfit;
    }

    public static void main(String[] args) {
        Fia121 fia121 = new Fia121();
        fia121.maxProfit(new int[] {7, 1, 5, 3, 6, 4});
    }
}
