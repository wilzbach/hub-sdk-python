# List of all builtins supported by the Storyscript engine
# Any changes here MUST be propagated to https://docs.storyscript.io/storyscript/functions/#built-ins
builtins = """
List[A] length -> int
List[A] append item:A -> List[A]
List[A] prepend item:A -> List[A]
List[A] random -> A
List[A] reverse -> List[A]
List[A] sort -> List[A]
List[A] min -> A
List[A] max -> A
List[A] sum -> A
List[A] contains item:A -> boolean
List[A] unique -> List[A]
List[A] remove item:A -> List[A]
List[A] index of:A -> int
List[A] replace item:A by:A -> List[A]
List[A] slice start:int -> List[A]
List[A] slice start:int end:int -> List[A]
List[A] slice end:int -> List[A]

Map[K,V] length -> int
Map[K,V] keys -> List[K]
Map[K,V] values -> List[V]
Map[K,V] remove key:K -> Map[K,V]
Map[K,V] flatten -> List[List[any]]
Map[K,V] contains key:K -> boolean
Map[K,V] contains value:V -> boolean
Map[K,V] get key:K default:V -> V

string length -> int
string replace item:string by:string -> string
string replace pattern:regexp by:string -> string
string contains pattern:regexp -> boolean
string contains item:string -> boolean
string split by:string -> List[string]
string uppercase -> string
string lowercase -> string
string capitalize -> string
string trim -> string
string startswith prefix:string -> boolean
string endswith suffix:string -> boolean
string substring start:int -> string
string substring start:int end:int -> string
string substring end:int -> string

int isOdd -> boolean
int isEven -> boolean
int absolute -> int
int increment -> int
int decrement -> int

float round -> int
float ceil -> int
float floor -> int
float sin -> float
float cos -> float
float tan -> float
float asin -> float
float acos -> float
float atan -> float
float log -> float
float log2 -> float
float log10 -> float
float exp -> float
float abs -> float
float isNaN -> boolean
float isInfinity -> boolean
float approxEqual value: float -> boolean
float approxEqual value: float maxRelDiff: float -> boolean
float approxEqual value: float maxAbsDiff: float -> boolean
float approxEqual value: float maxRelDiff: float maxAbsDiff: float -> boolean
float sqrt -> float
"""
