package java1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.StringTokenizer;

public class Test {

	public static void main(String[] args) {
		int[][] relation = {{1, 2}, {2, 3}, {2, 6}, {2, 5}, {3, 4}, {4, 5}};
		int target = 2;
		ArrayList<Integer> a = new ArrayList<Integer>();
		
		for(int i = 0; i < relation.length; i++) {
			for(int j = 0; j < relation[i].length; j++) {
				if(relation[i][j] == target) {
					a.add(Integer.parseInt(Arrays.toString(relation[i]).replaceAll("2", "")
							.replaceAll("\\[", "").replaceAll("]", "")
							.replaceAll(",", "").replaceAll(" ", "")));
				}
			}
		}
		
	    int friendCnt = 1 * a.size();
	    int point = 0;
	    int cnt = 0;
	    
	    for(int i = 0; i < a.size(); i++) {
	    	for(int j = i+1; j < a.size(); j++) {
	    		cnt++;
	    		System.out.println(a.get(i) + "\t" + a.get(j));
	    	}
	    }
		point = (cnt * 10) + (a.size()  *  5);
		System.out.print(cnt+ " " +  point);
	}
}
