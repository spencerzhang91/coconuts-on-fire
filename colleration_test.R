# This project is for the freaking essay.
# There are three functions defined here: batch_corr, batch_kappa and draw.

data <- read.csv("J:\\用地建设规模论文\\dataset.csv")
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
    # This function calculates the correlence between a group of iv and one dv
    # table: data source csv file
    # ivcs: independent variable column numbers
    # dvc: dependent variable column number
    # No return value(s)
    for (i in ivcs)
    {
        relativity <- cor.test(data[,i], data[, dvc])
        print(c(colnames(table)[i], colnames(table)[dvc])) 
        print(relativity)
    }
}

multicollinearity <- function(table, vg1, vg2, vg3)
{
    # This function solves the multicollinearity problem
    # table: data sourse csv file
    # vg1: independent variable group1 (population & constructed area)
    # vg2: independent variable group2 (3 compactness measurement indeces)
    # vg3: independent variable group3 (administrative indeces)
    multicol <- kappa(c(vg1, vg2, vg3))
    return (multicol)
}

batch_corr(data, 1:7, 8)
