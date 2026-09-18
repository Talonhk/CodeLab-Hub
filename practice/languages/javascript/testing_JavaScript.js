/* Testing for JavaScript

Write a function that checks if a given value is an instance of a given class or superclass. For this problem, an object is considered an instance of a given class if that object has access to that class's methods.

There are no constraints on the data types that can be passed to the function. For example, the value or the class could be undefined.
*/

/*Example 1:

Input: func = () => checkIfInstanceOf(new Date(), Date)
Output: true
Explanation: The object returned by the Date constructor is, by definition, an instance of Date.

Example 2:

Input: func = () => { class Animal {}; class Dog extends Animal {}; return checkIfInstanceOf(new Dog(), Animal); }
Output: true
Explanation:
class Animal {};
class Dog extends Animal {};
checkIfInstanceOf(new Dog(), Animal); // true

Dog is a subclass of Animal. Therefore, a Dog object is an instance of both Dog and Animal.

Example 3:

Input: func = () => checkIfInstanceOf(Date, Date)
Output: false
Explanation: A date constructor cannot logically be an instance of itself.

Example 4:

Input: func = () => checkIfInstanceOf(5, Number)
Output: true
Explanation: 5 is a Number. Note that the "instanceof" keyword would return false. However, it is still considered an instance of Number because it accesses the Number methods. For example "toFixed()".

Example 5:
Input func = () => checkIfInstanceOf(5n, Object)
Output: true
*/

function checkIfInstanceOf(obj, classFunction) {
  if (obj === null || obj === undefined || typeof classFunction !== "function") return false;

  // Handle primitives for their wrappers and Object
  const type = typeof obj;
  if (
    (type === "number" && (classFunction === Number || classFunction === Object)) ||
    (type === "string" && (classFunction === String || classFunction === Object)) ||
    (type === "boolean" && (classFunction === Boolean || classFunction === Object)) ||
    (type === "bigint" && (classFunction === BigInt || classFunction === Object)) ||
    (type === "symbol" && (classFunction === Symbol || classFunction === Object)) ||
    (type === "function" && classFunction === Object)
  ) return true;

  // Standard instanceof for everything else
  try {
    return obj instanceof classFunction;
  } catch {
    return false;
  }
}



/* Write code that enhances all arrays such that you can call the array.last() method on any array and it will return the last element. If there are no elements in the array, it should return -1.

You may assume the array is the output of JSON.parse.

 

Example 1:

Input: nums = [null, {}, 3]
Output: 3
Explanation: Calling nums.last() should return the last element: 3.

Example 2:

Input: nums = []
Output: -1
Explanation: Because there are no elements, return -1.

 

Constraints:

    arr is a valid JSON array
    0 <= arr.length <= 1000
*/


/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    return this.length === 0 ? -1 : this[this.length - 1];
    
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */