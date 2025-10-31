#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <utility>

using namespace std;

int partition_basic(vector<int>& nums, int low, int high) {
    int pivot = nums[high];
    int i = low - 1; // [low..i] 是所有小于 pivot 的区域

    for (int j = low; j < high; ++j) {
        if (nums[j] <= pivot) {
            ++i;
            swap(nums[i], nums[j]);
        }
    }

    // 把 pivot 放到中间（i+1 位置）
    swap(nums[i + 1], nums[high]);
    return i + 1;
}

void quick_sort(vector<int>& nums, int low, int high) {
    if (low >= high) return;

    int part_index = partition_basic(nums, low, high);
    quick_sort(nums, low, part_index - 1);
    quick_sort(nums, part_index + 1, high);
}

void insertion_sort(vector<int>& nums, int low, int high) {
    for (int i = low + 1; i <= high; ++i) {
        int key = nums[i];
        int j = i - 1;
        while (j >= low && nums[j] > key) {
            nums[j + 1] = nums[j];
            j--;
        }
        nums[j + 1] = key;
    }
}

pair<int, int> partition_optimized(vector<int>& nums, int low, int high) {
    // 三数取中
    int mid = (low + high) / 2;
    if (nums[low] > nums[mid]) swap(nums[low], nums[mid]);
    if (nums[low] > nums[high]) swap(nums[low], nums[high]);
    if (nums[mid] > nums[high]) swap(nums[mid], nums[high]);
    int pivot = nums[mid];

    // 三路划分
    int lt = low, i = low, gt = high;
    while (i <= gt) {
        if (nums[i] < pivot) {
            swap(nums[lt], nums[i]);
            lt++;
            i++;
        } else if (nums[i] > pivot) {
            swap(nums[i], nums[gt]);
            gt--;
        } else {
            i++;
        }
    }
    return {lt, gt};
}

void quick_sort_optimized(vector<int>& nums, int low, int high, int threshold = 10) {
    if (high - low <= threshold) {
        insertion_sort(nums, low, high);
        return;
    }

    auto [lt, gt] = partition_optimized(nums, low, high);
    quick_sort_optimized(nums, low, lt - 1, threshold);
    quick_sort_optimized(nums, gt + 1, high, threshold);
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

    vector<int> nums_normal = nums;
    vector<int> nums_optimized = nums;

    auto start = chrono::high_resolution_clock::now();
    quick_sort(nums_normal, 0, n - 1);
    auto end = chrono::high_resolution_clock::now();
    double time_normal = chrono::duration<double>(end - start).count();

    start = chrono::high_resolution_clock::now();
    quick_sort_optimized(nums_optimized, 0, n - 1, 10);
    end = chrono::high_resolution_clock::now();
    double time_optimized = chrono::duration<double>(end - start).count();

    if (nums_normal != nums_optimized) {
        cerr << "❌ 排序结果不一致！" << endl;
        return 1;
    } else {
        cout << "✅ 排序结果一致！" << endl;
    }

    ofstream fout_normal("sorted.txt");
    for (int x : nums_normal) fout_normal << x << " ";
    fout_normal.close();

    cout << "Normal Quick Sort Time: " << time_normal << "s\n";
    cout << "Optimized Quick Sort Time: " << time_optimized << "s\n";
    cout << "Speedup: " << time_normal / time_optimized << "x\n";

    return 0;
}
