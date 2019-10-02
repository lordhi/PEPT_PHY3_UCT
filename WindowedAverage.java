import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.BufferedInputStream;
import java.io.InputStreamReader;
import java.lang.Runtime;

public class WindowedAverage
{
	static double coefficient[] = {0.1, 0.15, 0.25, 0.25, 0.15, 0.1};
	
	public static void main(String args[])
	{
		try{
			double data[][] = readFile("../Data/h_hig_5.a");
			for (int i=5; i<data.length-5; i++)
				insertVelocity(data, i);
			writeFile(data, "../Data/h_hig_5.b");
		}catch(Exception e){
			e.printStackTrace();
			System.exit(0);
		}
	}

	public static void insertVelocity(double data[][], int point)
	throws Exception
	{
		double posDifference;
		double timeDifference;
		for (int i=1; i<4; i+=1)
		{
			for(int j=0; j<=5; j++)
			{
				posDifference = (data[point+j][i]-data[point+j-5][i]);
				timeDifference = (data[point+j][0]-data[point+j-5][0]);

				data[point][i+4] += coefficient[j]*posDifference/timeDifference;
				
				/*	Uncertainty propagation calculation, Tom said to use 10%

					//Uncertainty on position as a fraction of the position difference, squared
				data[point][i+7] += (Math.pow(data[point+j][4],2) 
					+ Math.pow(data[point+j-5][4],2))/Math.pow(posDifference,2);
					//Uncertainty on time as a fraction of the time difference, squared
					//Uncertainty on an individual time measurement was taken to be 0.5ms
				data[point][i+7] += 1/2*Math.pow(timeDifference,2);*/
			}
			//data[point][i+7] = Math.abs(data[point][i+4])*Math.sqrt(data[point][i+7]);
			data[point][i+7] = Math.abs(data[point][i+4])*0.1;
		}
	}

	public static void writeFile(double data[][], String filename)
	throws Exception
	{
		FileWriter fw = new FileWriter(filename);
		BufferedWriter bw = new BufferedWriter(fw);
		bw.write("t\tx\ty\tz\tu(r)\tvx\tvy\tvz\tu(vx)\tu(vy)\tu(vz)\r\n");
		StringBuilder tmp;
		for (int i=0; i<data.length; i++)
		{
			tmp = new StringBuilder(50);
			for (int j=0; j<11; j++)
			{
				tmp.append(data[i][j] + "\t");
			}
			bw.write(tmp.toString() + "\r\n");
		}
		bw.close();
		fw.close();
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