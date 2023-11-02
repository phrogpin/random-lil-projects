/* this is going ot be a tic tac toe game made in c because idk what to do right now i just feel like coding something small and random */
/* leaving a bunch of notes around the place because i am doing this around the time im learning arrays and a few other stuff in c */

#include <stdio.h>
#include <stdlib.h> 
#include <string.h>
#include <time.h>

// function to display the board 
void displayBoard(char board[3][3]); 

// function to check if the game has ended 
void gameEnd(char board[3][3], int gameOver);

// function for the player's turn
void playerTurn(char board[3][3]);

// function for the computer's turn
void computerTurn(char board[3][3]);

// main function 
int main(void) {
    // how to play
    printf("Welcome to Tic Tac Toe!\n");
    printf("To play, enter the number of the square you want to place your piece in.\n");
    printf("The board is numbered like this:\n");
    printf(" 0 | 1 | 2 \n");
    printf("-----------\n");
    printf(" 3 | 4 | 5 \n");
    printf("-----------\n");
    printf(" 6 | 7 | 8 \n");
    printf("You are X and the computer is O.\n");
    printf("Good luck!\n\n");

    // initialize the game over variable
    int gameOver = 0;

    // initialize the board 
    char board[3][3] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    /* 
    reminder that the first bracket is the row and the second is the column (making a 2d array)
    also this declaration sets it so that there are three rows and three columns.
    each column is given an empty ' ' to start out the game 
    */

    // game loop
    while (gameOver == 0) {
        // player turn
        playerTurn(board);

        // computer turn
        computerTurn(board);
        
        // check if game is over
        gameEnd(board, gameOver);

        // display the board
        displayBoard(board);

    }
    return 0;
}

void displayBoard(char board[3][3]) {
    printf(" %c | %c | %c \n", board[0][0], board[0][1], board[0][2]);
    printf("-----------\n");
    printf(" %c | %c | %c \n", board[1][0], board[1][1], board[1][2]);
    printf("-----------\n");
    printf(" %c | %c | %c \n", board[2][0], board[2][1], board[2][2]);
};

void gameEnd(char board[3][3], int gameOver) {
    // check if the board is full
    if (board[0][0] != ' ' && board[0][1] != ' ' && board[0][2] != ' ' && board[1][0] != ' ' && board[1][1] != ' ' && board[1][2] != ' ' && board[2][0] != ' ' && board[2][1] != ' ' && board[2][2] != ' ') {
        printf("The board is full!");
    }
    
    // check if there is a winner
    if (board[0][0] == 'X' && board[0][1] == 'X' && board[0][2] == 'X') {
        printf("You win!\n");
    } else if (board[1][0] == 'X' && board[1][1] == 'X' && board[1][2] == 'X') {
        printf("You win!\n");
    } else if (board[2][0] == 'X' && board[2][1] == 'X' && board[2][2] == 'X') {
        printf("You win!\n");
    } else if (board[0][0] == 'X' && board[1][0] == 'X' && board[2][0] == 'X') {
        printf("You win!\n");
    } else if (board[0][1] == 'X' && board[1][1] == 'X' && board[2][1] == 'X') {
        printf("You win!\n");
    } else if (board[0][2] == 'X' && board[1][2] == 'X' && board[2][2] == 'X') {
        printf("You win!\n");
    } else if (board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X') {
        printf("You win!\n");
    } else if (board[0][2] == 'X' && board[1][1] == 'X' && board[2][0] == 'X') {
        printf("You win!\n");
    } else if (board[0][0] == 'O' && board[0][1] == 'O' && board[0][2] == 'O') {
        printf("You lose!\n");
    } else if (board[1][0] == 'O' && board[1][1] == 'O' && board[1][2] == 'O') {
        printf("You lose!\n");
    } else if (board[2][0] == 'O' && board[2][1] == 'O' && board[2][2] == 'O') {
        printf("You lose!\n");
    } else if (board[0][0] == 'O' && board[1][0] == 'O' && board[2][0] == 'O') {
        printf("You lose!\n");
    } else if (board[0][1] == 'O' && board[1][1] == 'O' && board[2][1] == 'O') {
        printf("You lose!\n");
    } else if (board[0][2] == 'O' && board[1][2] == 'O' && board[2][2] == 'O') {
        printf("You lose!\n");
    } else if (board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O') {
        printf("You lose!\n");
    } else if (board[0][2] == 'O' && board[1][1] == 'O' && board[2][0] == 'O') {
        printf("You lose!\n");
    } else {
        printf("The game isn't over!\n");
    }

    // check if there is a tie
    if (board[0][0] != ' ' && board[0][1] != ' ' && board[0][2] != ' ' && board[1][0] != ' ' && board[1][1] != ' ' && board[1][2] != ' ' && board[2][0] != ' ' && board[2][1] != ' ' && board[2][2] != ' ') {
        printf("It's a tie!\n");
        gameOver = 1;
    }

};

void playerTurn(char board[3][3]) {
    int move;
    
    // ask the player for their move
    printf("\n\nEnter your move: ");
    scanf("%d", &move);
    

    int row = move / 3;
    int column = move % 3;
    
    // check if the move is valid
    // if player requested spot is empty, place move on the board using switch statement
    if (board[row][column] == ' ') {
        switch (move) {
            case 0:
                board[0][0] = 'X';
                break;
        
            case 1:
                board[0][1] = 'X';
                break;
        
            case 2: 
                board[0][2] = 'X';
                break;

            case 3:
                board[1][0] = 'X';
                break;
            
            case 4:
                board[1][1] = 'X';
                break; 
            
            case 5:
                board[1][2] = 'X';
                break;

            case 6:
                board[2][0] = 'X';
                break;

            case 7:
                board[2][1] = 'X';
                break;

            case 8: 
                board[2][2] = 'X';
                break;

            default:
                printf("Invalid move. Try again.\n");
                break;
        }
    } else {
        printf("Invalid move. Try again.\n");
    }

};

// finish this please 

void computerTurn(char board[3][3]) {
    srand(time(NULL));
    int random, row, column;

    // generate a random number
    random = rand() % 9;
    row = random / 3;
    column = random % 3;

    // check if the spot is empty
    if (board[row][column] == ' ') {
        // place the move on the board
        switch (random) {
            case 0:
                board[0][0] = 'O';
                break;
                
            case 1:
                board[0][1] = 'O';
                break;
                
            case 2:
                board[0][2] = 'O';
                break;

            case 3:
                board[1][0] = 'O';
                break;

            case 4:
                board[1][1] = 'O';
                break;

            case 5:
                board[1][2] = 'O';
                break;

            case 6:
                board[2][0] = 'O';
                break;

            case 7:
                board[2][1] = 'O';
                break;

            case 8:
                board[2][2] = 'O';
                break;

            default:
                printf("Invalid move. Try again.\n");
                break;
        }
    } else {
        // generate a new random number
        random = rand() % 9;
    }
};