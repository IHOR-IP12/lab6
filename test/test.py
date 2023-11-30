from src.main import build_trie
from src.main import Trie


def run_tests():
    patterns = ["the", "a", "there", "anaswe", "any", "by", "their"]
    trie = build_trie(patterns)

    assert trie.search("the")
    assert not trie.search("these")
    assert trie.search("their")
    assert not trie.search("thaw")

    assert trie.startsWith("the")
    assert trie.startsWith("ther")
    assert not trie.startsWith("xyz")

    empty_trie = Trie()
    assert not empty_trie.search("word")
    assert not empty_trie.startsWith("prefix")

    empty_trie.insert("word")
    assert empty_trie.search("word")
    assert not empty_trie.startsWith("prefix")

    print("Всі тести пройдено успішно!")


run_tests()

