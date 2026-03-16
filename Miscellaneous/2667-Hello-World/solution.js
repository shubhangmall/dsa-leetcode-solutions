/**
 * @return {Function}
 */
 
var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World";
    }
};

/**
 * time: O(1) — always returns the same string
 * space: O(1) — no extra space used
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */