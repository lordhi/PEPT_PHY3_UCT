public class VelocityUncertainty
{
	public double[] getUncertainties(double[] coordinate, double[] posUncertainty, double[] time)
	{
		double botUncertainty = 1/Math.sqrt(2);  // Assuming .5ms uncertainty on every time reading
		double[] uncertainty = new double[coordinate.length-10];  //Truncates first and last 5 readings
		double[] coefficients = {0.1, 0.15, 0.25, 0.25, 0.15, 0.1}; // Same coefficients
		
		for (int i = 5; i < coordinate.length-5; i++)
		{
			double squared_u = 0;
			for (int j = 5; j >= 0 ; j--)
			{
				double top = coordinate[i+j]-coordinate[i+j-5];  // Numerator of the velocity calculation
				double bot = time[i+j]-time[i+j-5];  // Denominator of velocity calculation
				double subvelocity = coefficients[j]*(top/bot);  // 1 part of velocity with coefficient
				double sqrtUncertainty = Math.sqrt((Math.pow(posUncertainty[i+j],2)+Math.pow(posUncertainty[i+j-5],2))/Math.pow(top,2) + 1/(2*Math.pow(bot,2)));  // The part of the uncertainty in the sqrt
				squared_u+= Math.pow(subvelocity*sqrtUncertainty,2); // The square of the uncertainty of the velocity part
			}
			uncertainty[i-5] = Math.sqrt(squared_u);

		}
	return uncertainty;
	}
}
