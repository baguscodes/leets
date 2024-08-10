func searchInsert(nums []int, target int) int {
    var pos int
    for i:= range nums{
        if nums[i]==target{
            pos=i
        }
        if target>nums[i]{
            pos=i+1
        }
    }
    return pos
}