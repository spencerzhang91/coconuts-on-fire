# This project is for the freaking essay.
# There are three functions defined here: batch_corr, batch_kappa and draw.

data <- read.csv("J:\\用地建设规模论文\\density.csv")
print(data)
for (j in 1:3)
for (i in 6:9)
{
  print(c(colnames(data)[j], colnames(data)[i])) 
  relativity <- cor.test(data[,j], data[,i])
  print(relativity)
}

batch_corr <- function(table, ivcs, dvc)
{
    # table: data source csv file
    # ivcs: independent variable column numbers
    # dvc: dependent variable column number
    # No return value(s)
    for (i in ivcs)
    {
        relativity <- cor.test(data[,i], data[, dvc])
        print(relativity)
    }
}