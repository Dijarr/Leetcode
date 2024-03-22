class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    var seen = [Int: Int]()
    for (index, value) in nums.enumerated() {
        let difference = target - value 
        if let diffIndex = seen[difference] {
            return [index, diffIndex]
        }
        seen[value] = index
    }
    return [] 
}
  
} 