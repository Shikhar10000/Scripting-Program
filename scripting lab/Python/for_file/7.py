def newtonsqrt(n):
	approx = 0.5*n
	better = 0.5*(approx+n/approx)
	while better!=approx;
		approx=better
		better=0.5*(approx+n/approx)
	return approx
