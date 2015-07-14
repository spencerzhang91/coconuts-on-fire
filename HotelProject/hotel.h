/* hotel.h -- constants and function prototypes */
#define QUIT 5
#define HOTEL1 80.00
#define HOTEL2 125.00
#define HOTEL3 155.00
#define HOTEL4 200.00
#define DISCOUNT 0.95
#define STARS "********************************"

// menu
int menu(void);

// get staying nights
int getnights(void);

// calculate price and display
void showprice(double, int);

