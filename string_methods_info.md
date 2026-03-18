# 🔎 print(help(str))

Help on class str in module builtins:

**class str(object)**
|  str(object='') -> str
|  str(bytes_or_buffer[, encoding[, errors]]) -> str
|
|  Create a new string object from the given object. If encoding or
|  errors is specified, then the object must expose a data buffer
|  that will be decoded using the given encoding and error handler.
|  Otherwise, returns the result of object.__str__() (if defined)
|  or repr(object).
|  encoding defaults to sys.getdefaultencoding().
|  errors defaults to 'strict'.
|
|  Methods defined here:
|
|  **__add__(self, value, /)**
|      Return self+value.
|
|  **__contains__(self, key, /)**
|      Return bool(key in self).
|
|  **__eq__(self, value, /)**
|      Return self==value.
|        
|  **__format__(self, format_spec, /)**
|      Return a formatted version of the string as described by format_spec.
|        
|  **__ge__(self, value, /)**
|      Return self>=value.
|        
|  **__getitem__(self, key, /)**
|      Return self[key].
|        
|  **__getnewargs__(...)**
|        
|  **__gt__(self, value, /)**
|      Return self>value.
|        
|  **__hash__(self, /)**
|      Return hash(self).
|        
|  **__iter__(self, /)**
|      Implement iter(self).
|        
|  **__le__(self, value, /)**
|      Return self<=value.
|        
|  **__len__(self, /)**
|      Return len(self).
|        
|  **__lt__(self, value, /)**
|      Return self<value.
|        
|  **__mod__(self, value, /)**
|      Return self%value.
|        
|  **__mul__(self, value, /)**
|      Return self*value.
|        
|  **__ne__(self, value, /)**
|      Return self!=value.
|        
|  **__repr__(self, /)**
|      Return repr(self).
|        
|  **__rmod__(self, value, /)**
|      Return value%self.
|        
|  **__rmul__(self, value, /)**
|      Return value*self.
|        
|  **__sizeof__(self, /)**
|      Return the size of the string in memory, in bytes.
|        
|  **__str__(self, /)**
|      Return str(self).
|        
|  **capitalize(self, /)**
|      Return a capitalized version of the string.
|        
|      More specifically, make the first character have upper case and the rest lower
|      case.
|        
|  **casefold(self, /)**
|      Return a version of the string suitable for caseless comparisons.
|        
|  **center(self, width, fillchar=' ', /)**
|      Return a centered string of length width.
|        
|      Padding is done using the specified fill character (default is a space).
|        
|  **count(...)**
|      S.count(sub[, start[, end]]) -> int
|        
|      Return the number of non-overlapping occurrences of substring sub in
|      string S[start:end].  Optional arguments start and end are
|      interpreted as in slice notation.
|        
|  **encode(self, /, encoding='utf-8', errors='strict')**
|      Encode the string using the codec registered for encoding.
|        
|      encoding
|        The encoding in which to encode the string.
|      errors
|        The error handling scheme to use for encoding errors.
|        The default is 'strict' meaning that encoding errors raise a
|        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
|        'xmlcharrefreplace' as well as any other name registered with
|        codecs.register_error that can handle UnicodeEncodeErrors.
|        
|  **endswith(...)**
|      S.endswith(suffix[, start[, end]]) -> bool
|        
|      Return True if S ends with the specified suffix, False otherwise.
|      With optional start, test S beginning at that position.
|      With optional end, stop comparing S at that position.
|      suffix can also be a tuple of strings to try.
|        
|  **expandtabs(self, /, tabsize=8)**
|      Return a copy where all tab characters are expanded using spaces.
|        
|      If tabsize is not given, a tab size of 8 characters is assumed.
|        
|  **find(...)**
|      S.find(sub[, start[, end]]) -> int
|        
|      Return the lowest index in S where substring sub is found,
|      such that sub is contained within S[start:end].  Optional
|      arguments start and end are interpreted as in slice notation.
|        
|      Return -1 on failure.
|