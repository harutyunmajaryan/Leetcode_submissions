class Solution(object):

  def wordPattern(self, pattern, s):
    """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
    word_list = []
    word = ""
    word_map = {}
    used_words = {}

    for char in s:
      if char == " ":
        if word:
          word_list.append(word)
          word = ""
      else:
        word += char
    if word:
      word_list.append(word)

    if len(pattern) != len(word_list):
      return False

    status = True
    for char, word in zip(pattern, list(word_list)):
      if char not in word_map:
        if word in used_words:
          status = False
          break
        word_map[char] = word
        used_words[word] = char
      elif word_map[char] == word:
        pass
      else:
        status = False
        break

    return status
        
