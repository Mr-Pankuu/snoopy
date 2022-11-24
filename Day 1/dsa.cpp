#include<stdio.h>
#include<conio.h>
int queue [5], f=1,r= -1;
void rear();
void front();
void show();
void exit();
int main()
{
    int ch;
    printf("1 REAR \n");
    printf("2 FRONT \n");
    printf("3 SHOW \n");
    printf("4 EXIT ");
    while(1)
    {
        printf("\n Enter choice:");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:rear();
                    break;
            case 2:front();
                break;
            case 3:show();
                break;
            case 4:exit();
                break;
            default:printf("Invalid option:");
        }

    }
    void rear()
    {  
        int item;
        if (r = 5-1)
        {
            printf("Queue is full");
        }
        else 
        {
            if (f==-1)
            {
                f=0;
            }
            printf("insert element is queue:")
            scanf("%d",&item);
            r= r+1;
            queue[r]=item;
        }
    }
    void front()
    {
        if(f==-1)
        {
            printf("Queue is empty:")
        }
        else 
        {
            printf("Deleted %d ",queue(f1));
            f=f+1;
        }
    }
    void show()
    {
        int i;
        if (f== -1)
        {
            printf("Queue is empty");
        }
        else
        {
            printf("Queue elements :");
            for (i = f; i<=r; i++)
            {
                printf("%d ",queue [i]);
            }
        }
    }
    return(0);
}
