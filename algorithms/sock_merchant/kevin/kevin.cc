#include <cassert>
#include <unordered_set>
#include <vector>

int sockMerchant(int n, const std::vector<int> input) {
  std::unordered_set<int> socks;
  // NOTE(kevin): C++17 has std::size
  // but hackerrank is limited to C++14
  socks.reserve(input.size());

  int count = 0;
  for (const auto& element : input) {
    if (socks.count(element)) {
      count++;
      socks.erase(element);
    } else {
      socks.insert(element);
    }
  }
  return count;
}

int main() {
  auto input = std::vector<int>{10, 20, 20, 10, 10, 30, 50, 10, 20};
  auto n = 9;

  auto want = 3;
  auto got = sockMerchant(n, input);
  assert(want == got);
}
