import java.util.Arrays;

/**
 * Calculate the maximum profit by removing billboards and satisfying the k rule
 * 
 * @author (Robert Mok)
 * @version (Bluej: 3.0.8 Java: 1.7.0_07)
 */
public class Billboard
{
    // instance variables
    private int[] billboard; //Keeps value of billboard
    private int[] profit; //Keeps the calculated profit loss
    private int[][] position; //Keeps the position and value of billboard;
    private int k; //The value of k
    private int maxprofit; //maximum profit
    private int cases; //number of times to go through the billboard values
    private int x; 
    private int y; //counter++ for profit[j+y]
    private int z;
    private int billboardprofit; //billboard profit
    int min; //keeps minimum value in each cases
    int min2; //keeps minimum value of the last case

    /**
     * Constructor for objects of class Billboard
     * @param profits is the values of the billboard
     * @param k is the number of billboards allowed to be together
     */
    public Billboard(int[] profits, int k)
    {
        // initialise instance variables
        billboard = new int[profits.length];
        for (int i = 0; i < profits.length; i++)
        {
            billboard[i] = profits[i];
        }
        profit = new int[profits.length];
        this.k = k;
        cases = billboard.length - k -1; //10-3-1 = 6 cases
        x = k+1;   //3+1 = 4
        y = 0; //counter up for profit[j+y]
        z = k+1; // starting at profit [ 4 ] to keep
        position = new int [k][2];
    }

    //Print object to string 
    public String toString() 
    {
        return "Billboards removed (profit): " + Arrays.deepToString(position) + " =>  profit loss of " + min2 +
                "\n    total value of billboards = " + billboardprofit +
                "\n    remaining maximum profit = " + maxprofit + "\n ";
        
    }
    
    /**
     * Calculate the maximum profit after removing billboards
     * @return the calculated maximum profit after removing billboards
     */
    public int maximumProfit()
    {
        //Copy billboard elements from (0 to x) to profit array
        for(int i = 0; i < x; i++)
        {
            profit[i] = billboard[i];
        }
        
        //Calculate the profit loss
        for (int i = 0; i < cases; i++) 
        {
            min = profit[y]; //a temporary minimum value to compare with 
            for (int j = 0; j < k+1; j++)   
            { 
                    if (profit[j+y] <= min)
                    {
                        min = profit[j+y];
                    }
            }
            profit[z+y] = min + billboard[z+y]; //keeps calculated profit loss in profit array;
            y++; //counter 
        }
        
        //Find min in the last k+1 values
        min2 = profit[profit.length-1]; //a temporary minimum value to compare with
        for (int i = 0; i < x; i++)
        {
            if (profit[profit.length-1-i] <= min2)
            {
                min2 = profit[profit.length-1-i];
                position[0][0] = profit.length-1-i; 
            }
        }
        
        //Calculate total billboard profit
        for (int i = 0; i < billboard.length; i++)
        {
            billboardprofit = billboardprofit + billboard[i];
        }
        
        //Calculate the maximum profit after removing billboards
        maxprofit = billboardprofit - min2;
        
        //Find and keep Billboard position and value
        position[0][1] = billboard[position[0][0]];
        int count = profit.length-k-k-3; //ending position to stop comparing
        int start = profit.length-k-2; //starting position to start comparing
        int min3 = min2 - position[0][1]; //calculate the previous minimum 
        int n = 1; //position array counter
        for (int i = start; i > count; i--)
        {   
            if (profit[i] == min3) //if profit loss is equal to the calculated previous minimum
            {
                position[n][0] = i; //keeps the position
                position[n][1] = billboard[i]; //keeps the value of billboard
                n++; //counter
                count = count - k; 
                start = start-k;
                if (profit[i]-billboard[i] != 0) 
                    min3 = profit[i] - billboard[i]; //update and calculate the next previous minimum
                else
                    break; 
            }
        }
        
        return maxprofit;
    }
}

