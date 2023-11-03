/* this is going to be me redoing a tic tac toe game made in c a couple years back because idk what to do right now i just feel like coding something small and random */
/* leaving a bunch of notes around the place because younger me did not want to do that 
and i was doing this around the time im learning arrays and a few other stuff in c */
/* coming back to this after three years is crazy */

#include <stdio.h>
#include <stdlib.h> 
#include <string.h>
#include <time.h>

// function to display the board 
void displayBoard(char board[3][3]); 

// function to check if the game has ended with a tie or winner
int checkWinner(char board[3][3], char player);
int checkTie(char board[3][3]);
int gameEnd(char board[3][3], int* gameOver);

// function for the player's turn
void playerTurn(char board[3][3]);

// function for the computer's turn
void computerTurn(char board[3][3]);

// main function 
int main(void) {
    srand(time(NULL)); // seed the random number generator
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

        // display the board
        displayBoard(board);
        
        // check if game is over
        gameOver = gameEnd(board, &gameOver);


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

int checkWinner(char board[3][3], char player) {
    // check if there is a winner
    // starting with defining the winning combinations for bot and player 
    const int winningCombinations[8][3] = {
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8},  // rows
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},  // columns
        {0, 4, 8}, {2, 4, 6}              // diagonals
    };

    for (int i = 0; i < 8; i++) {
        int a = winningCombinations[i][0];
        int b = winningCombinations[i][1];
        int c = winningCombinations[i][2];
        if (board[a / 3][a % 3] == player && board[b / 3][b % 3] ==  player && board[c / 3][c % 3] == player) {
            return 1; // player has won
        }
    }
    return 0; // no winner yet
}

int checkTie(char board[3][3]) {
    // check if the board is full 
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == ' ') {
                return 0; // the board is not full yet
            }
        }
    }
    return 1; // the board is full
}

int gameEnd(char board[3][3], int* gameOver) {
    int playerWin = checkWinner(board, 'X');
    int computerWin = checkWinner(board, 'O');
    int tie = checkTie(board);
    
    // if statements to check if the game is over
    if (playerWin) {
        printf("You win!\n\n");
        *gameOver = 1;
    } else if (computerWin) {
        printf("You lose!\n\n");
        *gameOver = 1;
    } else if (tie) {
        printf("It's a tie!\n\n");
        *gameOver = 1;
    } else {
        printf("The game isn't over!\n\n");
    }
    return *gameOver; // return the updated value of gameOver
};

void playerTurn(char board[3][3]) {
    int move;
    int validMove = 0; // add a flag to check if the move is valid

    while (!validMove) { // use a loop to keep asking for input until a valid move is reached 
    // display the board 
    displayBoard(board);

        // ask the player for their move
        printf("\n\nEnter your move: ");
        scanf("%d", &move);
        
        int row = move / 3;
        int column = move % 3;
        
        if (move >= 0 && move < 9 && board[row][column] == ' ') {
            // check if the move is within the valid range and if the space is empty 
            validMove = 1; // set flag to indicate that the move is valid
            board[row][column] = 'X';
        } else {
            printf("Invalid move. Please pick an empty space. (0 - 8).\n");
        }
    }

};

void computerTurn(char board[3][3]) {
    int row, column;

    // generate a random number
    int random = rand() % 9;
    row = random / 3;
    column = random % 3;
    
    while (board[row][column] != ' ') {
        random = rand() % 9;
        row = random / 3;
        column = random % 3;
    }
    
    // place the computer's move on the board
    board[row][column] = 'O';
};