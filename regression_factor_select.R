# determine the proper factors of a regression model
combinations <- function(ivnum)
{
    count <- 0
    for (i in ivnum)
    {
        n <- combn(ivnum, i)
        count <- count + ncol(n)
        print(count)
    }
    return(count)
}