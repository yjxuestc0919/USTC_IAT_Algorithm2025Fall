#include <algorithm>
#include <chrono>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <future>
using namespace std;

inline void swap_int(int& a, int& b) {
    int tmp = a;
    a = b;
    b = tmp;
}

int partition_base(vector<int>& nums, int left, int right) {
    int pivot = nums[left];
    int i = left+1, j = right;
    while (true) {
        while (i <= j && nums[j] > pivot) j--;
        while (i <= j && nums[i] < pivot) i++;
        if (i >= j) break;
        swap_int(nums[i], nums[j]);
        j -= 1;
        i += 1;
    }
    swap_int(nums[j], nums[left]);
    return j;
}

int random_partition(vector<int>& nums, int left, int right) {
    int pivot_index = rand() % (right - left + 1) + left;
    swap_int(nums[left], nums[pivot_index]);
    int pivot = nums[left];
    int i = left+1, j = right;
    while (true) {
        while (i <= j && nums[j] > pivot) j--;
        while (i <= j && nums[i] < pivot) i++;
        if (i >= j) break;
        swap_int(nums[i], nums[j]);
        j -= 1;
        i += 1;
    }
    swap_int(nums[j], nums[left]);
    return j;
}

int medium_num(int s, int m, int l) {
    if ((s <= m && m <= l) || (l <= m && m <= s)) return m;
    else if ((m <= s && s <= l) || (l <= s && s <= m)) return s;
    else return l;
}

int median_of_three_partition(vector<int>& nums, int left, int right) {
    int mid = left + (right - left) / 2;
    int medium_value = medium_num(nums[left], nums[mid], nums[right]);

    int pivot_index;
    if (medium_value == nums[mid]) pivot_index = mid;
    else if (medium_value == nums[right]) pivot_index = right;
    else pivot_index = left;

    swap_int(nums[left], nums[pivot_index]);
    int pivot = nums[left];

    int i = left+1, j = right;
    while (true) {
        while (i <= j && nums[j] > pivot) j--;
        while (i <= j && nums[i] < pivot) i++;
        if (i >= j) break;
        swap_int(nums[i], nums[j]);
        j -= 1;
        i += 1;
    }
    swap_int(nums[j], nums[left]);
    return j;
}

void insert_sort(vector<int>& nums) {
    for (int i = 1; i < nums.size(); i++) {
        int cur = nums[i];
        int j = i - 1;
        while (j >= 0 && nums[j] > cur) {
            nums[j + 1] = nums[j];
            j--;
        }
        nums[j + 1] = cur;
    }
}

void quick_sort(vector<int>& nums, int left, int right,
                string optimize = "random_pivot",
                bool use_insert_sort = false,
                int k = 16) 
{
    if (use_insert_sort && right - left <= k) return;
    if (left >= right) return;

    int index;
    if (optimize == "random_pivot") index = random_partition(nums, left, right);
    else if (optimize == "median_of_three") index = median_of_three_partition(nums, left, right);
    else index = partition_base(nums, left, right);

    quick_sort(nums, left, index - 1, optimize, use_insert_sort, k);
    quick_sort(nums, index + 1, right, optimize, use_insert_sort, k);

    if (use_insert_sort && left == 0 && right == nums.size() - 1) {
        insert_sort(nums);
    }
}

// 并行快速排序
void quick_sort_parallel(vector<int>& nums, int left, int right,
                         const string& optimize = "random_pivot",
                         bool use_insert_sort = false,
                         int k = 16,
                         int parallel_threshold = 50000)
{
    if (use_insert_sort && right - left <= k) return;
    if (left >= right) return;

    int index;
    if (optimize == "random_pivot") index = random_partition(nums, left, right);
    else if (optimize == "median_of_three") index = median_of_three_partition(nums, left, right);
    else index = partition_base(nums, left, right);

    // 子区间大小
    int left_size = index - 1 - left;
    int right_size = right - (index + 1);

    // 判断是否并行
    if (left_size > parallel_threshold || right_size > parallel_threshold) {
        auto fut = std::async(std::launch::async, [&]() {
            quick_sort_parallel(nums, left, index - 1, optimize, use_insert_sort, k, parallel_threshold);
        });
        quick_sort_parallel(nums, index + 1, right, optimize, use_insert_sort, k, parallel_threshold);
        fut.wait();
    } else {
        quick_sort_parallel(nums, left, index - 1, optimize, use_insert_sort, k, parallel_threshold);
        quick_sort_parallel(nums, index + 1, right, optimize, use_insert_sort, k, parallel_threshold);
    }

    if (use_insert_sort && left == 0 && right == nums.size() - 1) {
        insert_sort(nums);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ifstream fin("data.txt");
    int n;
    fin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) fin >> nums[i];
    fin.close();

    vector<int> quick_sorted = nums;
    vector<int> std_sorted = nums;

    auto start = chrono::steady_clock::now();
    if (!quick_sorted.empty()) {
        quick_sort_parallel(quick_sorted, 0, static_cast<int>(quick_sorted.size()) - 1,
                   "median_of_three", true, 70, 50000);
    }
    auto end = chrono::steady_clock::now();
    double time_quick = chrono::duration<double>(end - start).count();

    start = chrono::steady_clock::now();
    sort(std_sorted.begin(), std_sorted.end());
    end = chrono::steady_clock::now();
    double time_std = chrono::duration<double>(end - start).count();

    if (quick_sorted != std_sorted) {
        cerr << "❌ 排序结果不一致！" << endl;
        return 1;
    }

    ofstream fout_normal("sorted.txt");
    for (int x : quick_sorted) fout_normal << x << " ";
    fout_normal.close();

    cout << "✅ 排序结果一致！" << '\n';
    cout << "Quick Sort Time: " << time_quick << "s\n";
    cout << "std::sort Time: " << time_std << "s\n";
    cout << "Speedup (std::sort / Quick): " << time_std / time_quick << "x\n";

    return 0;
}
