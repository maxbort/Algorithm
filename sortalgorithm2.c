/* ID: 2018115736		>>> REPLACE WITH YOUR ID
 * NAME: Choi Hyo Jun	>>> REPLACE WITH YOUR NAME
 * OS: linux, Ubuntu 16.04
 * Compiler version: gcc 5.4.0 20160609
 */

// >>> (10/100) pts
// >>> IN THE TOP 4-LINES COMMENTS
// >>> LINE 1: REPLACE WITH YOUR ID (IF YOU HAVE NON-NUMERIC, IGNORE IT)
// >>> Line 2: REPLACE WITH YOUR NAME (NO HANGUL)
// >>> DO NOT CHANGE OS AND Compiler
// >>> COMPILE AND RUN YOUR CODE ON THE LINUX MACHINE

// HOMEWORK PROGRAMMING ASSIGNMENT 2-2
// WORDS ARE STORED IN VERY LARGE CONTAINER
// TO INTENTIONALLY MAKE COMPUTATION TIME MUCH LARGER
#include<stdio.h>
#include<stdlib.h>
#include<string.h>	// string library
#include<time.h>	// time library

// the following structure will store the variable-length word into
// the large-sized box, and the location will be random
// so that reading and writing the word into the container
// should take CONTAINER_SIZE/2 comparisons on the average
// --- to intentionally make search and other operations too much slow
#define CONTAINER_SIZE	4096
//#define CONTAINER_SIZE	8192
struct container {
  char box[CONTAINER_SIZE];
};

int assign_container(struct container *a, const char s[]) {
  int i, word_size, valid_loc_end, loc;

  word_size = strlen(s)+1;	// including termination null character

  if ( word_size > CONTAINER_SIZE ) return 0;	// fail to store

  // generate the position of the word randomly in the box
  valid_loc_end = CONTAINER_SIZE-word_size;	// +1 ?
  loc = rand()%valid_loc_end;

  // reset the container
  for (i=0; i<CONTAINER_SIZE; i++) a->box[i] = ' ';	// space
  for (i=0; i<word_size; i++) a->box[loc+i] = s[i];	// word
  a->box[loc+word_size] = '\0';	// termination character

  return 1;
}

// internal function - DO NOT USE
char *search_container(struct container *a) {
  int i;
  for (i=0; i<CONTAINER_SIZE; i++) {
    if ( a->box[i] != ' ' ) return a->box+i;
  }
  return NULL;	// not stored
}

int copy_container(struct container *a, struct container *b) {
  return assign_container(a,search_container(b));	// a = b
}

void swap_container(struct container *a, struct container *b,
    struct container *temp) {
  copy_container(temp,a);	// temp = a
  copy_container(a,b);		// a = b
  copy_container(b,temp);	// b = temp
}

int compare_container(struct container *a, struct container *b) {
  return strcmp(search_container(a), search_container(b));
}


// array processing
void swap_container_arr(struct container C[], int i, int j,
    struct container *temp) {
  swap_container(C+i, C+j, temp);
}

int compare_container_arr(struct container C[], int i, int j) {
  //return strcmp(search_container(C+i), search_container(C+j));
  return compare_container(C+i, C+j);
}


// <<SAME AS 2-1>>
// TIME MEASUREMENT USING FUNCTION clock() defined in time.h
// MEMORY USAGE MEASUREMENT USING malloc_c() AND strdup_c()
// WHICH REPLACE THE BUILT-IN FUNCTIONS malloc() and strdup()

#include<stdio.h>
// TIME
// THE FOLLOWING FUNCTIONS SHOW HOW TO MEASURE THE EXECUTION TIME
// USING A BUILT-IN FUNCTION clock() DEFINED IN time.h
// NOTE: STATIC VARIABLES ARE NECESSARY TO RECORD CLOCKS
// USAGE:
//    reset_timer();	// reset the start time
//    ....		// statements to measure time
//    t = elapsed_time_in_sec();
//    		// time in seconds from when reset_timer() was called

static clock_t clocks_start;	// global static variable for start clock
static void reset_timer()
{
  clocks_start = clock();	// record the current clock ticks
}

static double elapsed_time_in_sec()
  // returns time in seconds from the start
{
  return ((double) (clock() - clocks_start)) / CLOCKS_PER_SEC;
}

