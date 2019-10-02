import java.io.BufferedReader;
import java.io.FileReader;
import java.io.BufferedInputStream;
import java.io.InputStreamReader;
import java.lang.Runtime;

public class WindowedAverage
{
	static double coefficients[] = {0.1, 0.15, 0.25, 0.25, 0.15, 0.1};
	
	public static void main(String args[])
	{
		try{
			double data[][] = readFile("../Data/h_hig_5.a");
		}catch(Exception e){
			e.printStackTrace();
			System.exit(0);
		}
	}

	public static void insertVelocity(double data[][], int point)
	{
		double uvelocity;
		for (int i=1; i<4; i+=2)
		{
			for(int j=0; j<=5; j++)
			{
				data[point][i+3] += coefficients[j]*((data[point+j][i]-data[point+j-5][i])/(data[point+j][0]-data[point+j-5][0]));
			}
        	
		}
	}

	public static double[][] readFile(String filename)
	throws Exception
	{
		int lines = getLength(filename)-9;

		FileReader reader = new FileReader(filename);
		BufferedReader bufferedReader = new BufferedReader(reader);
		for (int i=0; i<9; i++)
			bufferedReader.readLine();

		double data[][] = new double[lines][11];
		String line;
		String tmp[];
		for(int i=0; i<lines; i++)
		{
			line = bufferedReader.readLine().trim().replaceAll(" +", " ");
			tmp = line.split(" ");
			for(int j=0; j<5;j++)
			{
				data[i][j] = Double.parseDouble(tmp[j]);
				System.out.println(data[i][j]);
			}
		}

		return data;
	}

	public static int getLength(String filename)
	throws Exception
	{
		Runtime rt = Runtime.getRuntime();
		Process process = rt.exec("wc -l " + filename);
		process.waitFor();

		BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
		
		String line = null;
		String otherline = null;
		while ((line = reader.readLine()) != null)
			otherline = line;
		reader.close();

		otherline = otherline.split(" ")[0];
		int length = Integer.parseInt(otherline);
		return length+1;
	}
}