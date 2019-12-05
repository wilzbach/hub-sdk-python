# List of all builtins supported by the Storyscript engine
# Any changes here MUST be propagated to
# https://docs.storyscript.io/storyscript/functions/#built-ins
builtins = [
    {
        "name": "length",
        "input_type": "List[A]",
        "return_type": "int",
        "desc": "returns the length of the list",
    },
    {
        "name": "append",
        "input_type": "List[A]",
        "return_type": "List[A]",
        "desc": "returns a new list with `item` added to the end of it",
        "args": {"item": {"type": "A", "desc": "Item to be appended"}},
    },
    {
        "name": "prepend",
        "input_type": "List[A]",
        "return_type": "List[A]",
        "desc": "returns a new list with `item` added to the start of it",
        "args": {"item": {"type": "A", "desc": "Item to be appended"}},
    },
    {
        "name": "random",
        "input_type": "List[A]",
        "return_type": "A",
        "desc": "returns a random element from this list",
        "args": {},
    },
    {
        "name": "reverse",
        "input_type": "List[A]",
        "return_type": "List[A]",
        "desc": "returns a new list, in reverse order",
        "args": {},
    },
    {
        "name": "sort",
        "input_type": "List[A]",
        "return_type": "List[A]",
        "desc": "returns a new list, sorted in an ascending fashion",
        "args": {},
    },
    {
        "name": "min",
        "input_type": "List[A]",
        "return_type": "A",
        "desc": "returns the lowest of the items in this list (if it contains numbers)",
        "args": {},
    },
    {
        "name": "max",
        "input_type": "List[A]",
        "return_type": "A",
        "desc": "returns the largest of the items in this list (if it contains numbers)",
        "args": {},
    },
    {
        "name": "sum",
        "input_type": "List[A]",
        "return_type": "A",
        "desc": "returns the sum of all the items in this list (if it contains numbers)",
        "args": {},
    },
    {
        "name": "contains",
        "input_type": "List[A]",
        "return_type": "boolean",
        "desc": "returns true if `item` is present, false otherwise",
        "args": {"item": {"type": "A", "desc": "Item to find in the list"}},
    },
    {
        "name": "unique",
        "input_type": "List[A]",
        "return_type": "List[A]",
        "desc": "returns a new list, which will contain only unique items",
        "args": {},
    },
    {
        "name": "remove",
        "input_type": "List[A]",
        "return_type": "List[A]",
        "desc": "returns a new list, with `item` removed from the list",
        "args": {"item": {"type": "A", "desc": "Item to be removed"}},
    },
    {
        "name": "index",
        "input_type": "List[A]",
        "return_type": "int",
        "desc": "returns the index of an item or -1 if the list doesn't contain the item",
        "args": {"of": {"type": "A", "desc": "Item to find in the list",}},
    },
    {
        "name": "replace",
        "input_type": "List[A]",
        "return_type": "List[A]",
        "desc": "returns a new list, where all occurrences of `item` replaced with `by`",
        "args": {
            "item": {"type": "A", "desc": "Item to search for in the list"},
            "by": {
                "type": "A",
                "desc": "Item to replace occurrences in the list with",
            },
        },
    },
    {
        "name": "slice",
        "input_type": "List[A]",
        "return_type": "returns a new list, with items starting from the index `start` (inclusive)",
        "desc": "",
        "args": {
            "start": {"type": "int", "desc": "Starting index (inclusive)"}
        },
    },
    {
        "name": "slice",
        "input_type": "List[A]",
        "return_type": "List[A]",
        "desc": "returns a new list, with items starting from the index `start` (inclusive), to the index `end` (exclusive)",
        "args": {
            "start": {"type": "int", "desc": "Starting index (inclusive)",},
            "end": {"type": "int", "desc": "Ending index (exclusive)",},
        },
    },
    {
        "name": "slice",
        "input_type": "List[A]",
        "return_type": "List[A]",
        "desc": "returns a new list, with all items until the index `end` (exclusive)",
        "args": {"end": {"type": "int", "desc": "Ending index (exclusive)"}},
    },
    {
        "name": "join",
        "input_type": "List[A]",
        "return_type": "string",
        "desc": "returns a string with all elements in list concatenated (joined) by the separator `sep`",
        "args": {
            "sep": {
                "type": "string",
                "desc": "Separator to concatenate individual list elements with",
            }
        },
    },
    # map
    {
        "name": "length",
        "input_type": "Map[K,V]",
        "return_type": "int",
        "desc": "returns the number of elements in the map",
        "args": {},
    },
    {
        "name": "keys",
        "input_type": "Map[K,V]",
        "return_type": "List[K]",
        "desc": "returns a list of all keys",
        "args": {},
    },
    {
        "name": "values",
        "input_type": "Map[K,V]",
        "return_type": "List[V]",
        "desc": "returns a list of all values",
        "args": {},
    },
    {
        "name": "remove",
        "input_type": "Map[K,V]",
        "return_type": "Map[K,V]",
        "desc": "returns a map without `key` in it",
        "args": {"key": {"type": "K", "desc": "Key to be removed"}},
    },
    {
        "name": "flatten",
        "input_type": "Map[K,V]",
        "return_type": "List[List[any]]",
        "desc": "returns a list of key/value pairs",
        "args": {},
    },
    {
        "name": "contains",
        "input_type": "Map[K,V]",
        "return_type": "boolean",
        "desc": "returns true if `key` exists in the map, false otherwise",
        "args": {"key": {"type": "K", "desc": "Key to search the map for"}},
    },
    {
        "name": "contains",
        "input_type": "Map[K,V]",
        "return_type": "boolean",
        "desc": "returns true if the `value` exists in the map, false otherwise",
        "args": {
            "value": {"type": "V", "desc": "Value to search the map for"}
        },
    },
    {
        "name": "get",
        "input_type": "Map[K,V]",
        "return_type": "V",
        "desc": "returns the value for the `key`, or a `default` value if it doesn't exist",
        "args": {
            "key": {"type": "K", "desc": "Key of the item to be retrieved"},
            "default": {
                "type": "V",
                "desc": "Default value to be used if the `key` doesn't exist",
            },
        },
    },
    # string
    {
        "name": "length",
        "input_type": "string",
        "return_type": "int",
        "desc": "returns the number of UTF-8 characters",
        "args": {},
    },
    {
        "name": "replace",
        "input_type": "string",
        "return_type": "string",
        "desc": "returns a string by replacing `item` with `by`",
        "args": {
            "item": {
                "type": "string",
                "desc": "Substring to be searched for in the string",
            },
            "by": {
                "type": "string",
                "desc": "Replacement string for item occurrences",
            },
        },
    },
    {
        "name": "replace",
        "input_type": "string",
        "return_type": "string",
        "desc": "replace all occurrences of the `pattern` RegExp /ab/ with `by`",
        "args": {
            "pattern": {
                "type": "regexp",
                "desc": "Pattern to be searched for in the string",
            },
            "by": {
                "type": "string",
                "desc": "Replacement string for pattern occurrences",
            },
        },
    },
    {
        "name": "contains",
        "input_type": "string",
        "return_type": "boolean",
        "desc": "returns true if the string matches the `pattern`, false otherwise",
        "args": {
            "pattern": {
                "type": "regexp",
                "desc": "Pattern to be searched for in the string",
            }
        },
    },
    {
        "name": "contains",
        "input_type": "string",
        "return_type": "boolean",
        "desc": "returns true if the string contains the sequence `item`, false otherwise",
        "args": {
            "item": {
                "type": "string",
                "desc": "Substring to be searched for in the string",
            }
        },
    },
    {
        "name": "split",
        "input_type": "string",
        "return_type": "List[string]",
        "desc": "returns a list by splitting the string with the delimiter",
        "args": {
            "by": {"type": "string", "desc": "Delimiter to split the list by"}
        },
    },
    {
        "name": "uppercase",
        "input_type": "string",
        "return_type": "string",
        "desc": "returns a string where all characters are upper-cased",
        "args": {},
    },
    {
        "name": "lowercase",
        "input_type": "string",
        "return_type": "string",
        "desc": "returns a string where all characters are lower-cased",
        "args": {},
    },
    {
        "name": "capitalize",
        "input_type": "string",
        "return_type": "string",
        "desc": "returns a string where the first letter of each word is capitalized",
        "args": {},
    },
    {
        "name": "trim",
        "input_type": "string",
        "return_type": "string",
        "desc": "returns a string with any leading and trailing whitespace (including tabs) removed",
        "args": {},
    },
    {
        "name": "startswith",
        "input_type": "string",
        "return_type": "boolean",
        "desc": "returns true if the string starts with `prefix`",
        "args": {
            "prefix": {
                "type": "string",
                "desc": "Prefix to check the string for",
            }
        },
    },
    {
        "name": "endswith",
        "input_type": "string",
        "return_type": "boolean",
        "desc": "returns true if the string ends with the `suffix`",
        "args": {
            "suffix": {
                "type": "string",
                "desc": "Suffix to check the string for",
            }
        },
    },
    {
        "name": "substring",
        "input_type": "string",
        "return_type": "string",
        "desc": "returns characters after the specified index",
        "args": {
            "start": {"type": "int", "desc": "Starting index (inclusive)"}
        },
    },
    {
        "name": "substring",
        "input_type": "string",
        "return_type": "string",
        "desc": "returns characters after the start index and until the end index",
        "args": {
            "start": {"type": "int", "desc": "Starting index (inclusive)"},
            "end": {"type": "int", "desc": "Ending index (exclusive)"},
        },
    },
    {
        "name": "substring",
        "input_type": "string",
        "return_type": "string",
        "desc": "returns characters until the specified index",
        "args": {"end": {"type": "int", "desc": "Ending index (exclusive)"}},
    },
    # int
    {
        "name": "isOdd",
        "input_type": "int",
        "return_type": "boolean",
        "desc": "returns true if the number is odd, false otherwise",
        "args": {},
    },
    {
        "name": "isEven",
        "input_type": "int",
        "return_type": "boolean",
        "desc": "returns true if the number is even, false otherwise",
        "args": {},
    },
    {
        "name": "absolute",
        "input_type": "int",
        "return_type": "int",
        "desc": "returns the absolute value of the number",
        "args": {},
    },
    {
        "name": "increment",
        "input_type": "int",
        "return_type": "int",
        "desc": "returns the number + 1",
        "args": {},
    },
    {
        "name": "decrement",
        "input_type": "int",
        "return_type": "int",
        "desc": "returns the number - 1",
        "args": {},
    },
    # float
    {
        "name": "round",
        "input_type": "float",
        "return_type": "int",
        "desc": "returns the nearest integer to the given number",
        "args": {},
    },
    {
        "name": "ceil",
        "input_type": "float",
        "return_type": "int",
        "desc": "returns the smallest integer not less than x",
        "args": {},
    },
    {
        "name": "floor",
        "input_type": "float",
        "return_type": "int",
        "desc": "returns the largest integer not greater than x",
        "args": {},
    },
    {
        "name": "sin",
        "input_type": "float",
        "return_type": "float",
        "desc": "returns the sine of the number",
        "args": {},
    },
    {
        "name": "cos",
        "input_type": "float",
        "return_type": "float",
        "desc": "returns the cosine of the number",
        "args": {},
    },
    {
        "name": "tan",
        "input_type": "float",
        "return_type": "float",
        "desc": "returns the tangent of the number",
        "args": {},
    },
    {
        "name": "asin",
        "input_type": "float",
        "return_type": "float",
        "desc": "returns the arcsine of the number",
        "args": {},
    },
    {
        "name": "acos",
        "input_type": "float",
        "return_type": "float",
        "desc": "returns the arccosine of the number",
        "args": {},
    },
    {
        "name": "atan",
        "input_type": "float",
        "return_type": "float",
        "desc": "returns the arctangent of the number",
        "args": {},
    },
    {
        "name": "log",
        "input_type": "float",
        "return_type": "float",
        "desc": "returns the logarithmic of the number",
        "args": {},
    },
    {
        "name": "log2",
        "input_type": "float",
        "return_type": "float",
        "desc": "returns the base 2 logarithm of the number",
        "args": {},
    },
    {
        "name": "log10",
        "input_type": "float",
        "return_type": "float",
        "desc": "returns the base 10 logarithm of the number",
        "args": {},
    },
    {
        "name": "exp",
        "input_type": "float",
        "return_type": "float",
        "desc": "",
        "args": {},
    },
    {
        "name": "abs",
        "input_type": "float",
        "return_type": "float",
        "desc": "returns the absolute value of the number",
        "args": {},
    },
    {
        "name": "isNaN",
        "input_type": "float",
        "return_type": "boolean",
        "desc": "returns the absolute value of the number",
        "args": {},
    },
    {
        "name": "isInfinity",
        "input_type": "float",
        "return_type": "boolean",
        "desc": "returns true if the number represents infinity, false otherwise",
        "args": {},
    },
    {
        "name": "approxEqual",
        "input_type": "float",
        "return_type": "boolean",
        "desc": "returns true if the number is approximately equal to `value`",
        "args": {
            "value": {
                "type": "float",
                "desc": "Value to compare the number to",
            }
        },
    },
    {
        "name": "approxEqual",
        "input_type": "float",
        "return_type": "boolean",
        "desc": "returns true if the number is approximately equal to `value`, within a relative tolerance",
        "args": {
            "value": {
                "type": "float",
                "desc": "Value to compare the number to",
            },
            "maxRelDiff": {
                "type": "float",
                "desc": "Relative tolerance (abs(num - value) / value <= maxRelDiff)",
            },
        },
    },
    {
        "name": "approxEqual",
        "input_type": "float",
        "return_type": "boolean",
        "desc": "returns true if the number is approximately equal to `value`, within a absolute tolerance (abs(num - value) <= maxAbsDiff)",
        "args": {
            "value": {
                "type": "float",
                "desc": "Value to compare the number to",
            },
            "maxAbsDiff": {
                "type": "float",
                "desc": "Absolute tolerance (abs(num - value) <= maxAbsDiff)",
            },
        },
    },
    {
        "name": "approxEqual",
        "input_type": "float",
        "return_type": "boolean",
        "desc": "returns true if the number is approximately equal to `value` (within a relative and absolute threshold)",
        "args": {
            "value": {
                "type": "float",
                "desc": "Value to compare the number to",
            },
            "maxRelDiff": {
                "type": "float",
                "desc": "Relative tolerance (abs(num - value) / value <= maxRelDiff)",
            },
            "maxAbsDiff": {
                "type": "float",
                "desc": "Absolute tolerance (abs(num - value) <= maxAbsDiff)",
            },
        },
    },
    {
        "name": "sqrt",
        "input_type": "float",
        "return_type": "float",
        "desc": "returns the square root of the number",
        "args": {},
    },
]
