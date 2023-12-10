#include <bits/stdc++.h>
using namespace std;

struct Node {
  int value = INT_MIN;
  long long xor_both;
};

Node xor_list;

void add_to_end(int val){
  Node *prev_addr = nullptr, *curr_node = &xor_list;
  if (curr_node->value == INT_MIN){
    curr_node->value = val; // first run
    return;
  }
  while (curr_node->xor_both){
    long next_addr = (long) prev_addr ^ (long) curr_node->xor_both;
    prev_addr = curr_node; curr_node = (Node*) next_addr;
  }
  Node* new_tail = new Node{val};
  curr_node->xor_both = (long) prev_addr ^ (long) new_tail;
}

Node get(int index){
  Node *prev_addr = nullptr, *curr_node = &xor_list;
  for (int i=0; i<index; i++){
    long long next_addr = (long long) prev_addr ^ (long long) curr_node->xor_both;
    prev_addr = curr_node; curr_node = (Node*) next_addr;
  }
  return *curr_node;
}

int main(){
  add_to_end(5);
  add_to_end(6);
  add_to_end(7);
  add_to_end(8);
  cout << get(0).value << endl;
  cout << get(1).value << endl;
  cout << get(2).value << endl;
  cout << get(3).value << endl;
  add_to_end(9);
  add_to_end(10);
  cout << get(4).value << endl;
  cout << get(5).value << endl;
}
