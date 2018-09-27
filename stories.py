import re
"""Madlibs Stories."""

class Story:
    """Madlibs story.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """     

    def __init__(self, words, text, title):
        """Create story with words and template text."""
        self.words = {word:self._humanize(word) for word in words}
        self.text = text
        self.title = title

    def _humanize(self,word):
        """The input is a word and output is a humanized version"""
        wordlist = word.split('_')
        wordlist = [word.capitalize() for word in wordlist]
        match = re.search(r"\d", word)
        if match:
            return 'Another ' + ' '.join(wordlist[:-1])
        return ' '.join(wordlist)

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.text

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

      


# Here's a story to get you started