// MEMORY
// Given (allowed): malloc_c(size_t) strdup_c(const char*)
// Allowed string functions: strcpy, strncpy, strlen, strcmp, strncmp
// Unallowed memory functions: memcpy, memccpy, memmove, wmemmove,
//    or other direct memory copy/move functions
//    these functions performs 'BLOCKED' operations so that
//    a large chunk of memory allocation or move operation are
//    efficiently implemented, so they break UNIT TIME assumption
//    in algorithm design
// Unallowed string functions: strdup

/////////////////////////////////////////////////////////////////////
// to compute used memory
// use malloc_c defined below, instead of malloc, calloc, realloc, etc.
// malloc_c accumulates the size of the dynamically allocated memory to
// global/static variable used_memory, so that we can measure the
// used amount of memory exactly.
/////////////////////////////////////////////////////////////////////
static size_t used_memory = 0;	// intial used memory is 0
static size_t used_memory_in_bytes()
  // returns the number of bytes allocated by malloc_c and strdup_c
{
  return used_memory;
}

void *malloc_c(size_t size)
{
  if ( size > 0 ) {
    // increase the required memory count
    used_memory += size;
    return malloc(size);
  }
  else return NULL;
}

// create a duplicate word with counting bytes
char *strdup_c(const char *s) {
  int size;
  size = strlen(s)+1;   // including last null character
  used_memory += size;
  return strdup(s);
}


// DO NOT USE malloc() and strdup()
// the below two lines detects unallowed usage of malloc and strdup
// NULL pointer will be returned, causing runtime errors
// NOTE: '#define' is effective only after declaration
#define malloc	NOT_ALLOWED
#define strdup	NOT_ALLOWED


/////////////////////////////////////////////////////////////
// start of main codes
/////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////
// print container array
/////////////////////////////////////////////////////////////
void print_container_arr( FILE *fp, struct container A[], int N )
  // A[]: container array to print
  // N:   size of the array
  // fp:  file pointer, stdout or stderr for screen display
{
  int i;
  fprintf(fp,"%d\n",N);
  for (i=0; i<N; i++) fprintf(fp,"%s ",search_container(A+i));
  fprintf(fp,"\n");
}

/////////////////////////////////////////////////////////////
// read words from a text file
// NOTE: using malloc_c() and strdup_c()
/////////////////////////////////////////////////////////////

// maximum length of a single string (word)
#define MAX_WORD_LEN	256

struct container *read_container_arr_textfile( const char infile[], int *pN )
  // returns an array of words, with its size stored in
  // the memory indicated by integer pointer variable pN
  // the retured memory should freed by the caller
{
  int i;
  FILE *fp;
  char buf[MAX_WORD_LEN];	// temporary string for fscanf
  struct container *A;

  // NOTE: a lot of part of the code below are file I/O error checking
  // simple code (without error checking)
  /*
  fp = fopen(infile,"r");
  fscanf(fp, "%d", pN);
  A = (struct container*)malloc_c(sizeof(struct container)*(*pN));
  for (i=0; i<(*pN); i++) {
    fscanf(fp, "%s", buf);
    assign_container(A+i, buf);
  }
  fclose(fp);
  return A;
  */

  // check for input file name
  if ( infile == NULL ) {
    fprintf(stderr, "NULL file name\n");
    return NULL;
  }

  // check for file existence
  fp = fopen(infile,"r");
  if ( !fp ) {
    fprintf(stderr, "cannot open file %s\n",infile);
    return NULL;
  }
  else {
    // check for number of elements
    if ( fscanf(fp, "%d", pN) != 1 || *pN <= 0 ) {
      fprintf(stderr, "cannot read number of elements %s\n",infile);
      return NULL;
    }
    else {
      A = (struct container*)malloc_c(sizeof(struct container)*(*pN));
      for (i=0; i<(*pN); i++) {
	if ( fscanf(fp, "%s", buf) != 1 ) {
	  fprintf(stderr, "cannot read value at %d/%d\n",i+1,(*pN));
	  *pN = i;	// read data items
	  fclose(fp);
	  return A;
	}
	else {
	  // assign the word stored in buf
	  assign_container(A+i, buf);
	}
      }
      fclose(fp);
      return A;
    }
  }
}

