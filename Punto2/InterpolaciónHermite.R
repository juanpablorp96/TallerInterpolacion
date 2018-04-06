diferencias.adelante <- function(dataX, dataY)
{
  #dataX : puntos fijos para construir el polinomio
  #dataY : valores conocidos para dataX
  n <- length(dataX)
  diferencias <- diff(dataY)/diff(dataX)  #diferencias hacia adelante
  ultimo <- diferencias[n-1] #la ultima diferencia la evaluamos hacia atras
  return(c(diferencias, ultimo)) #regresamos el vector con las diferencias
}
HermiteNo <- function(dataX, dataY, x)
{
  #dataX (vector) : puntos fijos para construir el polinomio
  #dataY (vector) : valores conocidos para dataX
  #x: punto a interpolar
  n <- length(dataX)
  M1 <- matrix(rep(0, 2*n*n ), nrow = n)  #construimos una matriz que iguale a la funcion 
  M1[,1] <- 1
  for(i in 2:(n*2)) #hay que tener cuidado con los subindices
  {
    M1[,i] <- dataX**(i-1)
  }
  M2 <- matrix(rep(0, 2*n*n ), nrow = n)#construimos una matriz que iguale a la primer                                                #derivada 
  M2[,1] <- 0
  M2[,2] <- 1
  for(i in 3:(n*2))
  {
    M2[,i] <- (i-1)*dataX**(i-2)#hay que tener cuidado con los subindices
  }
  #construimos el vector b, con la dataY y las primeras diferencias 
  b1 <- dataY
  b2 <- diferencias.adelante(dataX, dataY)
  b <- c(b1, b2)
  #pegamos las matrices 
  M <- rbind(M1, M2)
  coeficientes <- solve(M, b) #obtenemos los coeficientes
  res <- pol.no.naive(x, coeficientes)
  return(res)
}
Hermite.closure <- function(dataX, dataY) #objeto de tipo closure para fijar parametros 
{
  #dataX (vector) : puntos fijos para construir el polinomio
  #dataY (vector) : valores conocidos para dataX
  #ESTE OBJETO REGRESA UNA FUNCION CON PARAMETROS FIJOS
  function( x )
  {
    HermiteNo(dataX, dataY , x)
  }
}

###########
datax=c(0,1)
datay=c(1,2)

Hermite <- Hermite.closure(datax, dataY)