# This project is for the freaking essay.
# Jan 19 Tue
data <- read.csv("J:\\用地建设规模论文\\density.csv")
print(data)
for (j in 1:3)
for (i in 6:9)
{
  print(c(colnames(data)[j], colnames(data)[i])) 
  relativity <- cor.test(data[,j], data[,i])
  print(relativity)
}

batch_corr <- function()