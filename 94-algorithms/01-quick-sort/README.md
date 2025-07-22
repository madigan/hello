# Quick Sort

Invented by Tony Hoare in 1961, Quick Sort is able to do an in-place sort (space is O(1)) and has an average compute complexity of O(n log n).

## Algorithm

The algorithm has three steps:

1. Choose an element as a pivot.
2. Move anything smaller to one side, anything larger to the other
3. Repeat the process on each side of the pivot.

## Complexity

Since the array is sorted in place, the space complexity is constant.

The absolute worst case (if you pivot around the largest element in every segment) is O(N^2). However, this is very unlikely unless the array is already sorted, so the compute is generally considered to be O(n log n)

## Choosing the Pivot

The tricky part is actually choosing a pivot point.

### First/Last element

The easiest way is to just pick the first or last element in the section, but if the array is sorted this can lead to a worst-case performance of O(N^2).

### Random Element

If we choose an element at random, the odds of our worst case scenario become low (1/N).

The only drawback is if the RNG call is expensive.

### Median of [first, middle, last]

We can also pick the median of [first, middle, last] as the pivot, which avoids the O(N^2) case if the array is sorted, partially sorted, or follows a pattern.

## References

- [Michael Sambol](https://www.youtube.com/watch?v=Hoixgm4-P4M) does a great job explaining how the algorithm works.
- *The Algorithm Design Manual* (2nd Ed) by Steven S. Skiena, 123–129.