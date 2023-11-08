// task manager for myself to never use at all
// dont know how half of this code works because i just threw in a bunch of random stuff i tried learning day one of c 
// and also because i didnt fucking comment for shit lmao

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// structure to represent a task
struct Task {
    char description[100];
    int completed;
}; 

// function to add a task to the to-do list
void addTask(struct Task* tasks, int* taskCount, const char* description);

// function to mark a task as completed
void completeTask(struct Task* tasks, int taskCount, int index);

// function to display the to-do list
void displayTasks(struct Task* tasks, int taskCount);

void addTask(struct Task* tasks, int* taskCount, const char* description) {
    if (*taskCount < 100) {
        struct Task newTask;
        strcpy(newTask.description, description);
        newTask.completed = 0;
        tasks[(*taskCount)++] = newTask;
        printf("Task added: %s\n", description);
    } else {
        printf("To-do list is full. Cannot add more tasks.\n");
    }
}

void completeTask(struct Task* tasks, int taskCount, int index) {
    if (index >= 0 && index < taskCount) {
        tasks[index].completed = 1;
        printf("Task marked as completed: %s\n", tasks[index].description);
    } else {
        printf("Invalid task index. Please try again.\n");
    }
}

void displayTasks(struct Task* tasks, int taskCount) {
    if (taskCount == 0) {
        printf("To-do list is empty.\n");
    } else {
        printf("To-Do List:\n");
        for (int i = 0; i < taskCount; i++) {
            printf("%d. %s [%s]\n", i + 1, tasks[i].description, tasks[i].completed ? "Completed" : "Pending");
        }
    }
}

int main() {
    struct Task tasks[100];
    int taskCount = 0;
    int choice;

    do {
        printf("\nTo-Do List Application\n");
        printf("1. Add Task\n");
        printf("2. Mark Task as Completed\n");
        printf("3. Display Tasks\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter task description: ");
                char description[100];
                getchar(); // clear the newline character from the input buffer
                fgets(description, sizeof(description), stdin);
                addTask(tasks, &taskCount, description);
                break;
            case 2:
                printf("Enter the task number to mark as completed: ");
                int index;
                scanf("%d", &index);
                completeTask(tasks, taskCount, index - 1);
                break;
            case 3:
                displayTasks(tasks, taskCount);
                break;
            case 4:
                printf("Exiting the application. Goodbye!\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 4);

    return 0;
}
