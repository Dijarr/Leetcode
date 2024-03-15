class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        var scounter = [Character: Int]()
   // Count characters in s
        for char in s {
            scounter[char, default: 0] += 1
        }
        
        // Subtract counts for characters in t
        for char in t {
            guard let count = scounter[char] else {
                return false  // Character not found in s
            }
            if count == 1 {
                scounter.removeValue(forKey: char)
            } else {
                scounter[char] = count - 1
            }
        }
        
        // If scounter is empty, all characters matched
        return scounter.isEmpty
    }
}