class Match:
    def __init__(self, rest):
        self.rest = rest if rest else Nothing()

    def match(self, text):
        return self._do_match(text) == ""

class Range(Match):
     def __init__(self, a, b, text):
         self.text = text
        self.a = a
        self.b = b
    def Range(a,b);
        if ord(a) <= ord(b):
            return character_list = [chr(x) for x in range(ord(a), ord(b) + 1)]
        else: 
            return Range(b,a)

        for i in character_list:
            if i in text:
                return i
        return None 
    

class Plus(Match):
     def __init__(self, rest=None):
        super().__init__(rest)

    def _do_match(self, text): 
        if text == "":
            return None 
        else:
         for i in range(len(text) + 1): 
            if self.rest._do_match(text[i:]) == "":
                return ""
class Charset(Match):
     def __init__(self, rest=None):
        super().__init__(rest)
         
        for i in (set):
             if i in text:
                 return i
        return None 
    

class Nothing(Match):
    def __init__(self, rest=None):
        self.rest = None

    def _do_match(self, text):
        return text

class Any(Match):
    def __init__(self, rest=None):
        super().__init__(rest)

    def _do_match(self, text):
        #we have len(text) + 1 so it can iterate one last time through the whole text 
        for i in range(len(text) + 1): 
            if self.rest._do_match(text[i:]) == "":
                return ""
        return None

class Either(Match):
    def __init__(self, left, right, rest=None):
        super().__init__(rest)
        self.patterns = [left, right]

    def _do_match(self, text):
        for pat in self.patterns:
            remainder = pat._do_match(text)
            if remainder is None:
                continue
            if self.rest._do_match(remainder) == "":
                return ""
        return None

class Lit(Match):
    def __init__(self, chars, rest=None):
        super().__init__(rest)
        self.chars = chars

    def _do_match(self, text):
        end = len(self.chars)
        if text[:end] == self.chars:
            return self.rest._do_match(text[end:])
        return None
