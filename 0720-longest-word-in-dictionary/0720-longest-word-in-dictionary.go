func longestWord(words []string) string {
    sort.Strings(words)

    output := ""
    trie := &Trie{}
    for _, v := range words {
        if (*trie).Search(v[:len(v) - 1]) {
            (*trie).Insert(v)
            if len(v) > len(output) { output = v }
        }
    }
    return output
}


type Trie struct {
	Children    [26]*Trie
	IsEndOfWord bool
}


func (curr *Trie) Insert(word string) {
	for _, v := range word {
		index := int(v - 'a')
		if (*curr).Children[index] == nil {
			(*curr).Children[index] = &Trie{}
		}
		curr = curr.Children[index]
	}
	(*curr).IsEndOfWord = true
}

func (curr *Trie) Search(word string) bool {
    if len(word) == 0 { return true }
	for _, v := range word {
		index := int(v - 'a')
		if (*curr).Children[index] == nil {
			return false
		}
		curr = curr.Children[index]
	}
	return curr.IsEndOfWord
}