// wordcnt.c -- count characters, words and lines.
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#define STOP '|'
int main(void)
{
	char c;                     // read in character
	char prev;                  // character read before c
	long n_chars = 0L;          // number of characters
	int n_lines = 0;            // number of lines
	int n_words = 0;            // number of words
	int p_lines = 0;            // number of incomplete lines
	bool inword = false;        // if c is in a word, then inword is set true
	
	printf("Enter text to be analyzed(| to terminate): \n");
}
