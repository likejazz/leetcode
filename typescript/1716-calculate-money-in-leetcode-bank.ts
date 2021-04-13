function totalMoney(n: number): number {
    let quotient: number = Math.floor(n / 7)
    let remainder: number = n % 7
    let result: number = 0

    // Calculate full-weekly deposits.
    for (let i = 1; i <= quotient; i++) {
        for (let j = i; j < i + 7; j++) {
            result += j
        }
    }

    // Calculate uncomplete-weekly deposits.
    for (let i = quotient + 1; i <= quotient + remainder; i++) {
        result += i
    }

    return result
};
