#include <cmath>
#include <cstdio>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main() {
  int testCases;
  cin >> testCases;
  for(int i = 0; i < testCases; ++i){
    int testCases;
    string word;
    string cypherWord;
    string encryptedText;
    string text;
    map<char,string> columns;
    string key;
    string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";


    cin >> word;
    cin.ignore();
    getline(cin, encryptedText);

    //cout << encryptedText.length() << endl;
    for(int n = 0; n < word.length(); ++n){
      if(cypherWord.find(word[n]) == string::npos){
	cypherWord.push_back(word[n]);
	            
      }
              
    }

    for(int n = 0; n < cypherWord.length(); ++n){
      size_t position = alphabet.find(cypherWord[n]);
      alphabet.erase(alphabet.begin()+position);
              
    }

    for(int n = 0; n < cypherWord.length(); ++n){
      string columnString;
      columnString.push_back(cypherWord[n]);
      for(int d = n; d < alphabet.length(); d = d + cypherWord.length()){
	columnString.push_back(alphabet[d]);
	            
      }
      columns[cypherWord[n]] = columnString;
              
    }
    sort(cypherWord.begin(), cypherWord.end());

    for(int n = 0; n < cypherWord.length(); ++n){
      key.append(columns.find(cypherWord[n])->second);
              
    }

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    for(int n = 0; n < encryptedText.length(); ++n){
      if(encryptedText[n] == ' '){
	text.push_back(' ');
	continue;
	                
      }
      size_t pos = key.find(encryptedText[n]);
      text.push_back(alphabet[pos]);
              
    }
    cout << text << endl;

        
  }


  return 0;
  
}
