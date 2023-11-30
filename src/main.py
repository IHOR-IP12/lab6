class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEndOfWord

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def build_trie(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie


patterns = ["the", "a", "there", "anaswe", "any", "by", "their"]
trie = build_trie(patterns)

#слова

print(trie.search("the"))
print(trie.search("these"))
print(trie.search("their"))
print(trie.search("thaw"))

#префікси

print(trie.startsWith("the"))
print(trie.startsWith("ther"))
print(trie.startsWith(""))
