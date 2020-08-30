//leetcode submit region begin(Prohibit modification and deletion)
function findNumbers(nums: number[]): number {
    let count: number = 0;

    for (let num of nums) {
        if ((num.toString()).length % 2 == 0) {
            count++;
        }
    }
    return count;
};
//leetcode submit region end(Prohibit modification and deletion)

// 1295

let c: number = findNumbers([12, 345, 2, 6, 7896])
console.log(c);

// $ deno run test_leetcode.ts
