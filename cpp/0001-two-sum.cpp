class Solution {
    /*
     Key Takeaways
     -------------
     *  Nested loop brute force

     Complexity Analysis
     -------------------
     Time Complexity: O(n^2)
        *   nested loop: O(n^2)

     Space Complexity: O(1)
        *   no extra space required
    */
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};

class Solution {
    /*
     Key Takeaways
     -------------
     *  Map to keep track of visited nums
     *  Duplicate values in map does not matter because the
        algorithm will return before modification is necessary
     *  At each iteration, we can find the exact num to look for
        by taking (target - current)
     *  Check the map for the difference
     *  Map.find() - Map.end(): O(1) time complexity

     Complexity Analysis
     -------------------
     Time Complexity: O(n)
        *   one pass: O(n)
        *   map.find() - map.end(): O(1)

     Space Complexity: O(n)
        *   map: O(n)
    */
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> found;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int diff = target - nums[i];
            if (found.find(diff) != found.end()) {
                return {found[diff], i};
            }
            found[nums[i]] = i;
        }
        return {};
    }
};

class Solution {
    /*
     Key Takeaways
     -------------
     *  Sort nums
     *  Make a map of the original indices before sort
     *  2 pointers
        *   decrement right when sum > target
        *   increment left when sum < target
        *   if sum == target, return vector of indices
     *  Check if nums[l] == nums[r] to ensure correct
        indices are returned

     Complexity Analysis
     -------------------
     Time Complexity: O(nlogn)
        *   create map of original indices: O(n)
        *   sort: O(nlogn)
        *   two pointers: O(n)

     Space Complexity: O(n)
        *   map of original indices: O(n)
    */
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        int n = nums.size();
        unordered_map<int, vector<int>> originalIdx;
        for (int i = 0; i < n; i++) {
            if (originalIdx.find(nums[i]) != originalIdx.end())
                originalIdx[nums[i]].push_back(i);
            else
                originalIdx[nums[i]] = {i};
        }
        sort(nums.begin(), nums.end());

        int r = nums.size() - 1;
        int l = 0;
        while (l < r) {
            int lrSum = nums[l] + nums[r];
            if (lrSum > target)
                r--;
            else if (lrSum < target)
                l++;
            else {
                if (nums[l] == nums[r]) {
                    return {originalIdx[nums[l]][0], originalIdx[nums[r]][1]};
                }
                return {originalIdx[nums[l]][0], originalIdx[nums[r]][0]};
            }
        }
        return {};
    }
};
