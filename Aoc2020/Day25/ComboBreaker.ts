 let doorKey: number = 11349501;
let cardKey: number = 5107328;
let subjectNumber: number = 7;

function getLoopSize(key: number): number {
    let value: number = 1;
    let loopSize: number = 0;
    while (value !== key) {
        value = value * subjectNumber;
        value = value % 20201227;
        loopSize++;
    }

    return loopSize;
}

function getEncryptionKey(loopSize: number, subjectNumber: number): number {

    let value: number = 1;
    for (let i = 0; i < loopSize; i++) {
        value = value * subjectNumber;
        value = value % 20201227;
    }

    return value;

}


console.log(`Card Loop Size: ${getLoopSize(cardKey)}`);
console.log(`Door Loop Size: ${getLoopSize(doorKey)}`); 

console.log(`Encryption Key (Card): ${getEncryptionKey(getLoopSize(cardKey), doorKey)}`);
console.log(`Encryption Key (Door): ${getEncryptionKey(getLoopSize(doorKey), cardKey)}`);