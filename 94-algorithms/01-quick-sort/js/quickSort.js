import assert from "node:assert";

const given = [0, 4, 1, 2, 6, 9, 7, 2];
const expected = [0, 1, 2, 2, 4, 6, 7, 9];

/**
 * 
 * @param {number[]} arr The array to sort in place
 * @param {number} left the starting index
 * @param {number} right the ending index (inclusive)
 */
function quickSort(arr, left = 0, right = arr.length-1) {
  if (right - left > 1) {
    const pivot = partition(arr, left, right);
    quickSort(arr, left, pivot-1);
    quickSort(arr, pivot+1, right);
  }
}

function partition(arr, left, right) {
  // Choosing a random pivot point makes the average case more efficient for pre-sorted lists.
  // Naive: const pivot = right;
  // Random: const pivot = Math.floor(Math.random() * (right - left)) + left;
  // Or pick the median of first/middle/last
  const pivot = medianOf([arr[left], arr[(left + right) >> 1], arr[right]]);
  swap(arr, pivot, right);

  let highestI = left;
  for (let i = left; i < right; i++) {
    if (arr[i] < arr[right]) {
      swap(arr, i, highestI);
      highestI++;
    };
  }
  swap(arr, right, highestI)
  return highestI;
}

function swap(arr, a, b) {
  if (a === b) return;
  arr[a] ^= arr[b];
  arr[b] ^= arr[a];
  arr[a] ^= arr[b];
}

// Normally we would use quickselect instead of sort, but we know that array.length is always 3.
function medianOf(arr) {
  return arr.sort()[arr.length >> 1];
}

console.log("GIVEN", given);
quickSort(given);
console.log("EXPECTED", expected);
console.log("ACTUAL", given);
assert(given.every((v, i) => expected[i] === v));