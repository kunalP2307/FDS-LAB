public class MergeSort{

    public static void conquer(int array[],int lowBound,int mid,int upBound){
      
        int mergerd[] = new int[upBound - lowBound + 1];

        int i1 = lowBound;
        int i2 = mid +1;
        int x = 0;

        while(i1 <= mid && i2 <= upBound){
            if(array[i1] < array[i2]){
                mergerd[x++] = array[i1++]; 
                //x++; i++;
            }
            else{
                mergerd[x++] = array[i2++];
            }
        }   

        while(i1 <= mid)
            mergerd[x++] = array[i1++];
        
        while(i2 <= upBound)
            mergerd[x++] = array[i2++];

        for (int i=0, j=lowBound; i<mergerd.length; i++,j++)
            array[j] = mergerd[i];

    }

    public static void divide(int array[],int lowBound,int upBound){
        if (lowBound >= upBound){
            return;
        }
        int mid = lowBound + (upBound - lowBound) /2;
        divide(array,lowBound,mid);
        divide(array,mid+1,upBound);
        conquer(array,lowBound,mid,upBound);        
    }

    public static void main(String Args[]){

        int array[] = {24,242,243,54,23,542,64,12};
        int length = array.length;
        
        divide(array,0,length-1);

        for (int i=0; i<length;i++)
            System.out.println(array[i]+"\t");

        StackTraceElement[] stackTraceElements = Thread.currentThread().getStackTrace();

        for(int i=0; i<stackTraceElements.length; i++)
        System.out.println(stackTraceElements[i]);
    }

}