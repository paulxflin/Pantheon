# LeetCode

Solutions to Questions on LeetCode in Python

Categories:

1. Accepted: My accepted submissions for the problem
2. Revisited: Submissions from revisiting questions
3. Solution: LeetCode provided Solutions
4. Top Voted: Solutions from discussion section
5. Sample: From faster time/space complexity samples

## Easy

| #    | Title                          | Basic idea (One line)                                          |
| ---- | ------------------------------ | -------------------------------------------------------------- |
| 1    | Two Sum                        | Dict (num, index), O(n) time, O(n) space                       |
| 13   | Roman to Integer               | Subtract if smaller number before bigger, T: O(n), S: O(1)     |
| 14   | Longest Common Prefix          | Find shortest str and check each char, T: O(n\*l), S: O(l)     |
| 20   | Valid Parentheses              | Store open braces in a stack, pop for match, T&S: O(n)         |
| 21   | Merge Two Sorted Lists         | Iterative (compare and append to list), O(n) time, O(1) space. |
| 26   | Remove Dups from Sorted Array  | Two Pointers place uniques one after another, T: O(n), S: O(1) |
| 27   | Remove Element                 | Two pointers meet in middle, T: O(n), S: O(1)                  |
| 28   | Implement strStr()             | Lib find() or brute force, T: O(n\*m), S: O(1). Advanced: KMP  |
| 35   | Search Insert Position         | Bisect Binary Search, T: O(log n), S: O(1)                     |
| 53   | Maximum Subarray               | DP/Kandane's T: O(n), S: O(1). D&C T: O(n), S: O(log n)        |
| 66   | Plus One                       | Convert to int, T&S: O(n), Carry from right to left, S: O(1)   |
| 69   | Sqrt(x)                        | Binary Search with multiplication, T: O(log n), S: O(n)        |
| 70   | Climbing Stairs                | Optimised DP (Essentially Fibonacci), T: O(n), S: O(1)         |
| 83   | Remove Dups from Sorted List   | Set cur.next to next elem, increment o/w, T: O(n), S: O(1)     |
| 88   | Merge Sorted Array             | Two Pointers fill in nums1 in reverse order, T: O(n), S: O(1)  |
| 94   | Binary Tree Inorder Traversal  | Recursive/Iterative O(n) time, O(n) space                      |
| 100  | Same Tree                      | Recursively check nodes, O(n) time and space                   |
| 101  | Symmetric Tree                 | Recursive or Iterative + Stack/Queue, T&S: O(n)                |
| 104  | Maximum Depth of Binary Tree   | Recursion with levels, incrementing in child call, T&S: O(n)   |
| 108  | Convert Sorted Array to BST    | Recursively Build Left and Right Subtrees, T&S: O(n)           |
| 110  | Balanced Binary Tree           | Recursively Check tree balance, T&S: O(n)                      |
| 111  | Minimum Depth of Binary Tree   | BFS/DFS, BFS in most cases is better than DFS, T&S: O(n)       |
| 112  | Path Sum                       | Recursively check for path at leaf, T&S: O(n)                  |
| 118  | Pascal's Triangle              | Generate next row based on previous row, T&S: O(n)             |
| 119  | Pascal's Triangle II           | Store previous row to find next row, T: O(n^2), S: O(n)        |
| 121  | Best Time to Buy & Sell Stock  | Track min and profit / Kandane's Algorithm, T: O(n), S: O(1)   |
| 122  | Best Time to Buy/Sell Stock II | Buy at valleys, sell at peaks, T: O(n), S: O(1)                |
| 125  | Valid Palindrome               | Two Pointers in place check for isalnum(), T: O(n), S: O(1)    |
| 136  | Single Number                  | Counter (Hash) or Math, O(n) time, O(n) space. XOR O(1) space! |
| 141  | Linked List Cycle              | Tortoise and Hare, O(n) time, O(1) space                       |
| 155  | Min Stack                      | Store min for every node, O(1) push, pop, top, getMin          |
| 160  | Intersect of Two Linked Lists  | Two pointers two pass, O(n) time, O(1) space                   |
| 167  | Two Sum II - Input Arr Sorted  | Two pointer, T: O(n), S: O(1)                                  |
| 169  | Majority Element               | Boyer-Moore Voting Algorithm, O(n) time, O(1) space            |
| 171  | Excel Sheet Column Number      | Convery A-Z to 1-26 with 26 base mult, O(n) time, O(1) space   |
| 190  | Reverse Bits                   | Format in 32 bits and reverse or loop bit shift, T&S: O(1)     |
| 191  | Number of 1 Bits               | Bit operation to cancel least significant bit, T: O(n) S: O(1) |
| 202  | Happy Number                   | Use set to memorise seen numbers, T: O(loops \* dig), S: O(1)  |
| 203  | Remove Linked List Elements    | Single Pointer, Dummy Head, T: O(n), S: O(1)                   |
| 206  | Reverse Linked List            | Iteratively update the node, T: O(n), S: O(1)                  |
| 217  | Contains Duplicate             | Use Set to store seen values or compare lengths, T&S: O(n)     |
| 226  | Invert Binary Tree             | Recursively apply to invert to child within swap, T&S: O(n)    |
| 234  | Palindrome Linked List         | Reversed First Half == Second Half, T: O(n), S: O(1)           |
| 237  | Delete Node in a Linked List   | Set cur.val as next.val, cur.next = next.next, T&S: O(1)       |
| 242  | Valid Anagram                  | Use a Counter or Two Dicts and == comparator, T&S: O(n)        |
| 257  | Binary Tree Paths              | Recursive DFS adding Child Nodes, T&S: O(n)                    |
| 268  | Missing Number                 | Calculate expected sum and subtract sum nums, T: O(n), S: O(1) |
| 278  | First Bad Version              | Binary Search with Bisect + Wrapper, T: O(log n), S: O(1)      |
| 283  | Move Zeroes                    | Swap all non-zeros into final positions, T: O(n), S: O(1)      |
| 292  | Nim Game                       | Win if n % 4 != 0, O(n) time and space.                        |
| 303  | Range Sum Query - Immutable    | Memorisation of Accumulations, T&S: O(n)                       |
| 326  | Power of Three                 | Loop Divide, T: O(log n), Modulo largest power of 3, T&S: O(1) |
| 338  | Counting Bits                  | DP: ans[i] = ans[i >> 1] + (i & 1), T&S: O(n)                  |
| 344  | Reverse String                 | Library in place reverse(), T: O(n), S: O(1)                   |
| 345  | Reverse Vowels of a String     | Two Pointer Swap or Regex Findall and Sub, T&S: O(n)           |
| 349  | Intersection of Two Arrays     | Set intersection, T: O(n \* m), S: O(n+m)                      |
| 350  | Intersection of Two Arrays II  | Deduct from Counter, T&S: O(n+m)                               |
| 367  | Valid Perfect Square           | n to the power of 0.5 mod 1 == 0, T&S: O(1)                    |
| 374  | Guess Number Higher or Lower   | Binary Search, T: O(log n), S: O(1)                            |
| 383  | Ransom Note                    | Use a counter and subtract from ransomNote, T&S: O(m + n)      |
| 387  | First Unique Char in a String  | Use a Counter, and check minimum of val == 1, T: O(n), S: O(1) |
| 389  | Find the Difference            | Counter, Difference, or XOR, T: O(n), S: O(1), Counter S: O(n) |
| 392  | Is Subsequence                 | Two pointers and/or iterator, T: O(t), S: O(1)                 |
| 401  | Binary Watch                   | Collect One Bits List Comprehension / Backtracking, T&S: O(1)  |
| 409  | Longest Palindrome             | Use Counter to count number of odds or pairs, T&S: O(n)        |
| 412  | Fizz Buzz                      | Use if-elif-else or list comprehension, T&S: O(n)              |
| 441  | Arranging Coins                | Express with Maths, Complete the Square, T&S: O(1)             |
| 455  | Assign Cookies                 | Least Greedy Child first, T: O(g log g + s log s) S: O(g + s)  |
| 461  | Hamming Distance               | Take XOR of x and y, and count the number of ones, T&S: O(1)   |
| 463  | Island Perimeter               | Check adjacent for edge + Short Circuit, T: O(m\*n), S: O(1)   |
| 496  | Next Greater Element I         | Stack for smaller values, and dict containing ans, T&S: O(n)   |
| 500  | Keyboard Row                   | Set of both lines and lowercase word, T&S: O(n)                |
| 509  | Fibonacci Number               | Use two variables and a for loop, T: O(n), S: O(1)             |
| 520  | Detect Capital                 | Use inbuilts isupper, islower, istitle, T: O(n), S: O(1)       |
| 521  | Longest Uncommon Subsequence I | Same -> -1, o/w return longer string, T: (min(x, y)), S: O(1)  |
| 541  | Reverse String II              | Slice Assignment with slice reverse, T&S: O(n)                 |
| 557  | Reverse Words in a String III  | Split Reverse Join or Double Reverse, T&S: O(n)                |
| 559  | Maximum Depth of N-ary Tree    | DFS, O(n) time, O(n) space. BFS, O(n) time, O(n) space         |
| 561  | Array Partition I              | Sum + Stepped Slicing + Sort, T: O(n log n), S: O(n)           |
| 563  | Binary Tree Tilt               | Single Function Sum, Tilt, Update Res (Global), T&S: O(n)      |
| 589  | N-ary Tree Preorder Traversal  | Recursive Traversal or Iterative with Stack, T&S: O(n)         |
| 590  | N-ary Tree Postorder Traversal | Recursive Traversal or Pre-order R-L reverse, T&S: O(n)        |
| 605  | Can Place Flowers              | Greedily check 3 consecutive plots are empty, T: O(n), S: O(1) |
| 606  | Construct Str from Binary Tree | Conditionally expand left and right recursively, T&S: O(n)     |
| 617  | Merge Two Binary Trees         | Recursively add or chose one branch, T&S: O(m + n)             |
| 637  | Avg of Levels in Binary Tree   | DFS with Depth or compute average each level, T&S: O(n)        |
| 653  | Two Sum IV - Input is a BST    | DFS or BFS with adding and lookup using a set, T&S: O(n)       |
| 657  | Robot Return to Origin         | Track x and y while scanning through moves, T: O(n), S: O(1)   |
| 680  | Valid Palindrome II            | Two Pointers, check both cases l != r, T&S: O(n)               |
| 682  | Baseball Game                  | Perform ops on array and sum, T&S: O(n)                        |
| 690  | Employee Importance            | Emp Hashmap (id to inx or id to emp) + DfS or BFS, T&S: O(n)   |
| 696  | Count Binary Substrings        | Count Consecutive Groups and take min, T: O(n), S: O(1)        |
| 700  | Search in a Binary Search Tree | Iterative T: O(n), S: O(1) or Recursive search T&S: O(n)       |
| 703  | Kth Largest Elem in a Stream   | Heap of k elems, T: O(k log n + n) init, O(log n) add, S: O(k) |
| 704  | Binary Search                  | Binary Search with Bisect, T: O(log n), S: O(1)                |
| 709  | To Lower Case                  | Use python str.lower() method, T: O(n), S: O(1)                |
| 728  | Self Dividing Numbers          | Get each digit by converting to string, T: O(n\*l), S: O(n+l)  |
| 733  | Flood Fill                     | DFS + Skip if colour is not original, T&S: O(n)                |
| 744  | Find Smallest Letter > Target  | Binary Search using Bisect, T: O(log n), S: O(1)               |
| 746  | Min Cost Climbing Stairs       | Bottom Up DP 3 Vars, T: O(n), S: O(1)                          |
| 748  | Shortest Completing Word       | Filter the License, then Counter Subtraction, T&S: O(n)        |
| 766  | Toeplitz Matrix                | Check Part of Each Level Slices, T: O(m\*n), S: O(n)           |
| 771  | Jewels and Stones              | Set of Jewels + Sum Stones in Set, T: O(J+S), S: O(J)          |
| 783  | Min Dist Between BST Nodes     | In Order Traversal with DFS and cache pred, T: O(n), S: O(h)   |
| 804  | Unique Morse Code Words        | Set + Ord + List Comprehension, T&S: O(S)                      |
| 806  | Num of Lines To Write String   | Track current line width and num lines total, T: O(n), S: O(1) |
| 811  | Subdomain Visit Count          | Use a Counter and add the count to every subdom, T&S: O(n)     |
| 821  | Shortest Dist to a Character   | One Pass with find(), or Two Pass for left vs right, T&S: O(n) |
| 824  | Goat Latin                     | Apply rules to transform words with numeric index, T&S: O(n)   |
| 832  | Flipping an Image              | Modify i and len(n)-i-1 simultaneously, T: O(n), S: O(1)       |
| 844  | Backspace String Compare       | Two Pointers reverse scan, T: O(n), S: O(1)                    |
| 852  | Peak Index in a Mountain Array | Binary Seach, Golden-Section Search, T: O(log n), S: O(1)      |
| 860  | Lemonade Change                | Greedy Simulation, T: O(n), S: O(1)                            |
| 872  | Leaf-Similar Trees             | DFS + List Compare, T&S: O(t1 + t2)                            |
| 876  | Middle of the Linked List      | Two Pointers tortoise and hare, T: O(n), S: O(1)               |
| 883  | Projection Area of 3D Shapes   | Use sum with Zip and Listcomp or Map, T: O(n), S: O(1)         |
| 884  | Uncommon Words in 2 Sentences  | Find Words Appearing Once, T&S: O(n)                           |
| 888  | Fair Candy Swap                | Sums to find diff and Sets, T: O(n + m), S: O(n)               |
| 897  | Increasing Order Search Tree   | DFS + Dummy, T&S: O(n). DFS + Relinking, T: O(n), S: O(h)      |
| 905  | Sort Array By Parity           | Two Pointers In-Place Swap, T: O(n), S: O(1)                   |
| 908  | Smallest Range I               | Min score is Max - Min - 2k, T: O(n), S: O(1)                  |
| 917  | Reverse Only Letters           | Two Pointers, One pass, while-if loop, T&S: O(n)               |
| 922  | Sort Array By Parity II        | Two pointers even and odd swap, T: O(n), S: O(1)               |
| 925  | Long Pressed Name              | Two Pointers to match all letters in name, T: O(n), S: O(1)    |
| 929  | Unique Email Addresses         | Set + Find/Split local name for slicing, T&S: O(n)             |
| 933  | Number of Recent Calls         | Queue, O(1) time and space due to problem constraints          |
| 937  | Reorder Data in Log Files      | Separate into two lists, sort letters, T: O(n log n), S: O(n)  |
| 938  | Range Sum of BST               | DFS if parent strictly in range, O(n) time, O(h) space         |
| 942  | DI String Match                | Ad-Hoc high and low solution, T&S: O(n)                        |
| 944  | Delete Columns to Make Sorted  | Delete Row function with index access, T: O(n\*m), S: O(1)     |
| 961  | N-Repeated Elem in Size 2N Arr | Find first duplicate with set or use math sums, T&S: O(n)      |
| 965  | Univalued Binary Tree          | Depth First Search compare with root, T&S: O(n)                |
| 976  | Largest Perimeter Triangle     | Reverse Sort and Try Biggest Trio, T: O(n log n), S: O(n)      |
| 977  | Squares of a Sorted Array      | Two Pointers at either ends, O(n) time, O(n) space             |
| 993  | Cousins in Binary Tree         | Tuple with BFS, T&S: O(n). Tuple with DFS, T: O(n), S: O(h)    |
| 997  | Find the Town Judge            | Trusted - Trusts == n-1 for Judge, O(n + t) time, O(n) space   |
| 999  | Available Captures for Rook    | Move Vector in 4 directions, O(n) time, O(1) space             |
| 1002 | Find Common Characters         | Counter Intersection and elements, O(n) time, O(l) space       |
| 1005 | Max Sum Of Array After K Negs  | Sort, Negate Negs,Subtract Min if Odd, T: O(n log n), S: O(n)  |
| 1013 | Partition Arr into 3 Equal Sum | Each part will have a sum of the total/3, T: O(n), S: O(1)     |
| 1021 | Remove Outermost Parentheses   | Open = Closed, O(n) time and space                             |
| 1022 | Sum of Root To Leaf Bin Nums   | Recursive traversal and return 0 on non-leaf case, T&S: O(n)   |
| 1025 | Divisor Game                   | Even wins, odd loses O(1). Bottom up DP O(n \* sqrt(n)) time   |
| 1030 | Matrix Cells in Distance Order | Create coords and sort by distance key, T: O(n log n), S: O(n) |
| 1046 | Last Stone Weight              | Heap T: O(nlogn), S: O(n). bisect.insort T: O(n^2), S: O(n)    |
| 1047 | Remove All Adj Dups In String  | Use stack deleting top and ch dups, join for result, T&S: O(1) |
| 1051 | Height Checker                 | Use counting sort and iterate through heights, T&S: O(n)       |
| 1078 | Occurrences After Bigram       | Check the previous two with index or zip, T&S: O(n)            |
| 1089 | Duplicate Zeros                | Count Zeroes and Swap backwards, T: O(n), S: O(1)              |
| 1108 | Defanging an IP Address        | Use Python .replace('.', '[.]'), O(n\*m) time, O(n) space      |
| 1122 | Relative Sort Array            | Dict of indicies and sort by key, T: O(A log A + B), S: O(A+B) |
| 1137 | N-th Tribonacci Number         | Bottom Up DP with modulo, T: O(n), S: O(1)                     |
| 1160 | Find Words Formable by Chars   | Create a Counter, and compare items, T: O(n), S: O(1)          |
| 1189 | Maximum Number of Balloons     | Counter with Int Div of each char, T&S: O(n)                   |
| 1200 | Minimum Absolute Difference    | Sort the find min_diff in one pass, T: O(n log n), S: O(n)     |
| 1207 | Unique Number of Occurrences   | Len of set of counter's values vs len of counter, T&S: O(n)    |
| 1217 | Minimum Cost to Move Chips     | Count odds and evens, and take the minimum, T: O(n), S: O(1)   |
| 1221 | Split a Str in Balanced Strs   | Increment Res when num L - num R = 0, O(n) time, O(1) space    |
| 1252 | Cells with Odd Val in a Matrix | Odd Rows and Cols with XOR, T: O(n + m + L), S: O(m + n)       |
| 1266 | Min Time Visiting All Points   | Sum the max abs difference between points, T: O(n), S: O(1)    |
| 1281 | Product - Sum of Digits of Int | Map & Reduce, T&S: O(log n). Mod & Div, T: O(log n), S: O(1)   |
| 1290 | Convert Binary to Int in LL    | Bit Shift Left and Bitwise Or, T: O(n), S: O(1)                |
| 1295 | Find Nums with Even Num Digits | Find digits with integer division, T: O(n\*d), S: O(1)         |
| 1299 | Replace Elem with Greatest R   | Get max and replace right to left, T: O(n), S: O(1)            |
| 1304 | Find N Unique Ints Sum up to 0 | Min step of 2 between -1 and 1, generalise odd/even, T&S: O(n) |
| 1309 | Decrypt Str Alpha to Int Map   | Chr + Ord + Regex/Iterative + Deque/Listcomp, T&S: O(n)        |
| 1313 | Decomp Run-Length Encoded List | Traverse array in pairs and use for loop, T&S: O(n)            |
| 1323 | Maximum 69 Number              | Greedily replace leftmost 6 with 9, T&S: O(n)                  |
| 1332 | Remove Palindromic Subseqs     | At most 2 ops are needed to get empty str, a then b, T&S: O(n) |
| 1337 | The K Weakest Rows in a Matrix | Binary Search + Heap (Best). Column, T: O(m \* n), S: O(k)     |
| 1342 | Num Steps to Reduce Num to 0   | Binary Representation, O(bits) space and time                  |
| 1346 | Check if N and 2N Exist        | Counter + Accept if there are 2 zeros, T&S: O(n)               |
| 1351 | Count Negative Numbers in SM   | Negative Values form Staircase, O(n + m) time, O(n) space      |
| 1356 | Sort Ints by The Num of 1 Bits | Sorting key function to count ones, T: O(n log n), S: O(n)     |
| 1365 | How Many Nums Smaller than Cur | Smallest Index of sorted is equivalent, T: O(n log n), S: O(n) |
| 1370 | Increasing Decreasing String   | Counter with asc boolean flag, O(n) time and space             |
| 1374 | Gen Strs with Odd Count Chars  | Check if odd, use asterisk operator to gen string, T&S: O(n)   |
| 1380 | Lucky Numbers in a Matrix      | Intersection of max_col and min_row, T: O(n \* m), S: O(n + m) |
| 1385 | Find the Dist Between Two Arrs | Sort arr2 + Binary Search, T: O((m + n) log m), S: O(n)        |
| 1389 | Create Target Arr in Given Ord | Use mergesort get find final positions, T: O(n log n), S: O(n) |
| 1399 | Count Largest Group            | Sum digits and increment a counter dict, T: O(n), S: O(1)      |
| 1403 | Min Non-increasing Subseq      | Reverse Sort + Sum Target + Slicing, T: O(n log n), S: O(n)    |
| 1408 | String Matching in an Array    | Build Sentence + string.Count, T: O(w \* s), S: O(w)           |
| 1413 | Min Val to Get Pos Step Sum    | Track running sum with accumulate, T: O(n), S: O(1)            |
| 1417 | Reformat The String            | Abs(digits-letters) <= 1, start with longer list, T&S: O(n)    |
| 1422 | Max Score After Splitting Str  | Find largest net value, then add initial, T: O(n), S: O(1)     |
| 1431 | Kids With the Most Candies     | Subtract extraCandies from max, compare each, T&S: O(n)        |
| 1436 | Destination City               | Difference remaining after inbound-outbound set, T&S: O(n)     |
| 1441 | Build an Array With Stack Ops  | Push for all nums, pop if missing in target, T&S: O(n)         |
| 1446 | Consecutive Characters         | One pass count consecutive chars, T: O(n), S: O(1)             |
| 1450 | Num Students doing Homework    | Iterate through each element and compare, T: O(n), S: O(1)     |
| 1455 | Check If Word Occurs As Prefix | Split + Slice / string.startswith(), T&S: O(n)                 |
| 1460 | Make 2 Arrs Eq by Rev Sub-arrs | Put both arrays in a Counter and check for eq, T&S: O(n)       |
| 1464 | Max Prod of 2 Elems in an Arr  | Keep track of Max 2 elements in one pass, T: O(n), S: O(1)     |
| 1470 | Shuffle the Array              | Use zip for two split arrays, or manually append, T&S: O(n)    |
| 1475 | Final Prices with Special Disc | Store indicies in stack, subtract conditionally, T&S: O(n)     |
| 1480 | Running Sum of 1d Array        | Use Prior Element, sum in place, T: O(n), S: O(1)              |
| 1486 | XOR Operation in an Array      | XOR using for loop for O(n) time, or pattern match T&S: O(1)   |
| 1491 | Average Salary Exclude Min Max | Find sum, max, and min to compute res, T: O(n), S: O(1)        |
| 1496 | Path Crossing                  | Tuple Coord + Seen Set + Map Update, T&S: O(n)                 |
| 1502 | Can Make Arith Prog From Seq   | Find expected gap and swap sort to pos, T: O(n log n), S: O(1) |
| 1512 | Number of Good Pairs           | Hash + Math n \* (n-1) / 2, O(n) time, O(n) space              |
| 1528 | Shuffle String                 | Create list, insert s with indicies, O(n) time and space       |
| 1534 | Count Good Triplets            | Nested for-loops for generator expression, T: O(n^3), S: O(1)  |
| 1539 | Kth Missing Positive Number    | Binary Search non-missing vals in res, T: O(log n), S: O(1)    |
| 1544 | Make The String Great          | Use a stack to conditionally add and pop + swapcase, T&S: O(n) |
| 1556 | Thousand Separator             | Join chunks of 3 together in list with . separator, T&S: O(n)  |
| 1572 | Matrix Diagonal Sum            | Sum both diagonals and remove overlap, T: O(n), S: O(1)        |
| 1588 | Sum of All Odd Length Subarrs  | Consider the contribution of each elem, T: O(n), S: O(1)       |
| 1598 | Crawler Log Folder             | Find depth from main, use max or if at main level, T&S: O(n)   |
| 1603 | Design Parking System          | Array, Instance Var, or hashmap for spaces, T&S: O(1)          |
| 1608 | Special Arr with X Elems GEQ X | Reverse Sort Binary Search, T: O(n log n), S: O(n)             |
| 1614 | Max Nesting Depth of Parens    | Count Max Open Braces with left-right scan, T: O(n), S: O(1)   |
| 1624 | Largest Substr in 2 Eq Chars   | Subtract last index from first using a dict, T&S: O(n)         |
| 1629 | Slowest Key                    | One pass to compute the longest dur, T: O(n), S: O(1)          |
| 1636 | Sort Array by Increasing Freq  | Create counter and sort by tuple key, T: O(n log n), S: O(n)   |
| 1646 | Get Maximum in Generated Array | Multiply by mod to differentiate odd/even, T&S: O(n)           |
| 1656 | Design an Ordered Stream       | Create a list and move pointer to last None, T&S: O(n) insert  |
| 1662 | Check If Two String Arr are Eq | Use generator to compare each char, T: O(min(n, m)), S: O(1)   |
| 1672 | Richest Customer Wealth        | One Liner Max of sum of rows, T: O(m \* n), S: O(m)            |
| 1678 | Goal Parser Interpretation     | Inbuilt string replacement or regex sub, T&S: O(n)             |
| 1684 | Count Num of Consistent Strs   | Word is subset of accepted or sum-all, T: O(NW), S: O(1)       |
| 1688 | Count of Matches in Tournament | n-1 matches, T&S: O(1). Even/odd if/else: T: O(log n), S: O(1) |
| 1694 | Reformat Phone Number          | Use string.translate() to strip or re.sub(): T&S: O(n)         |
| 1700 | Num Students Unable to Eat Lun | Stop when nobody wants the top sandwich: T: O(n), S: O(1)      |
| 1704 | Determine if Halves Are Alike  | Check if letters are in vowel set, T: O(n), S: O(1)            |
| 1720 | Decode XORed Array             | XOR is the inverse of XOR, T: O(n), S: O(1)                    |
| 1710 | Maximum Units on a Truck       | Reverse sort by units per box + Greedy, T: O(n log n), S: O(n) |
| 1725 | Num Rects That Can Form The LS | Track max side, increase/reset count, T: O(n), S: O(1)         |
| 1732 | Find the Highest Altitude      | Track the Max Altitude going through array, T: O(n), S: O(1)   |
| 1742 | Max Number of Balls in a Box   | Find the pattern for the summation, T: O(n \* h), S: O(1)      |
| 1748 | Sum of Unique Elements         | Counter of nums and only add key if value is 1, T&S: O(n)      |
| 1758 | Min change to Make Alt Bin Str | Count num diff from expectation take min, T: O(n), S: O(1)     |
| 1763 | Longest Nice Substring         | Recursive Set + Swapcase, T: O(n^2), S: O(n)                   |
| 1768 | Merge Strings Alternately      | One Pointer or Python itertools zip_longest, T&S: O(n + m)     |
| 1773 | Count Items Matching a Rule    | Get Index for Key + Count Matching Items, T: O(n), S: O(1)     |
| 1779 | Find Nearest Point Same X or Y | One Pass if valid, track min dist and index, T: O(n), S: O(1)  |
| 1791 | Find Center of Star Graph      | Compare first and second edges for repeated edge, T&S: O(1)    |
| 1812 | Det Color of Chessboard Square | Even or odd steps from the a1 square, T&S: O(1)                |
| 1816 | Truncate Sentence              | Split, Slice up to k, Join, T&S: O(n)                          |
| 1822 | Sign of the Product of an Arr  | Change sign if negative, return if 0, T: O(n), S: O(1)         |
| 1827 | Min Ops to Make Arr Increasing | Greedy using prev and count variables, T: O(n), S: O(1)        |
| 1832 | Check if Sentence Is Pangram   | Convert Sentence to Set and check length, T&S: O(n)            |
| 1837 | Sum of Digits in Base K        | Take the modulo and integer divide, T: O(log n), S: O(1)       |
| 1844 | Replace All Digits with Chars  | Do the shift with Chr() and Ord(), T&S: O(n)                   |
| 1859 | Sorting the Sentence           | Split, Build String, then Join, T&S: O(n)                      |
| 1863 | Sum of All Subset XOR Totals   | Backtrack O(2^n) time, O(n) space. Bit O(n) time, O(1) space   |
| 1869 | Longer Segs of Ones than Zeros | Keep track of longest 1 and 0, O(n) space, O(1) time           |
| 1876 | Substrs Sz 3 Distinct Chars    | Set length + String Slicing, T: O(n), S: O(1)                  |
| 1880 | Check Word == Sum of Two Words | Use Ord to convert to letter value, cast word to int T&S: O(n) |
| 1897 | Move Chars to Make Strs Equal  | Use a Counter and divide all elems by len(w), T&S: O(n)        |
| 1903 | Largest Odd Number in String   | Find Rightmost Odd Digit and Slice, T: O(n), S: O(1)           |
| 1913 | Max Prod Diff Between 2 Pairs  | Find the two largest and smallest, find diff, T: O(n), S: O(1) |
| 1920 | Build Array from Permutation   | Use Euclidian Algorithm to transform nums, T: O(n), S: O(1)    |
| 1925 | Count Square Sum Triples       | Find c and check if it's whole, T: O(n^2), S: O(1)             |
| 1929 | Concatenation of Array         | Use concatenation or extend, T&S: O(n)                         |
| 1935 | Max Num of Words You Can Type  | Broken letter set, add words any letters in it, T&S: O(n)      |
| 1941 | Check All Chars Occurs Equally | Length of Counter(s).values() set, T&S: O(n)                   |
| 1945 | Sum of Digs of Str after Conv  | Iterate chars in string and sum each transform, T&S: O(n)      |
| 1957 | Delete Chars to Make Fancy Str | Join an ans array and keep track of conseq count, T&S: O(n)    |
| 1961 | Check If Str Is Prefix of Arr  | Check word in words are equal to slice, T: O(n), S: O(1)       |
| 1967 | Strs That are Substrs in Word  | Sum instances pattern is in word, T: O(n), S: O(1)             |
| 1974 | Min Time to Type Word Special  | Find min dist between consecutive letters, T: O(n) S: O(1)     |
| 1979 | Find GCD of Array              | Use Euclidean Algorithm, T: O(n + log(min(a,b))), S: O(1)      |
| 2000 | Reverse Prefix of Word         | Find index and reverse slice, T&S: O(n)                        |
| 2006 | Count Pairs With Abs Diff K    | Dictionary to store num prior seen vals, T&S: O(n)             |
| 2011 | Final Value of Var After Ops   | If-Else on index 1, or sum + generator, T: O(n), S: O(1)       |
| 2032 | Two Out of Three               | Use sets and take the intersections, T&S: O(n)                 |
| 2037 | Min Num Moves to Seat Everyone | Sort and sum abs diff of elements, T: O(n log n), S: O(n)      |
| 2042 | Check if Nums Asc in Sentence  | Split s, convert numeric words to int, check prev, T&S: O(n)   |
| 2053 | Kth Distinct Str in an Array   | Use a counter to check is distinct, loop in order, T&S: O(n)   |
| 2057 | Smallest Index With Equal Val  | Enumerate check in for loop and return first, T: O(n), S: O(1) |
| 2062 | Count Vowel Substrs of a Str   | Track latest positions of all vowels, T: O(n), S: O(1)         |
| 2068 | Check If Two Str are Almost Eq | Counter arithmetic or use set of chars, T: O(n), S: O(1)       |
| 2078 | Two Furthest Houses Dif Colors | One of the endpoints must be involved, T: O(n), S: O(1)        |
| 2085 | Count Common Words With One Oc | Counter for words, iterate either counter, T&S: O(n)           |
| 2089 | Find Target Inds After Sorting | Count smaller and eq elements, T&S: O(n)                       |
| 2103 | Rings and Rods                 | Create a dict with rod key and colour sets, T: O(n), S: O(1)   |

