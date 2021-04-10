function checkIfExist(arr: number[]): boolean {
    let map: Map<number, boolean> = new Map()
    let zero_exists: boolean = false

    for (let a of arr) {
        if (a != 0 || zero_exists) {
            map.set(a, true)
        } else {
            zero_exists = true
        }
    }

    for (let a of arr) {
        if (map.get(a * 2))
            return true
    }

    return false
};
