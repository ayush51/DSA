class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) 
    {
	//iterating the main vector
        for(int i=0;i<image.size();i++)
        {
		//reverse condition
		
            reverse(image[i].begin(),image[i].end());
			
			//iterating the sub vector
            for(int j=0;j<image[i].size();j++)
            {
			//inverting the image
			
                if(image[i][j]==1)
                    image[i][j]=0;
                else
                    image[i][j]=1;
					
            }
        }
		//end the code
        return image;
    }
};
