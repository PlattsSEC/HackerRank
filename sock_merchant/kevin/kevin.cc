#include <iostream>
#include <map>

int main() {

  int length = 0;

  std::map<int, int> socks;
  std::cin >> length;

  int pair_count = 0;
  int sock_integer;
  for (int i = 0; i < length; i++) {
    std::cin >> sock_integer;
    if (socks.count(sock_integer) != 0) {
      pair_count++;
      socks.erase(sock_integer);
    } else {
      socks[sock_integer] = 1;
    }
  }

  std::cout << pair_count << std::endl;
  return 0;
}
