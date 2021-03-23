#1 Write an R program to create three vectors a, b, c with 5 integers. Combine the three vectors to become a 3×5 matrix where each column represents a vector. 
#Print the content of the matrix. Plot a graph and label correctly.

a<-c(1,2,3,4,5)

b<-c(6,7,8,9,10)

c<-c(11,12,13,14,15)

m<-cbind(a,b,c)

print("Content of the said matrix:")

print(m)

plot(a, b, type="o", col="blue", pch="o", lty=1, main="Plot of vectors", ylim=c(0,15) )

points(a, c, col="red", pch="*")
lines(a, c, col="red",lty=2)

#2. Write a R program to create a Data frames which contain details of 5 employees and display the details. (Name, Age, Gender, Role and Length of service).
Employees = data.frame(Name=c("Mark James","Steve Sharpe","Katherine Style", "Jasmine Abdul","Matt Martin"),
                       
                       Age=c(23,22,25,26,32),
                       
                       Gender=c("M","M","F","F","M"),                      
                       
                       Role=c("Clerk","Manager","Executive","CEO","Assistant"),
                       
                       Service=c("1.5","10.5","8.0","0.5","4.5")
                       
)

print("Details of the employees:")                      

print(Employees)


#3. Import the GGPLOT 2 library and plot a graph using the qplot function.
#X axis is the sequence of 1:20 and the y axis is the x ^ 2. Label the graph appropriately. 

install.packages("ggplot2", dependencies = TRUE)
library(ggplot2)
#create dataframe
x<-c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
y<-c(x^2)
df <- data.frame(x, y)
print (df)
#plot graph
ggplot(data = df, aes(x, y = x^2))  +ggtitle("y=x^2") + 
  geom_point() 



#4. Create a simple bar plot of five subjects

#use dataset ToothGrowth
df <- data.frame(dose=c("D0.5", "D1", "D2"),
                 len=c(4.2, 10, 29.5))
head(df)

p<-ggplot(data=df, aes(x=dose, y=len)) + ggtitle("effect of Vitamin C on Tooth growth")  +
  geom_bar(stat="identity")
p


#5. Using the ggplot in-built data sets in RStudio and the qplot function, create a data visualization using your preferred data set.

?economics
ggplot(data = economics, aes(date, unemploy))  +ggtitle("Unemployment") + 
  geom_line(color = "blue") + ylab("Unemployment (000)")

ggplot(data = economics, aes(pce, psavert))  +ggtitle("Unemployment vs savings rate") + 
  geom_line(color = "blue") + xlab("consumption expenditure ($billion)") + ylab("Savings rate")


