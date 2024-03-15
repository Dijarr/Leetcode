class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var anagrams = [String: [String]]()
        for word in strs{
            let key = String(word.sorted())
            if var group = anagrams[key]{
                group.append(word)
                anagrams[key] = group
            }else {
                anagrams[key] = [word]
            }
        }
        return Array(anagrams.values) 
    }
}
