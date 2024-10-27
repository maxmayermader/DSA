class Solution {
    public int minimumSwap(String str1, String str2) {
        char s1[] = str1.toCharArray();
        char s2[] = str2.toCharArray();
        int n = s1.length;
        int f1[] = new int[2];
        int f2[] = new int[2];
        
        for(int i = 0; i<n; i++) {
            if(s1[i] == s2[i]) continue;
            f1[s1[i] - 'x']++;
            f2[s2[i] - 'x']++;
        }
        int cnt = 0;
        while(check(f1, f2)) {
            if(f1[0]>=2 && f2[1]>=2) {
                f1[0]-=2;
                f2[1]-=2;
            }
            else {
                f2[0]-=2;
                f1[1]-=2;
            }
            cnt++;
        }
        if(Math.max(f1[0], f1[1]) > 0) {
            if(f1[0] == 1 && f1[1] == 1 && f2[0] == 1 && f2[1] == 1)
                return cnt+2;
            return -1;
        }
        return cnt;
        
        
    }
    private boolean check(int f1[], int f2[]) {
        return (f1[0]>=2 && f2[1]>=2) || (f1[1] >= 2 && f2[0]>=2);
    }
}
 
 
 
// // if f1[1] >=2 && f2[0] >=2
// // if f1[0] >=2 && f2[0] >=2
 
// xy      yx.   x:2, y:2
// yx      xy.   x:2, y:2
 
// xx
// yy
 
 
// /**
 
//         x xxxxyyy y
//         y xxxxyyy x
//  */
 
 
// // (xy, yx) --> 2 swaps
// // (xx, yy) --> 1 swap
 
// //  xy. xxy. => xy
// //  yx. yyx  => xy
 
// // s1 = {x: 3}
 
// // s2 = {y: 3}
 
// // xy x
// // xy y     
 
// // xx y
// // yy x
 
 
// // x y
// // y x
 
 
// xy
// yx