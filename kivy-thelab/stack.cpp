#include<stdio.h>
#include<conio.h>
#define max 5
int stack[max],top= -1;
int no,item,del_item,i;
int push(int insert_item);
int pop();
int main()
{
    int x,y;
    char ch='y';
    
    do
    {
    printf("Menus:-\n");
    printf("1.push on stack\n2.pop from stack\n3.Display\n");
    printf("\nEnter a choice:-");
    scanf("%d",&no);
	switch(no)
	{
	case 1:
		printf("Enter the item:");
		scanf("%d",&item);
		x=push(item);
		printf("%d Item is inserted",x);
		break;
	case 2:
	    y=pop();
	    printf("%d Item is deleted",y);
	    break;
	case 3:
	    printf("Display the items of stack:-");
	    for(i=top;i>=0;i--)
	    {
			printf("\n___");
			printf("\n|%d|",stack[i]);

	    }
	    printf("\n___");
	    break;

	}
	    printf("\nDo you want to continue then press 'y' otherwise 'n'");
	    fflush(stdin);
	    scanf("%c",&ch);
	}
        while(ch!='n');
	
}
int push(int insert_item)
{
     if(top == (max-1))
    {
		printf("Stack Overflow\n");
		return 0;
    }
     else
    {
	    top=top+1;
	    stack[top]=insert_item;
        return stack[top];
    }
}
int pop()
{
    if(top== -1)
    {
	    printf("Stack Underflow\n");
        return 0;
    }
    else
    {
        del_item=stack[top];
        top=top-1;
        return del_item;
    }
}
