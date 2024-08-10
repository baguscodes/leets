func removeDuplicates(nums []int) int {
    var sol []int 
    sol = append(sol,nums[0])
    for i := 1; i < len(nums); i++ {
		if nums[i] != sol[len(sol)-1] {
			sol = append(sol, nums[i])
		}
	}
copy(nums, sol)
fmt.Println("sol:", sol)
fmt.Println("Length of sol:", len(sol))
return len(sol)
}