/////////////////////////////////////////////////////////////
// write words to a text file
/////////////////////////////////////////////////////////////
void write_container_arr_textfile( const char outfile[],
    struct container A[], int N )
  // write the given array of int string words, with its sie N
  // to file whose name given by outfile[]
  // uses print_container_arr
{
  FILE *fp;

  // NOTE: a lot of part of the code below are file I/O error checking
  // simple code (without error checking)
  /*
  fp = fopen(outfile,"w");
  print_container_arr(fp,A,N);
  fclose(fp);
  */

  // check for output filename
  if ( outfile == NULL ) {
    fprintf(stderr, "NULL file name\n");
    return;
  }

  // check for file existence
  fp = fopen(outfile,"w");
  if ( !fp ) {
    fprintf(stderr, "cannot open file for write %s\n",outfile);
  }
  else {
    print_container_arr(fp,A,N);
    fclose(fp);
  }
}

/////////////////////////////////////////////////////////////
// bubble sort
// source: https://ko.wikipedia.org/
/////////////////////////////////////////////////////////////
void bubble_sort_container_arr(struct container *arr, int n) {
  // moving array pointers
  int i, j;
  struct container temp;
  for (i=n-1; i>0; i--) {
    for (j=0; j<i; j++) {
      if ( compare_container_arr(arr, j, j+1) > 0 ) {
	swap_container_arr(arr, j, j+1, &temp);
      }
    }
  }
}

/* FILL */
/* NOTE: addtional funcstions can be defined */

/////////////////////////////////////////////////////////////
// insertion sort
/////////////////////////////////////////////////////////////
/*// source by Gil-Jin Jang, COMP319 AlgorithmsLecture 2Introduction to AlgorithmsSimple Sorting Methods(slide p.105)*/
void insertion_sort_container_arr(struct container *arr, int n) {
  int i,j;
  struct container temp;
  for(i = 0; i < n ; i++){
        for(j=i; j >=0 ; j--){
            if(compare_container_arr(arr,j,i) > 0){
                    swap_container_arr(arr,j,i, &temp);
                    i = j;
            }
        }

    }
}

/////////////////////////////////////////////////////////////
// selection sort
/////////////////////////////////////////////////////////////
/* source by Gil-Jin Jang, COMP319 AlgorithmsLecture 2Introduction to AlgorithmsSimple Sorting Methods(slide p.113)*/
void selection_sort_container_arr(struct container *arr, int n) {
  int i,j,k;
  struct container temp;
  for(i = 0; i < n; i++){
        k=i;
            for(j = i; j < n;j++){
                if(compare_container_arr(arr,k,j) > 0){
                    k=j;
                    swap_container_arr(arr,k,j,&temp);
                }
            }
        swap_container_arr(arr,i,k,&temp);

    }
}

/////////////////////////////////////////////////////////////
// main function
/////////////////////////////////////////////////////////////
int main(int argc, char *argv[])
{
  int n, num_words;
  int method;
  struct container *A;	// to store data to be sorted
  struct container *B;	// to store re-ordered strings

  if ( argc != 5 ) {
    fprintf(stderr, "argc = %d\n",argc);
    fprintf(stderr, "usage: %s method infile sortedfile revsortedfile\n",
	argv[0]);
    fprintf(stderr, " method = 1 --- bubble sort\n"
	" method = 2 --- insertion sort\n"
	" method = 3 --- selection sort\n");
    exit(0);
  }

  method = atoi(argv[1]);

  /* read text file of words:
   * number_of_intergers word1 word2 ... */
  A = read_container_arr_textfile(argv[2], &num_words);

  // start timer
  reset_timer();

  // sort the string array A
  // sort the string array A
  switch ( method ) {
    case 1: bubble_sort_container_arr(A, num_words);
	    break;
    case 2: insertion_sort_container_arr(A, num_words);
	    break;
    case 3: selection_sort_container_arr(A, num_words);
	    break;
  }

  // reverse the order of words in A and store it to B
  B = (struct container*) malloc_c(sizeof(struct container)*num_words);
  for (n=0; n<num_words; n++)
    copy_container(B+num_words-n-1, A+n);

  // display computation time and memory usage
  // NOTE: file I/O time not included
  fprintf(stdout,"TIME: %.5f seconds\n", elapsed_time_in_sec());
  fprintf(stdout,"MEMORY USAGE: %ld bytes\n", used_memory_in_bytes());

  // save results
  write_container_arr_textfile(argv[3], A, num_words);
  write_container_arr_textfile(argv[4], B, num_words);

  // free A and B
  free(B);
  free(A);
}

