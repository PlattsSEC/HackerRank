/*****************
 * Kevin Boyette *
 ****************/
#include <iostream>
#include <string>
#include <algorithm>
#include <locale>
#include <map>

std::string to_upper(std::string);

int main(void)
{
    std::string word, key;
    unsigned short inputs = 0;

    // Get word
    std::cout << "Enter a word: ";
    std::cin >> word;
    word = to_upper(word);

    // Get key
    std::cout << "Enter the key: ";
    std::cin >> key;
    key = to_upper(key);

    // Remove duplicate letters from key
    std::string letters = "";
    for (char& c : key) {
        size_t found = letters.find(c);
        if (found == std::string::npos) {
            letters = letters + c;
        }
    }

    std::string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    // Remove characters from alphabet
    for (size_t i = 0; i < letters.length(); ++i) {
        size_t location = alphabet.find(letters[i]);
        alphabet.erase(alphabet.begin() + location);
    }

    // Grab columns and put into a map
    std::map<char, std::string> jk;
    for (size_t i = 0; i < letters.length(); ++i) {
        std::string alpha_columns;
        alpha_columns.push_back(letters[i]);
        for (int j = i; j < alphabet.length(); j += letters.length()) {
            alpha_columns.push_back(alphabet[j]);
        }
        jk[letters[i]] = alpha_columns;
    }

    std::sort(letters.begin(), letters.end());

    // Generate a new key
    std::string new_key;
    for (auto c : letters) {
        new_key.append(jk.find(c)->second);
    }

    // Prepare and print out encrypted text
    std::string return_text;
    std::string new_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (char c : word) {
        if (c == ' ') {
            return_text.push_back(c);
            continue;
        }
        size_t position = new_key.find(c);
        return_text.push_back(new_alphabet[position]);
    }
    std::cout << return_text << std::endl;
}

std::string to_upper(std::string input)
{
    std::locale local;
    std::string new_string;
    for (size_t i = 0; i < input.length(); ++i) {
        new_string += std::toupper(input[i], local);
    }

    std::cout << new_string << std::endl;
    return new_string;
}
