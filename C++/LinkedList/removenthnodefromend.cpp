#include<bits/stdc++.h>
using namespace std;

class node{
  public:
  	int data;// DATA MEMBERS (STORES DATA OF CURRENT NODE)
  	node* next;//DATA MEMBERS (STORES ADDRESS OF NEXT NODE HENCE POINTER)

  	node(int val){
  		data = val;
  		next =  NULL;
    }
  		listnode* removenthnodefromend(listnode* &head, int n){
	listnode* start;
	start -> next = head;
	listnode* fast = start;
	listnode* slow =head;

	for(int = 1; i<=n; ++i){
		fast = fast->next;
	  while(fast->next != NULL){
	  	fast=fast->next;
	  	slow=slow->next;
	  }
	  slow->next = slow->next->next;

	  return start->next;
	}
}
 
};
void insertAtTail(node* &head, int val){
	node* n = new node(val);

    if(head == NULL){
     head = n;
     return;
    }

	node* temp = head;
	while(temp->next != NULL){
		temp=temp->next;
	}
	temp->next=n; 
}

void display(node* head){
	node* temp = head;
	while(temp!= NULL){
		cout<<temp->data<<"->";
		temp = temp->next;
	}
	cout << "NULL"<<endl;
}


int main(){
 
 listnode* head = NULL;
 insertAtTail(head,1);
 insertAtTail(head,2);
 insertAtTail(head,3);
 insertAtTail(head,4);
 display(head);

  listnode* new = removenthnodefromend(head, 2);
 display(new);

 return 0;
}