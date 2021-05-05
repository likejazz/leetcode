function numDifferentIntegers(word: string): number {
    // Extract only numbers from string
    let regex: RegExp = /[\d]+/g
    let match: RegExpExecArray | null
    let results: Set<BigInt> = new Set()

    while (match = regex.exec(word)) {
        results.add(BigInt(match[0]))
    }

    return results.size
};