## Medium

| #    | Title                                  | Basic idea (One line)                              |
| ---- | -------------------------------------- | -------------------------------------------------- |
| 33   | Search in Rotated Sorted Array         | Modified Binary Search, T: O(log n), S: O(1)       |
| 46   | Permutations                           | Use Itertools or DFS, T: O(n!), S: O(n! \* n)      |
| 64   | Minimum Path Sum                       | Grid Reduction at square, T: O(m\*n), S: O(1)      |
| 78   | Subsets                                | Itertools, DFS, or Iterative, T&S: O(n \* 2^n)     |
| 80   | Remove Duplicates from Sorted Array II | Set first n valid values, T: O(n), S: O(1)         |
| 92   | Reverse Linked List II                 | Iterative in place updates, T: O(n), S: O(1)       |
| 116  | Populating Next Right Ptr in Each Node | Traverse each level with next, T: O(n), S: O(1)    |
| 120  | Triangle                               | Top Down or Bottom Up Min Row, T: O(n^2), S: O(1)  |
| 131  | Palindrome Partitioning                | DFS palindrome backtrack, T: O(n \* 2^n), S: O(n)  |
| 147  | Insertion Sort List                    | Dummy + Predecessor + Disorder, T: O(n^2), S: O(1) |
| 173  | Binary Search Tree Iterator            | Generator or Stack, T: O(1), S: O(h) per next call |
| 306  | Additive Number                        | Find all Pairs and test seq, T: O(n^2), S: O(n)    |
| 347  | Top K Frequent Elements                | Counter most common O(n log k) or bucket T&S: O(n) |
| 464  | Can I Win                              | Top Down DP, choices as tuple key, T&S: O(2^n)     |
| 676  | Implement Magic Dictionary             | Diff = 1 for List/dict, Candidates, T&S: O(n \* s) |
| 720  | Longest Word in Dictionary             | Sort + Set, T: O(n log n), S: O(n)                 |
| 787  | Cheapest Flights Within K Stops        | BFS with two dicts, T&S: O(n^k + n^2)              |
| 840  | Magic Squares In Grid                  | Brute Force or 5 and 43816729, T: O(m\*n), S: O(1) |
| 849  | Maximize Distance to Closest Person    | Count spaces using prev pointer, T: O(n), S: O(1)  |
| 955  | Delete Columns to Make Sorted II       | Track unsorted strs using set, T: O(n\*m), S: O(n) |
| 1024 | Video Stitching                        | Two pass defaultdict for furthest end, T&S: O(n)   |
| 1053 | Previous Permutation With One Swap     | Find first increasing and swap, T: O(n), S: O(1)   |
| 1109 | Corporate Flight Bookings              | Sweep Lines, optimise overlaps, T: O(b+n), S: O(n) |
| 1507 | Reformat Date                          | Dict for months + slice day, T&S: O(1)             |
| 1552 | Magnetic Force Between Two Balls       | Binary Search, T: O(n \* (log n + log m)), S: O(n) |
| 1664 | Ways to Make a Fair Array              | Two sum pairs for even and odd, T: O(n), S: O(1)   |
| 1727 | Largest Submatrix With Rearrangements  | Sum column stacks, T: O(n \* m log m), S: O(1)     |
| 1764 | Form Arr Concat Subarrs of Another Arr | All groups == slice of nums l->r, T: O(n), S: O(1) |
| 1802 | Max Value at a Given Ind in an Array   | Binary Search, sum arith seq, T: O(log s), S: O(1) |
| 1864 | Min Swaps for alternating Binary Str   | Count Wrong Positions, T: O(n), S: O(1)            |
| 1877 | Minimize Maximum Pair Sum in Array     | Sort, Min + Max, T: O(n log n), S: O(n)            |
| 1981 | Min Diff Between Target & Chosen Elems | Set DP + look around, T: O(t \* n^2), S: O(t)      |
