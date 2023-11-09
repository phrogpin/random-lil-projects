/**
 * this function takes two integers as input and returns their sum.
 *
 * @param a the first integer.
 * @param b the second integer.
 */
int add(int a, int b) {
    // add the two integers and return the result.
    return a + b;
}

/**
 * this function takes an integer array and its length as input and returns the sum of its elements.
 *
 * @param arr the integer array.
 * @param len the length of the array.
 */
int sum(int arr[], int len) {
    int result = 0;
    // loop through the array and add each element to the result.
    for (int i = 0; i < len; i++) {
        result += arr[i];
    }
    return result;
}
#include <stdio.h>
#include <stdlib.h>
// this header file provides functions for manipulating strings.
#include <string.h>

// this program is a simple implementation of the game Hangman.
#include <string.h>
#include <time.h>

#define MAX_WORDS 10
#define MAX_WORD_LENGTH 20
#define MAX_GUESSES 6

// this is an array of strings.
char words[MAX_WORDS][MAX_WORD_LENGTH] = {
    "apple",
    "banana",
    "cherry",
    "orange",
    "grape",
    "watermelon",
    "pineapple",
    "kiwi",
    "mango",
    "pear"
};

// this function takes a string as input and returns its length.
int main() {
    srand(time(NULL));
    // generate a random number between 0 and MAX_WORDS - 1.
    int word_index = rand() % MAX_WORDS;
    char word[MAX_WORD_LENGTH];
    strcpy(word, words[word_index]);
    int word_length = strlen(word);
    char guessed_word[MAX_WORD_LENGTH];
    // initialize guessed_word to all underscores.
    for (int i = 0; i < word_length; i++) {
        guessed_word[i] = '_';
    }
    guessed_word[word_length] = '\0';
    int remaining_guesses = MAX_GUESSES;
    char guess;
    // loop until the user runs out of guesses or guesses the word.
    while (remaining_guesses > 0 && strcmp(word, guessed_word) != 0) {
        printf("Guess a letter: ");
        scanf(" %c", &guess);
        int found = 0;
        for (int i = 0; i < word_length; i++) {
            if (word[i] == guess) {
                guessed_word[i] = guess;
                found = 1;
            }
        }
        if (!found) { // if the guess was incorrect.
            remaining_guesses--;
            printf("Incorrect guess. %d guesses remaining.\n", remaining_guesses);
        }
        printf("%s\n", guessed_word);
    }
    if (strcmp(word, guessed_word) == 0) { // if the user guessed the word.
        printf("Congratulations! You guessed the word.\n");
    } else { // if the user ran out of guesses.
        printf("Sorry, you ran out of guesses. The word was %s.\n", word);
    }
    return 0;
}
