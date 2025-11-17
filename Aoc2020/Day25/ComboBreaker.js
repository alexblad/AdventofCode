var doorKey = 11349501;
var cardKey = 5107328;
var subjectNumber = 7;
function getLoopSize(key) {
    var value = 1;
    var loopSize = 0;
    while (value !== key) {
        value = value * subjectNumber;
        value = value % 20201227;
        loopSize++;
    }
    return loopSize;
}
console.log("Card Loop Size: ".concat(getLoopSize(cardKey)));
console.log("Door Loop Size: ".concat(getLoopSize(doorKey)));
