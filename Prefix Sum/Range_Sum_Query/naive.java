class NumArray {

    private int[] sumArray;
    private int size;

    public NumArray(int[] nums) {
        this.size = nums.length;
        this.sumArray = new int[this.size];

        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            sumArray[i] = sum;
        }
    }
    
    public int sumRange(int left, int right) {
        if (left == 0) {
            return sumArray[right];
        } else {
            return sumArray[right] - sumArray[left - 1];
        }
    }
}

public class naive {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5};
        NumArray numArray = new NumArray(nums);

        System.out.println("Sum of range (0, 2): " + numArray.sumRange(0, 2)); // Expected: 1+2+3 = 6
        System.out.println("Sum of range (2, 4): " + numArray.sumRange(2, 4)); // Expected: 3+4+5 = 12
        System.out.println("Sum of range (0, 4): " + numArray.sumRange(0, 4)); // Expected: 1+2+3+4+5 = 15
    }
}

class NumArray_original {

    private int[] nums;
    private int[] sumArray;
    private int size;

    public NumArray_original(int[] nums) {
        this.nums = nums;
        this.size = nums.length;
        this.sumArray = new int[this.size];

        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            sumArray[i] = sum;
        }
    }
    
    public int sumRange(int left, int right) {
        return sumArray[right] - sumArray[left] + nums[left];
    }
}

// slightly faster than the new one, as it avoids conditional checks
// this naive solution is fast enough
