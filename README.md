# python_assignment

Base26 Root
Given a non-negative integer in it’s base 26 representation, output its digital root. The digital root is the single digit obtained by a iterative process of finding the sum of digits. In the next iteration, the sum of the digits in the previous iteration is computed, and the process repeated until a single digit value is obtained.

Table
Please find below the base 26 table below






Input Format
The first line of input consists of a decimal integer t denoting the number of test cases. Then t test cases follow. The first line of each test case consists of a decimal integer l denoting the number of digits in the base26 integer. Second line of each test case consists of a base26 integer n.

Output Format
For each test case, output the digital root.

Constraints
1 <= t <= 10000 (decimal)

0 <= l <= 10000 (decimal)

Sample Input
3
6
deaths
10
zzzzzzzzzz
1
a
Sample Output
b
z
a
Explanation
For deaths

d + e + a + t + h + s = bz

b + z = ba

b + a = b

Answer is b

For zzzzzzzzzz

z + z + z + z + z + z + z + z + z + z = jq

j + q = z

Answer is z

For a

Answer is a
